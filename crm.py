from contact import Contact
import sys
class CRM:
    attributes = {'first name': 'first_name', 'last name': 'last_name'}
    def main_menu(self):
        while True: # repeat indefinitely
            self.print_main_menu()
            user_selected = int(input())
            self.call_option(user_selected)

    def print_main_menu(self):
        print('[1] Add a new contact')
        print('[2] Modify an existing contact')
        print('[3] Delete a contact')
        print('[4] Display all the contacts')
        print('[5] Search by attribute')
        print('[6] Exit')
        print('Enter a number: ')

    def call_option(self, user_selected):
        if user_selected == 1:
            self.add_new_contact()
        elif user_selected == 2:
            self.modify_existing_contact()
        elif user_selected == 3:
            self.delete_contact()
        elif user_selected == 4:
            self.display_all_contacts()
        elif user_selected == 5:
            self.search_by_attribute()
        elif user_selected == 6:
            print('Have a nice day :)')
            sys.exit()
    
    def add_new_contact(self):
        # get all the required info from our user:
        print('Enter First Name: ')
        first_name = input()

        print('Enter Last Name: ')
        last_name = input()

        print('Enter Email Address: ')
        email = input()

        print('Enter a Note: ')
        note = input()

        # call the appropriate method from the contact class (remember we imported it?):
        contact = Contact.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            note=note
            )

    def modify_existing_contact(self):
        updated = False
        contact_id = int(input('Whose contact do you wish to edit? (type in ID please) '))
        while not updated:
            print('[1] First Name')
            print('[2] Last Name')
            print('[3] Email')
            print('[4] Note')
            mod_choice = input('What would you like to change? ')
            if int(mod_choice) >= 1 and int(mod_choice) <= 4:
                mod_contact = Contact.get(id= contact_id)
                if int(mod_choice) == 1:
                    first_name_change = input('What would you like to change the first name to?: ')
                    mod_contact.first_name = first_name_change
                    mod_contact.save()
                    updated = True
                elif int(mod_choice) == 2:
                    last_name_change = input('What would you like to change the last name to?: ')
                    mod_contact.last_name = last_name_change
                    mod_contact.save()
                    updated = True
                elif int(mod_choice) == 3:
                    email_change = input('What would you like to change the email to?: ')
                    mod_contact.email = email_change
                    mod_contact.save()
                    updated = True
                elif int(mod_choice) == 3:
                    note_change = input('What would you like to change the note to?: ')
                    mod_contact.note = note_change
                    mod_contact.save()
                    updated = True
            else:
                print('Please enter one of the following numbers')


    def delete_contact(self):
        contact_id = int(input('Whose contact do you wish to edit? (type in ID please) '))
        del_contact = Contact.get(id= contact_id)
        del_contact.delete_instance()
        
    def display_all_contacts(self):
        print('')
        for contact in Contact.select():
            print(contact.first_name)
        print('')
    
    def search_by_attribute(self):
        searched = False
        while not searched:
            searched_attribute = (input('What do you want to search by?: '))
            if searched_attribute == 'exit':
                break
            search_attribute_variable = input('Please enter the search term: ')
            if searched_attribute == 'first_name':
                searched_contact = Contact.get(first_name = search_attribute_variable)
            elif searched_attribute == 'last_name':
                searched_contact = Contact.get(last_name = search_attribute_variable)
            elif searched_attribute == 'email':
                searched_contact = Contact.get(email = search_attribute_variable)
            if searched_contact:
                print('')
                print(searched_contact)
                print('')
                searched = True



                
a_crm_app = CRM()
a_crm_app.main_menu()