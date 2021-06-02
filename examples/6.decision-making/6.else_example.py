
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
    
    # check whether the response is 3 characters long
    elif len(response) == 3:
        print("Great.  I love short-named animals!")

    # check whether 'ph' exists within the response
    elif response.find('PH') >= 0: # remember, find() returns -1 if it does not find the substring
        print("All the great animals contain 'ph'!")

    # else is a 'catch-all' sort of branch
    else:
        print("I'm so sorry you like that animal.")
    

# call the function
ask_user_for_animal()
