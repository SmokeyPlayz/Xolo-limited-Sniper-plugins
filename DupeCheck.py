import json

def check_for_duplicates(config_file):
    with open(config_file, "r") as file:
        data = json.load(file)

    id_list = data["items"]["list"]
    unique_ids = set()
    duplicates = []

    print("List of IDs in the config:")
    for item_id in id_list:
        if item_id not in unique_ids:
            unique_ids.add(item_id)
        else:
            duplicates.append(item_id)
        print(item_id)

    if duplicates:
        print("\nDuplicate IDs found:")
        for dupe in duplicates:
            print(dupe)
    else:
        print("\nNo duplicate IDs found in the config.")

    # Wait for user input to close the program.
    input("Press Enter to exit...")

if __name__ == "__main__":
    config_file = "config.json"  # Replace with the actual name of your config file.
    check_for_duplicates(config_file)
