from importlib.resources import is_resource

MENU ={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
            "ingredients":{
                "water":250,
                "milk":100,
                "coffee":24,
            },
            "cost":3.0,
    },
}
profit = 0

resource = {
    "water":300,
    "milk":200,
    "coffee":100
}

def is_resource_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resource[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters? : ")) * 0.25
    total += int(input("how many dimes? : ")) * 0.1
    total += int(input("how many nickles? : ")) * 0.05
    total += int(input("how many pennies? : ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return the True when the payment is accepted, or False if many is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resource[item]-= order_ingredients[item]
    print(f"Here is your {drink_name}")

is_on =True

while is_on:
    choice =input("What would you like ? (espresso/latte/cuppuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

