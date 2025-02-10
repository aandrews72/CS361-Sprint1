import subprocess
import rsa
from cryptography.fernet import Fernet

print("\n\nTo get help and get more information, enter 'help' without the quotations into the command prompt.\n\n\n")

print("There are two forms of encryption provided: RSA (Rivest-Shamir-Adleman) with a 2048-bit key, and the Fernet encryption method, which combines an AES 128-bit key and a SHA-256 .\n\n")

print("Fernet is the symmetric cryptography option, where one key is needed for both encryption and decryption, while RSA is a assymetric cryptography options.\n\n")

print("To choose an encryption option with data to encrypt, enter the encryption option as well as the data to encrypt seperated by a space. For example: \"RSA Hello World!\" is correct, while \"RSAHello World!\" is not. Again, enter these without quotations.\n\n")

print("The original data, public key, private key (if applicable), and encrypted data may be returned to you.To see all of this information just write the encryption option and the string to encrypt. To see the original data, input 1 after the encryption method. To see the public or private key (if applicable), add 2 or 3 respectively, and to see the encrypted version of the data, input a 4. When selecting these options you can write each number after the other without spaces. For example, to get the original data, public key, and encrypted data for RSA, you can input \"RSA 124 Hello World!\". To get all of this information, you don't need to add any numbers and can just write \"RSA Hello World!\".\n\n")

print("If you choose an assymetric encryption method, you need to save both keys and make sure you store the private key in a secure location, such as the key management service (although it will be deleted at the conclusion of this session when you exit the program). The public key is used to encrypt the data, while the private key will decrypt it. \n\n")

print("If you choose the symmetric encryption method, you can use the individual key to both encrypt and decrypt your data. This should be stored securely.\n\n")

print("The original data, public key, private key (if applicable), and encrypted data may be returned to you.\n\n")


def rsa_enc(string):
    pub_key, priv_key = rsa.newkeys(256)
    encrypted_string = rsa.encrypt(string.encode(), pub_key).hex()
    return string, pub_key, priv_key, encrypted_string


def fernet_enc(string):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_string = fernet.encrypt(string.encode()).decode()
    # Return None since we don't get a private key for fernet
    return string, key.decode(), None, encrypted_string


while True:
    user_input = input("$ ").strip().lower()
    if user_input == "exit":
        subprocess.run(["python3", "exit.py"])
    elif user_input == "hash":
        subprocess.run(["python3", "hash.py"])
    elif user_input == "key":
        subprocess.run(["python3", "key-management.py"])
    elif user_input == "help":
        subprocess.run(["python3", "help.py"])

    # Correctly initialize input based on where the first space is
    split_input = user_input.split(" ", 1)
    if len(split_input) < 2:
        print("Invalid input. Enter encryption method followed by text to generate encrypted string.")
        continue

    enc_method, text = split_input
    number_flags = ""
    valid_nums = "1234"
    i = 0
    for char in text:
        if char not in valid_nums:
            break
        i += 1
    # Set the number flags to whatever is before i
    number_flags = text[:i]

    # Set text to i until the end of text and remove leading or trailing white space
    text = text[i:].strip()

    if not number_flags:
        number_flags = "1234"

    if enc_method == "rsa":
        string, pub_key, priv_key, encrypted_string = rsa_enc(text)
        pub_key_string = f"Modulus: {pub_key.n}\nExponent: {pub_key.e}"
        priv_key_string = f"Private exponent: {priv_key.d}"

    elif enc_method == "fernet":
        string, key, placeholder, encrypted_string = fernet_enc(text)

    if "1" in number_flags:
        print(f"Original string: {string}")
    if "2" in number_flags:
        if enc_method == "rsa":
            print("Public Key:\n" + pub_key_string)
        else:
            print(f"Key: {key}")
    if "3" in number_flags and enc_method == "rsa":
        print("Private Key:\n" + priv_key_string)
    if "4" in number_flags:
        print(f"Encrypted String: {encrypted_string}")
