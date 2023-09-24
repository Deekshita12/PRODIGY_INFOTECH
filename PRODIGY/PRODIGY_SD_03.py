import json

# Load contacts from a JSON file (if available)
def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

# Save contacts to a JSON file
def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Edit an existing contact
def edit_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the index of the contact to edit: ")) - 1
    if 0 <= index < len(contacts):
        contact = contacts[index]
        print("Editing contact:")
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        contact['name'] = input("Enter new name: ")
        contact['phone'] = input("Enter new phone number: ")
        contact['email'] = input("Enter new email address: ")
        print("Contact updated successfully!")
    else:
        print("Invalid index!")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the index of the contact to delete: ")) - 1
    if 0 <= index < len(contacts):
        del contacts[index]
        print("Contact deleted successfully!")
    else:
        print("Invalid index!")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
\