import os
import hashlib
import time
from datetime import datetime

SUBMISSION_DIR = "submissions"
LOG_FILE = "submission_log.txt"
LOGIN_LOG = "login_log.txt"
MAX_FILE_SIZE = 5 * 1024 * 1024  


failed_attempts = {}
last_attempt_time = {}

os.makedirs(SUBMISSION_DIR, exist_ok=True)

def log_submission(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

def log_login(message):
    with open(LOGIN_LOG, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")


def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()


def submit_assignment():
    filepath = input("Enter file path: ")

    if not os.path.exists(filepath):
        print("File does not exist.")
        return

   
    if not (filepath.endswith(".pdf") or filepath.endswith(".docx")):
        print("Only .pdf and .docx files allowed.")
        return

    
    if os.path.getsize(filepath) > MAX_FILE_SIZE:
        print("File exceeds 5MB limit.")
        return

    filename = os.path.basename(filepath)
    new_hash = get_file_hash(filepath)

    
    for existing_file in os.listdir(SUBMISSION_DIR):
        existing_path = os.path.join(SUBMISSION_DIR, existing_file)
        if existing_file == filename:
            if get_file_hash(existing_path) == new_hash:
                print("Duplicate submission detected (same name and content).")
                log_submission(f"Duplicate rejected: {filename}")
                return

    
    destination = os.path.join(SUBMISSION_DIR, filename)
    with open(filepath, "rb") as src, open(destination, "wb") as dst:
        dst.write(src.read())

    print("Submission successful.")
    log_submission(f"Submitted: {filename}")

def check_duplicate():
    filename = input("Enter filename to check: ")
    filepath = os.path.join(SUBMISSION_DIR, filename)

    if os.path.exists(filepath):
        print("File has already been submitted.")
    else:
        print("No submission found.")


def list_submissions():
    files = os.listdir(SUBMISSION_DIR)
    if not files:
        print("No submissions found.")
    else:
        print("Submitted Files:")
        for f in files:
            print("-", f)


def login():
    user = input("Enter username: ")
    password = input("Enter password: ")

    current_time = time.time()
    
    if user not in failed_attempts:
        failed_attempts[user] = 0
        last_attempt_time[user] = 0

    
    if failed_attempts[user] >= 3:
        print("Account locked due to multiple failed attempts.")
        log_login(f"{user} - Account locked")
        return

    
    if current_time - last_attempt_time[user] < 60:
        print("Warning: Multiple login attempts detected within 60 seconds.")
        log_login(f"{user} - Rapid login attempt")

    last_attempt_time[user] = current_time

    
    if user == "admin" and password == "1234":
        print("Login successful.")
        failed_attempts[user] = 0
        log_login(f"{user} - Login success")
    else:
        failed_attempts[user] += 1
        print(f"Login failed. Attempts: {failed_attempts[user]}")
        log_login(f"{user} - Login failed")

def main():
    while True:
        print("\n====== Secure Submission System ======")
        print("1. Submit assignment")
        print("2. Check if file already submitted")
        print("3. List submitted assignments")
        print("4. Simulate login attempt")
        print("5. Exit")
        print("=====================================")

        choice = input("Enter choice: ")

        if choice == "1":
            submit_assignment()
        elif choice == "2":
            check_duplicate()
        elif choice == "3":
            list_submissions()
        elif choice == "4":
            login()
        elif choice == "5":
            confirm = input("Are you sure you want to exit? (Y/N): ")
            if confirm.upper() == "Y":
                print("Exiting system.")
                break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
