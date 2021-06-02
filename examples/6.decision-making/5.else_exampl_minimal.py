
def ask_user_for_animal():
    """
    Ask the user for their favorite animal and output different responses based on that input.
    """

    # ask user a question
    response = input("What is your favorite animal? ")

    # convert to uppercase
    response = response.upper()

    # analyze the user's response

    # check whether the response is 'HIPPOPOTAMUS'
    if response == 'HIPPOPOTAMUS' or response == 'HIPPO':
        print("Wow.  I love hippos!")
    
    # else is a 'catch-all' sort of branch
    else:
        print("I'm so sorry you like that animal.")
    

# call the function
ask_user_for_animal()
