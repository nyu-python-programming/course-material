# open a plain text file... this returns a specialized data type that represents the file
f = open('data.txt', 'r')

# repeatedly reading a single line of data from the file
for i in range(3):
    line = f.readline().strip() # retrieve one line from the file    
    print(line) # print it out

# reset the file's internal cursor to go back to the beginning of the file
f.seek(0)

# repeatedly reading a single line of data from the file
for i in range(3):
    line = f.readline().strip() # retrieve one line from the file    
    print(line) # print it out

# close the file
f.close()
