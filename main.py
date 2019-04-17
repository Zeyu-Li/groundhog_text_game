""" Doom or Bloom

Course: CS 30
Period: 3
Date created: April 1, 2019
Date completed: April 18, 2019
By: Andrew Li

This is a text-based Python game that puts you at the site of the action
"""

from cout import slow, stylized
import json
import os
import time

global values
values = {}
global quit_flag
quit_flag = False
global enemies
enemies = {
    "groundhog": {

        'hp': 2,
        'attack': 1

    }

}


class Cover:

    def __init__(self):
        output("title", "p")

    def options(self):
        test = True
        load = stats()
        while test:
            stylized("NEW GAME")
            if not load:
                stylized("LOAD GAME")
            stylized("HELP")
            stylized("ABOUT")
            stylized("QUIT")

            option = user_input()

            if option in ("NEW GAME", "NEW", "N"):
                os.system('cls')
                return "new"
            elif option in ("LOAD GAME", "LOAD", "L"):
                os.system('cls')
                return "load"
            elif option in ("HELP", "H"):
                self.help()
                continue
            elif option in ("ABOUT", "A"):
                self.about()
                continue
            elif option in ("QUIT", "Q"):
                slow("\nThanks for playing")
                time.sleep(1.2)
                os.system('cls')
                return "break"
            else:
                print("\n Your input is not recognized, please try again\n")

    def help(self):
        output("help", "p")
        delay = input()

    def about(self):
        output("about", "p")
        delay = input()


class Options:

    def __init__(self):
        self.option = user_input().split(" ")

    def event_1_1(self):
        global quit_flag
        for action in self.option:
            if action in ("LOOK", "OBSERVE", "SEE", "PEEK", "VIEW"):
                slow("\nYou observe the hole and find that it is large enough")
                slow("for you to climb in")
                return True
            elif action in ("CRAWL", "CLIMB", "SNEAK"):
                return False
            elif action in ("HINT", "AID", "HELP"):
                slow("Hint: What would a groundhog do?")
                return True
            elif action in ("QUIT", "Q"):
                quit_flag = True
                return False
            else:
                slow("Sorry, this action is not permitted, please try again")
                return True


class Fight:

    global enemies

    def tutorial(self):
        self.tutorial_enemy_attack("groundhog")

    def tutorial_enemy_attack(self, enemy):
        special_loops(4, "A")


class Events:

    global quit_flag

    def __init__(self):
        pass

    def begin(self):
        # output("Ev1", "s")
        test = True
        while test:
            test = Options().event_1_1()

        if quit_flag:
            return 0

        values["area"] = 1

        self.one()

    def one(self):
        # output("Ev2", "s")
        Fight().tutorial()
        self.two()

    def two(self):
        pass
        self.three()

    def three(self):
        pass
        self.four()

    def four(self):
        pass
        return "done"

# start of standard functions


def stats():

    global values

    if not os.path.exists('stats.json'):
        with open('stats.json', 'w') as fp:
            stats = {
                "area": "0",
                "hp": "5",
                "attack": "1"
            }
            json.dump(stats, fp)

        values = {
            "area": 0,
            "hp": 5,
            "attack": 1
            }

        return False

    else:
        with open('stats.json', 'r') as fp:
            stats = json.load(fp)
            values["area"] = int(stats['area'])
            values["hp"] = int(stats['hp'])
            values["attack"] = int(stats['attack'])

        if values["area"] == 0:
            return True


def user_input():

    return (str(input("> ").strip())).upper()


def output(part, type_):
    with open('text.json', 'r') as fp:
        text = json.load(fp)

    if (type_ == "p"):
        print(text[part])
    elif (type_ == "s"):
        slow(text[part])


def special_loops(time_requested, button, tries=4):
    for i in range(tries):

        start_time = time.clock()
        user_input = str(input(f"Hit \"{button}\": ").strip()).upper()
        end_time = time.clock()

        if user_input == button:
            if end_time - start_time > time_requested:
                print("Too slow. Try again\n")
                continue

            slow("You dodged successfully")
            return True
        else:
            if i == tries:
                if not values['hp'] - enemies[enemy]["attack"] == 0:
                    values['hp'] = values['hp'] - enemies[enemy]["attack"]
                    slow("You took 1 damage.")
                    slow(f"Now you have {values['hp']} hp left")
                    continue
                slow("The groundhog missed")
                continue
            slow("It's getting closer")


def main():

    option = Cover().options()

    if option == "new":
        Events().begin()
    elif option == "load":
        # switch statements
        area = values["area"]
        if area == 1:
            Events().one()
        elif area == 2:
            Events().two()
        elif area == 3:
            Events().three()
        elif area == 4:
            Events().four()
    else:
        return 0

    slow("\nThanks for playing")
    time.sleep(1.2)
    os.system('cls')

# system calls name
if __name__ == "__main__":
    main()
