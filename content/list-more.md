---
layout: github
title: More About Lists
permalink: /list-more
redirect_from: /list-more.md
---

# More about Lists

## List functions

- `x = [0, 1, 2]`
- find out how many elements are in a list: `len(x)` # -> `3`
- append a single value to a list: `x.append(3)` # -> `[0, 1, 2, 3]`
- append a sequence to a list: `x.extend("cat")` # -> `[0, 1, 2, 3, 'c', 'a', 't']`
- remove the last element from a list: `x.pop()` # -> `[0, 1, 2, 3, 'c', 'a']`
- remove any element from a list: `x.pop(4)` # -> `[0, 1, 2, 3, 'a']`
- remove the first occurance: `x.remove("a")` # -> `[0, 1, 2, 3]`
- insert an element into the list: `x.insert(2, "foo")` # -> `[0,1,'foo',2,3]`
- reverse a list: `x.reverse()` # -> `[3, 2, 1, 0]`
- sort a list: `x.sort()` # -> `[0, 1, 2, 3]`

## Multidimensional Lists

A two-dimensional list:

```python
x = [
    [ "this is" , "the first" , "row" ],
    [ "another", "list, another", "row" ],
    [ "the" , "last" , "row" ]
]
```

- access individual elements: `x[1][0]` # -> `"another"`
- overwrite individual elements: `x[2][2] = "stand"`
- looping through multidimensional list with nested for loops

## Examples

### Comparison of mutable vs. immutable data types

```python
#ints, floats, bools, nonetypes, and strings are all immutable
#lists and dictionaries are mutable

x = 5
y = x #for immutable data types, the assignment operator makes a copy
x = 10

print(y)

x = [1,2,3,4]
y = x #for mutable data types, the assignment operator makes an alias
x.reverse()

print(y)
```

### Referring to list elements by their index numbers

```python
 # this is indexing. x[1] will access to second element, x[0] will access to first element, etc.

 # x points to a particular list value in memory
 x = [
    "tomatoes",
    "potatoes",
    "sprats",
    "frings",
    "diet coke",
]

#so x[0] will print out tomatoes, x[1] will print out potatoes
print(x[1])

# manually add a new element to the list
#x[5] = "carrots" # this causes an error, because the the index 5 is higher than any element in the list
x.append("carrots") #this is the proper way to add a new element to the list at index 5


# example of how to loop through the elements of a list
for i in x:
    print(i)
```

### List functions

```python
x = [] #create a blank list
x.append("bob") #add an element to the list
x.append("sheila")
x.append("ramon")
x.append("polina")
x.append("francisco")
x.pop() #removes the last element from the list
x.pop()
x.pop(1) #if you indicate an index, it deletes the element with that index
x.insert(1, "francisco") #inserts a new element at index 1
x.extend("kat")#extend adds elements from a sequence into the list

#note that apend and extend do different things... know the difference!
#x.extend(["harry", "alicia", "shmuli"])
#x.append(["harry", "alicia", "shmuli"])

print(x) #do you really need a comment explaining this line?
```

### List functions (again)

```python
homeTowns = ["Denver", "Brooklyn", "Croton-on-Hudson", "Tupelo", "Mahopac", "Albany", "Boston", "Istanbul", "Medellin", "Jacksonville", "Osnabrueck", "Seattle", "San Diego", "Scranton", "San Antonio", "Sacramento", "Montval", "Weston"]

#get the length of any list using the len() function
lengthOfList = len(homeTowns)

#add another element to the list
homeTowns.append("New York")

#insert a new element into position #3 the old-school way
pos = 8
firstPart = homeTowns[:pos]
secondPart = homeTowns[pos:]
homeTowns = firstPart + ["Newark"] + secondPart

#insert a new element into position #3 the modern way
homeTowns.insert(8, "Vancouver")

#extend the list
homeTowns.extend(["foo", "bar"])

#remove the last element from the list based on its position
homeTowns.pop()
homeTowns.pop(len(homeTowns)-1)

#remove the first occurance of a specific value
homeTowns.remove("Medellin")

#try to remove the first occurance of a specific value that is actually not in the list
counter = 0
for value in homeTowns:
    if value == "San Francisco":
        homeTowns.pop(counter)
    counter = counter + 1

#reverse the order of a list
homeTowns.reverse()

#sort the order of a list alphabetically or numerically
homeTowns.sort()

print(homeTowns)
```

