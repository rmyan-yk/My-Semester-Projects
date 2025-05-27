#Random Image Generator

#Objective:
#Create a Python program that displays a random image from a selected theme each time the user desires a recommendation. The images must be stored as URLs in an array. Additionally, display a description of each image based on which one is randomly chosen.

#Innit
from PIL import Image
import requests
from io import BytesIO
import time
import random

#Instructions
##1. Choose a Theme
###UFC Knockouts
###Find at least 5 image URLs that match your chosen theme.
###If the URL is too long, use a URL shortener like https://tinyurl.com/.
####1. https://tinyurl.com/3ayy2y5u (Last, F. (2024). The Top 25 Knockouts in UFC History. Bleacherreport.com. https://bleacherreport.com/articles/649762-the-top-25-knockouts-in-ufc-history)
####2. https://tinyurl.com/3j44vsnh (Last, F. (2024). The Top 25 Knockouts in UFC History. Bleacherreport.com. https://bleacherreport.com/articles/649762-the-top-25-knockouts-in-ufc-history)
####3. https://tinyurl.com/bdzk224f (Last, F. (2024). The Top 25 Knockouts in UFC History. Bleacherreport.com. https://bleacherreport.com/articles/649762-the-top-25-knockouts-in-ufc-history)
####4. https://tinyurl.com/mvtnj2p9 (Last, F. (2024). The Top 25 Knockouts in UFC History. Bleacherreport.com. https://bleacherreport.com/articles/649762-the-top-25-knockouts-in-ufc-history)
####5. https://tinyurl.com/5dpk3kua (Last, F. (2024). The Top 25 Knockouts in UFC History. Bleacherreport.com. https://bleacherreport.com/articles/649762-the-top-25-knockouts-in-ufc-history)

#IMPORTANT: Credit the source for each image. Include details such as:
##Website name
##Author
##URL
##Article name
##Date
##CC License
####The adorable face of a dog. Image source: The Dog API. 2009. Accessed via https://cdn2.thedogapi.com/images/0LJiOVlxp.jpg CC BY-NC 2.0.

##2. Store These Images in an Array as Strings
###Copy the image address from an image online to acquire its URL.
###Store the URLs in a Python list.
UFC = [str("https://tinyurl.com/3ayy2y5u"), str("https://tinyurl.com/3j44vsnh"), str("https://tinyurl.com/bdzk224f"), str("https://tinyurl.com/mvtnj2p9"), str("https://tinyurl.com/5dpk3kua")]

##3. Introduce Users to the Program
###Add an introduction message explaining what the program does.
###Use the time library to create delayed text output before displaying the image.
print("Welcome to Random Top 5 UFC Knockouts! Here, I will provide you a random TOP 5 UFC knockout for your enjoyment!")


###Use a while loop to allow users to view multiple random images.
while True:
    print("Generating Image...")
    time.sleep(3)
###Use the provided code (attached to the Google Doc) to display the image in an interactive window (will not work in terminal).
    def open_image(url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.show()

##5. Print a Description of the Image
###After displaying the image, print a description and why you are recommending that item
###The text should adapt to the random image that is displayed using if statements.
        if url == "https://tinyurl.com/3ayy2y5u":
            print("Dan Henderson KO's Michael Bisbing in the 2nd Round. Just look at this powerbomb!!")
        elif url == "https://tinyurl.com/3j44vsnh":
            print("Gabriel Gonzaga KO's Mirko Cro Cop. Savage work! Look how his neck bends")
        elif url == "https://tinyurl.com/bdzk224f":
            print("Lyoto Machida KO's Rashad Evans in the 2nd Round. This is iconic and devastating. Punch of hell!!")
        elif url == "https://tinyurl.com/mvtnj2p9":
            print("Anderson Silva KO's Vitor Belfort in the FIRST Round. Amazing from one of the GOATs! Watching the fight clip cements a legacy!")
        elif url == "https://tinyurl.com/5dpk3kua":
            print("BJ Penn KO Caol Uno 11 seconds into Round 1!! Even though this fight is not very known, look at Uno's body position! zzzz to sleep!")


##4. Randomly Pull an Image from the List and Display It
###Use the random module to select an image.
    open_image(random.choice(UFC))
    
###Has user to whether to run program again or leave
    again = input("Would you like another image?")
    if again == "yes":
        print("OK!")
    elif again == "no":
        print("Come again another time!")
        break

##6. Add Finishing Touches
###Define functions to organize your code.
###Add comments to explain your logic.
