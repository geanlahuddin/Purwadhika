from tabulate import tabulate
from operator import itemgetter

# DATA LIST
contact_list = [
    {'ContactID': 'polrestabandung', 'Sector':'Keamanan', 'Name': 'Polresta Bandung', 'Contact': '02285871980', 'Email':'polresbandung@polri.go.id','Address':'Jalan Trunojoyo No.3'},
    {'ContactID': 'pemkabbandung', 'Sector':'Pemerintahan', 'Name': 'Pemkab Bandung', 'Contact': '02289785467', 'Email':'pemkabbandung@bandungkab.go.id','Address':'Jalan Raya Soreang KM 17 No. 212'},
    {'ContactID': 'puskesmasbaleendah', 'Sector':'Kesehatan', 'Name': 'Puskesmas Baleendah', 'Contact': '02287951454', 'Email':'puskesmasbaleendah@gmail.com','Address':'Jalan Raya Banjaran No. 241'},
]

## READ DATA FUNCTION
def read_data():
    print(tabulate(contact_list, headers='keys', tablefmt='pretty'))

## VIEW CONTACT MENU (READ DATA)
def view_menu():
    submenu_view = int(input('''
    Sub Menu View Contact
    
    1. Show All Contact
    2. Contact Information By ID
    0. Back to Main Menu
    
    Choose Menu Number: 
    '''))

    if submenu_view == 1:
        read_data()
    elif submenu_view == 2:
        while True:
            read_data()
            contID = input("Please input ContactID: ")
            found = True
            for i in range(len(contact_list)) :
                if contID == contact_list[i]['ContactID']:
                    print(f'\nInformation About Contact with ContactID: {contID} : ')
                    print(f"\nName             \t: {contact_list[i]['Name']}")
                    print(f"Sector             \t: {contact_list[i]['Sector']}")
                    print(f"Contact    \t\t: {contact_list[i]['Contact']}")
                    print(f"Email             \t: {contact_list[i]['Email']}")
                    print(f"Address            \t: {contact_list[i]['Address']}") 
                    main()
                else:
                    found = False
            if found is False:
                print("ContactID not Found. Please try again") #Keluar output contactID not found 3 baris. Minta tolong feedbacknya
            else:
                print('Invalid Input. Try again')
    elif submenu_view == 0:
        main()
    else:
        print('Invalid input. Try again')

    
# FIND CONTACT MENU (FILTERING DATA)
def find_contact():
    submenu_find = int(input('''
    Sub Menu Find Contact:
    
    1. By Sector
    2. By Name
    0. Back to main menu
    
    Choose Menu Number: 
    '''))
    if submenu_find == 1:
        while True:
            sector_find = input('Please enter contact sector: ')
            if sector_find.replace(' ','').isalpha() == True:
                sector_find = sector_find.title()
                found = True
                for i in range(len(contact_list)) :
                    if sector_find == contact_list[i]['Sector']:
                        print(f'Contact {sector_find} : ')
                        print(f"\nSector             \t: {contact_list[i]['Sector']}")
                        print(f"Name             \t: {contact_list[i]['Name']}")
                        print(f"Contact    \t\t: {contact_list[i]['Contact']}")
                        print(f"Email             \t: {contact_list[i]['Email']}")
                        print(f"Address            \t: {contact_list[i]['Address']}")
                        print(f'\nInformation about contact with Sector: {sector_find}')
                        main()
                    else: 
                        found = False
                if found is False:
                    print(f"Wrong contact sector. Please input the right contact name \n")
            else:
                print('Invalid Input. Try again')
    elif submenu_find == 2:
        while True:
            name_find = input('Please input contact name: ')
            if name_find.replace(' ','').isalpha() == True:
                name_find = name_find.title()
                found = True
                for i in range(len(contact_list)) :
                    if name_find == contact_list[i]['Name']:
                        print(f'Contact {name_find} : ')
                        print(f"\nSector             \t: {contact_list[i]['Sector']}")
                        print(f"Name             \t: {contact_list[i]['Name']}")
                        print(f"Contact    \t\t: {contact_list[i]['Contact']}")
                        print(f"Email             \t: {contact_list[i]['Email']}")
                        print(f"Address            \t: {contact_list[i]['Address']}")
                        print(f'\nInformation about contact with Name: {name_find}')
                        main()
                    else : 
                        found = False
                if found is False:
                    print(f"Wrong contact Name. Please input the right contact name") 
            else:
                print('Invalid Input. Try again')
    elif submenu_find == 0:
        main()
    else:
        print('Please input the right menu')

