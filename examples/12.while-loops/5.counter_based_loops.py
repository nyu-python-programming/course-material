def main():
    i = 0 # start off a counter at its starting value

    # iterate as long as that counter is less than some max threshold value
    while i < 10:
        print("Hello")
        i += 1 # increment the counter with every iteration (same as i = i + 1)

    # run the following after the loop terminates
    print("Done! Printed out hello {} times.".format(i))

# run the function
main()
