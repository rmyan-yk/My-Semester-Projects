import time
import random
from PIL import Image
import requests
from io import BytesIO
fps_games = ["Call of Duty Warzone", "CS:GO", "Overwatch", "Doom",
              "Rainbow Six Siege", "Valorant", "Battlefield 2042", "Titanfall 2"]
fps_images = ["https://tinyurl.com/z5n8epp2", #Image of the game Call of Duty Warzone that was made in March 10th, 2020.
#I got the image from https://wallpapersden.com/gaming-poster-of-call-of-duty-warzone-wallpaper/, it was published 11/6/21.
              "https://tinyurl.com/f8bb3vd9", #Image of the game Counter Strike Global, I got the image from https://pixelz.cc/images/counter-strike-global-offensive-cs-go-logo-uhd-4k-wallpaper/ , and they published the image on an unknown date.
              "https://tinyurl.com/4wwvbezf", #This image is Overwatch, and I got the image from https://www.imdb.com/title/tt4332152/awards/ which was posted in 2016.
                "https://tinyurl.com/43xybc89",#This image is a cover for the game Doom, I got the image from https://wallpaperaccess.com/doom-game which was posted in 2021, it's a wallpaper page.
                "https://tinyurl.com/5n7ejfzs",#This image is rainbow 6 siege, the website it's from is https://hdqwalls.com/download/1440x1080/tom-clancys-rainbow-six-siege-2017 and it was published in 2023.
                "https://tinyurl.com/ydfdujsj", #This image is valorant, and I got it from this wallpaper website, https://wallpaperaccess.com/full/3037987.jpg and it was published 2 years ago.
                  "https://tinyurl.com/bdh4uc8z", #This image is battlefield 2042, and I got it from the epic games store website, https://store.epicgames.com/ko/p/battlefield-2042 and it was pbulsihed 3 years ago.
                    "https://tinyurl.com/p2uybepj"] #This image is titanfall 2 and I got this image from https://www.getdroidtips.com/titanfall-2-searching-data-center/ and it was published on 9/12/23

def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def fps_recommend(ans):

    if ans == "yes":
        print("Finding FPS game for user to play")
        time.sleep(2)

        randomfpsgame = random.choice(fps_games)
        if randomfpsgame == "Call of Duty Warzone":
            open_image(fps_images[0])
            print("This FPS game is Call of Duty Warzone. " \
            "Call of Duty warzone is an immersive FPS game that "
            "includes multiplayer and single player. Warzone is a combat military type of game where you go agaisnt others in a blood thirsted battle to win your warzone game.")

        if randomfpsgame == "CS:GO":
            open_image(fps_images[1])
            print("This is CS:GO. CS:GO is an immersive multiplayer FPS game where 2 teams, terrorists or counter terrorists combat each other. Counter terrorists must eliminate all terrorists or defuse a planted boomb.")

        if randomfpsgame == "Overwatch":
            open_image(fps_images[2])
            print("This is Overwatch, a 5v5 FPS multiplayer game where you can choose your own characters and their special abilities to eliminate your enemy within the rounds.")

        if randomfpsgame == "Doom":
            open_image(fps_images[3])
            print("This is Doom, a FPS singleplayer storyline game where you play as a battlelusted space marine who dedicated his life to killing demons")

        if randomfpsgame == "Rainbow Six Siege":
            open_image(fps_images[4])
            print("This is Rainbow Six Siege. Similar to CS:GO, Rainbow Six Siege is a FPS 5v5 multiplayer game where players can be counter terrorists or terrorists. Counter terrorists must eliminate all terrorists or defuse a planted boomb.")

        if randomfpsgame == "Valorant":
            open_image(fps_images[5])
            print("This is Valorant. Similar to Rainbow Six Siege and CS:GO, this is also a 5v5 FPS multiplater game. However, players can choose their character and special abilities, competeting against each other uniquely.")

        if randomfpsgame == "Battlefield 2042":
            open_image(fps_images[6])
            print("This is Battlefield 2024. A large-scale FPS multiplayer game where players on opposite sides, use military equipment and tactics to capture and maintain all marked objectives.")

        if randomfpsgame == "Titanfall 2":
            open_image(fps_images[7])
            print("This is Titanfall 2. A singleplayer FPS shooter. You are a rifeman with a giant robot that has to stop catastrophe on the world.")

while True:
    ans = input("Would you like a FPS game recommendation?")
    fps_recommend(ans)
    if ans == "no":
        print("Understandable, have a nice day!")
        break
















