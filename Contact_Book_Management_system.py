import os

FILE_PATH = 'contacts.txt'

def load_contacts():
    contacts = {}
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            for line in file:
                name, email, phone, address = line.strip().split('|')
                contacts[name] = {'Email': email, 'Phone': phone, 'Address': address}
    return contacts



def Save_Contacts(contacts):
    with open(FILE_PATH, 'w') as file:
        for name, details in contacts.items():
            file.write(f"{name}|{details['Email']}|{details['Phone']}|{details['Address']}\n")


def Add_Contact(contacts):
    name=input("Enter Your Name: ")
    email=input("Enter Your Email: ")
    phone=input("Enter Your Phone Number: ")
    address=input("Enter Your Address: ")

    if phone in [details['Phone'] for details in contacts.values()]:
        print(" Duplicate phone number!")
        return
    contacts[name]={'Email':email,'Phone':phone,'Address':address}
    print("Contact added successfully")
    

def View_Contact(contacts):
    if contacts:
        print("\nContact List:")
        for name,details in contacts.items():
            print(f"Name:{name}, Email:{details['Email']}, Phone:{details['Phone']}, Address:{details['Address']}")


def Remove_Contact(contacts):
    name = input("Enter the name of the contact to remove: ")
    if name in contacts:
        del contacts[name]
        print("Contact removed successfully!")
    else:
        print("Error: Contact not found!")



def Search_Contact(contacts):
    keyword=input("Enter keyword to search: ").lower()
    results=[]
    for name,details in contacts.items():
        if keyword in name.lower() or any(keyword in str(value).lower() for value in details.values()):
            results.append(f"Name: {name}, Email: {details['Email']}, Phone: {details['Phone']}, Address: {details['Address']}")

    if results:
        print("\n Search List: ")
        for result in results:
            print(result)

    else:
        print("No matching contact found")



contacts=load_contacts()


while True:
    print("\n\n********WELCOME TO MY CONTACT BOOK MANAGEMENT SYSTEM********")
    print("\n1.Add Contact")
    print("2.View Contact")
    print("3.Remove Contact")
    print("4.Search Contact")
    print("5.Exit")


    option=input("Enter you choose option: ")


    if option=='1':
        Add_Contact(contacts)
        Save_Contacts(contacts)

    elif option=='2':
        View_Contact(contacts)

    elif option=='3':
        Remove_Contact(contacts)
        Save_Contacts(contacts)

    elif option=='4':
        Search_Contact(contacts)

    elif option=='5':
        print("Thank you for using this program...")
        break
    else:
        print("Invilid choices..")
