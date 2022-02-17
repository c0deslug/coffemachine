MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

machine_comm = ""

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
# TODO 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# TODO 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
#


def resource_check(command):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    if machine_comm == "espresso":
        if water < 50:
            print("Sorry there is not enough water")
            return 1
        elif coffee < 18:
            print("Sorry there is not enough coffee")
            return 1
    elif machine_comm == "latte":
        if water < 200:
            print("Sorry there is not enough water")
            return 1
        elif milk < 150:
            print("Sorry there is not enough milk")
            return 1
        elif coffee < 24:
            print("Sorry there is not enough coffee")
            return 1
    if machine_comm == "cappuccino":
        if water < 250:
            print("Sorry there is not enough water")
            return 1
        elif milk < 100:
            print("Sorry there is not enough milk")
            return 1
        elif coffee < 24:
            print("Sorry there is not enough coffee")
            return 1


def money_check(command):
    global resources
    print("Please insert coins.")
    change = float(0)
    total_money = float(0)
    quarter = int(input("How many quarters? "))
    dime = int(input("How many dimes? "))
    nickel = int(input("How many nickels? "))
    penny = int(input("How many pennies? "))
    total_money = float( (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01))
    e_cost = float(MENU['espresso']['cost'])
    l_cost = float(MENU['latte']['cost'])
    c_cost = float(MENU['cappuccino']['cost'])
    if machine_comm == "espresso" and total_money >= e_cost:
        change = round(total_money - e_cost, 2)
        print("Here is your espresso! ☕ Enjoy.")
        print(f"Your change is {change}$")
        resources['water'] = resources['water'] - 50
        resources['coffee'] = resources['coffee'] - 18
        resources['money'] = float(resources['money'] + 1.5)
        return resources['water'], resources['coffee'] , resources['money']
    elif machine_comm == "latte" and total_money >= l_cost:
        change = round(total_money - l_cost, 2)
        print("Here is your latte! ☕ Enjoy.")
        print(f"Your change is {change}$")
        resources['water'] = resources['water'] - 200
        resources['milk'] = resources['milk'] - 150
        resources['coffee'] = resources['coffee'] - 24
        resources['money'] = float(resources['money'] + 2.5)
        return resources['water'], resources['coffee'], resources['milk'], resources['money']
    elif machine_comm == "cappuccino" and total_money >= c_cost:
        change = round(total_money - c_cost, 2)
        print("Here is your cappuccino! ☕ Enjoy.")
        print(f"Your change is {change}$")
        resources['water'] = resources['water'] - 250
        resources['milk'] = resources['milk'] - 100
        resources['coffee'] = resources['coffee'] - 24
        resources['money'] = float(resources['money'] + 3.0)
        return resources['water'], resources['coffee'], resources['milk'], resources['money']
    else:
        print("Sorry, not enough money. Here's a refund.")


while machine_comm != "off":

    machine_comm = input("What would you like? (espresso/latte/cappuccino): ")

    if machine_comm == "off":
        exit()
    elif machine_comm == "report":
        print(f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']} "
          f"\nMoney: $ {resources['money']}")
    elif (machine_comm == "espresso") or (machine_comm == "latte") or (machine_comm == "cappuccino"):
        if resource_check(machine_comm) == 1:
            pass
        else:
            money_check(machine_comm)
    else:
        pass




# TODO 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# TODO 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.
# TODO 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink

