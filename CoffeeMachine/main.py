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

resource = {
    "water":300,
    "milk":200,
    "coffee":100
}

def calculate_resources():
    return ""

def generate_report():
    for key,value in resource.items():
        print(f"{key} : {value}")

user_input = True
while user_input:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    match user_input:
        case "espresso" | "latte" | "cappuccino":
            print(f"{user_input}")
        case "report":
            calculate_resources()
        case "off":
            user_input = False

