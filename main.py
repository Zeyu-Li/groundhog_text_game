""" Doom or Bloom

Course: CS 30
Period: 3
Date created: April 1, 2019
Date completed: April 18, 2019
By: Andrew Li

This is a text-based Python game that puts you at the site of the action
"""

# import from custom module
from cout import slow, stylized
# import from STL
import json
import os
import time
import random

# global vars
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
    """ this class houses the cover screen for the game when it loads in """

    def __init__(self):
        output("title", "p")

    def options(self):
        """ options for title screen """

        test = True
        load = stats()
        while test:
            stylized("NEW GAME")
            if load:
                stylized("LOAD GAME")
            stylized("HELP")
            stylized("ABOUT")
            stylized("QUIT")

            option = user_input()

            if option in ("NEW GAME", "NEW", "N"):
                os.system('cls')
                os.remove("stats.json")
                stats()
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
        """ Outputs help text """

        output("help", "p")
        delay = input()

    def about(self):
        """ Outputs about text """

        output("about", "p")
        delay = input()


class Options:
    """ this class hold methods for whenever a action require options """

    global quit_flag

    def __init__(self, options):
        """ get user input """

        if options == 2:
            print("| Attack | Run | Hide | Quit |")
        self.option = user_input().split(" ")

    def event_1(self):
        """ first intro event """

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
                slow("or enter help")
                return True

    def event_2(self):
        """ fighting option menu """

        test = True
        while test:
            if self.option == "ATTACK":
                slow("You hit the first groundhog and it falls to the ground")
                break
            elif self.option == "HIDE":
                slow("Stop hiding")
                continue
            elif self.option == "RUN":
                slow("Don't be a coward")
                continue
            elif self.option in ("QUIT", "Q"):
                quit_flag = True
                return 0
            else:
                slow("That is not a possible option")


class Fight:
    """ class for fight sequences """

    global enemies
    global quit_flag

    def tutorial(self):
        """ tutorial fight sequence """

        self.tutorial_enemy_attack("groundhog")
        if quit_flag:
            return "quit"
        slow("Now you have dodged the groundhog and there is time to do" +
             "something. What do you do?")

        Options(2).event_2()

        if quit_flag:
            return "quit"

        level_up()

    def normal(self, enemy_, time, possible_button):
        """ this is how a normal non-tutorial enemy is fought """

        my_list = ['A'] + ['B'] * 9
        if random.choice(my_list) == 'B':
            self.enemy_attack(possible_button, time, enemy_)
            if quit_flag:
                return "quit"

        Options(2).event_2
        # TODO: fight options

    def tutorial_enemy_attack(self, enemy):
        """ tutorial enemy attack; It is impossible to die """
        special_loops(4, "A", enemy)

    def enemy_attack(self, possible_button, time, enemy_):
        """ first real enemy (can die) """

        button = str(random.choice(possible_button))
        loop(time, button, enemy_, 2)
        if quit_flag == "Over":
            game_over()
        elif quit_flag:
            return "quit"


class Events:
    """ timeline of events """

    global quit_flag

    def begin(self):
        """ tutorial """

        output("Ev1", "s")
        test = True
        while test:
            test = Options(1).event_1()

        if quit_flag:
            return 0

        values["area"] = 1

        self.one()

    def one(self):
        """ tutorial fight sequence """

        output("Ev2", "s")
        Fight().tutorial()

        if quit_flag:
            return 0

        values["area"] = 2

        self.two()

    def two(self):
        """ another fight sequence """

        slow("Now, you have defeated the groundhog, a second one approaches")
        Fight().normal("groundhog", 2, ("B", "A"))

        if quit_flag:
            return 0

        values["area"] = 3

        self.three()

    def three(self):
        pass
        # TODO: third event (another looking sequence)

        values["area"] = 4

        self.four()

    def four(self):
        pass
        return "done"

# start of standard functions


