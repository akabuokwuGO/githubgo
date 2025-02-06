class Email:
    """This Initialises the instance variables for each email."""

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
        self.a_spam_mail = False

    def mark_as_read(self):
        """The function to mark email as read"""
        self.has_been_read = True

    def mark_as_spam(self):
        """The function to mark email as spam"""
        self.a_spam_mail = True

# This is the inbox list
inbox = []

def populate_inbox():
    """The function to add message to the email."""
    sample_emails = [
        ("sample_email1@task9.com", "Welcome to HyperionDev!", "Welcome to the Skills for Life Training"),
        ("sample_email2@task9.com", "Great work on the bootcamp!", "Please send in your report as soon as posible"),
        ("sample_email3@etask9.com", "Your excellent marks!", "This is to acknowledge your performance"),
    ]
    for email_address, subject_line, email_content in sample_emails:
        inbox.append(Email(email_address, subject_line, email_content))

def list_emails():
    """This will list all emails in the inbox with their subject lines and indices."""
    if not inbox:
        print("\nYour inbox is empty.\n")
        return

    print("\nYour Inbox:")
    for index, email in enumerate(inbox):
        status = "[Read]" if email.has_been_read else "[Unread]"
        spam_status = "[Spam]" if email.a_spam_mail else ""
        print(f"{index}: {email.subject_line} {status} {spam_status}")

def read_email(index):
    """This will displays the selected email and mark it as read."""
    try:
        email = inbox[index]
        print(f"\nFrom: {email.email_address}\nSubject: {email.subject_line}\nContent: {email.email_content}\n")
        email.mark_as_read()
        print(f"Email from {email.email_address} marked as read.\n")
    except IndexError:
        print("\nInvalid email index. Please try again.\n")

def list_unread_emails():
    """This will list all unread emails in the inbox."""
    print("\nUnread Emails:")
    unread_found = False
    for index, email in enumerate(inbox):
        if not email.has_been_read:
            unread_found = True
            print(f"{index}: {email.subject_line}")
    if not unread_found:
        print("No unread emails.\n")

def mark_email_as_spam(index):
    """This will mark the selected email as spam."""
    try:
        email = inbox[index]
        email.mark_as_spam()
        print(f"\nEmail from {email.email_address} marked as spam.\n")
    except IndexError:
        print("\nInvalid email index. Please try again.\n")

def delete_email(index):
    """This will deletes the selected email from the inbox."""
    try:
        email = inbox.pop(index)
        print(f"\nEmail from {email.email_address} with subject '{email.subject_line}' deleted.\n")
    except IndexError:
        print("\nInvalid email index. Please try again.\n")

# Populate inbox with sample emails at startup
populate_inbox()

def email_menu():
    """This will displays the email menu and process any user input."""
    while True:
        print("\nThe Email Menu:")
        print("Press 1. To Read an email")
        print("Press 2. To View unread emails")
        print("Press 3. To Mark an email as spam")
        print("Press 4. To Delete an email")
        print("Press 5. To Exit the application")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            list_emails()
            try:
                index = int(input("\nEnter the index of the email to read: ").strip())
                read_email(index)
            except ValueError:
                print("\nPlease enter a valid number.\n")
        elif choice == "2":
            list_unread_emails()
        elif choice == "3":
            list_emails()
            try:
                index = int(input("\nEnter the index of the email to mark as spam: ").strip())
                mark_email_as_spam(index)
            except ValueError:
                print("\nPlease enter a valid number.\n")
        elif choice == "4":
            list_emails()
            try:
                index = int(input("\nEnter the index of the email to delete: ").strip())
                delete_email(index)
            except ValueError:
                print("\nPlease enter a valid number.\n")
        elif choice == "5":
            print("\nThe End")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

# This is main email menu
if __name__ == "__main__":
    email_menu()
