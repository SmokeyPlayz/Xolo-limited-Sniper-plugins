import re
import pyperclip
import subprocess

# Regular expression to match Roblox item links
roblox_link_pattern = r'https://www\.roblox\.com/catalog/(\d+)/'

def extract_roblox_id(text):
    match = re.search(roblox_link_pattern, text)
    if match:
        return match.group(1)
    return None

while True:
    user_input = input("Paste a Roblox item link (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    roblox_id = extract_roblox_id(user_input)
    if roblox_id:
        pyperclip.copy(roblox_id)  # Copy the Roblox ID to the clipboard
        print(f"Extracted Roblox Item ID: {roblox_id} (copied to clipboard)")

        # Open addrobloxid.py
        subprocess.run(["python", "addrobloxid.py"])  # Replace with the correct script name
    else:
        print("Not a valid Roblox item link.")

print("Script exiting.")
