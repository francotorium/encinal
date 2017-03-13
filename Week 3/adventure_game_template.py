# instructions:
# erase the placeholder text (number_one, number_two, etc.) and replace it with your own text.
 
# number_one = decide what you want to call your game. use this name as the function name.
# number_two = a line of text. this is what the user will read before making the first decision.
# number_three = the first decision.

# number_four = the first choice of the first decision.
# number_five = a line of text. this is what the user will read before making the second decision.
# number_six = the second decision (given the first choice of the first decision was selected).
# number_seven = the first choice of the second decision.
# number_eight = a line of text. this is what the user will read after making the second decision.
# number_nine = the second choice of the second decision.
# number_ten = a line of text. this is what the user will read after making the second decision.

# number_eleven = the second choice of the first decision.
# number_twelve = a line of text. this is what the user will read before making the second decision.
# number_thirteen = the second decision (given the second choice of the first decision was selected).
# number_fourteen = the first choice of the second decision.
# number_fifteen = a line of text. this is what the user will read after making the second decision.
# number_sixteen = the second choice of the second decision.
# number_seventeen = a line of text. this is what the user will read after making the second decision.

def number_one():

    print(number_two)
    choice1 = str(raw_input(number_three))

    if (choice1 == number_four):
        print(number_five)
        choice2 = str(raw_input(number_six))
        if (choice2 == number_seven):
            print(number_eight)
        if (choice2 == number_nine):
            print(number_ten)

    if (choice1 == number_eleven):
        print(number_twelve)
        choice2 = str(raw_input(number_thirteen))
        if (choice2 == number_fourteen):
            print(number_fifteen)
        if (choice2 == number_sixteen):
            print(number_seventeen)
    
    print("The end!")

number_one()