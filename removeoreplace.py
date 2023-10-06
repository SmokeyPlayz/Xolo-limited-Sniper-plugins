import json

with open("config.json", "r") as file:
    existing_config = json.load(file)

action = input("Enter 'remove' to remove an item ID or 'replace' to replace an item ID: ")

if action == "remove":
    remove_id = input("Enter the ID to remove: ")

    try:
        remove_id = int(remove_id)
        items_list = existing_config["items"]["list"]

        if remove_id in items_list:
            items_list.remove(remove_id)

            with open("config.json", "w") as file:
                json.dump(existing_config, file, indent=4)

            print("Item ID", remove_id, "removed from the configuration.")
        else:
            print(f"Item ID {remove_id} not found in the configuration.")
    except ValueError:
        print("Invalid input. Please enter a valid Roblox item ID (a number).")

elif action == "replace":
    old_id = input("Enter the existing ID to replace: ")
    new_id = input("Enter the new ID to replace it with: ")

    try:
        old_id = int(old_id)
        new_id = int(new_id)
        items_list = existing_config["items"]["list"]

        if old_id in items_list:
            items_list[items_list.index(old_id)] = new_id

            with open("config.json", "w") as file:
                json.dump(existing_config, file, indent=4)

            print("Item ID", old_id, "replaced with ID", new_id, "in the configuration.")
        else:
            print(f"Item ID {old_id} not found in the configuration.")
    except ValueError:
        print("Invalid input. Please enter valid Roblox item IDs (numbers).")

else:
    print("Invalid action. Please enter 'remove' or 'replace'.")

input()
