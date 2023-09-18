import re
import os

try:
    with open('aianswer.txt', 'r', encoding='utf-8') as file:
        ai_response = file.read()
except FileNotFoundError:
    print("Error: 'aianswer.txt' not found")
    ai_response = None

if ai_response is not None:
    # Find and extract content between triple backticks (```python) and (```)
    start_markers = ["```python", "```"]
    end_marker = "```"
    start_index = -1

    for marker in start_markers:
        start_index = ai_response.find(marker)
        if start_index != -1:
            start_marker = marker
            break

    if start_index != -1:
        end_index = ai_response.find(end_marker, start_index + len(start_marker))
    else:
        end_index = -1

    if start_index != -1 and end_index != -1:
        python_content = ai_response[start_index + len(start_marker):end_index]

        # Check if 'aipythonanswer.txt' exists and compare its content with python_content
        aipythonanswer_path = 'aipythonanswer.txt'

        try:
            with open(aipythonanswer_path, 'r', encoding='utf-8') as aipython_file:
                existing_content = aipython_file.read()

            if existing_content != python_content:
                # If python_content is different, delete 'aipythonanswer.txt' and create a new one
                try:
                    os.remove(aipythonanswer_path)
                except FileNotFoundError:
                    pass  # Ignore if the file doesn't exist

                with open(aipythonanswer_path, 'w', encoding='utf-8') as python_file:
                    python_file.write(python_content)
                print("------------------------------ Python content updated sucessfully ------------------------------")
            else:
                print("------------------------------ Python content is the same as previous content extracted content. ------------------------------")
        except FileNotFoundError:
            # If 'aipythonanswer.txt' doesn't exist, create it and save python_content to it
            with open(aipythonanswer_path, 'w', encoding='utf-8') as python_file:
                python_file.write(python_content)
            print("------------------------------Python content extracted sucessfully------------------------------")
    else:
        print("------------------------------No Python code found from response------------------------------")
else:
    print("------------------------------No AI response------------------------------")


# Function to extract code block between "```python" or "```"
def extract_code_block(text):
    code_block = ""
    in_code_block = False
    for line in text:
        if line.strip() == "```python" or line.strip() == "```":
            if in_code_block:
                in_code_block = False
            else:
                in_code_block = True
        elif in_code_block:
            code_block += line
    return code_block.strip()


# Function to search for "pip install" and extract the package name
def extract_pip_package_name(text):
    matches = re.findall(r'pip install ([^\s]+)', text)
    if matches:
        # Remove non-English characters
        package_name = re.sub(r'[^a-zA-Z]', '', matches[0])
        return package_name
    return None

# Read the content of 'aianswer.txt' in UTF-8
with open('aianswer.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()


# Check if the content is not empty
if content:
    # Extract code block
    code_block = extract_code_block(content)

    # Extract and save pip package name to 'pip.txt'
    pip_package_name = extract_pip_package_name(''.join(content))
    if pip_package_name:
        with open('installpip.txt', 'w', encoding='utf-8') as pip_file:
            pip_file.write(pip_package_name)
