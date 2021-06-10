import os

def clearScreen():
    os.system('cls')

def showMenu():
    clearScreen()
    print("Menu options:")
    print("1. Option one")
    print("2. Option two")
    print("3. Option three")
    print("4. Option four")
    print("5. Exit\n")
    
    selection = int(input("Please choose an option (1-5):"))
    return selection

selection = 0

while(selection != 5):
    selection = showMenu()
    clearScreen()
#    print(f"selection = {selection}")
    if(selection == 1):
        print("You selected Option one!\n")
        input("Return to continue...")
    elif(selection == 2):
        print("You selected Option two!\n")
        input("Return to continue...")
    elif(selection == 3):
        print("You selected Option three!\n")
        input("Return to continue...")
    elif(selection == 4):
        print("You selected Option four!\n")
        input("Return to continue...")

print("Bye!")