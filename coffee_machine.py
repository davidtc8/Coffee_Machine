import art
#import data

coffe_is_on = True
water = 100
milk = 50
coffee = 76
money = 2.5
espresso = 1.5
latte = 2.5
cappuccino = 3

while coffe_is_on:

    print(art.logo)
    decision = input("What would you like? (espresso/latte/cappuccino): ")

    money_penny = int(input("How many pennies do you have?: "))
    money_nickel = int(input("How many nickels do you have?: "))
    money_dimes = int(input("How many dimes do you have?: "))
    money_quarter = int(input("How many quarters do you have?: "))

    penny = money_penny * .01
    nickel = money_nickel * .05
    dime = money_dimes * .1
    quarter = money_quarter * .25
    total_money = penny + nickel + dime + quarter

    def lattef():
        global total_money
        global latte
        if total_money > latte:
            change = total_money - latte
            print(f"Here's your change: {change}")
        else:
            print("You don't have enough money, sorry Unu")

    if decision == 'off':
        coffe_is_on = False
        print('bibubiub... The Machine is off')
        break
    elif decision == 'report':
        print(water + 'ml')
        print(milk + 'ml')
        print(coffee + 'g')
        print('$' + money)
    elif decision == 'latte':
        lattef()
