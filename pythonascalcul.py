#trust fund buddy--Good

print("""
                                    Trust fund buddy

totals your monthly spending so that trust fund doesn't run out 
(and forced tu get a real job)

please enter the requested monthly costs, sibce you are rich,

ignore pennies and only enter dollar amounts.


""")

car = input("Lamorghini tune ups:")

car =int(car)

rent =int(input("Manhataan appartment:"))
jet = int(input ("Private jet Rental: "))
gifts = int(input("Gifts: "))
foods = int(input("Dining inputs: "))
staff = int(input("Staff(buttlers, chef, driver, assistant): "))
guru = int(input("Personal Gurur and Coach: "))
games = int(input("Computer games: "))

total = car + rent + jet + gifts + foods + staff + guru + games

print("\nGrand Total: " + str(total))
input("\n\n Press the enter key to exit")