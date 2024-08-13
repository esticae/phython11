
#prints a line of code ^

playing = input("Do you want to play a game?" + " " + "Hit Enter to continue:")

score = input("yes or no: ").strip().lower() ##Collects input removes any extra

if score != "yes": ##if condition deos not equal to
    quit() ##quit()- quits code
print("----------")
print("lets play")
print("----------")
answers = 0

print("Question: What is the primary function of a CPU in a computer system?\n")
print("A. Store data permanently")
print("B. Execute instructions and process data")
print("C. Provide network connectivity")
print("D. Manage peripheral devices")
answer = input("A) B) C) D): ").strip().upper()
if answer =="B":
    print("your cheating but correct!: The primary function of a CPU is to execute instructions and process data. ")

else:
    print("Incorrect. The correct answer is B. ")


