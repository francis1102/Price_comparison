"""Component 1 of price comparison -
Get the name of the user and make sure its not blank
Created by Francis Torcuato
"""


def not_blank(question, error_message):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print(error_message)
        else:
            return response


# ******** Main Routine ********
name = not_blank("What's your name: ", "You can't leave this blank...")

