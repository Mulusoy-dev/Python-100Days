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
}

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
coffee_flag = True


def coin_status():
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return total


while coffee_flag:
    coffee_status = input("What Would You like? (espresso/latte/cappuccino): ")
    print("Please insert coins.")
    final_coin = coin_status()
    if coffee_status == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {coin_status()}")

    elif coffee_status == "espresso":
        water = water - 50
        coffee = coffee - 18
        if water <= 0:
            print("Sorry there is not enough water.")
            coffee_flag = False
            break
        elif milk <= 0:
            print("Sorry there is not enough milk.")
            coffee_flag = False
            break
        elif coffee <= 0:
            print("Sorry there is not enough coffee.")
            coffee_flag = False
            break
        if final_coin >= 1.50:
            final_coin = final_coin - 1.5
            print(f"Here is {final_coin} in charge.")
            print("Here is your Espresso. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
            coffee_flag = False

    elif coffee_status == "latte":
        water = water - 200
        milk = milk - 150
        coffee = coffee - 24
        if water <= 0:
            print("Sorry there is not enough water.")
            coffee_flag = False
            break

        elif milk <= 0:
            print("Sorry there is not enough milk.")
            coffee_flag = False
            break
        elif coffee <= 0:
            print("Sorry there is not enough coffee.")
            coffee_flag = False
            break

        if final_coin >= 2.50:
            final_coin = final_coin - 2.5
            print(f"Here is {final_coin} in charge.")
            print("Here is your Espresso. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
            coffee_flag = False

    elif coffee_status == "cappuccino":
        water = water - 250
        milk = milk - 100
        coffee = coffee - 24
        if water <= 0:
            print("Sorry there is not enough water.")
            coffee_flag = False
            break
        elif milk <= 0:
            print("Sorry there is not enough milk.")
            coffee_flag = False
            break
        elif coffee <= 0:
            print("Sorry there is not enough coffee.")
            coffee_flag = False
            break
        if final_coin >= 3.00:
            final_coin = final_coin - 3.0
            print(f"Here is {final_coin} in charge.")
            print("Here is your Espresso. Enjoy!")

        else:
            print("Sorry that's not enough money. Money refunded.")
            coffee_flag = False

    else:
        coffee_flag = False