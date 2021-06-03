
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

# ask the user for a number
user_number = input("Please enter a number: ")
# if the user's response is numeric, convert it to an int
if user_number.isnumeric():
    user_number = int(user_number)

# ask the user for a word
user_word = input("Please enter a word: ")
# chastise the user if they have entered something that is not a word
if not user_word.isalpha():
    print("Tsk tsk, you should have entered a real word!")

# ask the user for an arbitrary value
user_arbitrary_value = input("Please enter an arbitrary value: ")
# convert the value to a boolean if it is the word "True" or "False"
if user_arbitrary_value == "True" or user_arbitrary_value == "False":
    user_arbitrary_value = bool(user_arbitrary_value)

# call the function with an argument... this is the value that gets placed into the parameter variable
do_something(user_number, user_word, user_arbitrary_value)

