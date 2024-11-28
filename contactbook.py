class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        print("Enter the following details:")
        name = input("Name: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully!\n")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.\n")
            return
        print("\nList of Contacts:")
        for contact in self.contacts:
            print(contact)
        print()

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print(contact)
                found = True
        if not found:
            print("No contact found.\n")

    def update_contact(self):
        search_term = input("Enter name or phone number of the contact to update: ")
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print("Current details: ", contact)
                name = input("New Name (Leave blank to keep the same): ")
                phone = input("New Phone (Leave blank to keep the same): ")
                email = input("New Email (Leave blank to keep the same): ")
                address = input("New Address (Leave blank to keep the same): ")

                if name: contact.name = name
                if phone: contact.phone = phone
                if email: contact.email = email
                if address: contact.address = address

                print("Contact updated successfully!\n")
                return
        print("Contact not found.\n")

    def delete_contact(self):
        search_term = input("Enter name or phone number of the contact to delete: ")
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully!\n")
                return
        print("Contact not found.\n")
def main():
    contact_book = ContactBook()
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
