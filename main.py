from langchain_huggingface import HuggingFacePipeline
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from transformers import BitsAndBytesConfig
import torch
from langchain.prompts import PromptTemplate

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

llm = HuggingFacePipeline.from_model_id(
    model_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 20, "repetition_penalty":1.15},
    model_kwargs={"quantization_config": quantization_config, "torch_dtype": torch.bfloat16}
)

# Define the prompt template
template = """You are an AI assistant for a dental clinic, dedicated to helping patients book appointments. Always maintain a polite and professional demeanor.

Appointment Requests:

If a patient wants to book an appointment, kindly ask for their preferred date and time.
If the patient provides a date and time, confirm by responding.
Ensure all required information is gathered. If any details are missing or unclear, politely ask the patient for clarification.

Multiple Appointments:

Allow patients to book additional appointments if needed.

End of Conversation:

If the patient indicates they want to end the conversation (e.g., by saying "bye," "exit," or "quit"), acknowledge it and end the interaction.
If the patient wishes to continue, remain available and ready to assist.

Thinking Process:

Always read the patient's response ({input}) carefully.
Think before responding to ensure all queries are addressed appropriately.
Strictly Keep the chat short and relevant.

Current conversation:
{history}
Patient: {input}
Agent:"""

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=template
)

# Initialize conversation memory
memory = ConversationBufferMemory(human_prefix="Patient", ai_prefix="Agent")

# Initialize conversation chain with the prompt template
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True
)

# Simulated appointment storage
appointments = {}

def book_appointment(date, time):
    """Simulate booking an appointment."""
    appointment_key = f"{date}_{time}"
    if appointment_key in appointments:
        return False
    appointments[appointment_key] = True
    return True

def handle_conversation(user_input):
    """Handle the conversation flow."""
    response = conversation.predict(input=user_input)
    
    # Check if the response contains appointment details
    if "Booking appointment for" in response:
        # Extract date and time from the response
        parts = response.split("Booking appointment for")[-1].strip().split("at")
        if len(parts) == 2:
            date = parts[0].strip()
            time = parts[1].strip().rstrip('.')
            
            # Attempt to book the appointment
            if book_appointment(date, time):
                return f"Great! Your appointment is confirmed for {date} at {time}."
            else:
                return f"I'm sorry, but the slot for {date} at {time} is already taken. Can you provide another date and time?"
    
    return response

# Main conversation loop
print("Agent: Hello! How can I help you today?")
while True:
    user_input = input("Patient: ")
    if user_input.lower() in ['exit', 'quit', 'bye', 'thank you']:
        print("Agent: Thank you for using our service. Goodbye!")
        break

    response = handle_conversation(user_input)
    print(f"Agent: {response}")