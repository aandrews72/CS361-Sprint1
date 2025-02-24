import hashlib
import subprocess
import os
import signal

# Seperate print statements to make it more readable
print("\n\nTo get help and get more information, enter 'help' without the quotations into the command prompt.\n\n")

print("There are two forms of hash generation provided. SHA-256 (Secure Hash Algorithm 256-bits), and MD5 (Message Digest Algorithm 5). MD5 is no longer secure but fairly popular for non-critical data.\n")

print("To choose a hash generation option, enter the hash method you would like to use in all caps, followed by a space, and the data to hash. For example: \"MD5 this is not very secure\", or \"SHA-256 this is much more secure\" without the quotations are valid. But \"MD5lets try this\" or \"sha-256 this wont work\" will both fail.\n")

print("It is generally impossible to decrypt hashed data. So if you need an original copy of the data, keep it stored. This is used to compare hashed data, such as if a user enter a password, a website may compare the generated hash of that password with the originally stored hash when a user registered for a service.\n")

print("The original data you wanted to hash, the hash itself, and the hashed data will be returned to you.\n\n")


while True:
    user_input = input("$ ").strip().lower()
    if user_input == "exit":
        subprocess.run(["python3", "exit.py"])
    elif user_input == "encrypt":
        subprocess.run(["python3", "encryption.py"])
    elif user_input == "key":
        subprocess.run(["python3", "key-management.py"])
    elif user_input == "help":
        subprocess.run(["python3", "help.py"])

    # Correctly initialize input based on where the first space is
    split_input = user_input.split(" ", 1)
    if len(split_input) < 2:
        print("Invalid input. Enter hash method followed by text to generate a hash for")
        continue

    hash_method, text = split_input

    if hash_method != "md5" and hash_method != "sha-256":
        print("Incorrect formatting of hash generation algorithm. Must enter either MD5 or SHA-256 followed by the text to create a hash for.")

    elif hash_method == "sha-256":
        hashed_text = hashlib.sha256(text.encode()).hexdigest()

    elif hash_method == "md5":
        hashed_text = hashlib.md5(text.encode()).hexdigest()

    else:
        print("Input the correct hash methods of either MD5 or SHA-256 followed by text to generate a hash for.")
    print(f"Hash method: {hash_method}")
    print(f"Original text: {text}")
    print(f"Hashed text: {hashed_text}")
