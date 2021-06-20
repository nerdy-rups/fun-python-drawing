import Drawing as D
def taking_input():
    global Choice
    Choice = input("What do you want to draw?\n")
    #print("I am from inside function", Choice)

def input_usage():
    if Choice.upper() == "HUT":
        print("Correct answer\n Enjoy")
        D.hut()
    elif Choice.upper() == "FLOWER":
        D.flower()
    elif Choice.upper() == 'NOTHING':
        print ("Ok! bye")
        quit()
    else:
        print("Not found anything, please try again")
        taking_input()
        input_usage()

taking_input()
input_usage()

second_input = input ("Try again?\n")

while second_input.upper() == 'YES':
    #if second_input.upper() == 'YES':
    taking_input()
    import Drawing as D
    input_usage()
    second_input = input ("Try again?\n")
    if second_input.upper() == "No":
        break

if second_input.upper() == "NO":
    print("Thank you, bye")
    quit()

