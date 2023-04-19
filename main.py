# =======================================================================
# Project: Personal Assistant App
# Description: An interactive app built with Python.
# The app lets users:
# - add, delete, save, and retrieve data.
# Background: Coursework for Skillcrush's "Getting Started with Python" course.

# ==== *** ====

# The main.py file contains the code that manages the logic of/operates the app. It:
# - initiates a new instance of the PersonalAssistant class and passes data to the PersonalAssistant class.
# - retrieves and saves data to json files.
# - handles interaction with the user by promting the user to enter input and by displaying messages to the user.
# =======================================================================

# Imports JSON:
import json

# Imports PersonalAssistant.py file:
from PersonalAssistant import PersonalAssistant

# Opens json file and converts json data to a Python dictionary using load():
# Creates new instance of PersonalAssistant class and passes data from the json file:
with open("todo.json",
          "r") as todos, open("birthdays.json",
                              "r") as birthdays, open("contacts.json",
                                                      "r") as contacts:
    todo_list = json.load(todos)
    birthday_list = json.load(birthdays)
    contact_list = json.load(contacts)
    assistant = PersonalAssistant(todo_list, birthday_list, contact_list)

done = False

while not done:
    user_command = input("""
How can I help you?

    **** To-dos *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list
    **** Birthdays *****
    4: Get a birthday
    5: Add a birthday
    6: Remove a birthday
    **** Contacts *****
    7: Get a single contact 
    8: Add a contact 
    9: Delete a contact 

    Select a number or type 'Exit' to quit: 
    
    """)
    # Add to-do:
    if user_command == "1":
        user_input = input("Item to add to to-do list: ")
        print(f"\n {assistant.add_todo(user_input)}")
    # Remove to-do:
    elif user_command == "2":
        # Prints existing to-do items:
        print("\nYour to-do list: \n")
        for item in assistant.get_todo():
            print(item)
        # Removes to-do item specified by user:
        user_input = input("\nItem to remove from to-do list: ")
        print(f"\n {assistant.remove_todo(user_input)}")
    # Get to-dos:
    elif user_command == "3":
        # Prints existing to-do items:
        print("\nYour to-do list: \n")
        for item in assistant.get_todo():
            print(item)
    # Get birthdays:
    elif user_command == "4":
        # Prints existing birthdays:
        print("\nYour birthday list: \n")
        for name in assistant.get_birthdays():
            print(name)
        # Gets birthday specified by user:
        user_input = input(
            "\nWhich birthday do you want to get from the list: ")
        print(f"\n {assistant.get_birthday(user_input)}")
    # Add birthdays
    elif user_command == "5":
        name = input("\nEnter the name of the person: ")
        birthday = input("\nEnter their birthday (MM/DD/YYYY): ")
        print(f"\n {assistant.add_birthday(name, birthday)}")
    # Remove birthdays
    elif user_command == "6":
        # Prints existing birthdays:
        print("\nYour birthday list: \n")
        for name in assistant.get_birthdays():
            print(name)
        # Removes birthday specified by user:
        user_input = input(
            "\n Enter a name to remove from the birthday list: ")
        print(f"\n {assistant.remove_birthday(user_input)} ")
    # Get contacts:
    elif user_command == "7":
        # Prints existing contacts list:
        print("\nYour contacts list: \n")
        for name in assistant.get_contacts():
            print(name)
        # Gets contact specified by user:
        user_input = input(
            "\nWhich name do you want to get from the contacts list: ")
        print(f"\n {assistant.get_contact(user_input)}")
    # Add contacts:
    elif user_command == "8":
        name = input("\nEnter the name of your new contact: ")
        job_title = input("\nEnter the job title of your new contact: ")
        print(f"\n {assistant.add_contact(name, job_title)}")
    # Remove contacts:
    elif user_command == "9":
        # Prints existing contacts:
        print("\nYour contacts list: \n")
        for name in assistant.get_contacts():
            print(name)
        # Removes contact specified by user:
        user_input = input(
            "\nWhich contact do you want to delete from the list: ")
        print(f"\n {assistant.remove_contact(user_input)}")
    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")

# Saves (writes) to-do, birthday, and contacts data back to the json files:
with open("todo.json", "w") as write_todos, open("birthdays.json",
                                                 "w") as write_birthdays, open(
                                                     "contacts.json",
                                                     "w") as write_contacts:
    json.dump(assistant.get_todo(), write_todos)
    json.dump(assistant.get_birthdays(), write_birthdays)
    json.dump(assistant.get_contacts(), write_contacts)
