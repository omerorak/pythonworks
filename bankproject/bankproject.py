"""
Python is a program for obtaining bank card password and card and seeing information by entering the system ...
Bank Card Number Anatomy : 5304 4642 1234 5678

1- The first number indicates the type of card (1,2 = boarding cards; 3 = travel tourist cards; 4,5 = banking debit cards; 6 = business cards; 7 = oil companies; 8 = telecommunications companies; 9 = national duty)
2- First 6 digits bank identification number
3- 7-15 digits account identification number
4- Last digit control number
"""
import time
import random
import json
import datetime

def bank():
    while True:
        print("Welcome to Interbank Card Center(ICC)")
        print("What action do you want to do?")
        start = int(input("1-Account transactions \n2-Personal card application \n3-Corporate card application \n4-Exit \nYour Choose = "))

        if start ==1:
            cardnumber = input("Enter your card number : ")
            liste1 = []
            for i in cardnumber :
                liste1.append(i)
            if len(liste1) != 16:
                print("You entered your card number incorrectly !")
                time.sleep(3)
                continue
            elif len(liste1) == 16:
                password   = input("Enter your password : ")
                liste2 = []
                for i in password :
                    liste2.append(i)
                cardnumber = int(cardnumber)
                password = int(password)

                if len(liste2) != 4:
                    print("You entered your password incorrectly !")
                    time.sleep(3)
                    continue
                elif len(liste2) == 4:
                    customernumber = int(input("Enter your customernumber : "))
                    try:
                        while True:
                            with open(f"{customernumber}.json") as f:
                                data = json.load(f)
                                print(f"Welcome {data['name']} {data['surname']}")
                                print("Account Balance = ",data["balance"]," TL")
                                time.sleep(5)
                                print("What action do you want to do?")
                                operation = int(input("1-Withdraw Money \n2-Deposit Money \n3-View Account Balance \n4-Send money to another account\n5-Return Main Menu \nYour Choose : "))
                                if operation ==1:
                                    if(data["balance"]<=0):
                                        print(f"There is not enough balance in your account :( Your current balance = {data['balance']}")

                                    elif(data["balance"]>0):
                                        withdrawmoney = int(input("Enter the amount you want to withdrawmoney : "))
                                        newbalance = data["balance"]
                                        lastbalance = newbalance-withdrawmoney
                                        customernumber2 = customernumber
                                        lastinfo = {
                                            "cardnumber" : cardnumber,
                                            "password"   : password,
                                            "customernumber" : customernumber,
                                            "balance" : lastbalance,
                                            "name" : data["name"],
                                            "surname" : data["surname"]
                                        }
                                        with open(f"{customernumber2}.json","w") as f:
                                            json.dump(lastinfo,f)
                                        print(f"Your account balance : {lastbalance}")
                                        print("Your withdrawal has been successfully processed :)")
                                        continue
                                                                            

                                elif operation ==2:
                                    depositmoney = int(input("Enter the amount you want to deposit : "))
                                    newbalance = data["balance"]
                                    lastbalance = newbalance+depositmoney
                                    customernumber2 = customernumber
                                    lastinfo = {
                                        "cardnumber" : cardnumber,
                                        "password"   : password,
                                        "customernumber" : customernumber,
                                        "balance" : lastbalance,
                                        "name" : data["name"],
                                        "surname" : data["surname"]
                                    }
                                    with open(f"{customernumber2}.json","w") as f:
                                        json.dump(lastinfo,f)
                                    print(f"Your account balance : {lastbalance}")
                                    print("Your deposit has been successfully processed :)")
                                    continue

                                elif operation ==3:
                                    print("Account Balance = ",data["balance"]," TL")
                                    time.sleep(5)
                                    continue

                                elif operation ==4:
                                    receivercustomernumber = int(input("Enter the customer number of the person you want to send money to : "))
                                    receivercardnumber = int(input("Enter the card number of the person you want to send money to : "))                                   
                                    sendmoney = int(input("Amount of money to send : "))
                                    if (data["balance"]-sendmoney)<0:
                                        print("You do not have sufficient funds for this transaction ! You are directed to the main menu ...")
                                        time.sleep(3)
                                        continue
                                    elif (data["balance"]-sendmoney)>0:
                                        lastbalance = data["balance"]-sendmoney
                                        customernumber2 = customernumber
                                        lastinfo = {
                                            "cardnumber" : cardnumber,
                                            "password"   : password,
                                            "customernumber" : customernumber,
                                            "balance" : lastbalance,
                                            "name" : data["name"],
                                            "surname" : data["surname"]
                                        }
                                        with open(f"{customernumber2}.json","w") as f:
                                            json.dump(lastinfo,f)

                                        with open(f"{receivercustomernumber}.json") as f:
                                            dataa = json.load(f)

                                        lastinfo2 = {
                                            "cardnumber" : receivercardnumber,
                                            "password"   : dataa["password"],
                                            "customernumber" : receivercustomernumber,
                                            "balance" : sendmoney,
                                            "name" : dataa["name"],
                                            "surname" : dataa["surname"]
                                        }
                                        with open(f"{receivercustomernumber}.json","w") as f:
                                            json.dump(lastinfo2,f)

                                        print("Sending money is successful ,you are directed to the main menu ... ")
                                        time.sleep(3)
                                        continue

                                elif operation ==5:
                                    break
                            

                                else :
                                    print("You dialed incorrectly or incorrectly, you are directed to the main menu ...")
                                    time.sleep(3)
                                    continue
                            


           
                    except IOError:
                        print("Customer not found.You are taken to the main menu ...")
                        time.sleep(3)
                        continue



        elif start==2:
            print("Select the card type you want to apply : ")
            cardtype = int(input("1-Airlines Card \n2-Travel and Entertainment Card \n3-Banking and Credit Card \nYour Choose : "))
            print("Select the bank you want to apply for a card : ")
            bankname = int(input("1-HSBC \n2-GarantiBBVA \n3-DeutscheBank \n4-Akbank \nYour Choose : "))
            password = input("Set Your Password (Must be 4 digits) : ")
            liste = []
            for i in password :
                liste.append(i)
            if len(liste) ==4:
                if cardtype ==1:
                    typenumber = "1"
                    if bankname ==1:
                        bankid = "21042"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }
                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==2:
                        bankid = "15092"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==3:
                        bankid = "23021"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==4:
                        bankid = "09091"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                elif cardtype ==2:
                    typenumber = "3"
                    if bankname ==1:
                        bankid = "21042"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==2:
                        bankid = "15092"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==3:
                        bankid = "23021"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==4:
                        bankid = "09091"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                elif cardtype ==3:
                    typenumber = "4"
                    if bankname ==1:
                        bankid = "21042"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==2:
                        bankid = "15092"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==3:
                        bankid = "23021"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==4:
                        bankid = "09091"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

            elif len(liste) !=4:
                print("Password must be 4 digits !")
                time.sleep(3)
                continue

            

        elif start==3:
            print("Select the card type you want to apply : ")
            cardtype = int(input("1-Commercial Banking Cards \n2-Petroleum Companies Card \n3-Telecommunications Companies Card \n4-National Assignment Card \nYour Choose : "))
            print("Select the bank you want to apply for a card : ")
            bankname = int(input("1-HSBC \n2-GarantiBBVA \n3-DeutscheBank \n4-Akbank \nYour Choose : "))
            password = input("Set Your Password (Must be 4 digits) : ")
            liste = []
            for i in password :
                liste.append(i)
            if len(liste) ==4:
                if cardtype ==1:
                    typenumber = "6"
                    if bankname ==1:
                        bankid = "21042"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==2:
                        bankid = "15092"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==3:
                        bankid = "23021"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==4:
                        bankid = "09091"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                elif cardtype ==2:
                    typenumber = "7"
                    if bankname ==1:
                        bankid = "21042"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==2:
                        bankid = "15092"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==3:
                        bankid = "23021"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==4:
                        bankid = "09091"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                elif cardtype ==3:
                    typenumber = "8"
                    if bankname ==1:
                        bankid = "21042"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==2:
                        bankid = "15092"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==3:
                        bankid = "23021"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==4:
                        bankid = "09091"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                elif cardtype ==3:
                    typenumber = "9"
                    if bankname ==1:
                        bankid = "21042"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==2:
                        bankid = "15092"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==3:
                        bankid = "23021"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

                    elif bankname ==4:
                        bankid = "09091"
                        name = input("What is your name ? : ")
                        surname = input("What is your surname ? : ")
                        customerid=str(random.randint(1000000000,9999999999))
                        cardnumber = int(typenumber+bankid+customerid)
                        customernumber = random.randint(100000,999999)
                        customerinformation = {
                            "cardnumber" : cardnumber,
                            "password"   : password,
                            "customernumber" : customernumber,
                            "balance" : 0,
                            "name" : name,
                            "surname" : surname
                        }

                        with open(f"{customernumber}.json","a") as f:
                            json.dump(customerinformation,f)
                        print(f"Account Information : \nCardNumber = {cardnumber} \nCustomerNumber = {customernumber} \nPassword = {password} ")
                        time.sleep(5)
                        print("Your account has been successfully created. You are taken to the main menu ...")
                        time.sleep(3)

            elif len(liste) !=4:
                print("Password must be 4 digits !")
                time.sleep(3)
                continue

        elif start==4:
            print("Your exit from the system is being carried out ...")
            time.sleep(3)
            break

        else:
            print("You dialed incorrectly or incorrectly, you are directed to the main menu ...")
            time.sleep(3)
            continue

bank()