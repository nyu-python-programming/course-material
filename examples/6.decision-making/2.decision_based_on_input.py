
def analyze_color_preference():
    """
    A function that asks the user for their favorite color, and
    outputs a message specific to 'green', 'red', and 'purple,
    but nothing for any other response.
    """

    # ask the user a question, store their response
    response = input("What's your favorite color? ")

    # make sure the user's input is in lowercase
    response = response.lower()

    # compare the user's input to lowercase hard-coded literals
    if response == 'green':
        print("I'm proud of you!")

    if response == 'red':
        print("Wow!  That's a great color.")

    if response == 'purple':
        print("Good choice!")

# call the function
analyze_color_preference()
