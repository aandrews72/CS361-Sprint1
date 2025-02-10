import subprocess
import os
import signal


def main():
    print("Are you sure you want to exit? Doing so will permanently delete all the keys you have stored in this session!\n\n")
    
    while True:
        user_request = input("Input yes to exit and delete all your keys input no to keep your keys\n\n$ ").strip()
        if user_request == "yes":
            os.killpg(os.getpgrp(), signal.SIGTERM)
        elif user_request == "no":
            print("\n\nTo get help and get more information, enter 'help' without the quotations into the command prompt.\n\nTo go to the Encryption service, enter 'encrypt' without quatations.\n\nTo go to the Hash Generation service, enter 'hash' without quatations.\n\nTo go to the Key Management service, enter 'key' without quatations.\n\nThese can be entered at any time to navigate to those service options.\n")
        elif user_request == "exit":
            subprocess.run(["python3", "exit.py"])
        elif user_request == "hash":
            subprocess.run(["python3", "hash.py"])
        elif user_request == "encrypt":
            subprocess.run(["python3", "encryption.py"])
        elif user_request == "key":
            subprocess.run(["python3", "key-management.py"])
        elif user_request == "help":
            subprocess.run(["python3", "help.py"])
        else:
            print("Invalid command, enter one of the following: yes no exit hash encrypt key help")


main()
