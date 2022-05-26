import math     #importing math lib for calculations

print("HI...\nLet's Convert the Currency..!\nWhich Currency would you like to Convert: \n")   #welcome message for user

print("1."'USD',"\t\t\tUS Currency")
print("2."'EUR',"\t\t\tEuro Currecny")
print("3."'DINAR',"\t\tKuwait Currency")
print("4."'RIYAL',"\t\tSaudi Arabia Currency")
print("5."'WON',"\t\t\tSouth Korea Currency")
print("6."'BAHT',"\t\t\tThailand Currency")
print("7."'POUND',"\t\tUk Currency")
print("8."'LIRA',"\t\t\tTurkish Currency")
print("9."'BOLIVAR',"\t\tVenezuela Currency")
print("10."'RUBLE',"\t\tRussia Currency",'\n')

def Currency_Coventer():    #creating a function

    while True:     # While-condition

        
        user_currency = input("\nChoose any one above Currency you want to convert: ")   #user message to choose any currencies
        Indian_rupee = float(input("Enter the amount in Currencies: "))  # user message to enter amount in indian rupees
        ans = user_currency
        print("This is amount in Indian rupees")

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

        Try_again = input("\nDo you want to try again(Y/N): ")    #try again input message to the user
        if Try_again.upper() =="Y": #converts lowercase to uppercase
            Currency_Coventer()    #calling a function if try again is "Y".
            print("Thank You....!") #message to user
        break   #breaks the condition if try again is "N".

Currency_Coventer()    #calling a function outside


