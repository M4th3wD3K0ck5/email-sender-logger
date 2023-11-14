import smtplib
from email.message import EmailMessage
import getpass
from datetime import datetime
from cryptography.fernet import Fernet


ENCRYPTION_KEY = b'qxtC5hrI8uLEbCY9xR1ZjtBCxLGtx4KL0qVpBFyF_pk='
cipher_suite = Fernet(ENCRYPTION_KEY)

def encrypt_text(text):
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text):
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text

def save_to_log(sender_email, recipient_email, message_content):
    log_entry = f"\nTimestamp: {datetime.now()}\nSender Email: {sender_email}\nRecipient Email: {recipient_email}\nMessage Content: {message_content}\n"
    encrypted_entry = encrypt_text(log_entry)

    with open("email_log.txt", "ab") as log_file:
        log_file.write(encrypted_entry)

def get_user_email():
    while True:
        email = input("Enter your email address: ")
        if "@" in email:
            return email
        else:
            print("Please enter a valid email address.")

def get_sender_email():
    while True:
        email = input("Enter an email address you want to send an email to: ")
        if "@" in email:
            return email
        else:
            print("Please enter a valid email address.")


def get_user_confirmation(prompt):
    while True:
        answer = input(f"{prompt} Yes or No: ").lower()
        if answer in ["yes", "no", "y", "n"]:
            return answer
        else:
            print("Please enter a valid response.")

def get_user_input(prompt):
    return input(prompt)

def get_user_app_password():
    return getpass.getpass("Enter your app password: ")

def send_email():
    sender_email = get_user_email()
    sender_password = get_user_app_password()
    recipient_email = get_sender_email()
    message_content = get_user_input("Please enter your message here: ")

    print(f"\nSender Email: {sender_email}")
    print(f"Recipient Email: {recipient_email}")
    print(f"Message Content: {message_content}")

    confirmation = get_user_confirmation("Are you happy with the entered information?")
    
    if confirmation == "yes":
        # Create an EmailMessage object
        message = EmailMessage()
        message.set_content(message_content)

        # Email subject and recipients
        message["Subject"] = input("Enter the subject of the message\n")
        message["From"] = sender_email
        message["To"] = recipient_email

        # Connect to the SMTP server
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            
            # Send the email
            server.send_message(message)
            
        print("Email sent successfully!")

        # Save the email details to the log
        save_to_log(sender_email, recipient_email, message_content)
    else:
        print("Operation canceled.")

def start():
    send_email()

if __name__ == "__main__":
    start()
