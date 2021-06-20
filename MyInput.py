import time
import Drawing as D
def taking_input():
    global Choice
    Choice = input("What do you want to draw?\nhut or flower?\n")
    #print("I am from inside function", Choice)

def input_usage():
    if Choice.upper() == "HUT":
        print("Correct answer\nEnjoy")
        D.hut()
    elif Choice.upper() == "FLOWER":
        print("Smart!!")
        D.flower()
    elif Choice.upper() == 'NOTHING':
        print ("Ok! Bye")
        time.sleep(2)
        quit()
    else:
        print("Not found anything, please try again\n")
        taking_input()
        input_usage()

taking_input()
input_usage()

second_input = input ("Try again?\n")

while second_input.upper() == 'YES':
    taking_input()
    input_usage()
    second_input = input ("Try again?\n")
    if second_input.upper() == "NO":
        break

if second_input.upper() == "NO":
    print("Thank you, bye")
    time.sleep(2)
    quit()

