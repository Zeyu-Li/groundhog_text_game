""" Doom or Bloom

Course: CS 30
Period: 3
Date created: April 1, 2019
Date completed: April 18, 2019
By: Andrew Li

This is a text-based Python game that puts you at the site of the action
"""

# import from custom module
from cout import Text
# import from STL
import json
import os
import time
import random

# global vars
T = Text()
global values
values = {}
global quit_flag
quit_flag = False
global enemies
enemies = {
    "groundhog": {

        'hp': 2,
        'attack': 1

    },
    "spider": {
        'hp': 9,
        'attack': 2
    }
}


class Cover:
    """ this class houses the cover screen for the game when it loads in """

    def __init__(self):
        """ outputs title screen art/stylized text """
        output("title", "p")

    def options(self):
        """ options for title screen """

        test = True
        load = stats()
        while test:
            T.stylized("NEW GAME")
            if load:
                T.stylized("LOAD GAME")
            T.stylized("HELP")
            T.stylized("ABOUT")
            T.stylized("QUIT")

            option = user_input()

            if option in {"NEW GAME", "NEW", "N"}:
                os.system('cls')
                os.remove("stats.json")
                stats()
                return "new"
            elif option in {"LOAD GAME", "LOAD", "L"}:
                os.system('cls')
                return "load"
            elif option in {"HELP", "H"}:
                self.help()
                continue
            elif option in {"ABOUT", "A"}:
                self.about()
                continue
            elif option in {"QUIT", "Q"}:
                quit()
            else:
                print("\nYour input is not recognized, please try again\n")

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

    def event_1(self, option):
        """ first intro event; option argument represents the user input """

        for action in option:
            if action in {"LOOK", "OBSERVE", "SEE", "PEEK", "VIEW"}:
                T.slow("\nYou observe the hole and find that it is large" +
                       "\nenough for you to climb in")
                return True
            elif action in {"CRAWL", "CLIMB", "SNEAK"}:
                return False
            elif action in {"HINT", "AID", "HELP"}:
                T.slow("Hint: What would a groundhog do?")
                return True
            elif action in {"QUIT", "Q"}:
                quit()
            else:
                T.slow("Sorry, this action is not permitted, please try\n" +
                       "again or enter help")
                return True

    def event_2(self):
        """ fighting option menu """

        test = True
        while test:

            option = print("| Attack | Run | Hide | Quit |")
            option = user_input()

            if option == "ATTACK":
                return "ATTACK"
            elif option == "HIDE":
                T.slow("Stop hiding")
                continue
            elif option == "RUN":
                T.slow("You try to run away but it doesn't work")
                return "RUN"
            elif option in {"QUIT", "Q"}:
                quit()
            else:
                T.slow("That is not a possible option")

    def cave(self, option):
        """ events in the cave """

        for action in option:
            if action in {"LOOK", "OBSERVE", "SEE", "PEEK", "VIEW"}:
                T.slow("\nYou observe the archway to the room and find\n" +
                       "that it is large enough for you to walk in")
                return True
            elif action in {"CRAWL", "GO", "SNEAK", "WALK", "JOG", "RUN"}:
                return False
            elif action in {"HINT", "AID", "HELP"}:
                T.slow("Hint: Just go into the room and " +
                       "don't think if the consequences")
                return True
            elif action in {"QUIT", "Q"}:
                quit()
            else:
                T.slow("Sorry, this action is not permitted, please try\n" +
                       "again or enter help")
                return True


class Fight:
    """ class for fight sequences """

    global enemies
    global values
    global quit_flag

    def tutorial(self):
        """ tutorial fight sequence """

        self.tutorial_enemy_attack("groundhog")
        if quit_flag:
            quit()
        T.slow("Now you have dodged the groundhog and there is time to do\n" +
               "something. What do you do?")

        while True:
            if Options().event_2() == "RUN":
                T.slow("The groundhog is still chasing you")
                continue
            else:
                T.slow("You have defeated the groundhog")
                break

        level_up()

        time.sleep(1)

    def normal(self, enemy_, time, possible_button):
        """ this is how a normal non-tutorial enemy is fought """

        my_list = ['A'] + ['B'] * 9
        if random.choice(my_list) == 'B':
            self.enemy_attack(possible_button, time, enemy_)

        while True:
            if Options().event_2() == "RUN":
                self.enemy_attack(possible_button, time, enemy_)
            else:
                enemies[enemy_]['hp'] = enemies[enemy_]['hp'] - values['hp']
                enemy_hp = enemies[enemy_]['hp']
                if enemies[enemy_]['hp'] > 0:
                    T.slow(f"You hit the {enemy_} and it has {enemy_hp} hp")
                    self.enemy_attack(possible_button, time, enemy_)
                else:
                    T.slow(f"The {enemy_} falls")
                    return 0

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
            quit()


