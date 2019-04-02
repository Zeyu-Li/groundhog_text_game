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


class Print:

    def instant(self, text):

        print(f"---==  {text}  ==---\n".center(60))

        return 0

    def slow(self, text):

        print(text)
        return 0


class Event:
    """All events"""

    # def __init__(self):
    #     action = str(input("What do you do?").split())

    def beginning(self):

        possible = ["look", "crouch", "observe", "see", "go", ""]

        if (action in possible):

            # switch statsement

            return 0

        else:

            return "not possible"


class Cover():

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

        Pr.instant("NEW GAME")

        Pr.instant("HELP")

        if not load:
            Pr.instant("LOAD GAME")

        Pr.instant("QUIT")

        option = str(input("> ")).split().upper()

        return option


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

    print(""""
    2019: You fall into a nuclear dump site

    Yearning for sunlight to photosynthesize,
    you venture with your newly mutated roots
    in hopes of reaching fresh air and sunlight

    As you wonder around on your studded roots,
    you find a small hole

    """)

    Ev.beginning()


def init():

    # global vars
    global area
    global hp
    global attack
    global special

    # shortened versions
    Ev = Event()
    Co = Cover()
    Pr = Print()


def main():

    init()

    option = Co.title()

    if not option:

        Pr.slow("Thanks for playing")
        return 0

    start()
    return 0

# system calls name
if __name__ == "__main__":

    main()
