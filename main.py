""" Doom or Bloom

Course: CS 30
Period: 3
Date created: April 1, 2019
Date completed: April
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

            # TODO: optimize 

            if char == "\"":
                continue

            sys.stdout.write(char)

            time.sleep(.03)

        return 0


class Event:
    """All events"""

    def beginning(self):

        # TODO: starting adventure

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

        load = stats()

        test = True

        while True:

            Pr.instant("NEW GAME")

            Pr.instant("HELP")

            if not load:
                Pr.instant("LOAD GAME")

            Pr.instant("QUIT")

            # user option
            option = user_input()

            if option == "QUIT":

                Pr.slow("Thanks for playing")
                return "BREAK"

            elif option == " HELP":

                Co.help()



        return 0

    def help(self):

        print("\n To start this game, enter \"new game\"".center(20))
        print("If you have previously played this game,".center(20))
        print("if you don't see the option, report the bug in the following url:".center(20))
        print("https://github.com/Zeyu-Li/text_game/issues".center(20))

def user_input():

    return (str(input("> ").split())).upper()



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


def start():

    intro = """"
    2019: You fall into a nuclear dump site

    Yearning for sunlight to photosynthesize,
    you venture with your newly mutated roots
    in hopes of reaching fresh air and sunlight

    As you wonder around on your studded roots,
    you find a small hole

    With limited time on your leaves, what do you do?
    """

    Pr.slow(intro)

    Ev.beginning()

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

    if option == "BREAK":

        return 0

    # start()
    return 0

# system calls name
if __name__ == "__main__":

    main()
