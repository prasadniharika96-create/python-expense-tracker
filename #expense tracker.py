#expense tracker

expense =[]
Starting_balance= float(input("ENTER YOUR TOTAL AMOUNT YOU HAVE:"))
while(True):
    total=0
    print("------EXPENSE TRACKER------")
    print("1. Add Expense")
    print("2. view your expense")
    print("3. total expense")
    print("4.balance left")
    print("5.EXIT")

   

    choice = int(input(" ENTER YOUR CHOISE: "))

    if choice == 1:
        name= input("EXPENSE NAME: ")
        amt=float(input(" ENTER THE AMOUNT: "))
        qty= int(input("ENTER THE QUANTITY OF THE ITEM: "))
        expense.append([name,amt,qty])

        print("--EXPENSE ADDED SUCCESSFULLY--")

    elif choice == 2 :
        print(" YOUR EXPENSES :- ")
        for item in expense:
            print("[name",item[0],",Rs:", item[1] , ",qnty:", item[2],"]")

    elif choice == 3:
        print("---TOTAL EXPENSE---")
        
        for item in expense:
            total+= (item[1]*item[2])
        print("TOTAL EXPENSE : Rs",total)
        
    elif choice==4:
        print("------------AMOUNT LEFT------------")
        balance=Starting_balance-total
        if balance < 0 :
            print("!!! YOU ARE EXCEEDING YOUR SPENDING LIMIT !!!")
            print("YOU HAVE EXCEEDED YOUR LIMIT BY :",balance)
        print("total spent:",Starting_balance,"-",total)
        print("remaining balance:",balance)

    elif choice==5:
        print("!!!YOU ARE EXITING EXPENSE TRACKER!!!")
        print("-------THANK YOU-------")
        break
    else:
        print("SORRY! YOU HAVE ENTERED AN INVALID CHOICE !!!!!")
        print("!! PLEASE try AGAIN !!")

