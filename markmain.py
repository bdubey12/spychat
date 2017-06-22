#importing the data from different file
from spy_details import spy, Spy, ChatMessage, allies
from steganography.steganography import Steganography
from termcolor import colored

STATUS_MESSAGES = ['Winston, Winston Churchill', 'Diplomacy is the art of telling people to go to hell in such a way that they ask for direction']

#simple python code for display
print (colored("Hello! Let\'s  begin","yellow"))
#string concatenation with help of + symbol
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)

#function is created for adding status
def add_status():

    updated_status_message = None
#use of if-else condition for status checking
    if spy.current_status_message != None:

        print (colored('Your current status message is %s \n',"blue")) % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")
#use of nested if condition for status message
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1
#use of for loop
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

#length of status message is being checked
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message

#function is created for adding ally
def add_ally():

    new_ally = Spy('','',0,0.0)

    new_ally.name = raw_input("Please add your ally's name: ")
    new_ally.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_ally.name = new_ally.salutation + " " + new_ally.name

    new_ally.age = raw_input("Age?")
    new_ally.age = int(new_ally.age)

    new_ally.rating = raw_input("Spy rating?")
    new_ally.rating = float(new_ally.rating)

    if len(new_ally.name) > 0 and new_ally.age > 12 and new_ally.rating >= spy.rating:
        allies.append(new_ally)
        print 'Ally Added!'
    else:
        print 'Sorry! Wrong entry.  Can\'t add spy with the details you provided'

    return len(allies)

#function for selecting ally
def select_a_ally():
    item_number = 0
#use of for loop
    for ally in allies:
#use of placeholders instead of string concatenation
        print '%d. %s %s aged %d with rating %.2f is online' %(item_number +1, ally.salutation, ally.name, ally.age,
                                                        ally.rating)
        item_number = item_number + 1

    ally_choice = raw_input("Choose from your allies")

    ally_choice_position = int(ally_choice) - 1

    return ally_choice_position

#function for sending message
def send_message():

    ally_choice = select_a_ally()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)

    allies[ally_choice].chats.append(new_chat)

    print " Secret message image is ready!"

#function for reading message
def read_message():

    sender = select_a_ally()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    allies[sender].chats.append(new_chat)

    print "Your secret message has been saved!"

#function for reading chat history
def read_chat_history():

    read_for = select_a_ally()

    print '\n6'

    for chat in allies[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), allies[read_for].name, chat.message)

#function for starting chat
def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:


        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_allies = add_ally()
                    print 'You have %d allies' % (number_of_allies)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

if existing == "Y":
    start_chat(spy)
else:

    spy = Spy('','',0,0.0)


    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid spy name'
