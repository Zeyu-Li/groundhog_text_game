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


class Cover:

    def title(self):
        output("title", "p")


def output(part, _print):
    with open('text.json', 'r') as fp:
        text = json.load(fp)

    print(text[part])


def main():

    Cover().title()

# system calls name
if __name__ == "__main__":
    main()
