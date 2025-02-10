import subprocess


print("\n\nTo get help and get more information, enter \"help\" without the quotations into the command prompt.\n\n\n")

print("You may either add, remove, or view the previously added keys. Importantly, when you exit this program, the keys will be lost! This is for short-term key management.\n\n")


print("To add a key, input \"add\" without quotations and press enter or return. Then you will enter a string to associate with the key, for example: \"AES key for file integrity checks\", without quotations. After entering that string, you can add the key on the new blank line. The key will be associated with a number to help the deletion process, it will be assigned the first available number starting at 1.\n\n")


print("To view a key, you will input \"view\" without quotations and press enter or return. You will then see the string describing the key, the key's assigned number, and the key on a new line.\n\n")


print("To delete a key, input \"delete X\" without quotations where X is the number assigned to it.\n\n") 


keys = []

while True:
    user_input = input("$ ").strip().lower()

    if user_input == "exit":
        subprocess.run(["python3", "exit.py"])
    elif user_input == "hash":
        subprocess.run(["python3", "hash.py"])
    elif user_input == "encrypt":
        subprocess.run(["python3", "encryption.py"])
    elif user_input == "help":
        subprocess.run(["python3", "help.py"])
    
    elif user_input == "add":
        description = input("Enter a description for the key: ").strip()
        key = input("Enter the key: ").strip()
        keys.append({"id": len(keys) + 1, "description": description, "key": key})
        print(f"Key added with ID {len(keys)}\n")

    elif user_input == "view":
        if not keys:
            print("No keys stored\n")
        else:
            for key in keys:
                print(f"ID: {key['id']}\nDescription: {key['description']}\nKey: {key['key']}\n")
    
    elif user_input.startswith("delete"):
        user_input = user_input.split()
        if len(user_input) < 2 or not user_input[1].isdigit():
            print("Invalid delete format. Use: delete X where X is the ID of the key to delete\n")
        else:
            key_id = int(user_input[1])
            found = False
            for key in keys:
                if key["id"] == key_id:
                    keys.remove(key)
                    print(f"Deleted key with ID {key_id}\n")
                    found = True
                    break
            if not found:
                print("Invalid key ID.\n")
    else:
        print("Invalid input. Try again.\n")