# Validation Phone Number
import regex
def validate_phone_number(number):
    pattern = r"\d{10,12}"
    match = regex.match(pattern, number)
    return match is not None

def get_valid_phone_number():
    while True:
        user_input = input("Enter a phone number (10 - 12 digits): \n")
        if validate_phone_number(user_input):
            print("Valid phone number. Thank you!\n")
            return(user_input)
            break
        else:
            print("Invalid phone number. Please try again.\n")

# Validation Email
def validate_email(surel):
    pattern = r'\b\w+(?:\.*\w*\d*){2,}\@\w+\.+\w+(?:\.*\w*){2,}\b'
    match = regex.match(pattern, surel)
    return match is not None

def get_valid_email():
    while True:
        user_input = input("Please Input your new contact email: \n")
        if validate_email(user_input):
            print("Valid Email. Thank you!\n")
            return(user_input)
            break
        else:
            print("Invalid email format. Please try again.\n")

# Validation Name
def validate_sector():
    while True:
        user_input = input('Please enter contact sector: ')
        if user_input.isalpha() == True:
            return(user_input)
            break
        else:
            print('Invalid input. Please try again and only use alphabet')

# Validation Name
def validate_name():
    while True:
        user_input = input('Please input contact name: ')
        if user_input.replace(' ','').isalpha() == True:
            return(user_input)
            break
        else:
            print('Invalid input. Try agan and only use alphabet')

# ADD CONTACT MENU (CREATE DATA)
def add_contact():
    submenu_add = int(input('''
    Sub Menu Add Contact
    1. Add Contact
    0. Back to Main Menu

    Choose Menu Number: 
    '''))
   
    if submenu_add == 1:
        while True:
            input_nama = input('Enter New Contact Name: ')
            new_contact = input_nama.replace(' ', '')
            for i in range(len(contact_list)):
                if new_contact.lower() in contact_list[i]['ContactID']:
                    print('Contact Already Listed')
                    break
                else:
                    print('Fill in your new contact information!')
                    new_sector = validate_sector().title()
                    new_name = input_nama.title()
                    new_numb = get_valid_phone_number()
                    new_email = get_valid_email()            
                    new_addres = input('Input contact addres: \n').capitalize()
                    new_id = new_name.replace(' ','').lower()

                    confirm = input('Save Data? (Y/N) : \n').capitalize()
                    if confirm == 'Y':
                        contact_list.append({
                            'ContactID' : new_id,
                            'Sector': new_sector,
                            'Name' : new_name,
                            'Contact' : new_numb,
                            'Email' : new_email,
                            'Address' : new_addres
                        })
                        read_data()
                        print('Your new contact saved!')
                        main()
                    elif confirm == 'N':
                        print('\n Your new contact is not saved. You will back to main menu')
                        main()
                    else:
                        print('Choose Y/N. We lost your new contact data, please Re-input') 
            else:
                print('Choose Y/N. We lost your new contact data, please Re-input')      
    elif submenu_add == 0:
        main()
    else:
        print('Invalid input. Try again')


