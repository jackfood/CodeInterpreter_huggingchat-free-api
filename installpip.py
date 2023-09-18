import subprocess
import os

# Read the package name from ~pip.txt
with open("installpip.txt", "r") as file:
    package_name = file.read().strip()

# Define the pip install command as a list
pip_install_command = ["pip", "install", package_name]

try:
    # Use subprocess to run the pip install command
    subprocess.run(pip_install_command, check=True)
    print(f"------------------------------ Successfully installed {package_name} ------------------------------")
except subprocess.CalledProcessError as e:
    print(f"------------------------------ Failed to install {package_name}: {e} ------------------------------")
