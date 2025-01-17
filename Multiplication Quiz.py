### Project 1: Multiplication Quiz Project
#**Summary**: This program quizzes the user on their multiplication skills.
#**Key Features**: 
    #Displays score at the end of the quiz
    #Allows users to choose the number of questions to answer
    #Uses random library to generate numbers between 1-12

#Innit
#Use the random library to generate a random multiplication problem and allow the user to answer it.
import random
total = 0
right = 0

#Welcome the user to the game and structure your code
print("Welcome to Mulplication Practice Quizes!")
start = input("Would you like to begin? (yes / no)")
if start == "yes":
    print("Lets start!")
#Quiz Length: Allow user to choose how many questions are in the quiz
    questions = int(input("How many questions would you like to solve today?"))
#Use a loop to repeat the process
    for i in range(questions):
        num1 = random.randint(1,12)
        num2 = random.randint(1,12)
        print(str(num1)+" times "+str(num2)+" equals what?")
        answer = int(input("Type your answer"))
#Check to see if the user's answer correct
        if answer == num1 * num2:
            right = right + 1
#Update the score accordingly
            total = total + 1
            print("Correct! Onto the next problem!")
        else:
            print("Wrong! Onto the next problem!")
#Update the score accordingly
            total = total + 1

#Give the user their final score
    final_score = (right / total) * 100
    print("Your final score is: "+str(right)+" / "+str(total)+" or "+str(final_score)+"%")

#Cancel
elif start == "no":
    print("Come back another time!")

