#McDonalds Simulator
#Innit
burger_num = 0
nuggets_num = 0
McChicken_num = 0

def burger():
    print("you ordered a burger")

def nuggets():
    print("You ordered 4 nuggets")

def McChicken():
    print("you ordered a McChicken")

def pay():
    total = (burger_num * 5.95) + (nuggets_num * 3.95) + (McChicken_num * 4.95)
    print("Your total is $"+str(total))
#Code
#Beginning Story
print("Welcome to McDonald's World!")
print("You enter the magical restaurant of Mcdonalds, where you can order can eat to your heart's content. Only catch is that you have to pay. Order freely to your choosing and have fun!!!")

#Choices and Gameplay Code
print("Would you like to enter Mcdonalds or go home?")
player = input("McDonalds or Go home")
if player == "McDonalds":
    while True:
        print("Welcome to Mcdonalds! What would you like to order?")
#Eat 3 choices of food, side, and drink
        main_food = int(input("Burger is option 1, nuggets is option 2, McChicken is option 3, or pay is option 4"))
        if main_food == 1:
            burger()
            burger_num = burger_num + 1
            print("You have "+str(burger_num)+" burgers, "+str(nuggets_num)+" nuggets and "+str(McChicken_num)+" McChickens")
        elif main_food == 2:
            nuggets()
            nuggets_num = nuggets_num + 4
            print("You have "+str(burger_num)+" burgers, "+str(nuggets_num)+" nuggets and "+str(McChicken_num)+" McChickens")
        elif main_food == 3:
            McChicken()
            McChicken_num = McChicken_num + 1
            print("You have "+str(burger_num)+" burgers, "+str(nuggets_num)+" nuggets and "+str(McChicken_num)+" McChickens")
#Going to pay code and ending of part 1 of the game
        elif main_food == 4:
            print("Now proceed to the register")
            pay()
            print("Handed with the bill, you are expected to pay. You reach into your wallet to check how much cash you have. But will you have enough?/   lets find out in part 2...")
            break

#Go home (Quit game before playing)
elif player == "Go home":
    print("You decided to go home before even stepping into the restaurant :( You're stuck hungry and sad. Maybe you might cook yourself a healthy meal, but it won't taste as good...")


