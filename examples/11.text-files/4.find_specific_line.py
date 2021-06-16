# open a plain text file... this returns a specialized data type that represents the file
f = open('data.txt', 'r')

# read all lines from the file
lines = f.readlines() # this returns a list of lines

# get the fourth line from the list
line_number = 10 # human-friendly line number
line = lines[line_number - 1].strip()

# print out the line
print(line)