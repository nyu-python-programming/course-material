# open a plain text file... this returns a specialized data type that represents the file
f = open('data.txt', 'r')

# read all lines from the file
lines = f.readlines() # this returns a list of lines

# loop through all the lines
for line in lines:
    line = line.strip()
    print(line)

# move the internal cursor back to the beginning of the file
f.seek(0)

# read a single line... since we used seek to return to the beginning of the file, this will be the first line of the file
line = f.readline().strip()
print("The first line of the poem is '{}'.".format(line))
