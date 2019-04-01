""" Doom or Bloom

Course: CS 30
Period: 3
Date created: April 1, 2019
Date completed: April
By: Andrew Li
This is a text-based Python game

"""

# import modules


# shortened versions
Ev = Event() 


class Event():
    """All events"""

    def __init__(self):
        action = str(input("What do you do?").split())

    def beginning(self):

        possible = ["look", "crouch", "observe", "see", "go", ""]

        if (action in possible):

            #switch statement

        else:

            return "not possible"


def title():
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


def start():

    print(""""
    2019: You fall into a nuclear dump site

    Yarning for sunlight to photosynthesize,
    you venture with your newly mutated roots
    in hopes of reaching fresh air and sunlight

    As you wonder around on your studded roots,
    you find a small hole

    """)

    Ev.beginning()


def main():

    title()
    start()
    return 0

# system calls name
if __name__ == "__main__":
    main()
