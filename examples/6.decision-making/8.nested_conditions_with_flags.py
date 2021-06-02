
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

    # make a bunch of flags
    is_vegetarian = False
    is_vegan = False
    eats_soy_cheese = False

    # check whether what the user typed is in the list of affirmative responses
    if vegetarian in affirmations:
        # we determined the user is a vegetarian!
        is_vegetarian = True

    # do something if the user is a vegetarian
    if is_vegetarian:
        vegan = input("Are you vegan? ") # a follow-up question
        vegan = vegan.lower() # convert to lowercase
        is_vegan = vegan in affirmations

    # do something special for those who are vegan
    if is_vegan:
        # ask a follow-up question again
        soy_cheese = input("Do you eat soy cheese? ")
        soy_cheese = soy_cheese.lower()
        eats_soy_cheese = soy_cheese in affirmations

    # do something special for those who eat soy cheese
    if is_vegan and eats_soy_cheese:
        # do something because they eat soy cheese
        print("Good.  I'm sure it goes well melted on a sandwich.")
    elif is_vegan:
        # print something for those who do not eat soy cheese
        print("I'm not a fan either.")

    # do something special for those vegetarians who are not vegan
    if is_vegetarian and not is_vegan:
        # for those who are vegetarian but not vegan
        print("I was vegetarian for ten years, but never vegan!")

    # do something special for meat eaters    
    if not is_vegetarian:
        # do something if they are not vegetarian
        print("Enjoy your animal product.")

# call the function
ask_user_for_vegetarian_status()