class Events:
    """ timeline of events; primary class that drives all the pieces """

    global quit_flag
    global values

    def begin(self):
        """ tutorial """

        output("Ev1", "s")
        test = True
        while test:
            request = user_input().split(" ")
            test = Options().event_1(request)

        values["area"] = 1

        self.one()

    def one(self):
        """ tutorial fight sequence """

        output("Ev2", "s")
        Fight().tutorial()

        if quit_flag:
            quit()

        values["area"] = 2

        self.two()

    def two(self):
        """ another fight sequence """

        T.slow("Now, you have defeated the groundhog, a second one approaches")
        Fight().normal("groundhog", 2, ("B", "A"))

        if quit_flag:
            quit()

        values["hp"] = values["max_hp"]
        hp = values["hp"]

        T.slow("As you defeat the groundhog, you absorb the nutrients from\n" +
               f"the groundhogs and recover your HP back to {hp}")

        values["area"] = 3

        self.three()

    def three(self):
        """ last objective (another looking sequence) """

        T.slow("You gather your breath and see that the cavernous space is\n" +
               "dark and wide. A streak of light rests in the corner of\n" +
               "your eye. It appears to be in a small room. What do you do?")

        test = True
        while test:
            request = user_input().split(" ")
            test = Options().cave(request)

        T.slow("You walk to the archway and you spot a giant spider\n" +
               "Unfortunately, as you back away slowly, it saw\n" +
               "you and smacks into the archway")

        time.sleep(1.5)

        values["area"] = 4

        self.four()

    def four(self):
        """ boss battle """

        Fight().normal("spider", 1.5, ("Z", "X", "W", "F"))

        T.slow("As the spider dies, you go into the room and find an\n" +
               "opening and walk into the light")
        T.slow("To be continued")

        time.sleep(1.5)

        quit()

        # END OF THE PROGRAM


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
        T.slow(text[part])


def special_loops(time_requested, button, enemy, tries=4):
    """ sequence for tutorial fight; you must hit a button by
    time_requested amount of time
    time_requested = time needed to accomplish button press
    button = button that needs to be pressed
    enemy = attacking enemy
    tries = number of tries till the enemy hits you """

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

                T.slow("You dodged successfully")
                return True
            elif user_input in ("Q", "QUIT"):
                quit_flag = True
                return 0
            else:
                if i == tries-1:
                    if not values['hp'] - enemies[enemy]["attack"] == 0:
                        values['hp'] = values['hp'] - enemies[enemy]["attack"]
                        T.slow(f"The {enemy} has hit you!\n" +
                               "You took 1 damage.\n" +
                               f"Now you have {values['hp']} hp left\n")
                        continue
                    T.slow("The groundhog missed")
                    continue
                T.slow("It's getting closer")


def loop(time_requested, button, enemy, tries=4):
    """ sequence for tutorial fight; you must hit a button by
    time_requested amount of time
    time_requested = time needed to accomplish button press
    button = button that needs to be pressed
    enemy = attacking enemy
    tries = number of tries till the enemy hits you """

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

                T.slow("You dodged successfully")
                return True
            elif user_input in ("Q", "QUIT"):
                quit_flag = True
                return 0
            else:
                if i == tries - 1:
                    if not values['hp'] - enemies[enemy]["attack"] == 0:
                        values['hp'] = values['hp'] - enemies[enemy]["attack"]
                        T.slow(f"The {enemy} has hit you!\n" +
                               "You took 1 damage.\n" +
                               f"Now you have {values['hp']} hp left\n")
                        continue
                    quit_flag = "Over"
                    return 0
                T.slow("It's getting closer")


def level_up():
    """ level up sequence """

    # level up is always +1 attack and +1 or +2 hp
    values["attack"] = values["attack"] + 1
    values["max_hp"] = values["max_hp"] + random.randint(1, 2)
    max_hp = values["max_hp"]
    attack = values["attack"]

    T.slow(f"Good job, you leveled up\n HP: {max_hp}, Attack: {attack} ")

    values["hp"] = values["max_hp"]


def game_over():
    """ gameover function re inits all values and resets the program """

    T.slow("Game Over")
    time.sleep(1)

    global values
    values = {}
    global quit_flag
    quit_flag = False

    # resets program in event of game over
    main()
    os._exit(0)


def quit():
    """ function for everytime you select quit """

    # stores char values and exits program
    end()
    T.slow("\nThanks for playing")
    time.sleep(1.2)
    os.system('cls')
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
        # switch statements for which area you are in
        area = values["area"]
        if area == 1:
            Events().one()
        elif area == 2:
            Events().two()
        elif area == 3:
            Events().three()
        elif area == 4:
            T.slow("The spider is attacking you")
            time.sleep(1)
            Events().four()
        else:
            T.slow("Unknown error in loading")
            quit()
    else:
        return 0

    quit()

# system calls name
if __name__ == "__main__":
    main()
