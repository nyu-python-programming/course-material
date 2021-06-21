def main():

    list_of_words = ['hippopotamus', 'platypus', 'mongoose', 'raven']

    # iterate through this list using a simple while loop
    is_more_values = True # a FLAG!
    while is_more_values:
        word = list_of_words.pop(0) # returns the first value from the list AND pops it off
        print("The word is '{}'.".format(word) )
        # determine whether there are any more values in the list left
        if len(list_of_words) == 0:
            # if the list is empty, cause the loop to terminate next cycle
            is_more_values = False

# call the main function
main()
