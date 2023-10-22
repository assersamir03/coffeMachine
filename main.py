import resourses

things = resourses.Menu


def makeDrink(Drink):
    things['resources']['water'] = things['resources']['water'] - things[Drink]['igredients']['water']
    things['resources']['milk'] = things['resources']['milk'] - things[Drink]['igredients']['milk']
    things['resources']['coffee'] = things['resources']['coffee'] - things[Drink]['igredients']['coffee']


def moneyCalc(penny, nickel, dime, quarter):
    penny = penny * 0.1
    nickel = nickel * 0.5
    dime = dime * 0.10
    quarter = quarter * 0.25
    return penny + nickel + dime + quarter


def moneyEntry():
    penney = int(input('how enter the pennies: '))
    nickels = int(input('how enter the nickels: '))
    dimes = int(input('how enter the dimes: '))
    quarters = int(input('how enter the quarters: '))
    return penney, nickels, dimes, quarters


def checkViable(name):
    getStuff = things[name]['igredients']
    getStuff2 = things['resources']
    waterResource = getStuff2['water']
    milkResource = getStuff2['milk']
    coffeeResource = getStuff2['coffee']
    waterDrink = getStuff['water']
    coffeeDrink = getStuff['coffee']
    milkDrink = getStuff['milk']
    if waterDrink <= waterResource and milkDrink <= milkResource and coffeeDrink <= coffeeResource:
        return True
    else:
        return False


def main():
    choice = input("what do you want (espresso/late/cuppucino): ")
    if choice == 'report':
        for i, j in things['resources'].items():
            print(f"{i} : {j}")
    elif choice == 'espresso':
        if checkViable('espresso'):
            money = moneyEntry()
            money = moneyCalc(money[0], money[1], money[2], money[3])
            if money < things['espresso']['cost']:
                print(f'not enough money!... money got refunded ')
                main()
            else:
                money = money - things['espresso']['cost']
                things['resources']['money'] = things['resources']['money'] + things['espresso']['cost']
                print(f'here is the the change {money}')
                makeDrink('espresso')
        else:
            print('we dont have the ingredients')
    elif choice == 'cuppucino':
        if checkViable('cuppucino'):
            money = moneyEntry()
            money = moneyCalc(money[0], money[1], money[2], money[3])
            if money < things['cuppucino']['cost']:
                print(f'not enough money!... money got refunded ')
                main()
            else:
                money = money - things['cuppucino']['cost']
                things['resources']['money'] = things['resources']['money'] + things['cuppucino']['cost']
                print(f'here is the the change {money}')
                makeDrink('cuppucino')
        else:
            print('we dont have the ingredients')
    elif choice == 'late':
        if checkViable('late'):
            money = moneyEntry()
            money = moneyCalc(money[0], money[1], money[2], money[3])
            if money < things['late']['cost']:
                print(f'not enough money!... money got refunded ')
                main()
            else:
                money = money - things['late']['cost']
                things['resources']['money'] = things['resources']['money'] + things['late']['cost']
                print(f'here is the the change {money}')
                makeDrink('late')
        else:
            print('we dont have the ingredients')
    main()


main()
