

import csv
import time

def chooseOption():
    print('--- --- --- Main Menu --- --- ---')
    option = input('Choose option:\n' \
         '[1] Create new text file\n' \
         '[2] Read text file content\n'
         '[3] Append to text file\n'
         '[4] Search text file\n' \
         '[5] Export to CSV\n' \
         '[6] Exit program\n'
         'option = ')
    return option

option = chooseOption()
while option != '6':
    if option == '1': #Create
        pass #TODO: Implement the Requirement 1 here
        
        try:
            file_name= input("Enter name of your new file: ")
            with open(f"C:\\User\\USERNAME!\\Downloads\\{file_name}.txt",'w') as new_file: #CHANGE 'USERNAME!' TO YOUR DIRECTORY
                pass
        except ValueError:
            print("Please enter a valid file name. Returning to menu")
        except:
            print("an error occured during the CREATE operation!")

    elif option == '2':  # Read
        pass #TODO: Implement the Requirement 2 here

        try: 
            given_file = input("Enter name of existing file for opening: ")
            with open('given_file','r') as existing_file:
                content = existing_file.read()
                print(f'Contents of{given_file}')
                print(content)
        except:
            print("An error occurred during the READ operation!")

    elif option == '3':  # Append
        try:
            pass #TODO: Implement the Requirement 3 here
            given_file = input("Enter name of existing file for appending: ")
            append_input = input("Enter string literals of what will be input:")
            with open('given_file', 'r') as existing_file:
                existing_file.write(append_input)
                print("text has been appended successfully. :3")
        except:
            print("An error has occurred during the APPEND operation!")


    elif option == '4':  # Find
        pass #TODO: Implement the Requirement 4 here
        given_file = input("Enter the file you would like to be searched: ")
        desired_text = input("Enter the string you'd like to be found within the file: ")
        try:
            with open('given_file', 'r') as existing_file:
                text= existing_file.read()
                if desired_text in text:
                    index = text.index(desired_text)
                    print(f"Text found at index {index}.")
                else:
                    print("No results.")
        except:
            print("An error occurred during the FIND operation! ")

    elif option == '5':  # Export
        pass #TODO: Implement the Requirement 5 here
        given_file = input("Enter the name of the file you wish to be read and exported: ")
        new_file = input("Enter the name of the CSV file to which the data will be exported.")
        try:
            with open('given_file', 'r') as pass_file, open(csv_file, 'w', newline='') as csv_file:
                new_file = csv.writer(csv_file, dialect= 'text')
                for line in pass_file:
                    values= line.split()
                    new_file.writerow(values)
        except:
            print("An error occured during the EXPORT operation!")

    else:
        print('Invalid option!')
    time.sleep(1.5)
    print('Going Back to main menu ',end='')
    for i in range(4):
        print('.', end='')
        time.sleep(.4)
    print()
    option = chooseOption()
