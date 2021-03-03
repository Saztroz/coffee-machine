from main import resources, MENU

#check to see if enough resources
def check_resources(coffee_ingredients):
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

#deduct required amount of resources to make drink from total resources
def deduct_resources(coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]


#ask for payment, make sure its enough, add to profit and return change
def make_payment(coffee_cost):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total_paid = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
    
    if total_paid < drink["cost"]:
        print("Sorry that's not enough money. Money Refunded")
        return False
    else:
        paid_amount = total_paid - drink["cost"]
        change = format(paid_amount, '.2f')
        print(f"Here is ${change} in change.")
        print("Here is your latte. Enjoy!")
        return True

is_on = True
profit = 0

while is_on:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if coffee_choice == "off":
        is_on = False
    elif coffee_choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']}ml\nMoney: ${profit} ")
    else:
        drink = MENU[coffee_choice]
        if check_resources(drink["ingredients"]):
            deduct_resources(drink["ingredients"]) 
            if make_payment(drink["cost"]):
                profit += drink["cost"]
            

            

