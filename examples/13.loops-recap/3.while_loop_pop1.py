def main():

    list_of_words = ['hippopotamus', 'platypus', 'mongoose', 'raven']

    # iterate through this list using a simple while loop
    while list_of_words != []:
        word = list_of_words.pop(0) # returns the first value from the list AND pops it off
        print("The word is '{}'.".format(word) )

# call the main function
main()
