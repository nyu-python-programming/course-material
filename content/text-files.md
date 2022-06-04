---
layout: github
title: Text Files
permalink: /text-files
redirect-from: /text-files.md
---

# Text files

## Files in Python

### Opening a text file

Text files can be opened in one of three distinct ways:

Read mode:

```python
#e.g.
f = open("data.csv", "r") #open in read mode
```

Write mode:

```python
#e.g.
f = open("data.csv", "w") #open in write mode
```

Append mode:

```python
#e.g.
f = open("data.csv", "a") #open in append mode
```

### Reading the contents of a text file

Read the entire file in one fell swoop:

```python
#e.g.
theFullMonty = f.read() #read entire file
```

Read just a single line at a time:

```python
#e.g.
line1 = f.readline() #get the first line
line2 = f.readline() #get the second line
#etc...
```

Loop through all lines:

```python
#e.g.
for line in f:
    #do something
```

### Checking whether a file already exists

Python\'s [os module](modules) contains
useful methods for checking whether any given file already exists in the
file system.

## Character encoding issues

There are several popular [encoding schemes for text
files](http://www.joelonsoftware.com/articles/Unicode.html): Unicode,
ASCII, UTF-8, UTF-16, etc. Each encoding scheme has a different system
for converting the characters you type on a keyboard into the numeric
codes that are ultimately stored in the computer\'s memory. In order to
read and write to a text file properly from a program, you will need to
know which encoding scheme a given text file uses.

### The problem

Python\'s `open()` function defaults to using whatever the default
encoding scheme is on the computer you\'re using. Often that\'s not good
enough. If you don\'t specify the correct encoding scheme, your program
may crash if it encounters a character that is not found in the encoding
scheme it is using.

### One solution

In situations where you need to use a specific encoding scheme,
[Python\'s codecs module](https://docs.python.org/3/library/codecs.html)
can help. One easy solution is to specify the encoding scheme you would
like to use when opening a file. You can do this easily with the codecs
module\'s `open()` function, rather than the default `open()` function

```python
import codecs

#the following example opens the file with utf-8 encoding
f = codecs.open("data.csv", mode='r', encoding='utf-8')
```

## Strings in Python

Python has lots of [useful String-related
functions](string-basics.md).

### String-related functions that return a String

- `.upper()` - returns an uppercase version of the string
- `.lower()` - returns a lowercase version of the string
- `.title()` - returns a version of the string with the first letter of
  every word capitalized.
- `.capitalize()` - returns a version of the string with the first
  letter capitalized
- `.strip()` - returns a version of the string with any leading
  whitespace removed
- `.rstrip()` - returns a version of the string with any trailing
  whitespace removed
- `.join(_some_list_)` - returns a string that has all items from the
  list argument separated using the string as separator

### String-related functions that return an Integer

- `.find(x)` - returns the index position in the String at which x is
  found

### String-related functions that return a Boolean

- `.isupper()` - returns boolean True if the string is uppercase, False
  otherwise
- `.islower()` - returns boolean True if the string is lowercase, False
  otherwise
- `.isnumeric()` - returns a boolean True if the string represents a
  number, False otherwise

### String-related functions that return a List

- `.split(_some_delimiter_)` - returns a list based on the contents of
  the string, by splitting the string everywhere it finds the
  delimiter specified as the argument

## Lists in Python

### Useful functions

[List functions](list-more) that modify an existing List:

- `.append(some_value)` - adds the value as a new element at the end of
  the list

## Example programs

### Data files

The following programs assume you have two text files in the same
folder:

**mydata.txt**:

`The first line in the text file`\
`The second line in the text file`

**sloppy_data.csv**:

`1,Peace Food,Manhattan,New York`\
`2,Bareburger,manhattan,new York`\
`3,Why not,manhattan, New york`\
`4,five guys, Manhattan, New York`\
`5,katz DELI,manhattan,new york`

### Grab entire contents of a text file

Read the entire contents of the file, and print them out.

```python
#open a text file in read mode
f = open("mydata.txt", "r")

#pull all the data out of the file into a variable
theTextInTheFile = f.read()

#print out the contents of the file
print(theTextInTheFile)
```

### Loop through each line of a text file and chop off line breaks

Remove the line break from the end of each file, and then print it out.

```python
#open a text file in read mode
f = open("mydata.txt", "r")

#loop through each line in the file, one by one
for line in f:

    #remove the line break from the end of the string
    line = line.rstrip()

    #print out the line
    print(line)
```

### Loop through all words in a text file

Loop through each word in the file (assuming words are separated by
spaces), and print it out.

```python
#open a text file in read mode
f = open("mydata.txt", "r")

#get the full text from the file
theFullText = f.read()

#split the text into a List of words by space delimiters
words = theFullText.split()

#loop through each word and analyze it
for word in words:

    #print for debugging
    print(word)
```

### Count the occurrences of a given word in a text file

Loop through each word in the file (assuming words are separated by
spaces), and print out how many times a search term is found. For
simplicity, this program does not account for punctuation, which would
cause problems in this code.

```python
#open a text file in read mode
f = open("mydata.txt", "r")

#get the full text from the file
theFullText = f.read()

#split the text into a List of words by space delimiters
words = theFullText.split()

#what word are we looking for?
searchTerm = "Ronkonkoma"

#keep a counter of how many times we found the word that we're looking for
counter = 0

#loop through each word and analyze it
for word in words:

    #check whether the word matches our searchTerm (case-insensitive)
    if word.lower() == searchTerm.lower():

        #if so, increment the counter
        counter = counter + 1

#print out the result
print("We found the word", searchTerm, counter, "times.")
```

### Fix sloppy capitalization in a CSV data file

Loop through each line in a CSV text file, loop through each value in
the line and modify it in some way (in this example, we simply
capitalize a word we are searching for). Store the modified values in a
two-dimensional list. Loop through this two-dimensional list and output
the modified values to a file.

```python
#####################################################
#PART 1 - SCRAPE THE DATA FROM A CSV FILE
#####################################################

#open a file in read mode
f = open("sloppy_data.csv", "r")

clean_data = [] #this will store the cleaned up data from all lines

#loop through each line in the file
for line in f:

    new_line = [] #this will store the cleaned up list of values in this one line

    line = line.strip() #get rid of line break on every line
    data = line.split(',') #split by commas to get a list of values

    #loop through every value in this list
    for thing in data:

        #if the value is 'ronkonkoma', convert it to uppercase 'RONKONKOMA'
        if thing == "ronkonkoma":
            thing = thing.upper()

        #append this value to the "clean" list of values in this line
        new_line.append(thing)

    #append this cleaned up data to the list
    clean_data.append(new_line)

#close the file
f.close()


#####################################################
#PART 2 - WRITE THE CLEANED UP DATA TO A NEW CSV FILE
#####################################################

#open a file in write mode
f = open("sloppy_data_fixed.csv", "w")

#loop through each list of cleaned up data... each list represents one line
for line_as_list in clean_data:

    #convert this line (currently stored a list) to a string with comma-separated values
    line_as_string = ",".join(line_as_list)

    #write this line's data to a file, along with a line break
    f.write(line_as_string + "\n")

#close the file
f.close()
```

## More examples

### Data file

These programs assume you have a text file named "`data.txt`" in the
same folder as your Python program. The data.txt file stores student
grades as comma separated values (CSV format). This type of format is
commonly used by spreadsheet programs like Microsoft Excel.

_Example data file_

This is our example \"`data.txt`\" file in CSV format.

```
Adam,85 Mark,22 Erica,100 Kaitlin,98 Spencer,69 John,88 Wilson,95
Spencer,49 Faith,89 Andrew,90 Celia,90 Mike,90
```

### Writing to a file

This program allows users to append new grades to the data.txt file.

Note that this program exhibits a bug if the user enters \"exit\" in
response to the first question.

```python
#this program allows us to append student grades to an existing data.txt file

#flag to indicate whether we opened the file or not
isFileOpen = False

try:
    myFile = open("data.txt", mode="a")
    isFileOpen = True
except FileNotFoundError:
    print("oops, sorry, didn't find the file... my bad")
except IOError:
    print("There was an IO error")
except:
    print("Sorry, I don't know what went wrong")

#if the file is open, start writing/appending to it
if isFileOpen:
    studentName = input("Please enter a student name:")
    studentGrade = input("Please enter this student's grade:")

    while studentName != "exit" and studentGrade != "exit":
        if studentName == "exit":
            break
        myFile.write(studentName + "," + studentGrade + "\n")
        studentName = input("Please enter a student name:")
        if studentName == "exit":
            break
        studentGrade = input("Please enter this student's grade:")
        if studentGrade == "exit":
            break

    myFile.close()
```

### Reading from a file

This program reads the grades from the data.txt file and outputs the
average grade for all students found in the file.

```python
#this program opens a file named "data.txt" that holds a student grade in each line in the format <name>,<grade>
#the program outputs the average grade of all students

#flag to keep track of whether we opened the file or not
isFileOpen = False

#open up a text file in read-only mode
try:
    myFile = open("data.txt", "r")
    isFileOpen = True #set flag to true now that we've opened the file
except FileNotFoundError:
    print("oops, sorry, didn't find the file... my bad")
except IOError:
    print("There was an IO error")
except:
    print("Sorry, I don't know what went wrong")


#if we've opened the file successfully, read from it
if isFileOpen:
    #read file all at once
    #dataFromFile = myFile.read() #read entire file and store in variable
    #print(dataFromFile) #print out entire file


    #keep track of the sum of all grades so we can get the average later
    runningTotal = 0

    #keep track of how many students we find in the text file
    numStudents = 0

    #read one line from a file
    line = myFile.readline()

    #make sure line has something in it
    while line != "":
        #increment the student counter
        numStudents = numStudents + 1

        #print it out
        line = line.rstrip("\n") #strip off trailing line break
        #print(line)

        #break up the string along the commas
        data = line.split(",")
        #print(data)
        #add the current student's grade to the running total
        runningTotal = runningTotal + int(data[1])


        #read another line
        line = myFile.readline()


#calculate the average grade
average = runningTotal/numStudents

#format it to look nice as a string
niceLookingAverage = format(average, ".2f")

#print out the average grade
print(niceLookingAverage)
```
