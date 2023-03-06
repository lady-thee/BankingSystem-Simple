# A BANKING SYSTEM PROGRAM
# A PROGRAM FOR FUNCTION OPERATION

import time
import random
import datetime
import os

username = []
password = []

account = {}


def display(a):
    print(a)


def userinput(x):
    return input(x)


def banner():
    display('WELCOME TO PYTHON BANKING SYSTEM')
    user = userinput('ENTER 1 FOR LOGIN \n 2 FOR REGISTER \n 3 TO QUIT:\n')
    if user == '1':
        display('\n')
        time.sleep(3)
        login()

    elif user == '2':
        display('\n')
        time.sleep(3)
        register()

    elif user == '3':
        display('THANK YOU FOR BANKING WITH US, COME AGAIN...\n GOODBYE!')
        time.sleep(3)
        quit()

    else:
        display('YOU HAVE NOT SELECTED ANY NUMBER')
        time.sleep(3)
        banner()


def register():
    acct = []
    display('WELCOME TO THE REGISTRATION PANEL')
    while True:
        uname = userinput('Enter Username:\n')
        if uname not in username:
            username.append(uname)
            break
        else:
            display('Username already exists... try again')
    userp = userinput('Enter Password:\n')
    password.append(userp)

    acctnumber = ''
    for x in range(10):
        acctnumber += str(random.randint(0, 9))
    acct.append(acctnumber)

    fullname = userinput('Enter Full Name:\n')
    acct.append(fullname)

    while True:
        acctbalance = userinput('Enter Starting Balance:\n')
        if acctbalance.isdigit():
            acctbalance = int(acctbalance)
            acct.append(acctbalance)
            break
        else:
            display('Please Enter Figures Only')

    phone = userinput('Enter phone number:\n')
    acct.append(phone)

    account[uname] = acct

    display('PROCESSING....')
    time.sleep(3)
    display('ACCOUNT CREATED \n A RECEIPT HAS BEEN GENERATED FOR YOU!')

    try:
        file = open('receipt.txt', 'x')
        file.close()
    except FileExistsError:
        pass
    finally:
        file = open('receipt.txt', 'w')
        acctbalance = str(acctbalance)
        timecreated = str(datetime.datetime.now())
        contents =  'CUSTOMER USERNAME:\t\t' + uname + '\n' + '' \
                    'CUSTOMER PASSWORD:\t\t' + userp + '\n' + '' \
                    'CUSTOMER NAME:\t\t' + fullname + '\n' + '' \
                    'CUSTOMER ACCOUNT BALANCE\t\t' + acctnumber + '\n' + '' \
                    'CUSTOMER BALANCE\t\t' + acctbalance + '\n' + '' \
                    'CUSTOMER PHONE\t\t' + phone + '\n' + '' \
                    'Time Created' + timecreated

        file.write(contents)
        file.close()
        time.sleep(1)
        os.startfile('receipt.txt')

        user = userinput('ENTER 1 TO REGISTER AGAIN \n 2  TO LOGIN  \n 3 TO QUIT:')
        if user == '1':
            display('\n')
            time.sleep(3)
            register()

        elif user == '2':
            display('\n')
            time.sleep(3)
            login()

        elif user == '3':
            display('THANK YOU FOR BANKING WITH US, COME AGAIN...\n GOODBYE!')
            time.sleep(3)
            quit()
        else:
            display('You have not selected any thing...')
            banner()


def login():
    display('WELCOME TO LOG IN PANEL')
    if len(username) == 0:
        display('NO USER CREATED YET')
        display('PLEASE CREATE AN ACCOUNT\n')
        time.sleep(2)
        register()
    for x in range(3):
        uname = userinput('Enter username:\n')
        userp = userinput(('Enter password:\n'))
        if uname in username and userp in password:
            display('Login Successful')
            time.sleep(3)
            dashboard(uname)
        else:
            display('INVALID USERNAME OR PASSWORD...TRY AGAIN!')
            break
    display('WE COULD NOT LOCATE ACCOUNT WITH THE DETAILS PROVIDED')
    display('THANKS FOR BANKING WITH US... HAVE A NICE DAY!')
    quit()


