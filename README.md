# Half-CodeInterpreter_HFembedded

This repository contains a Python-based Half-CodeInterpreter that interfaces with an AI chat service, extracts and executes Python code from chat responses, and manages Python package installations.

## Getting Started

Before you can use this Half-CodeInterpreter, you'll need to set up your environment and configure the necessary files.

### Prerequisites

- Python 3.7 or higher
- [Hugging Chat API](https://github.com/Soulter/hugging-chat-api) library

## Installation

To get started with the Half-CodeInterpreter, follow these steps:

1. **Clone the Hugging Chat API Repository:**

   First, clone the Hugging Chat API repository and install the `hugchat` library by running the following commands in your terminal:

   ```bash
   git clone https://github.com/Soulter/hugging-chat-api.git
   cd hugging-chat-api
   pip install .
   ```

2. **Clone this Repository:**

   Clone this Half-CodeInterpreter repository and navigate to its directory:

   ```bash
   git clone https://github.com/yourusername/Half-CodeInterpreter_HFembedded.git
   cd Half-CodeInterpreter_HFembedded
   ```

3. **Copy Required Files:**

   Copy all the required files, including `CodeInterpreterHF.py`, `extractpython.py`, `installpip.py`, and the `.env` configuration file, to your project directory.

4. **Configure `.env` File:**

   Update the `.env` file with your Hugging Face credentials (email and password).

Now your Half-CodeInterpreter is set up and ready to use. You can proceed to the "Usage" section for instructions on how to run the chatbot interface and interact with the AI chat service.


## Usage

To use the Half-CodeInterpreter and interact with the AI chat service, follow these steps:

1. **Run the CodeInterpreterHF.py Script:**

   Use the following command to run the `CodeInterpreterHF.py` script using Python:

   ```bash
   python CodeInterpreterHF.py
   ```

   This script launches the chatbot interface, allowing you to:

   - Start conversations with the AI chat service.
   - Send user input to the chatbot.
   - Extract and execute Python code from chatbot responses.
   - Manage Python package installations as needed.

2. **Interact with the Chatbot:**

   Once the chatbot is running, you can interact with it by following the on-screen instructions. Here are some common actions you can perform:

   - Enter user input when prompted and receive responses from the chatbot.
   - Use 'q' or 'quit' to exit the chatbot.
   - Use 'c' or 'change' to change the conversation.
   - Use 'n' or 'new' to start a new conversation.

3. **Extract and Execute Python Code:**

   When the chatbot responds with Python code, the script will extract and execute it. You can observe the execution of Python code and any output or errors in the console.

4. **Manage Package Installations:**

   If the chatbot instructs you to install Python packages, the script will handle it automatically. You don't need to manually install packages; the script will execute the necessary installation commands.


## Files and Explanation

This repository contains several files that play crucial roles in the functioning of the Half-CodeInterpreter_HFembedded project:

1. **CodeInterpreterHF.py**:
   - This is the primary script responsible for interfacing with the AI chat service and managing Python code execution.
   - **Functionality**:
     - Imports necessary libraries and modules.
     - Loads user credentials securely from the `.env` file.
     - Manages conversations with the AI chat service.
     - Accepts user input and communicates with the chatbot.
     - Extracts and executes Python code from AI responses.
     - Manages the installation of Python packages as required.

2. **extractpython.py**:
   - A supporting script for extracting Python code from AI responses and updating `aipythonanswer.txt`.
   - **Functionality**:
     - Reads AI responses from `aianswer.txt`.
     - Extracts Python code enclosed in triple backticks (```python```).
     - Compares and updates the extracted code in `aipythonanswer.txt`.

3. **installpip.py**:
   - Another supporting script responsible for installing Python packages specified in `installpip.txt`.
   - **Functionality**:
     - Reads the package name from `installpip.txt`.
     - Constructs a `pip install` command for the specified package.
     - Executes the `pip install` command to install the package.

4. **.env**:
   - The `.env` file is a configuration file used to store sensitive information, such as your Hugging Face credentials (email and password).
   - **Functionality**:
     - Stores `HFEMAIL` and `HFPASSWORD` environment variables securely.
     - These credentials are loaded by `CodeInterpreterHF.py` to log in to the AI chat service safely.

These files work together to create a functional Half-CodeInterpreter that allows you to interact with the AI chat service, extract and execute Python code, and manage Python package installations when necessary. Make sure to configure the `.env` file with your actual Hugging Face credentials before running the project.
