# Dental Clinic AI Assistant

## Overview
This project is an AI assistant for a dental clinic, designed to help patients book appointments through a conversational interface. The assistant is powered by LangChain, integrated with a HuggingFacePipeline using the Mistral-7B-Instruct-v0.2 model for natural language processing.

## Features
- **Appointment Booking:** Helps patients book appointments by asking for their preferred date and time.
- **Multiple Appointments:** Supports booking multiple appointments in a single session.
- **Conversation Management:** Maintains a polite and professional tone throughout the interaction.
- **Exit Keywords:** Ends the conversation when the patient says "bye," "exit," or "quit."

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine using the following command:

```
git clone https://github.com/YashAmin0/SpaceO-Practical-task.git
cd SpaceO-Practical-task
```

### 2. Create and Activate a Virtual Environment
Set up a virtual environment to manage dependencies:

```
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Required Dependencies
Install the necessary Python packages by running:

```
pip install -r requirements.txt
```

### 4. Run the Application
Start the AI assistant by executing:

```
python main.py
```

### 5. Interact with the Assistant
Booking an Appointment: Simply type your request, and the assistant will guide you through the process.
Ending the Conversation: Type "bye," "exit," or "quit" to end the session.

### Conversation Flow Description
The AI assistant follows a structured conversation flow:

Initialization:

The assistant greets the patient and asks how it can assist.

Booking Process:

If a patient wants to book an appointment, the assistant asks for the preferred date and time.
Upon receiving the details, it attempts to book the slot.
If successful, it confirms the booking. If the slot is taken, it requests an alternative time.

Handling Multiple Appointments:

The patient can book multiple appointments in one session.

Ending the Conversation:

The conversation can be ended by the user at any time using keywords like "bye," "exit," or "quit."
The assistant will acknowledge and terminate the interaction.
