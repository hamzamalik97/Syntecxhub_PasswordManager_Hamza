import json
from cryptography.fernet import Fernet
import os

# Generate key (first time only)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load key
def load_key():
    return open("key.key", "rb").read()

# Encrypt data
def encrypt_data(data, fernet):
    return fernet.encrypt(data.encode()).decode()

# Decrypt data
def decrypt_data(data, fernet):
    return fernet.decrypt(data.encode()).decode()

# Load passwords
def load_passwords():
    if not os.path.exists("passwords.json"):
        return {}
    with open("passwords.json", "r") as file:
        return json.load(file)

# Save passwords
def save_passwords(data):
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

# Main program
def main():
    if not os.path.exists("key.key"):
        generate_key()

    key = load_key()
    fernet = Fernet(key)

    master = input("Enter master password: ")

    if master != "admin123":
        print("Wrong master password!")
        return

    while True:
        print("\n1. Add Password")
        print("2. View Passwords")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Choose option: ")
        data = load_passwords()

        if choice == "1":
            site = input("Enter site: ")
            username = input("Enter username: ")
            password = input("Enter password: ")

            encrypted_pass = encrypt_data(password, fernet)

            data[site] = {
                "username": username,
                "password": encrypted_pass
            }

            save_passwords(data)
            print("Saved successfully!")

        elif choice == "2":
            for site in data:
                decrypted_pass = decrypt_data(data[site]["password"], fernet)
                print(f"{site} | {data[site]['username']} | {decrypted_pass}")

        elif choice == "3":
            site = input("Enter site to delete: ")
            if site in data:
                del data[site]
                save_passwords(data)
                print("Deleted!")
            else:
                print("Not found!")

        elif choice == "4":
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()