# EDIT CONTACT MENU (UPDATE DATA)
def edit_contact():
    submenu_edit = int(input('''
    Sub Menu Edit Contact
    1. Edit Contact
    0. Back to Main Menu

    Choose Menu Number: 
    '''))

    if submenu_edit == 1:
        read_data()
        while True:
            edit_input = input('Choose ContactID that will be edited: \n')
            for i in range(len(contact_list)):
                while True:
                    if edit_input == contact_list[i]['ContactID']:
                        opsi_edit = int(input('''
                        Column that can be edited 
                        1. Sector
                        2. Name
                        3. Contact
                        4. Email
                        5. Addres

                        Choose column you will be edited: 
                        '''))
                        if opsi_edit == 1: #Edit Sector
                            sector_edit = input('Input new sector: \n').title()
                            confirm_edit = input('Are you sure want to edited data? Choose (Y/N)\n').capitalize()
                            if confirm_edit =='Y':
                                contact_list[i]['Sector'] = sector_edit
                                read_data()
                                print('Contact Edit Successfully')
                                main()
                            elif confirm_edit =='N':
                                print('Contact not edited')
                            else:
                                print('Invalid input. Try again')
                        
                        elif opsi_edit == 2: #Edit Name
                            name_edit = validate_name().title()
                            confirm_edit = input('Are you sure want to edited data? Choose (Y/N)\n').capitalize()
                            if confirm_edit =='Y':
                                contact_list[i]['Name'] = name_edit
                                contact_list[i]['ContactID'] = name_edit.replace(' ','').lower()
                                read_data()
                                print('Contact Edit Successfully')
                                main()
                            elif confirm_edit =='N':
                                print('Contact not edited')
                            else:
                                print('Invalid input. Try again')
                        
                        elif opsi_edit == 3: #Edit Contact
                            numb_edit = get_valid_phone_number()
                            confirm_edit = input('Are you sure want to edited data? Choose (Y/N)\n').capitalize()
                            if confirm_edit =='Y':
                                contact_list[i]['Contact'] = numb_edit
                                read_data()
                                print('Contact Edit Successfully')
                                main()
                            elif confirm_edit =='N':
                                print('Contact not edited')
                            else:
                                print('Invalid input. Try again')
                        
                        elif opsi_edit == 4: #Edit Email
                            email_edit = get_valid_email()
                            confirm_edit = input('Are you sure want to edited data? Choose (Y/N)\n').capitalize()
                            if confirm_edit =='Y':
                                contact_list[i]['Email'] = email_edit
                                read_data()
                                print('Contact Edit Successfully')
                                main()
                            elif confirm_edit =='N':
                                print('Contact not edited')
                            else:
                                print('Invalid input. Try again')   
 
                        elif opsi_edit == 5: #Edit Address
                            address_edit = input('Input new address: \n')
                            confirm_edit = input('Are you sure want to edited data? Choose (Y/N)\n').capitalize()
                            if confirm_edit =='Y':
                                contact_list[i]['Address'] = address_edit
                                read_data()
                                print('Contact Edit Successfully')
                                main()
                            elif confirm_edit =='N':
                                print('Contact not edited')
                            else:
                                print('Invalid input. Try again')                    
                        else:
                            print('Invalid input. Try again')                         
                    else:
                        print('ContactID not found. Try again') 
                        break
                    
    elif submenu_edit == 0:
        main()
    else:
        print('Invalid input. Try again')
                
                        
## DELETE CONTACT MENU (DELETE DATA)
def delete_contact():
    submenu_del = int(input('''
    Sub Menu Delete Contact
    1. Delete Contact
    0. Back to Main Menu

    Choose Menu Number: 
    '''))
    if submenu_del == 1:
        read_data()
        while True:
            del_input = input('Choose ContactID that will be deleted: \n')
            for i in range(len(contact_list)):
                if del_input == contact_list[i]['ContactID']:
                    confirmDel = input(f'Are you sure want to deleted Contact with ContactID {del_input}? Choose (Y/N)\n').capitalize()
                    if confirmDel == 'Y':
                        del contact_list[i]
                        read_data()
                        print(f'\nContactID {del_input} deleted successfully')
                        main()
                    elif confirmDel == 'N':
                        print('\nContact not deleted. You will back to main menu')
                        main()
                    else:
                        print('Invalid Input. Please try again.')
    elif submenu_del == 0:
        main()
    else:
        print('Invalid input. Please try again')

def main():
    while True:
        try:
            print('''
            
            Main Menu
            1. View All Contact
            2. Find Contact
            3. Add New Contact
            4. Edit Contact
            5. Delete Contact
            0. Exit
            ''')

            opsi = int(input('Choose Menu: '))
            if opsi == 1:
                view_menu()
            elif opsi == 2:
                find_contact()
            elif opsi == 3:
                add_contact()
            elif opsi == 4:
                edit_contact()
            elif opsi == 5:
                delete_contact()
            elif opsi == 0:
                print('Thank you, See you later!')
                break
            else:
                print('Your Input is not valid!')
        except:
            print('Input the right menu number. Try again')
main()