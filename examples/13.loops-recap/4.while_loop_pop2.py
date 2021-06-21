def main():
    
    list_of_words = ['hippopotamus', 'platypus', 'mongoose', 'raven']

    # iterate through this list using a simple while loop
    while len(list_of_words) > 0:
        word = list_of_words.pop(0) # returns the first value from the list AND pops it off
        print("The word is '{}'.".format(word) )

# call the main function
main()
