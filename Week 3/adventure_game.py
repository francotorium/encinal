def sid_game():

    print("You enter the kitchen. It is dark and you can only make out a pop-tart on the floor.")
    choice1 = str(raw_input("Do you pick up the pop-tart? [enter 'yes' or 'no']: "))

    if (choice1 == "yes"):
        print("You have picked up the pop-tart!")
        print("You are not hungry, but the pop-tart is edible.")
        choice2 = str(raw_input("Do you eat the pop-tart? [enter 'yes' or 'no']: "))
        if (choice2 == "yes"):
            print("Wow, now you are really full and feel sick. Time to go to bed!")
        if (choice2 == "no"):
            print("You drop the pop-tart on the floor. Time to go to bed!")

    if (choice1 == "no"):
        print("You walk past the pop-tart and blindly run into the fridge.")
        choice2 = str(raw_input("Do you open the fridge? [enter 'yes' or 'no']: "))
        if (choice2 == "yes"):
            print("It's not healthy to eat a meal so late at night. Time to go to bed!")
        if (choice2 == "no"):
            print("Wow, this kitchen visit was pointless. Time to go to bed!")
    
    print("The end!")

sid_game()