def stats():
    """ grab and dump stats from player some json file """

    global values

    if not os.path.exists('stats.json'):
        with open('stats.json', 'w') as fp:
            stats = {
                "area": "0",
                "hp": "5",
                "max_hp": "5",
                "attack": "1"
            }
            json.dump(stats, fp)

        values = {
            "area": 0,
            "hp": 5,
            "max_hp": 5,
            "attack": 1
            }

        return False

    else:
        with open('stats.json', 'r') as fp:
            stats = json.load(fp)
            values["area"] = int(stats['area'])
            values["hp"] = int(stats['hp'])
            values["max_hp"] = int(stats['max_hp'])
            values["attack"] = int(stats['attack'])

        if values["area"] == 0:
            return False
        return True


def user_input():
    """ getting user input from terminal """

    return (str(input("> ").strip())).upper()


def output(part, type_):
    """ outputs string in variety of ways from the text.json file
    - part is the requested printing section
    - type_ is how to print pat (p = standard print; s = slow print)
    """

    with open('text.json', 'r') as fp:
        text = json.load(fp)

    if (type_ == "p"):
        print(text[part])
    elif (type_ == "s"):
        slow(text[part])


def special_loops(time_requested, button, enemy, tries=4):
    """ sequence for tutorial fight; you must hit a button by
    time_requested amount of time
    time_requested = time needed to accomplish button press
    button = button that needs to be pressed
    enemy = attacking enemy
    tries = number of tries till the enemy hits you"""

    global enemies
    global quit_flag
    test = True
    while test:
        for i in range(tries):

            start_time = time.time()
            user_input = str(input(f"Hit \"{button}\": ").strip()).upper()
            end_time = time.time()

            if user_input == button:
                if end_time - start_time > time_requested:
                    print("Too slow. Try again\n")
                    continue

                slow("You dodged successfully")
                return True
            elif user_input in ("Q", "QUIT"):
                quit_flag = True
                return 0
            else:
                if i == tries-1:
                    if not values['hp'] - enemies[enemy]["attack"] == 0:
                        values['hp'] = values['hp'] - enemies[enemy]["attack"]
                        slow(f"The {enemy} has hit you!")
                        slow("You took 1 damage.")
                        slow(f"Now you have {values['hp']} hp left")
                        continue
                    slow("The groundhog missed")
                    continue
                slow("It's getting closer")


def loop(time_requested, button, enemy, tries=4):
    """ sequence for tutorial fight; you must hit a button by
    time_requested amount of time
    time_requested = time needed to accomplish button press
    button = button that needs to be pressed
    enemy = attacking enemy
    tries = number of tries till the enemy hits you"""

    global enemies
    global quit_flag

    test = True
    while test:
        for i in range(tries):

            start_time = time.time()
            user_input = str(input(f"Hit \"{button}\": ").strip()).upper()
            end_time = time.time()

            if user_input == button:
                if end_time - start_time > time_requested:
                    print("Too slow. Try again\n")
                    continue

                slow("You dodged successfully")
                return True
            elif user_input in ("Q", "QUIT"):
                quit_flag = True
                return 0
            else:
                if i == tries-1:
                    if not values['hp'] - enemies[enemy]["attack"] == 0:
                        values['hp'] = values['hp'] - enemies[enemy]["attack"]
                        slow(f"The {enemy} has hit you!")
                        slow("You took 1 damage.")
                        slow(f"Now you have {values['hp']} hp left")
                        continue
                    quit_flag = "Over"
                    return 0
                slow("It's getting closer")


def level_up():
    """ level up sequence """

    values["attack"] = values["attack"] + 1
    values["max_hp"] = values["max_hp"] + random.randint(1, 2)
    max_hp = values["max_hp"]
    attack = values["attack"]

    slow(f"Good job, you leveled up\n HP: {max_hp}, Attack: {attack} ")

    values["hp"] = values["max_hp"]


def game_over():
    """ gameover function re inits all values and resets the program """

    slow("Game Over")
    time.sleep(1)

    global values
    values = {}
    global quit_flag
    quit_flag = False

    main()
    os._exit(0)


def end():
    """ closing method that stores the values such as hp, attack, etc """

    global values
    with open('stats.json', 'w') as fp:
        stats = {

            'area': str(values["area"]),
            'hp': str(values["hp"]),
            'max_hp': str(values["max_hp"]),
            'attack': str(values["attack"])

        }

        json.dump(stats, fp)


def main():
    """ main call function """

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

    end()
    time.sleep(1.2)
    os.system('cls')

# system calls name
if __name__ == "__main__":
    main()
