import art
from data import menu
import os
import time

def clear():
    """
    This function will clear the console, every time
    we need to buy another coffee
    """
    os.system('cls') #on Windows System

#variable to keep the game running
coffe_is_on = True
game_finished = False

#variables needed for the machine to work
water = 900
milk = 800
coffee = 100
money = 0
total_money = 0
ingredients_amount = water + milk + coffee
enough_ing = 0

#all the ingredients that the machine has in the form of a dictionary
#to keep track of the ingredients that we have left
ingredients = {'water': water, 'milk': milk, 'coffee': coffee}

#values from latte:
values_latte = menu['latte']
latte_ingredients = values_latte['ingredients']
latte_cost = values_latte['cost']
latte_ingredients_amount = 0

#values from espresso:
values_espresso = menu['espresso']
espresso_ingredients = values_espresso['ingredients']
espresso_cost = values_espresso['cost']
espresso_ingredients_amount = 0

#values from cappuccino:
values_capuccino = menu['cappuccino']
cappuccino_ingredients = values_capuccino['ingredients']
cappuccino_cost = values_capuccino['cost']
cappuccino_ingredients_amount = 0

#this for loop will give me the total ingredients needed for each type of coffee:
#total ingredients needed to create a latte
for amount in latte_ingredients.values():
    latte_ingredients_amount += amount

#total ingredients needed to create an espresso
for amount2 in espresso_ingredients.values():
    espresso_ingredients_amount += amount2

#total ingredients needed to create a Capuccino
for amount3 in cappuccino_ingredients.values():
    cappuccino_ingredients_amount += amount3

