import random

def get_random():
    return random.randint(1, 10)

# generate 100 random numbers between 1 and 10 inclusive
for i in range(100):
    rand1 = get_random()
    print(rand1)
    