def dashboard(user):
    display('USER DASHBOARD')
    display('GOOD DAY' + user)
    user_choice = userinput('ENTER 1 FOR BALANCE 2. FOR DEPOSIT 3. FOR WITHDAWAL 4. FOR TRANSFER 5. TO QUIT')

    if user_choice == '1':
        display('\n')
        time.sleep(3)
        balance(user)

    elif user_choice == '2':
        display('\n')
        time.sleep(3)
        deposit(user)

    elif user_choice == '3':
        display('\n')
        time.sleep(3)
        withdraw(user)

    elif user_choice == '4':
        display('\n')
        time.sleep(3)
        transfer(user)

    elif user_choice == '5':
        display('\n')
        time.sleep(3)
        banner()

    else:
        display('INVALID ENTRY:\n')
        time.sleep(3)
        dashboard(user)


def balance(users):
    actbal = account[users][2]
    display('Balance Console')
    display('YOUR BALANCE WILL BE READY IN A MINUTE')
    display('PROCESSING...')

    time.sleep(3)
    receipt()

    actbal = str(actbal)
    display('ACCOUNT BALANCE: N' + actbal)
    display('\n')
    dashboard(users)


def receipt():
    display('Do you want to have a receipt?')
    rec = userinput('Please type in Yes or No:\t')
    if rec == 'yes':
        display('SORRY NO RECEIPTS AT THE MOMENT')
        time.sleep(3)
    elif rec == 'no':
        display('Please wait...')
        time.sleep(2)
    else:
        display('NO INPUT')


def deposit(users):
    actbal = account[users][2]
    display('DEPOSIT CONSOLE')


    while True:
        price = userinput('Enter amount to deposit:\t')
        if price.isdigit():
            price = int(price)
            if price < 500:
                display('enter amount above 500')
            else:
                break

        else:
            display('enter figures only')
    actbal += price
    display('PROCESSING...')
    account[users][2] = actbal
    time.sleep(1)
    display('TRANSACTION SUCCESSFUL')
    user_choice = userinput('ENTER 1. TO DEPOSIT AGAIN \n 2. TO GO BACK')
    if user_choice == '1':
        time.sleep(3)
        deposit(users)
    elif user_choice == '2':
        display('\n')
        time.sleep(3)
        dashboard(users)
    else:
        display('INVALID INPUT')
        time.sleep(2)
        dashboard(users)


def withdraw(users):
    actbal = account[users][2]
    display('WITHDRAWAL CONSOLE')

    while True:
        price = userinput('Enter amount to withdraw:\t')
        if price.isdigit():
            price = int(price)
            if price > actbal:
                display('INSUFFICIENT FUNDS')
            else:
                break

        else:
            display('enter figures only')
    actbal -= price
    display('PROCESSING...')
    account[users][2] = actbal
    time.sleep(1)
    display('TRANSACTION SUCCESSFUL')
    user_choice = userinput('ENTER 1. TO WITHDRAW AGAIN \n 2. TO GO BACK')
    if user_choice == '1':
        time.sleep(3)
        withdraw(users)
    elif user_choice == '2':
        display('\n')
        time.sleep(3)
        dashboard(users)
    else:
        display('INVALID INPUT')
        time.sleep(2)
        dashboard(users)


def transfer(users):
    display('TRANSFER PANEL')
    actbal = account[users][2]
    while True:
        receiver = userinput('enter account user name: ')
        if receiver in username:
            receiverbal = account[receiver][2]
            break
        else:
            display('invalid account...try again')

    while True:
        price = userinput('Enter amount to transfer:\t')
        if price.isdigit():
            price = int(price)
            if price > actbal:
                display('INSUFFICIENT FUNDS')
            else:
                break

        else:
            display('enter figures only')

    actbal -= price
    receiverbal += price
    display('PROCESSING....')
    account[users][2] = actbal
    account[receiver][2] = receiverbal
    display('TRANSFER SUCCESSFUL...')
    user_choice = userinput('ENTER 1. TO TRANSFER AGAIN \n 2. TO GO BACK')
    if user_choice == '1':
        time.sleep(3)
        transfer(users)
    elif user_choice == '2':
        display('\n')
        time.sleep(3)
        dashboard(users)
    else:
        display('INVALID INPUT')
        time.sleep(2)
        dashboard(users)



# banner()

