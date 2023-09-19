import subprocess
import os
from dotenv import load_dotenv
load_dotenv()

# Get the current working directory
current_directory = os.getcwd()
prompt_file_path = os.path.join(current_directory, 'prompt.txt')
user_original_prompt = os.path.join(current_directory, 'temp_original_prompt.txt')

# Read the package name from ~pip.txt
with open("installpip.txt", "r", encoding='utf-8') as file:
    package_name = file.read().strip()
with open(user_original_prompt, 'r', encoding='utf-8') as original_prompt:
    post_pip_installed_prompt = original_prompt.read()

# Define the pip install command as a list
pip_install_command = ["pip", "install", package_name]

try:
    # Use subprocess to run the pip install command
    subprocess.run(pip_install_command, check=True)
    print(f"-- Successfully installed {package_name} --")

    # Write (installpip.txt & _temp_prompt.txt) into (prompt.txt)
    with open(prompt_file_path, 'w', encoding='utf-8') as file:
        file.write(f"Successfully installed Python Package {package_name}. {post_pip_installed_prompt}")

except subprocess.CalledProcessError as e:
    print(f"-- Failed to install {package_name}: {e} --")

    prompt_file_path = os.path.join(current_directory, 'prompt.txt')
    with open(prompt_file_path, 'w', encoding='utf-8') as file:
        file.write(f"Failed installation of Package {package_name}. Rewrite alternative for {post_pip_installed_prompt}")
