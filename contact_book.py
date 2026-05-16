contacts = {}
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact Added Successfully!")
    elif choice == "2":
        if contacts:
            print("\n--- Saved Contacts ---")
            for name, details in contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {details['Phone']}")
                print(f"Email: {details['Email']}")
                print(f"Address: {details['Address']}")
        else:
            print("No contacts available.")
    elif choice == "3":
        search = input("Enter Name to Search: ")

        if search in contacts:
            print("\nContact Found!")
            print(f"Name: {search}")
            print(f"Phone: {contacts[search]['Phone']}")
            print(f"Email: {contacts[search]['Email']}")
            print(f"Address: {contacts[search]['Address']}")
        else:
            print("Contact not found.")

    elif choice == "4":
        update = input("Enter Name to Update: ")

        if update in contacts:
            phone = input("Enter New Phone Number: ")
            email = input("Enter New Email: ")
            address = input("Enter New Address: ")

            contacts[update] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }

            print("Contact Updated Successfully!")
        else:
            print("Contact not found.")
    elif choice == "5":
        delete = input("Enter Name to Delete: ")

        if delete in contacts:
            del contacts[delete]
            print("Contact Deleted Successfully!")
        else:
            print("Contact not found.")
    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid Choice. Please try again.")