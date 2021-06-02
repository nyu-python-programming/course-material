
def ask_user_for_vegetarian_status():
    """
    Ask the user whether they are vegetarian.
    Ask follow-up questions for those who are.
    """

    # ask the user for their response
    vegetarian = input("Are you a vegetarian? ")

    # convert it to lowercase so we can ignore case
    vegetarian = vegetarian.lower()

    # make a list of affirmative responses
    affirmations = ['yes', 'yeah', 'y', 'definitely', 'for sure', 'of course']

    # check whether what the user typed is in the list of affirmative responses
    if vegetarian in affirmations:
        # do something if the user is a vegetarian
        vegan = input("Are you vegan? ") # a follow-up question
        vegan = vegan.lower() # convert to lowercase
        if vegan in affirmations:
            # ask a follow-up question again
            soy_cheese = input("Do you eat soy cheese? ")
            soy_cheese = soy_cheese.lower()
            if soy_cheese in affirmations:
                # do something because they eat soy cheese
                print("Good.  I'm sure it goes well melted on a sandwich.")
            else:
                # print something for those who do not eat soy cheese
                print("I'm not a fan either.")
        else:
            # for those who are vegetarian but not vegan
            print("I was vegetarian for ten years, but never vegan!")
    
    else:
        # do something if they are not vegetarian
        print("Enjoy your animal product.")

# call the function
ask_user_for_vegetarian_status()
