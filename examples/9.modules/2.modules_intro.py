# import a module
import my_module as m

# reference a variable in the module
print("The first number is {}.".format(m.x))

# call one of the functions within the module
print("The second number is {}.".format(m.nonsense1()))

# call one of the functions within the module
message = "Your age in dog years is {}.".format(m.nonsense2())
print(message)

