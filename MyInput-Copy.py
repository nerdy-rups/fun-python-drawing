import Hut
def taking_input():
    global Choice
    Choice = input("What do you want to draw\n")
    #print("I am from inside function", Choice)

def input_usage():
    if Choice == "Hut":
        print("Correct answer\n Enjoy")
        Hut.hut()
    elif Choice == "Flower":
        Hut.flower()
    else:
        print("Not found anything, please try again")
        taking_input()
        input_usage()

taking_input()
input_usage()