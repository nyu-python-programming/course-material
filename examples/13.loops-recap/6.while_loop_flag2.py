def main():

    list_of_words = ['hippopotamus', 'platypus', 'mongoose', 'raven', 'kiwi']

    # iterate through this list using a simple while loop
    is_more_values = True # a FLAG!
    i = 0 # an accumulator!
    while is_more_values:
        word = list_of_words[i]
        print("The word is '{}'.".format(word) )
        i += 1 # increment the accumulator
        # determine whether we have reached the end of the list
        if i == len(list_of_words):
            # cause the loop to terminate if so
            is_more_values = False

# call the main function
main()
