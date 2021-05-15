from menu import menu, res


# Todo : function to check resources
def check_resources(uc):
    """Check the resources availability and update the resources"""
    water = menu[uc]['ingredients']['water']
    milk = menu[uc]['ingredients']['milk']
    coffee = menu[uc]['ingredients']['coffee']
    money = menu[uc]['cost']
    not_enough = ""
    should_continue = True
    if res['water'] < water:
        not_enough += " water,"
        should_continue = False
    if res['milk'] < milk:
        not_enough += " milk,"
        should_continue = False
    if res['coffee'] < coffee:
        not_enough += " coffee"
        should_continue = False
    if not should_continue:
        print(f"Sorry there is not enough{not_enough}.")
    else:
        res['water'] -= water
        res['milk'] -= milk
        res['coffee'] -= coffee
    return should_continue, money


# Todo : function to print report
def report(money):
    """Print  report of resources"""
    print(f"Water : {res['water']}\nMilk : {res['milk']}\nCoffee : {res['coffee']}\nMoney : ${money}")


# Todo : function to collect coins and return change
def collect_coin(money):
    """Collect coins from customer and return change"""
    print(f"Please insert ${money} in coins : ")
    quarters = 0.25*int(input("How many quarters? : "))
    total = quarters
    if quarters < money:
        dimes = 0.1*int(input("How many dimes? : "))
        total += dimes
        if total < money:
            nickels = 0.05*int(input("How many nickels? : "))
            total += nickels
            if total < money:
                pennies = 0.01*int(input("How many pennies? : "))
                total += pennies
    # quarters = int(input("How many quarters? : "))
    # dimes = int(input("How many dimes? : "))
    # nickels = int(input("How many nickels? : "))
    # pennies = int(input("How many pennies? : "))
    # total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    if money > total:
        print("Sorry that's not enough money. Money refunded.")
        should_continue = False
    elif money < total:
        change = round((total - money), 2)
        print(f"Here is ${change} in change")
        should_continue = True
    else:
        should_continue = True
    return should_continue


# todo: function for coffee machine
def coffee_machine():
    """Coffee machine : Make 3 types of coffee"""
    # res = resources
    money = 0
    machine_state = 'on'
    while machine_state == 'on':
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == 'report':
            report(money)
        elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
            should_continue, cost = check_resources(user_choice)
            if should_continue:
                should_continue = collect_coin(cost)
                if should_continue:
                    money += cost
                    print(f"Here is your {user_choice} ☕. Enjoy")
        elif user_choice == 'off':
            machine_state = 'off'
            print("Turning machine off.\nBYE!!")
        else:
            print("Invalid drink name!!!")


coffee_machine()
