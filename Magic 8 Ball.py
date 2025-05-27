#Magic 8 Ball Program

#Objective:
##The objective of this assignment is to create a Magic 8 Ball program using Python. The program should generate random answers from a predefined list of responses and provide a user-friendly interface for asking questions and receiving answers.

#Innit

import random

#Requirements:
##Create a list variable named responses to store a set of at least 15 predefined responses.

magiclist = ["It is certain",
          "Reply hazy, try again",
          "Don’t count on it",
          "It is decidedly so",
          "Ask again later",
          "My reply is no",
          "Without a doubt",
          "Better not tell you now",
          "My sources say no",
          "Yes definitely",
          "Cannot predict now",
          "Outlook not so good",
          "You may rely on it",
          "Concentrate and ask again",
          "Very doubtful",
          "As I see it, yes",
          "Most likely",
          "Outlook good",
          "Yes",
          "Signs point to yes"]

#Main
print("Welcome to Magic 8 Ball Adviser")

##Repeat the process if the user responds with "yes" or "y" and exit the program if the user responds with "no" or "n".

while True:

##Prompt the user to enter a yes-or-no question and store it in a variable.

    print("Ask any yes or no question!")
    question = input("Ask me anything :>")

##Validate the user's input to ensure it ends with a question mark. If not, ask the user to re-enter the question.

    if question.endswith("?"):

##Use the random.choice() function to select a random response from the responses list.
##Generate and display a random response from the responses list.

        print(random.choice(magiclist))
    else:
       print("Use a question mark next time")

##Ask the user if they want to ask another question.

    print("Would you like to ask another question?")
    again = input("Yes or No")
    upagain = again.upper()
    if upagain == "YES":
        print("Loading...")
    elif upagain == "NO":
        print("Bye!")
        break

#Instructions:
##Import the random module at the beginning of the file using the following line of code:
##Define the responses list variable and populate it with at least 15 different responses.
##Create a while loop to repeat the question-answering process until the user chooses to exit.

#Inside the loop:
##Prompt the user to enter a yes-or-no question and store it in a variable.
##Use an if statement and the endswith() function to check if the question ends with a question mark. If not, ask the user to re-enter the question.
##Use random.choice() with the responses list to select a random response.
##Display the selected response to the user.
##Prompt the user if they want to ask another question. If the response is "no" or "n", exit the loop.

##Test the program by running it and asking different questions.

