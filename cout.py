import time
import sys


class Text:
    """ this is a simple module used for outputing text
    the first args is the text that needs to be outputted """

    def stylized(self, text):
        """ outputs in the form of ---== *some_text ==--- """

        print(f"---==  {text}  ==---\n".center(42))
        return 0

    def slow(self, text):
        """ outputs one letter at a time with about
        .03 seconds between outputs """

        for char in text:

            if char == "\"":
                continue

            # sout in what looks like Java syntax and pause for a little bit
            sys.stdout.write(char)
            time.sleep(.03)

        print("\n")
        return 0
