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

RESOURCE = {
    "water":300,
    "milk":200,
    "coffee":100
}
def get_coin(chosen_drink):
    print("Please insert coins.")
    quarters = int(input("how many quarters: "))
    dimes = int(input("how many dimes: "))
    nickles = int(input("how many nickles: "))
    pennies = int(input("how many pennies: "))
    inserted_prize = (0.25*quarters)+(0.1*dimes)+(0.05*nickles)+(0.01*pennies)
    remaining_change = inserted_prize-(MENU[chosen_drink]["cost"])
    print(f"Here is ${round(remaining_change,2)} in change.")
    print(f"Here is your {chosen_drink} ☕ Enjoy!")
    updated_resources(chosen_drink)

def updated_resources(chosen_drink):
    for resource_key,resource_value in RESOURCE.items():
        for key, value in MENU[chosen_drink]['ingredients'].items():
            if resource_key == key:
                RESOURCE[resource_key] =  RESOURCE[resource_key] - value
                if RESOURCE[resource_key] < 0:
                    print(f"Sorry there is not enough {resource_key}")


def generate_report():
    for key,value in RESOURCE.items():
        if value <= 0:
            value = 0
        print(f"{key} : {value}")

user_input = True
while user_input:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    match user_input:
        case "espresso" | "latte" | "cappuccino":
            get_coin(user_input)
        case "report":
            generate_report()
        case "off":
            user_input = False

