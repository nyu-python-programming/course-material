age = input("Please enter your age: ") # note that input always returns a string

dog_age = int(age) / 7 # note that division always results in a float

dog_age = int(dog_age) # convert to int, if that's what you want

dog_age = str(dog_age) # convert to string, so we can concatenate it to other strings

message = "Your age in dog years is " + dog_age + "!" # concatenate three strings together

print(message)
