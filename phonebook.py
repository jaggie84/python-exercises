# Phonebook app
import pickle

book = {}

def load_entries():
    global book
    try:
        with open ('phonebook.pickle', 'rb') as fh:
            book = pickle.load(fh)
    except:
        book = {}
        
load_entries()

def save_entries():
    with open('phonebook.pickle', 'wb') as fh:
        pickle.dump(book, fh)
        


def intro():
    while True:
        print ("""Electronic Phone Book)
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit""")
    #use pickle to save data 
    #use pickle to call saved data
        ans = int(input("Please select a menu option 1-5: "))
        if ans == 1:
            ent = input("Please enter an entry for lookup: ")
            ent = ent.lower()
            load_entries()
            if ent in book:
                print (book[ent])
            else:
                print ("There is no listing for that person.")
        elif ans == 2:
            name = input("Please enter full name: ")
            name = name.lower()
            num = input("Phone number: ")
            email = input("Email: ")
            book[name] = {}
            book[name]['phone'] = num
            book[name]['email'] = email
            save_entries()
            print ('An entry for ' + name.capitalize() + " was saved.")
            
        elif ans == 3:
            name = input("Which entry would you like to delete? ")
            name = name.lower()
            load_entries()
            del book[name]
            print("The entry for", name.capitalize(), "was deleted as requested.")
            save_entries()
        elif ans == 4:
            load_entries()
            for key, value in book.items():
                print ('{}: {}'.format(key, value))
        elif ans == 5:
            print ("Thanks, come again soon!")
            break
        else: 
            print ("Please enter a number 1-5.")

intro()