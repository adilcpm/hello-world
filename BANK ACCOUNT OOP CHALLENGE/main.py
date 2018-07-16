import time

accountlist = [["None","None"]]
banking = True

def readlist():
    with open('BANK ACCOUNT OOP CHALLENGE\\account-list.txt','r') as filehandle:
        content = filehandle.readlines()
        for line in content:
            item = line.split()
            item[1] = int(item[1])
            accountlist.append(item)

def writelist():
    with open('BANK ACCOUNT OOP CHALLENGE\\account-list.txt','w') as filehandle:
        for item in accountlist:
            if item[0] == "None" and item[1] == "None":
                pass
            else:
                filehandle.writelines(f"{item[0]} {item[1]}\n")

def closeacc(accnum):
    try:
        if accountlist[accnum][0] != "None":
            accountlist[accnum][1] = "Closed_Account,owner:_"+ accountlist[accnum][0]
            accountlist[accnum][0] = "None"
            print(accountlist[accnum][1])
            print("\n\nYour Account was succesfully Deleted ! ")
        else:
            print("\n\nNo Account Found ")
        again()
    except IndexError:
        print("\n\nNo account found !")
        again()

def again():
    try:
        againvar=input("\n\nDo you want to use the bank again? Y for Yes, N for No : " ).upper()
        if againvar =='Y':
            bank()
        elif againvar =='N':
            close()
        else:
            print("Choose again")
            again()
    except ValueError:
        print("\n\nTry again !")

def close():
    global banking
    print("\n\nHave a good day ! ")
    writelist()
    banking = False

def accounts(token):
    if token == 1:
        name = input("\n\nWhat is your name ? : ")
        startingbalance = int(input("\n\nHow much do you wanna deposit (type 0 for no starting deposit) ? : "))
        accountlist.append([name,startingbalance])
        print(f"\n\n\nYour Account Number is : {len(accountlist)-1} \n\nPlease take care of the Account Number\nit is used to Access your account and Close your account")
        time.sleep(5)
        again()

    elif token == 2:
        transact(int(input("\n\nEnter your account Number : ")))
    
    elif token == 3:
        print("\n\nYou are about to close your account ! ")
        lastcheck = input("Are you sure ? Y for Yes, N for No : ").upper()
        if lastcheck == 'Y':
            closeacc(int(input("\n\nEnter your account number : ")))
        elif lastcheck == 'N':
            bank()
        else:
            print("Invalid input, try again. ")
            accounts(token)

    else:
        print("\n\nYou have chosen an invalid option, try again.")
        try:
            accounts(int(input("\n\n1 - New Account\n2 - Use Existing Account\n3 - Close Account\n\n")))
        except ValueError:
            print("\n\nYou have chosen an invalid option, try again.")

def bank():
    print("\n\n\n\n\n\n\n\n\n\nWelcome the the Python Bank \n\nWhat do you wanna do for today?")
    accounts(int(input("\n\n1 - New Account\n2 - Use Existing Account\n3 - Close Account\n\n")))

def transact(accnum):
    try:    
        if accountlist[accnum][0] == "None":
            print("\n\nNo account found, try again. ")
            time.sleep(5)
            bank()
        else:
            token = int(input("\n\n1 - Account Info\n2 - Balance\n3 - Deposit\n4 - Withdraw\n\n"))
            try:
                if token==1:
                    print(f"\n\nAccount owner : {accountlist[accnum][0]}\nAccount balance : {accountlist[accnum][1]}")
                    again()
            
                elif token==2:
                    print(f"\n\nAccount balance : {accountlist[accnum][1]}")
                    again()

                elif token==3:
                    deposit = int(input("\n\nHow much you want to deposit ? : "))
                    accountlist[accnum][1] += deposit
                    print(f"\nDeposit Successful !\nNew Balance : {accountlist[accnum][1]}")
                    again()

                elif token==4:
                    withdraw = int(input("\n\nHow much you want to withdraw ? : "))
                    if withdraw > accountlist[accnum][1]:
                        print("\n\nInsuffiecient Funds !")
                    elif withdraw < accountlist[accnum][1]:
                        accountlist[accnum][1] -= withdraw
                        print(f"\nWithdrawal Successful !\nNew Balance : {accountlist[accnum][1]}")
                    again()
            
                else:
                    print("\n\nChoose between the options .")
                    transact(accnum)
        
            except ValueError:
                print("You have chosen an invalid option, try again.")

    except IndexError:
        print("\n\nNo account found, try again.")
        time.sleep(5)
        bank()
    except ValueError:
        print("\n\nYou are supposed to enter a account number, try again.")

readlist()
while banking == True:
    bank()