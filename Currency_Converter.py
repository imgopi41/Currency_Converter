import math     #importing math lib for calculations

print("HI...\nLet's Convert the Currency..!\nWhich Currency would you like to Convert: \n")   #welcome message for user

print("1."'USD')            #USA                    #10 different currencies
print("2."'EUR')            #Euro
print("3."'DINAR')          #Kuwaiti Dinar
print("4."'RIYAL')          #Saudi Arabia
print("5."'WON')            #South Korea
print("6."'BAHT')           #Thailand
print("7."'POUND')          #Uk
print("8."'LIRA')           #Turkish
print("9."'BOLIVAR')        #Venezuela
print("10."'RUBLE','\n')    #Russia

def Currency_Coventer():    #creating a function
    while True:     # While-condition

        Indian_rupee = float(input("Enter the amount in Indian Rupees: "))  #user message to enter amount in indian rupees
        user_currency = input("Enter the Currency you want to convert: ")   #user message to choose any currencies


        if user_currency =="USD":   #if-else condition is applied, Indian rupees is tallied to there respective currencies
            result = Indian_rupee * 76.24
            print(result)

        elif user_currency =="EUR":
            result = Indian_rupee * 84.17
            print(result)

        elif user_currency =="DINAR":
            result = Indian_rupee * 250.87
            print(result)

        elif user_currency =="RIYAL":
            result = Indian_rupee * 20.33
            print(result)

        elif user_currency =="WON":
            result = Indian_rupee * 15.92
            print(result)

        elif user_currency =="BAHT":
            result = Indian_rupee * 2.27
            print(result)

        elif user_currency =="POUND":
            result = Indian_rupee * 100.20
            print(result)

        elif user_currency =="LIRA":
            result = Indian_rupee * 5.14
            print(result)

        elif user_currency =="BOLIVAR":
            result = Indian_rupee * 5631.09
            print(result)

        elif user_currency =="RUBLE":
            result = Indian_rupee * 0.73
            print(result)

        Try_again = input("Do you want to try again(Y/N): ")    #try again input message to the user
        if Try_again.upper() =="Y": #converts lowercase to uppercase
            Currency_Coventer()    #calling a function if try again is "Y".
            print("Thank You....!") #message to user
        break   #breaks the condition if try again is "N".

Currency_Coventer()    #calling a function outside


