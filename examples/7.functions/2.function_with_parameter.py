
# define a function... a.k.a some code to store away in memory for later use
# this function definition has one parameter
def do_something(word):
    # code within a function must be indented to the right compared to the definition line
    message = "The word of the moment is: {}.".format(word)
    print(message)


# call the function with an argument... this is the value that gets placed into the parameter variable
do_something("innocuous")

# call the same function again with a different argument
do_something("portentious")

# call the same function again with a different argument
do_something("indignant")
