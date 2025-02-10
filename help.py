import subprocess
import os
import signal


print("\nTo get help and get more information, enter \"help\" without the quotations into the command prompt.\n\n\n")

print("Navigation:\n\nTo go to the Encryption service, enter \"encrypt\" without quatations.\n\nTo go to the Hash Generation service, enter \"hash\" without quatations.\n\nTo go to the Key Management service, enter \"key\" without quatations.\n\nThese can be entered at any time to navigate to those service options.\n\n\n")

print("Important Information:\n\nIn the Key Management section, the keys will only be saved until you exit the program or end the terminal session.\n\nTo exit, enter \"exit\" without quotations.")

while True:
    user_request = input("$ ").strip().lower()
    
    if user_request == "exit":
        subprocess.run(["python3", "exit.py"])
    elif user_request == "hash":
        subprocess.run(["python3", "hash.py"])
    elif user_request == "encrypt":
        subprocess.run(["python3", "encryption.py"])
    elif user_request == "key":
        subprocess.run(["python3", "key-management.py"])
    else:
        print("Invalid command, enter one of the following: exit hash encrypt key help")
