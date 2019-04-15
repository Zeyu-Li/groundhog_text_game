""""
Boilerplate project by Andrew Li
Description: 
"""
import json

def main():

    with open('text.json', 'w') as f:
        text = {

        'title': """
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
""",

        'help': """

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

        """,
        
    'about': """
    This is a text-based Python game made for a class project.

    If you wish to modify it, please read license,
    other than that, please enjoy the game ;)

    To continue, press the enter key

    """,

    'Ev1': """"
    2019: You fall into a nuclear dump site

    Yearning for sunlight to photosynthesize,
    you venture with your newly mutated roots
    in hopes of reaching fresh air and sunlight

    As you wonder around on your studded roots,
    you find a small hole

    With limited time on your non-exist hands, what do you do?
        """,
        }
        json.dump(text, f)
    return 0

# system calls main
if __name__ == "__main__":
    main()