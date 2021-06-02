
def analyze_color_preference():
    """
    A function that asks the user for their favorite color, and
    outputs a message specific to 'green', 'red', and 'purple,
    but nothing for any other response.

    The conditions used to analyze the input are mutually exclusive.
    """

    # ask the user a question, store their response
    response = input("What's your favorite color? ")

    # make sure the user's input is in lowercase
    response = response.lower()

    # check whether the first character is a g
    if response[0] == 'g': # the condition could also be response.startswith('g')
        print("I'm proud of you!")

    # check whether the user's response has 3 characters
    elif len(response) == 3:
        print("Wow!  That's a great color.")

    # check whether the word ends in 'le'
    elif response[-2 : ] == 'le': # the condition could also be response.endswith('le')
        print("Good choice!")

    # check whether the response is red
    elif response == 'red':
        print("It's red!")

# call the function
analyze_color_preference()
