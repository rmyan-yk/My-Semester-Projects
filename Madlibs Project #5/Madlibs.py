#Madlibs
#Use appropriate variable names that make the code easy to read and understand.


#Introduce users to the game of MadLib with print() statements
print("Welcome to MadLibs! I have a nice story for you :)")
start = int(input("If you want the story, press 1! If not, press 2"))
if start == 1:
#Ask the user to enter words for the blanks in the story. You can use the input() function to get user input
    adjective = input("Enter an adjective")
    name = input("Enter a name")
    animal = input("Enter an animal")
    food = input("Enter a food")
    number = int(input("enter a number between 1-10"))
    color = input("Enter a color")
    body_part = input("Enter a body part")
    drink = input("Enter a drink")
    plural_noun = input("Enter a plural noun")
    emotion = input("Enter a emotion")

#Create a story with the user's input using string concatenation
#Print the completed story to the console using the print() function.
    print("Story Title: A Day at the Zoo Today, I went to the "+str(adjective)+" zoo with my best friend "+str(name)+". We saw a "+str(adjective)+" "+str(animal)+" jumping up and down in its cage. The zookeeper said it loves to eat "+str(food)+" and sleeps for "+str(number)+" hours every day! Later, we watched a "+str(color)+" "+str(animal)+" painting pictures with its "+str(body_part)+". I couldn't believe my eyes! We laughed so hard that we spilled our "+str(drink)+" on the ground. Finally, we bought some "+str(plural_noun)+" from the gift shop and went home feeling "+str(emotion)+". It was the most "+str(adjective)+" day ever!)")
elif start == 2:
    print("Goodbye")

#Story must have at least 4 inputs

