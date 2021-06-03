
# define a function... a.k.a some code to store away in memory for later use
# this function definition has three parameters
def do_something(num, word, arbitrary_value):
    # code within a function must be indented to the right compared to the definition line
    product = num * 10
    sentence = "The word of the moment is: {}.".format(word)
    is_boolean = type(arbitrary_value) == bool

    # print out different depending upon the first argument value
    if product > 20:
        print("Thank you for entering a value greater than 2!")
    else:
        print("I'm so sorry, your number is less than 3.")

    # print out the sentence
    print(sentence)

    # print out different messages, depdning upon whether the third argument was a boolean value
    if is_boolean:
        print("Thanks for the boolean value!")
    else:
        print("Thanks for not supplying a boolean value!")    

# call the function with an argument... this is the value that gets placed into the parameter variable
do_something(2, "innocuous", True)

