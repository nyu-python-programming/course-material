
def get_user_age():
    age = input("What's your age? ")
    age = int(age)
    return age

def get_dog_age(age):
    dog_age = age / 7
    return dog_age

def output_result(dog_age):
    dog_age = format(dog_age, '.1f')
    print("Your age in dog years is: {}.".format(dog_age))

# get the user's age
age = get_user_age()

# convert to dog years
dog_age = get_dog_age(age)

# output the result
output_result(dog_age)