### Sort order

```python
#sort numeric lists
x = [10, 20.1, 5.0, 100, -6, 1]
x.sort()
x.reverse() #flip it in reverse order
print(x)

#sort string lists
x = ["bob", "rodrigo", "alonso", "zlata", "kevin", "xio"]
x.sort()
print(x)

#cannot sort mixed type lists
#x = ["bob", 10, True, None, 1.9, False, [], "harry"]
#x.sort() #an error... why would you ever want to do this?
#print(x)

#sort boolean list
x = [False, True, False, True, True, False, False]
x.sort() #falses are like 0, Trues are like 1
print(x)

#cannot sort NoneType values... why would you want to?
#x = [None, None, None, None]
#x.sort() #an error
#print(x)
```

### Populating a list from user input, and then reversing its order

```python
listOfNumbers = [] #blank list

keepLooping = True #flag

#loop until the flag is false
while keepLooping:
    num = input("What's the number?")
    if num.lower() == "get me out of here!":
        keepLooping = False
    elif num.isnumeric():
        num = int(num)
        listOfNumbers.append(num)
    else:
        print("Please enter a number...")

#reverse the order of the list
#listOfNumbers.reverse()
listOfNumbers = listOfNumbers[::-1]

#loop through the list and print out all the values
for value in listOfNumbers:
    print(value)

print("Done")
```

### Calculating averages

```python
average = 0
readings = []

reading = ""

while reading != "exit":
    reading = input("Please enter a reading: ")
    if reading.isnumeric():
        reading = int(reading)
        readings.append(reading) #add new element to list

sum = 0
for reading in readings:
    sum = sum + reading

numReadings = len(readings) #how many readings are there?
average = sum / numReadings  #caculate the average

print("The average reading was: ", average)
```

### Mood diagnostic tool

```python
def getNumberFromMood(mood):
    if mood == "angry":
        return 0
    elif mood == "sad":
        return 1
    elif mood == "apathetic":
        return 2
    elif mood == "happy":
        return 3

def getMoodFromNumber(num):
    if num == 0:
        return "angry"
    elif num == 1:
        return "sad"
    elif num == 2:
        return "apathetic"
    elif num == 3:
        return "happy"

moods = []
response = ""

while response != "exit":
    response = input("Please enter your current mood: ")
    if response != "exit":
        moods.append(response)

sum = 0
i = len(moods) - 1
counter = 0

while i > 0:
    sum = sum + getNumberFromMood(moods[i])
    i = i - 1
    counter = counter + 1
    if counter == 7:
        break

average = sum / len(moods)
average = round(average) #round to the closest integer

print(average)

mood = getMoodFromNumber(average)

print(mood)
```

### Characters

Strings and Lists are both Sequence data types, and so share a lot in
common.

```python
x = "this is a string"

#x[2] = "u" #this is an error... you cannot modify strings... they are immutable
#loop through the characters in the string, the same way you loop through elements in a list

for character in x:
    print(character)
```

### Aliases

```python
x = [
        "tomatos",
        "potatoes",
        "sprats",
        "frings",
        "diet coke"
]

# make an alias of x that points to the same list value in memory
y = x

# this works just like the previous example.
y[2] = "buttered haddock"

for element in x:
    print(element)
```

### Slicing

```python
x = [
    "tomatos",
    "potatoes",
    "sprats",
    "frings",
    "diet coke"
]

# copy of the first 3 element in x stored in y
y = x[0:3] #use slice indexing
x[2] = 'butternut squash'

#loop through the copy
for element in y:
    print(element)
y = x[::] # starting:ending:spacing(?) if the last one is -1, the list will be backwards.

# negative number always start from end of list to the biginning

#check whether a value exists as an element in the list
if "sprats" in x:
    print("ooooh, you like sprats??")
```

### Tic Tac Toe (the basic idea)

