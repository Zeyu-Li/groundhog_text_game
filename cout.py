import time
import sys


def stylized(text):

    print(f"---==  {text}  ==---\n".center(42))
    return 0


def slow(text):

    for char in text:

        if char == "\"":
            continue

        # sout in what looks like Java syntax and pause for a little bit
        sys.stdout.write(char)
        time.sleep(.03)

    print("\n")
    return 0