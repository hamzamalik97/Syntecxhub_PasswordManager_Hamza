# Syntecxhub_PasswordManager_Hamza

## Internship: Syntecxhub | Week 1 Task
## Program: Cybersecurity
## Intern: Hamza

## Project: Password Manager

A Python-based Password Manager that securely stores user credentials using AES encryption (Fernet). Requires a master password for access.

## Features
- Add credentials (website, username, password)
- View all saved passwords
- Search password by website
- Delete password by website
- Fernet (AES) encryption
- Stores data in local JSON file
- Master password authentication

## File Structure
Syntecxhub_PasswordManager_Hamza/
├── password_manager.py
├── passwords.json (auto-created)
├── key.key (auto-created)
└── README.md

## Requirements
- Python 3.x
- cryptography library

## Installation
pip install cryptography

## How to Run
python password_manager.py

## Master Password
admin123

## Encryption
Uses Fernet encryption (AES-128 + HMAC-SHA256) from the Python cryptography library. Passwords are never stored in plain text.

## Technologies Used
- Python
- cryptography (Fernet)
- JSON file handling
- os module
