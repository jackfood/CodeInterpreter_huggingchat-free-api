import os
import subprocess
import time
from hugchat import hugchat
from hugchat.login import Login
from dotenv import load_dotenv

load_dotenv()
hf_email = os.getenv("HFEMAIL")
hf_password = os.getenv("HFPASSWORD")

# Define the paths to your Python scripts
python_script_path_extractpy = 'extractpython.py'
python_script_path_installpy = 'installpip.py'

# Define the current directory
current_directory = os.getcwd()
prompt_file_path = os.path.join(current_directory, 'prompt.txt')
pythoncode_path = os.path.join(current_directory, 'aipythonanswer.txt')


# Login to the chat service
sign = Login(hf_email, hf_password)
cookies = sign.login()
sign.saveCookiesToDir()

# Initialize the chatbot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict()) 
conversation_id = chatbot.new_conversation()
chatbot.change_conversation(conversation_id)

print('[[ Welcome to AI. Let\'s talk! ]]')
print('\'q\' or \'quit\' to exit')
print('\'c\' or \'change\' to change conversation')
print('\'n\' or \'new\' to start a new conversation')

while True:
    if os.path.exists(pythoncode_path):
        with open(pythoncode_path, 'w', encoding='utf-8') as file:
            file.write('')
    if os.path.exists(prompt_file_path):
        with open(prompt_file_path, 'r', encoding='utf-8') as file:
            saved_input = file.read().strip()
            if saved_input:
                user_input = saved_input
                print(f"Existing Prompt - '{saved_input}', proceed to run")
            else:
                user_input = input('> ')
    if user_input.lower() == '':
        pass
    elif user_input.lower() in ['q', 'quit']:
        break
    elif user_input.lower() in ['c', 'change']:
        print('Choose a conversation to switch to:')
        print(chatbot.get_conversation_list())
    elif user_input.lower() in ['n', 'new']:
        print('Clean slate!')
        conversation_id = chatbot.new_conversation()
        chatbot.change_conversation(conversation_id)
    else:
        response = chatbot.chat(user_input)
        print(response)
        
        # Clear the content of 'prompt.txt'
        with open(prompt_file_path, 'w', encoding='utf-8') as file:
            file.write('')

        with open('aianswer.txt', 'w', encoding='utf-8') as file:
            file.write(response)
            time.sleep(0.2)

        # Check if 'aianswer.txt' exists and read its contents
        aianswer_file_path = os.path.join(current_directory, 'aianswer.txt')
        if os.path.exists(aianswer_file_path):
            with open(aianswer_file_path, 'r', encoding='utf-8') as file:
                ai_response = file.read()

            # Execute extractpython.py if needed
            process_extractpy = subprocess.Popen(['python', python_script_path_extractpy], shell=True)
            process_extractpy.wait()

            # Check if aipythonanswer.txt is not empty
            aipythonanswer_path = 'aipythonanswer.txt'
            if os.path.exists(aipythonanswer_path) and os.path.getsize(aipythonanswer_path) > 0:
                with open(aipythonanswer_path, 'r', encoding='utf-8') as aipython_file:
                    python_script_content = aipython_file.read()
                    time.sleep(0.5)
                # Run the Python script from aipythonanswer.txt
                try:
                    print("\n******  Code Executed  *******\n")
                    exec(python_script_content)
                    print("\n******  Code Ended Sucess ****\n")
                    time.sleep(1.0)


                except Exception as e:
                    print("Error executing Python script:", str(e))
                    # Copy the error response
                    error_response = str(e)
                    print("Error Response:", error_response)
                    print("\n******  Code Ended (Err) *****\n")
                    with open(prompt_file_path, 'w', encoding='utf-8') as file:
                        file.write(error_response)
                        time.sleep(0.5)

                    # Check if pip.txt exists and run the install script if necessary
                    pip_txt_path = os.path.join(current_directory, "installpip.txt")
                    install_script_path = os.path.join(current_directory, "installpip.py")

                    if os.path.exists(pip_txt_path) and os.path.getsize(pip_txt_path) > 0:
                        process_pipinstall = subprocess.Popen(['python', install_script_path], shell=True)
                        process_pipinstall.wait()

                        with open(pip_txt_path, 'r', encoding='utf-8') as aipython_file:
                            python_script_content = aipython_file.read()

                        with open(prompt_file_path, 'w', encoding='utf-8') as file:
                            file.write(f"Packing {python_script_content} Installed.")
                            os.remove("installpip.txt")
                            time.sleep(0.5)
                    else:
                        print("****pip infomration does not exist or is empty. Not running the install script.****\n")
            else:
                print("-------AI Reponse is Empty-------\n")
        else:
            print("-------Error: unable to find response in python directory-------\n")

        time.sleep(0.2)
