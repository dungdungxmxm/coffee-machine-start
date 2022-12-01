import art
from replit import clear

resources = {"Water": 300, "Milk": 200, "Coffee": 100, "Money": 0}

recipe = {
    "espresso": {
        "Water": 50,
        "Milk": 0,
        "Coffee": 18,
        "Money": 1.50
    },
    "latte": {
        "Water": 200,
        "Milk": 150,
        "Coffee": 24,
        "Money": 2.50
    },
    "cappuccino": {
        "Water": 250,
        "Milk": 100,
        "Coffee": 24,
        "Money": 3.00
    }
}

coins = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}


def check_sufficient(drink):
    for item in resources:
        if resources[item] < drink[item] and item != 'Money':
            return False
    return True


def calculate_money(quarters, dimes, nickles, pennies):
    total = quarters * coins["quarters"] + dimes * coins["dimes"] + nickles * coins["nickles"] \
            + pennies * coins["pennies"]
    return total


def change_resource(drink):
    resources["Water"] = resources["Water"] - drink["Water"]
    resources["Milk"] = resources["Milk"] - drink["Milk"]
    resources["Coffee"] = resources["Coffee"] - drink["Coffee"]
    resources["Money"] = resources["Money"] + drink["Money"]


def get_resource():
    water = resources["Water"]
    milk = resources["Milk"]
    coffee = resources["Coffee"]
    money = resources["Money"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"


def coffee_machine():
    print(art.logo)
    is_on = True
    while is_on: 
      choice = input("What would you like? (espresso/latte/cappuccino): ")
      if choice == 'off':
          is_on = False
      elif choice == 'report':
          print(get_resource())
      else:
          drink = recipe[choice]
          price = drink["Money"]
  
          if not check_sufficient(drink):
              print("Sorry there is not enough water.")
              print("---------------------------------")
          else:
              # insert coins
              print("Please insert coins.")
              quarters = int(input("How many quarters?: "))
              dimes = int(input("How many dimes?: "))
              nickles = int(input("How many nickles?: "))
              pennies = int(input("How many pennies?: "))
  
              money = calculate_money(quarters, dimes, nickles, pennies)
  
              if money < price:
                  print("Sorry that's not enough money. Money refunded.")
              else:
                  change = round(money - price, 2)
                  change_resource(drink)
                  print(f"Here is ${change} in change.")
                  print(f"Here is your {choice} ☕. Enjoy!")
                  print("---------------------------------")
                
coffee_machine()
