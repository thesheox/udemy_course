water=500
milk=200
coffee=80
money=0

penny=0.0
nickel=0.0
dime=0.0
quarter=0.0


def report():
    global money
    global water
    global coffee
    global milk
    print(f"money : {money}$")
    print(f"water: {water}ml")
    print(f"coffee: {coffee}g")
    print(f"milk: {milk}ml")
def coffee_money(penny,nickel,dime,quarter):
    total_money=0

    total_money += penny * 0.01
    total_money += nickel * 0.05
    total_money += dime * 0.1
    total_money += quarter * 0.25
    return total_money



def check_resources(kind_of_coffee):
    global water
    global coffee
    global milk
    if kind_of_coffee=="espresso":
        if water<50:
            print("not enough water")
            return False
        elif coffee<18:
            print("not enough coffee")
            return False
        else:
            return True
    elif kind_of_coffee=="latte":
        if water<200:
            print("not enough water")
            return False
        elif coffee<24:
            print("not enough coffee")
            return False
        elif milk<150:
            print("not enough milk")
            return False
        else:
            return True
    elif kind_of_coffee=="cappuccino":
        if water<250:
            print("not enough water")
            return False
        elif coffee<24:
            print("not enough coffee")
            return False
        elif milk<100:
            print("not enough milk")
            return False
        else:
            return True

def latte():
    global money
    global water
    global coffee
    global milk
    money+=2.5
    water-=200
    coffee-=24
    milk-=150

def cappuccino():
    global money
    global water
    global coffee
    global milk
    money+=3
    water-=250
    coffee-=24
    milk-=100

def espresso():
    global money
    global water
    global coffee
    global milk
    money+=1.5
    water-=50
    coffee-=18


continue_buy=True
while(continue_buy!="no"):
    which_coffee=input("what do you want? \n espresso : 1.50$ \n latte : 2.50$ \n cappuccino : 3.00$ \n report \n")
    if which_coffee=="report":
        report()
    elif check_resources(which_coffee):
        given_penny=int(input("how many pennies?"))
        given_nickel=int(input("how many nickels?"))
        given_dime=int(input("how many dimes?"))
        given_quarter=int(input("how many quarters?"))
        given_money=coffee_money(given_penny,given_nickel,given_dime,given_quarter)

        if which_coffee=="espresso":
            if given_money>=1.5:
                change=given_money-1.5
                print(f"here is {change}$ in change")
                print("here is your espresso")
                espresso()
            else:
                print("not enough money")

        elif which_coffee=="latte":
            if given_money>=2.5:
                change = given_money - 2.5
                print(f"here is {change}$ in change")
                print("here is your latte")
                latte()
            else:
                print("not enough money")

        elif which_coffee=="cappuccino":
            if given_money>=3:
                change = given_money - 3
                print(f"here is {change}$ in change")
                print("here is your cappuccino")
                cappuccino()
            else:
                print("not enough money")


    continue_buy=input("Do you want to continue?")