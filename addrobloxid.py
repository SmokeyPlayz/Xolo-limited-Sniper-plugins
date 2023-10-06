import json

with open("config.json", "r") as file:
    existing_config = json.load(file)

new_id = input("Enter the ID for the new item: ")

try:
    new_id = int(new_id)
    existing_config["items"]["list"].append(new_id)

    with open("config.json", "w") as file:
        json.dump(existing_config, file, indent=4)

    print("Item added with ID:", new_id)
except ValueError:
    print("Invalid input. Please enter a valid Roblox item ID (a number).")

input()
