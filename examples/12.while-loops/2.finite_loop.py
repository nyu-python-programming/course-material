import random

def main():
    # a finite loop....
    # this loop will keep on iterating as long as the random number that is generated is not a 5
    while random.randint(1, 10) != 5:
        print("Hello")
        
    # this will run whenever the loop terminates
    print("Done!")

# call the main function
main()