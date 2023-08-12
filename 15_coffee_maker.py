"""
Following the assignment instructions to create a coffee maker simulation. I was playing around with functions in 
a dictionary because I thought it was cool. This app probably wasn't the best usage for that though.
"""
import menu


def add_ingredients(avail_ingredients):
    avail_ingredients["water"] += int(input("How much water would you like to add? "))
    avail_ingredients["milk"] += int(input("How much milk would you like to add? "))
    avail_ingredients["coffee"] += int(input("How much coffee would you like to add? "))


def check_ingredients(water_needed, water_avail, milk_needed, milk_avail, coffee_needed, coffee_avail):
    if water_needed <= water_avail and milk_needed <= milk_avail and coffee_needed <= coffee_avail:
        return True
    return False


def choose_coffee():
    while True:
        print(f"There are {len(menu.MENU)} coffee options available.")
        for item in menu.MENU:
            print(f"\t{item.title()} [{item.title()}]: ${menu.MENU.get(item).get('cost'):.2f} per cup")
        user_input = input("Make your selection: ").lower()
        if user_input in menu.MENU:
            # Runs the make coffee function and updates the profits on a successful coffee creation
            if make_coffee(user_input):
                return float(menu.MENU.get(user_input).get("cost"))
            else:
                return 0
        print(f"\nThere was an incorrect selection. Please try again.\n")


def get_option():
    """Prompts the users and returns the input as a valid string [m, a, f, i]"""
    while True:
        print(f"WELCOME! What would you like to do?")
        print(f"\tMake coffee [M]:")
        print(f"\tAdd ingredients [A]:")
        print(f"\tPrint financial report [F]:")
        print(f"\tPrint ingredient report [I]:")
        print(f"\tTurn off the coffee machine [OFF]:")
        user_input = input("Enter your selection: ").lower()
        if user_input in ["m", "a", "f", "i", "off"]:
            return user_input
        print(f"\nThat was an incorrect selection. Please try again.\n")


def ing_report():
    print("The following ingredients are available.")
    print(f"Water: {available_ingredients.get('water')}")
    print(f"Milk: {available_ingredients.get('milk')}")
    print(f"Coffee: {available_ingredients.get('coffee')}")


def make_coffee(coffee_type):
    """Takes the coffee type and profits, returns true if the coffee is made,
       false if there are not enough ingredients"""

    print(f"\tYour {coffee_type} is being made...")
    water_needed = menu.MENU.get(coffee_type).get("ingredients").get("water") \
        if (menu.MENU.get(coffee_type).get("ingredients").get("water") is not None) else 0
    water_avail = available_ingredients.get("water")
    milk_needed = menu.MENU.get(coffee_type).get("ingredients").get("milk") \
        if (menu.MENU.get(coffee_type).get("ingredients").get("milk") is not None) else 0
    milk_avail = available_ingredients.get("milk")
    coffee_needed = menu.MENU.get(coffee_type).get("ingredients").get("coffee") \
        if (menu.MENU.get(coffee_type).get("ingredients").get("coffee") is not None) else 0
    coffee_avail = available_ingredients.get("coffee")

    # Checks ingredients
    if not check_ingredients(water_needed, water_avail, milk_needed, milk_avail, coffee_needed, coffee_avail):
        print(f"\tThere was not enough ingredients to make your {coffee_type}. Please fill the machine.")
        return False
    # Reduces the ingredients
    available_ingredients["water"] -= water_needed
    available_ingredients["milk"] -= milk_needed
    available_ingredients["coffee"] -= coffee_needed

    print(f"\tYour {coffee_type} is ready!")
    return True


def shut_down():
    print("Powering down.")
    exit()


def update_profits(profits, cost):
    profits += cost


functions = {"m": choose_coffee,
             "a": add_ingredients,
             "i": ing_report,
             "make_coffee": make_coffee,
             "off": shut_down,
             "update_profits": update_profits}
available_ingredients = {"water": 2000, "milk": 500, "coffee": 100}


def coffee_machine():
    profits = 0.0

    while True:
        user_input = get_option()
        if user_input == "m":
            profits += functions.get(user_input)()
        elif user_input == "a":
            functions.get(user_input)(available_ingredients)
        elif user_input == "f":
            print(f"Profits: ${profits:.2f}")
        else:
            functions.get(user_input)()


if __name__ == '__main__':
    coffee_machine()
