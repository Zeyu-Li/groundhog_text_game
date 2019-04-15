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
from print import *


slow("Hi")


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
                os.system('cls||echo -e \\\\033c')
                return "break"
            elif option == "HELP":
                Co.help()
            elif option == "ABOUT":
                Co.about()
            elif option in ( "NEW GAME", "NEW", "N"):
                os.system('cls||echo -e \\\\033c')
                return "new"
            elif option in ("LOAD GAME", "LOAD", "L"):
                os.system('cls||echo -e \\\\033c')
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

        Pr.slow(""""
    2019: You fall into a nuclear dump site

    Yearning for sunlight to photosynthesize,
    you venture with your newly mutated roots
    in hopes of reaching fresh air and sunlight

    As you wonder around on your studded roots,
    you find a small hole

    With limited time on your non-exist hands, what do you do?
        """)

        test = True

        while test:
            option = user_input().split(" ")

            # switch statement for actions attempted by user
            for action in option:

                if action in ["LOOK", "OBSERVE", "SEE", "PEEK", "VIEW"]:
                    Pr.slow("You observe the hole and find that it is large enough for you to climb in")
                    continue
                elif action in ("CRAWL", "CLIMB", "SNEAK"):
                    test = False
                    break
                elif action in ("HINT", "AID", "HELP"):
                    Pr.slow("Hint: What would a groundhog do?")
                    continue
                elif action in ("QUIT", "Q"):
                    end()
                    return 0
                else:
                    Pr.slow("Sorry, this action is not permitted, please try again")

        super().one()

    def one(self):

        global values

    #     Pr.slow(""""
    # You climb out of the hole and observe a few groundhogs,
    # but something doesn't seem right.

    # Upon closer inspection, you see most of the groundhogs as deformed

    # However, you seem to have gotten too close, so the groundhogs are rush towards you

    # You hope to dodge them

    #     """)

        game_state = loops(False, 5, "A")

        while not game_state:
            if damage(game_state):
                return 0

            game_state = loops(False, 5, "A")

        Pr.slow("You now have a time to pause, what do you do?")
        print("| Attack | Run | Hide | Quit |")

        test = True

        while test:

            option = user_input()

            if option == "ATTACK":
                Pr.slow("You hit the first groundhog and it falls")
                test = False
                break
            elif option == "HIDE":
                Pr.slow("Stop hiding")
            elif option == "RUN":
                Pr.slow("Don't be a coward")
            elif option in ("QUIT", "Q"):
                end()
                return 0


        Pr.slow("Another one is running towards you, what do you do?")
        print("| Attack | Run | Hide |")

        test = True
        while test:

            option = user_input()

            if option == "ATTACK":
                game_state = loops(False, 4, "B")
                if not game_state:
                    Pr.slow("You did not hit the groundhog and it claws you")
                    Pr.slow("You took 1 damage")
                print(f"You have {values[1]} hp")
                Pr.slow("You hit the Second groundhog and it falls")
                test = False
                break
            elif option == "HIDE":
                Pr.slow("Stop hiding")
            elif option == "RUN":
                Pr.slow("You run around, but you will never outrun or out tire the groundhog")

# start of standard functions
def user_input():

    return (str(input("> ").strip())).upper()

def loops(out_of_time, time_reqested, button, tries = 5):

    for i in range(tries):

        start_time = time.clock()
        user_input = str(input(f"Hit \"{button}\": ").strip()).upper()
        end_time = time.clock()

        print(end_time - start_time)

        if (user_input == button):
            
            if end_time - start_time > time_reqested:

                print("Too slow. Try again\n")
                continue

            Pr.slow("You dodged successfully")
            return True
        else:
            if i == 5:
                return False
            Pr.slow("It's getting closer")
            out_of_time = False
            continue

def damage(game_state):

    if values[1] == 0:
        
        Pr.slow("Game over")
        return True

    values[1] = values[1] - 1
    Pr.slow("You took 1 damage")
    print(f"You have {values[1]} hp")

def stats():

    global values

    if not os.path.exists('stats.json'):

        with open('stats.json', 'w') as fp:
            stats = {

                'area': '0',
                'hp': '5',
                'attack': '5'

            }
            json.dump(stats, fp)

        # TODO: if enough time, change this to a list
        values = [0, 5, 5]

    else:

        with open('stats.json', 'r') as fp:

            stats = json.load(fp)

            

            values[0] = list(stats.values())[0]
            values[1] = list(stats.values())[1]
            values[2] = list(stats.values())[2]

        if values[0] != 0:
            return True

        return False

def end():

    Pr.slow("\nThanks for playing")

    with open('stats.json', 'w') as fp:
        stats = {

            'area': str(area[0]),
            'hp': str(hp[1]),
            'attack': str(attack[2])

        }

        json.dump(stats, fp)

# init vars
# TODO: if enough time, change this to a list
global values
values = [0, 5, 5]
Ev = Event()
Co = Cover()
Pr = Print()


def main():

    # option = Co.title()

    # # if break is called, end program
    # if option == "break":
    #     return 0
    # elif option == "new":
    #     Ev.beginning()
    # elif option == "load":

        # # TODO: switch statements?
        # return 0

    Ev.one()
    end()
    return 0

# system calls name
if __name__ == "__main__":
    main()
