# =======================================================================
# Project: Personal Assistant App

# The PersonalAssistant.py file contains the PersonalAssistant class (i.e. "blueprint").
# The PersonalAssistant class contains the app logic and accepts data (json) as arguments from the main.py file.
# =======================================================================


class PersonalAssistant:
    def __init__(self, todos, birthdays, contacts):
        self.todos = todos
        self.birthdays = birthdays
        self.contacts = contacts

    # Adds a new item to the todo list:

    def add_todo(self, new_item):
        if new_item in self.todos:
            return f"{new_item} is already on your to-do list!"
        else:
            self.todos.append(new_item)
            return f"{new_item} has been added to your to-do list!"

    # Removes an item from the todo list:

    def remove_todo(self, todo_item):
        if todo_item in self.todos:
            #Gets the index for the todo_item in the list:
            index = self.todos.index(todo_item)
            #Uses the index to remove the todo_item from the list:
            self.todos.pop(index)
            return f"{todo_item} has been removed from the list!"
        else:
            print("The to-do item is not on the list!")

    # Gets the existing todo list:

    def get_todo(self):
        return self.todos

    # Gets the existing birthdays list:

    def get_birthdays(self):
        return self.birthdays

    # Gets a single birthday from the birthdays list:

    def get_birthday(self, name):
        if name in self.birthdays:
            return f"{name}'s birthday is on {self.birthdays[name]}."
        else:
            return "Can't find a birthday for this person!"

    # Adds a new birthday:

    def add_birthday(self, name, date):
        if name in self.birthdays:
            return f"You already have a birthday for {name} on your list!"
        else:
            self.birthdays[name] = date
            return f"{name}'s birthday has been added to your list!"

    # Removes a birthday:

    def remove_birthday(self, name):
        if name in self.birthdays:
            self.birthdays.pop(name)
            return f"{name}'s birthday has been removed from your list!"
        else:
            return f"Sorry. Could not find this name on your list!"

    # Gets the existing contacts list:

    def get_contacts(self):
        return self.contacts

    # Gets a single contact from the contacts list:

    def get_contact(self, name):
        if name in self.contacts:
            return f"{name}: {self.contacts[name]}"
        else:
            return "There is no contact with that name!"

    # Adds a new contact to the list:

    def add_contact(self, name, job_title):
        if name in self.contacts:
            return f"{name} is already in your contacts!"
        else:
            self.contacts[name] = job_title
            return f"{name} has been added to your contacts!"

    # Removes a contact from the contacts list:

    def remove_contact(self, name):
        if name in self.contacts:
            self.contacts.pop(name)
            return f"{name} has been removed from your contacts list!"
        else:
            return "Sorry. Could not find this name on your list!"
