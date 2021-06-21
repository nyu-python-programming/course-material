def main():
    
    list_of_words = ['hippopotamus', 'platypus', 'mongoose', 'raven', 'kiwi']

    # iterate through this list using a simple while loop
    i = 0
    while i < len(list_of_words):
        word = list_of_words[i] # returns the first value from the list AND pops it off
        print("The word is '{}'.".format(word) )
        # increment the value of the counter
        i += 1

# call the main function
main()
