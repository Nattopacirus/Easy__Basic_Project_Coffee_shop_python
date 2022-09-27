#Function
#Nattopacirus/Easy__Basic_Project_Coffee_shop_python-For-Learning


def choose_name_coffee(coffee, typec, cost):
    print("---You choose %s %s %d baht---" % (typec, coffee, cost))


def recieved_change(inMoney):
    if inMoney >= cost:
        print("You recieved a change of %d baht." % (inMoney - cost))
        print("---Thank you---")
    elif inMoney < cost:
        print("Not enough money\n---Please try again---")


#start
print("---Welcome to Nat's Coffee---")
print(" ")
start_program = int(input("Please type 1 to show menu:  "))
print(" ")
print(" ")
if start_program == 1:
    print("---Choose the menu--- \n 1. Espresso \n 2. Cappucino \n 3. Latte")
    print(" ")
    Select_coffee = SCF = int(input("Select coffee:  "))
    print(" ")
    if SCF == 1 or SCF == 2 or SCF == 3:
        if SCF == 1:
            coffee = "Espresso"
        elif SCF == 2:
            coffee = "Cappucino"
        elif SCF == 3:
            coffee = "Latte"
        print(
            "---Choose the type of coffee--- \n 1.  Hot 55 Baht \n 2.  Cold 60 Baht"
        )
        print(" ")
        print(" ")
        select_type = STy = int(input("Select type:  "))
        if STy == 1 or STy == 2:
            if STy == 1:
                typec = "Hot"
                cost = 55
            elif STy == 2:
                typec = "Cold"
                cost = 60
            choose_name_coffee(coffee, typec, cost)
            print(" ")
            Input_money = int(input("Input your money:  "))
            inMoney = Input_money
            recieved_change(inMoney)

        else:
            print("Sorry , Something went wrong, Please try again.")
    else:
        print("Sorry , Something went wrong, Please try again.")
else:
    print("Sorry , Something went wrong.")