#while loop that starts the machine with its given functions
while coffe_is_on:
    def game_over():
        global coffe_is_on
        global game_finished
        coffe_is_on = False
        game_finished = True

    #This print statements are for me to know how many ingredients are needed for each type of coffee
    #each time it loops the 'ingredients_amount' will be decreasing

    def type_of_coffee(decision):
        """
        Thi function will take the variable 'decision' as an argument
        and will return the change$, the coffee needed and subtract the ingredients
        """
        global water
        global coffee
        global money
        if decision == 'latte':
            if total_money > latte_cost:
                water -= latte_ingredients['water']
                coffee -= latte_ingredients['coffee']
                change = total_money - latte_cost
                money += latte_cost
                print(f"Here's your change: {round(change, 2)}")
                print(f"Latte ingredients needed: {latte_ingredients_amount}")
                print(f"Ingredients left: {ingredients_amount}")
                print(f"Here's your {decision} ☕")
            else:
                print("You don't have enough money, sorry Unu")
                game_over()
        elif decision == 'espresso':
            if total_money > espresso_cost:
                water -= espresso_ingredients['water']
                coffee -= espresso_ingredients['coffee']
                change = total_money - espresso_cost
                money += espresso_cost
                print(f"Here's your change: {round(change, 2)}")
                print(f"Capuccino ingredientes finish: {espresso_ingredients_amount}")
                print(f"Ingredients left: {ingredients_amount}")
                print(f"Here's your {decision} ☕")
            else:
                print("You don't have enough money, sorry Unu")
                game_over()
        elif decision == 'cappuccino':
            if total_money > cappuccino_cost:
                water -= cappuccino_ingredients['water']
                coffee -= cappuccino_ingredients['coffee']
                change = total_money - cappuccino_cost
                money += cappuccino_cost
                print(f"Here's your change 💸: {round(change, 2)}")
                print(f"Capuccino ingredientes finish: {cappuccino_ingredients_amount}")
                print(f"Ingredients left: {ingredients_amount}")
                print(f"Here's your {decision} ☕")
            else:
                print("You don't have enough money, sorry Unu")
                game_over()

    def enough_ingredients(decision):
        """
        This function will review if we have enough ingredients to create the coffee,
        if we don't have anough ingredients, the machine will turn off
        """
        global coffe_is_on
        global ingredients_amount
        global game_finished
        if decision == 'latte':
            if water < latte_ingredients['water']:
                print('There is not enough water 🧊')
                game_finished = True
                return "Not enough ingredients"
            elif milk < latte_ingredients['milk']:
                print('There is not enough milk 🥛')
                game_finished = True
                return "Not enough ingredients"
            elif coffee < latte_ingredients['coffee']:
                print('There is not enough coffee ☕')
                game_finished = True
                return "Not enough ingredients"
            else:
                ingredients_amount -= latte_ingredients_amount
        if decision == 'cappuccino':
            if water < cappuccino_ingredients['water']:
                print('There is not enough water 🧊')
                game_finished = True
                return "Not enough ingredients"
            elif milk < cappuccino_ingredients['milk']:
                print('There is not enough milk 🥛')
                game_finished = True
                return "Not enough ingredients"
            elif coffee < cappuccino_ingredients['coffee']:
                print('There is not enough coffee ☕')
                game_finished = True
                return "Not enough ingredients"
            else:
                ingredients_amount -= cappuccino_ingredients_amount
        if decision == 'espresso':
            if water < espresso_ingredients['water']:
                print('There is not enough water 🧊')
                game_finished = True
                return "Not enough ingredients"
            elif milk < espresso_ingredients['milk']:
                print('There is not enough milk 🥛')
                game_finished = True
                return "Not enough ingredients"
            elif coffee < espresso_ingredients['coffee']:
                print('There is not enough coffee ☕')
                game_finished = True
                return "Not enough ingredients"
            else:
                ingredients_amount -= espresso_ingredients_amount

    def total_moneyf():
        """
        This function will asks us how much money do we have
        and it will return the total amount of money
        """
        money_penny = int(input("How many pennies do you have?: $"))
        money_nickel = int(input("How many nickels do you have?: $"))
        money_dimes = int(input("How many dimes do you have?: $"))
        money_quarter = int(input("How many quarters do you have?: $"))
        penny = money_penny * .01
        nickel = money_nickel * .05
        dime = money_dimes * .1
        quarter = money_quarter * .25
        return penny + nickel + dime + quarter

    def decisionf(decision):
        """
        This function will take decision as an argument and will start to check
        which kind of coffee do we want
        """
        global coffe_is_on
        global total_money
        if decision == 'off':
            coffe_is_on = False
            print('bibubiub... The Machine is off')
            game_over()
            time.sleep(5)
            clear()
        elif decision == 'report':
            print(f"Water: {str(water)}" + 'ml 🧊')
            print(f"Milk: {str(milk)}" + 'ml 🥛')
            print(f"Coffee: {str(coffee)}" + 'g ☕')
            print("Money in the machine: " + '$' + str(money) + '💸')
            order = input("Would you like to make an order? (Type 'y' or 'n'): ")
            if order == 'y':
                clear()
                main()
            else:
                game_over()
                clear()
        elif decision == 'latte':
            type_of_coffee(decision)
        elif decision == 'cappuccino':
            type_of_coffee(decision)
        elif decision == 'espresso':
            type_of_coffee(decision)

    def another_drink():
        """
        This function will asks us if we want another drink after we have bought one
        """
        global coffe_is_on
        print('\n')
        drink = input("Would you like to buy another drink? ☕: (Type 'y' or 'n'): ")
        if drink == 'n':
            game_over()
            clear()
        else:
            clear()
            main()

    def main():
        print(f"Ingredients Starter: {ingredients_amount}")
        print(f"Latte ingredients total: {latte_ingredients_amount}")
        print(f"espresso ingredients total: {espresso_ingredients_amount}")
        print(f"cappuccino ingredients total: {cappuccino_ingredients_amount}")
        print(art.logo)
        global total_money
        global enough_ing
        decision = input("What would you like 🤗? (espresso/latte/cappuccino): ")
        if decision == 'report':
            decisionf(decision)
        elif decision == 'off':
            decisionf(decision)
        enough_ing = enough_ingredients(decision)
        if game_finished is True:
            if enough_ing == "Not enough ingredients":
                print(f"Are you nuts 🤪?, we don't have ingredients left to give you your filthy {decision} 😒")
                time.sleep(5)
                game_over()
                clear()
        else:
            total_money = total_moneyf()
            decisionf(decision)
            another_drink()

    main()
    #clear the console
