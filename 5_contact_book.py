import json
def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=2)
def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\n=== Contact List ===")
        for contact in contacts:
            print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")
def add_contact(contacts, name, phone, email, address):
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    save_contacts(contacts)
    print(f"\nContact '{name}' added successfully!")
def search_contact(contacts, search_term):
    found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    display_contacts(found_contacts)
def update_contact(contacts, name, new_phone, new_email, new_address):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address
            save_contacts(contacts)
            print(f"\nContact '{name}' updated successfully!")
            return
    print(f"\nContact '{name}' not found.")

def delete_contact(contacts, name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"\nContact '{name}' deleted successfully!")
            return
    print(f"\nContact '{name}' not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(contacts, name, phone, email, address)

        elif choice == '2':
            display_contacts(contacts)

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_contact(contacts, search_term)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            update_contact(contacts, name, new_phone, new_email, new_address)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(contacts, name)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()