A game of [Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe)
requires a variety of list-related techniques in one example. The
following code shows the basic idea of how to store the game board as a
two-dimensional list.

```python
 def showBoard():
     global board
     for row in board:
         for col in row:
             print(col, end="")
         print()

 board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
    ]

 player = "0"
 counter = 0

 while True:
     showBoard()

     print("Please enter the row and column where you'd like to move in the format: 1,1")
      move = input("Where would you like to go?")

     #the split method chops up a string and returns a list
     coordinates = move.split(",")
     row = int(coordinates[0])
     col = int(coordinates[1])

     board[row][col] = player

     if counter % 2 == 0:
         player = "X"
     else:
         player = "O"

     counter = counter + 1
```

### Tic Tac Toe (complete)

This version of the Tic Tac Toe game includes various kinds of input
validation, and checks for wins with each move.

```python
 def printBoard():
     global board
     print("-------")
     for row in board:
         print("|", end="")
         for col in row:
             col = format(col, "1s")
             print(col, end="|")
         print()
         print("-------")


 #set up the blank game board as a two-dimensional list
 board = [

             ["", "", ""],
             ["", "", ""],
             ["", "", ""]

         ]


 #set up variables for each player
 player1 = "X"
 player2 = "O"

 #set a variable that stores the player whose turn it is currently
 currentPlayer = player1

 #kick into the game loop

 while True:
     #print out the board
     printBoard()

     #ask the user to enter their move
     print("It is", currentPlayer + "'s turn.")
     move = input("Where would you like to go?")

     #convert what the user entered into two numbers (as strings for now)
     move = move.replace(" ", "") #remove any spaces from the input

     #validate the input
     if move.find(",") < 0:
         print("Sorry, that's not a valid move...")
         print("Please enter the row and column as integers starting from zero serparated by commas")
         continue

     #parse the move
     pos = move.split(",") #spit the input into two parts, around the comma
     row = pos[0] #get the first value
     col = pos[1] #get the second value

     #convert them to integers, if possible
     if row.isnumeric() and col.isnumeric():
         row = int(row)
         col = int(col)
     else:
         print("Sorry, that's not a valid move...")
         print("Please enter the row and column as integers starting from zero serparated by commas")
         continue


     #implement the move...

     isValidNumbers = len(board) > row and len(board[row]) > col
     if isValidNumbers:
         isEmptySpot = board[row][col] == ""
         if isEmptySpot:
             #allow the move to occur
             board[row][col] = currentPlayer
         else:
             print("Sorry, that position is taken.  Please try a different position")
             continue
     else:
         print("Sorry, that's not a valid move...")
         print("Please enter the row and column as integers starting from zero serparated by commas")
         continue

     #check to see whether anybody won...

     #set up a flag
     isWon = False

     #check for horizontal wins in each row by seeing if the same values are in each column... ignore empty rows
     if board[0][0] != "" and (board[0][0] == board[0][1] == board[0][2]):
         isWon = True
     if board[1][0] != "" and (board[1][0] == board[1][1] == board[1][2]):
         isWon = True
     if board[2][0] != "" and (board[2][0] == board[2][1] == board[2][2]):
         isWon = True

     #check for vertical win in each column by seeing whether the same values are in each row... ignore empty columns
     if board[0][0] != "" and (board[0][0] == board[1][0] == board[2][0]):
         isWon = True
     if board[0][1] != "" and (board[0][1] == board[1][1] == board[2][1]):
         isWon = True
     if board[0][2] != "" and (board[0][2] == board[1][2] == board[2][2]):
         isWon = True

     #check for diagonal wins in both directions... ignore empty diagonal lines
     if board[0][0] != "" and (board[0][0] == board[1][1] == board[2][2]):
         isWon = True
     if board[0][2] != "" and (board[0][2] == board[1][1] == board[2][0]):
         isWon = True

     if isWon:
         #quit the loop
         break


     #flip turns
     if currentPlayer == player1:
         currentPlayer = player2
     else:
         currentPlayer = player1


 #if the program reaches this point, the game is over...

 #print the board one last time
 printBoard()

 #announce the winner
 print("The game is over")
 print(currentPlayer, "won.")
```
