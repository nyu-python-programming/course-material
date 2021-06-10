# import a module
import my_module

# reference a variable in the module
print("The first number is {}.".format(my_module.x))

# call one of the functions within the module
print("The second number is {}.".format(my_module.nonsense1()))

# call one of the functions within the module
message = "Your age in dog years is {}.".format(my_module.nonsense2())
print(message)

