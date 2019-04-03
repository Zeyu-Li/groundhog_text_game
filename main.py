""" Doom or Bloom

Course: CS 30
Period: 3
Date created: April 1, 2019
Date completed: April 5, 2019
By: Andrew Li

This is a text-based Python game
"""

# import modules
import json
import os
import time
import sys


class Print:
    """ print actions """

    def instant(self, text):

        print(f"---==  {text}  ==---\n".center(60))
        return 0

    def slow(self, text):

        for char in text:

            if char == "\"":
                continue

            # sout in what looks like Java syntax and pause for a little bit
            sys.stdout.write(char)
            time.sleep(.03)

        print("\n")
        return 0

    def regular(self, text):

        print(text.center(20))
        return 0


class Cover():
    """ title screen """

    def title(self):

        print("""
            |||||     |||||    |||||   ||     |||
            ||  ||   |     |  |     |  ||||  ||||
            ||   ||  |     |  |     |  || |||| ||
            ||   ||  |     |  |     |  ||  ||  ||
            ||  ||   |     |  |     |  ||      ||
            |||||     |||||    |||||   ||      ||


                     |||||     ||||
                    |     |   |   ||
                    |     |   | |||
                    |     |   |||
                    |     |   | ||
                     |||||    |  ||


        |||||  ||      |||||    |||||   ||     |||
        ||  || ||     |     |  |     |  ||||  ||||
        |||||  ||     |     |  |     |  || |||| ||
        ||  || ||     |     |  |     |  ||  ||  ||
        ||  || ||     |     |  |     |  ||      ||
        |||||  ||||||  |||||    |||||   ||      ||

    """)

        # loads stats or inits json files that store player data
        load = stats()

        while True:

            Pr.instant("NEW GAME")

            if not load:
                Pr.instant("LOAD GAME")

            Pr.instant("HELP")

            Pr.instant("ABOUT")
            
            Pr.instant("QUIT")

            # user option
            option = user_input()

            # option switch statements
            if option in ("QUIT", "Q"):
                Pr.slow("\nThanks for playing")
                return "break"
            elif option == "HELP":
                Co.help()
            elif option == "ABOUT":
                Co.about()
            elif option in ( "NEW GAME", "NEW", "N"):
                return "new"
            elif option in ("LOAD GAME", "LOAD", "L"):
                return "load"
            else:
                Pr.regular("\n Your input is not recognized, please try again\n")

        return 0

    def help(self):

        Pr.regular("""
        To start this game, enter \"new game\", \"new\", or \"n\".
        If you have previously played this game,
        you should see load game that can be activated if 
        \"load game\", \"load\", or \"l\" is entered.

        WARNING: if you start a new game, the saved game will be overwritten!

        If you want to report a bug, go to the following url:
        https://github.com/Zeyu-Li/text_game/issues

        Suggestions will also be accepted and feel free to fork this project
        ** remember this is licensed with the MIT license

        To continue, press the enter key

        """)

        delay = input("")

        return 0

    def about(self):

        Pr.regular("""
        This is a text-based Python game made for a class project.

        If you wish to modify it, please read license,
        other than that, please enjoy the game ;)

        To continue, press the enter key

        """)

        delay = input("")

        return 0


class Event:
    """ All events """

    def beginning(self):

        # TODO: continue adventure thing

        Pr.slow(""""
    2019: You fall into a nuclear dump site

    Yearning for sunlight to photosynthesize,
    you venture with your newly mutated roots
    in hopes of reaching fresh air and sunlight

    As you wonder around on your studded roots,
    you find a small hole

    With limited time on your non-exist hands, what do you do?
        """)

        option = user_input().split(" ")

        # switch statement for actions attempted by user
        for action in option:

            if action in ("LOOK", "OBSERVE"):

                Pr.slow("You observe the hole and find that it is large enough for you to climb in")

        return 0


# start of standard functions
def user_input():

    return (str(input("> ").strip())).upper()


def stats():

    if not os.path.exists('stats.json'):

        with open('stats.json', 'w') as fp:
            stats = {

                'area': '0',
                'hp': '5',
                'attack': '5',
                'special': '5'

            }

            json.dump(stats, fp)

    else:

        with open('stats.json', 'r') as fp:

            stats = json.load(fp)

            area = list(stats.values())[0]
            hp = list(stats.values())[1]
            attack = list(stats.values())[2]
            special = list(stats.values())[3]

        if area != 0:
            return True

        return False

# init vars
global area
global hp
global attack
global special
Ev = Event()
Co = Cover()
Pr = Print()


def main():

    option = Co.title()   

    # if break is called, end program
    if option == "break":
        return 0
    elif option == "new":
        Ev.beginning()
    elif option == "load":

        # TODO: switch statements?
        return 0

    return 0

# system calls name
if __name__ == "__main__":
    main()
