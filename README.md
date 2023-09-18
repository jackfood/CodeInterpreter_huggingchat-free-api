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
