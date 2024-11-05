cat_attributes = {
    "intelligence": 10,
    "energy": 50,
    "weight": 10,
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter the name of your cat: ")
colour = input("Enter the colour of your cat: ")

# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. show stats")

    if option == '1' and cat_attributes["energy"] > 5:
        print("You play with your cat.")
        cat_attributes["energy"] -= 5
        cat_attributes["weight"] -=  - 0.8
    elif option == '2' and cat_attributes["energy"] > 5:
        print("You train your cat. ")
        cat_attributes["intelligence"] += 5
        cat_attributes["energy"] -= 5
        cat_attributes["weight"] -= 0.6
    elif option == '3':
        print("Here is your cat's stats: ")
        print("Your cat's energy currently is" + cat_attributes["energy"])
        print("Your cat's intelligence currently is" + cat_attributes["intelligence"])
        print("Your cat's weight currently is" + cat_attributes["weight"])
    else:
        print("It seems your cat does not have enough energy for these actions.")
        print("Nothing happens.")

    if cat_attributes['energy'] < 0:
        print("Your cat runs out of energy, it drifts off into sleep ")
        cat_attributes["energy"] += 40