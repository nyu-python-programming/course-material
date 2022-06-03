---
layout: github
title: Modules
permalink: /modules
redirect_from: /modules.md
---

# Modules

## About

Modules provide additional functionality (in the form of readymade
variables, functions, and classes) that is not loaded into the Python
interpreter by default. So importing a module simply loads these things
into the Python interpreter\'s memory so you can refer to them in your
code.

Some modules are included with the standard Python distribution and are
\"built-in\". Others require that you download and install them as
\"add-ons\".

### [A module by any other name](https://en.wikipedia.org/wiki/A_rose_by_any_other_name_would_smell_as_sweet)\...

While these are called \"modules\" in Python, sets of useful functions,
variables, and classes often go by other names in different programming
languages and their cultures:

- library
- Application Programming Interface (API)
- framework

Some may argue that there are differences in these terms, but they are
often used interchangeably in everyday parlance.

### built-ins

Built-in modules come bundled with Python:

- \_\_main\_\_ module/library is built-in to the interpreter by
  default
  - includes [built-in
    functions](https://docs.python.org/3.6/library/functions.html)
    you can refer to without explicitly importing a module
  - e.g. print(), input(), str(), int(), float(), etc\...
- [Python\'s standard distribution
  modules](http://docs.python.org/3/py-modindex.html) are bundled with
  Python when you download and install it, but not imported into the
  interpreter automatically.
  - e.g. math, random, urllib, etc\...

### add-ons

Add-on modules are not included with the standard Python distribution,
and must be downloaded and installed to be used:

- [a list of some useful add-on
  modules](https://wiki.python.org/moin/UsefulModules)

#### package managers

Adding new add-on modules to Python on a computer can be complicated,
time consuming, and thankless. For this reason, package managers -
programs that have been designed to provide a simple interface for
module installations - are often used. [pip](https://pip.pypa.io) is a
popular Python package manager.

### importing modules

There are two ways to import the functions from a module, for example:

- `import random`
- `from random import *`

### using code in modules

How you refer to the functions within a module from your code depends
upon how you imported it:

If you imported in the style, \"import random\", for example, you would
call that module\'s functions like this:

- `random.randint(1, 100)`
- `random.randrange(10)`
- `random.random()`
- `random.uniform(1.0, 10.0)`
- `random.seed(10)`

If you imported in the style, `from random import *`, for example, you would call that module\'s functions like this:

- `randint(1,100)`
- `randrange(10)`
- `random()`
- `uniform(1.0, 10.0)`
- `seed(10)`

## Random module

The random module contains lots of functions related to generating pseudo-random numbers, such as:

- `randint()`
- `randrange()`
- `random()`
- `uniform()`
- `seed()`

### generating a pseudo-random integer within a defined range

```python
import random
x = random.randint(10, 20) #generates an int between 10 and 20, inclusive
```

### generating pseudo-random numbers

```python
import random

#roll the dice
die1 = int((random.random() * 6) + 1)
die2 = int((random.random() * 6) + 1)

total = die1 + die2

if die1 == 1 and die2 == 1:
    print("Snake eyes!")

print("Your total is: " + str(total))
```

### How to shift the range of a pseudo-random number

This example shows how to take a pseudo-random number from within one range (0 to 0.999 in this example) and shift it to an equivalent number within another range (20 to 99.999 in this example).

```python
#import the random module
import random

#generate a random float betwen 0 and 0.99999
x = random.random()

#shift that number to be in the range between 20 to 99.9999
x = (x * 80) + 20

#print out the number
print(x)
```

### Specifying the seed used to generate random numbers

The seed is the \"kernel\" that your computer then applies a series of
mechanical operations onto until it turns into a believable-looking
pseudo-random number. Two random number generators that are given the
same seed will generate the same random numbers. This is the core of
many bank security systems.

```python
 import random

 print("Pseudo-random set of numbers based on seed 4")
 random.seed(4)
 print(random.random())
 print(random.random())
 print(random.random())
 print(random.random())
```

```python
 print("\nSame pseudo-random set of numbers based on seed 4")
 random.seed(4)
 print(random.random())
 print(random.random())
 print(random.random())
 print(random.random())
```

```python
 print("\nDifferent pseudo-random set of numbers based on seed 111")
 random.seed(111)
 print(random.random())
 print(random.random())
 print(random.random())
 print(random.random())
```

These methods in the random module allow you to have more flexibility in
the type of random numbers you generate.

### Using random.randrange(), random.randint(), and random.uniform()

```python
 import random

 #use randrange function
 print("Get a random number between 0-9")
 x = random.randrange(10)
 print(x)

 print("\nGet a random number between 50-100")
 x = random.randrange(50, 101)
 print(x)

 print("\nGet a even random number between 50-100")
 x = random.randrange(50, 101, 2)
 print(x)

 #use the randint function
 print("\n Get a random integer between 1-10")
 x = random.randint(1, 10)
 print(x)

 #use the uniform function
 print("\n Get a random float betweeen 1-10")
 x = random.uniform(1, 11)
 print(x)

 print("\n Get a random float with two decimal places betweeen 1-10 starting from a float with more decimal places")
 x = random.uniform(1, 11)
 x = x * 100 #shift the decimal point over two places to the right
 x = int(x) #slice off the remaining decimal point values
 x = x / 100 #shift the decimal point back two places to the left
 print(x)
```

## Math module

The math module contains lots of useful functions and variables related
to algebra and trigonometry, such as:

### Basics

Functions:

- `ceil()`
- `floor()`
- `pow()`
- `sqrt()`
- `factorial()`

Example:

```python
 import math
 x = 10.2
 y = math.ceil(x) #11
 z = math.floor(x) #10
```

### Trigonometry

Functions:

- `cos()`
- `sin()`
- `tan()`
- `acos()`
- `asin()`

Properties:

- `pi`
- `e`

Example:

```python
 #import the math module
 import math

 #call the math module's cos() function
 x = math.cos(90)

 #print out the result
 print("The cosine of 90 is", x)

 #print out the value of pi, which is a variable in the math module
 print("The value of pi is ", math.pi)
```

## Datetime module

The datetime module includes:

- collection of objects and functions related to dates, including
  today\'s date
- when printing out the value, the date defined from date.today or
  other date functions are integers in format of yyyy-mm-dd.
- see [official
  documentation](http://docs.python.org/3.3/library/datetime.html)

### Determine the day of the week

```python
 from datetime import *

 def getFriendlyDayFromInt(dayNum):
     #receive the numeric day as input in the variable dayNum
     #figure out what weekday is based on the dayNum
     if dayNum == 0:
         weekday = "Monday"
     elif dayNum == 1:
         weekday = "Tuesday"
     elif dayNum == 2:
         weekday = "Wednesday"
     elif dayNum == 3:
         weekday = "Thursday"
     elif dayNum == 4:
         weekday = "Friday"
     elif dayNum == 5:
         weekday = "Satuday"
     elif dayNum == 6:
         weekday = "Sunday"
     else:
         weekday = "" #another way to assign a default value to day
     #send the human-friendly day as output from the function
     return weekday

 def foo():
     today = date.today() #get today's date as a "date object"
     weekdayNum = date.weekday(today) #conver the "date object" to a number between 0-6
     friendlyDay = getFriendlyDayFromInt(weekdayNum) #convert that number to a human-friendly day
     print(friendlyDay) #print that day out

 #start up
 foo()
```

### Parse the day of the week a bit more

```python
 from datetime import *

 def isEarlyInTheWeek(num):
     if num < 2:
         return True
     return False #you don't need an else since this line is only ever executed when the if statement evaluates to false

 def isHumpday(num):
     if num == 2:
         return True
     return False

 def isWeekday(num):
     if num < 5:
         return True
     return False

 def isWeekendDay(num):
     if num >= 5:
         return True
     return False

 d = date.today()
 n = date.weekday(d)

 if isWeekday(n):
     print("Today is a weekday!!!")
     if isEarlyInTheWeek(n):
         print("It's still early in the week... don't despair.")
     elif isHumpday(n):
         print("Halfway there...")
     else:
         print("The weekend is almost here!")
 elif isWeekendDay(n):
     print("Today is a weekend!!!")
```

## OS module

The os module gives you access to the operating system, including
browsing the computer\'s file system, including all files and folders.

### Examples of using the OS module

Import the OS module:

`import os`

Get the [current working
directory](basic-computer-concepts.md#Current_working_directory)
where the current code file is located:

`currentDirectory = os.getcwd()`

Get a list of names of files in the current working directory:

`listOfFiles = os.listdir(currentDirectory)`

Find out if a file exists already:

`fileExists = os.path.isfile("somefile.txt")`

Get the size of a particular file in bytes:

`size = os.stat("somefile.txt").st_size`

Get the last modified date of a particular file in bytes:

`date = os.stat("somefile.txt").st_mtime`

### Accessing the computer\'s file system

```python
 import os

 #get the current working directory (by default the folder where this program is saved)
 myCurrentDirectory = os.getcwd()

 #get a list of the files in the current working directory
 myListOfFiles = os.listdir(myCurrentDirectory)

 #print out that list of files in this folder
 print(myListOfFiles)

 #loop through each filename in the list
 for filename in myListOfFiles:
     #print out each filename
     print(filename)
```

## Turtle module

The turtle module is used to teach programming visually. Some teachers
like it.

- [official
  documentation](http://docs.python.org/3/library/turtle.html#module-turtle)

### turtle module example geometric drawing program

This program draws a simple geometric shape.

```python
 import turtle

 turtle.color('red', 'yellow')
 turtle.begin_fill()
 while True:
     turtle.forward(200)
     turtle.left(170)
     if abs(turtle.pos()) < 1:
         break
 turtle.end_fill()
 turtle.done()
```

### turtle module example spastic turtle program

This program makes the turtle jiggle around uncontrollably.

```python
 import turtle
 import random

 turtle.color('blue', 'green')
 turtle.begin_fill()
 turtle.speed(0)

 while True:
     #you should really check to make sure the turtle does not go out of bounds... not doing that here...

     #move forward by a random amount
     myNum = random.randint(1,10)
     turtle.forward(myNum)

     #turn a random angle
     myAngle = random.randint(0, 360)
     turtle.left(myAngle)

 turtle.end_fill()
 turtle.done()
```

## CSV module

Python\'s [csv module](https://docs.python.org/3.6/library/csv.html) is
useful for reading and writing text files where the data in the file is
written in comma-separated values (CSV) format. CSV is the most common
text file format for text data from spreadsheets or databases.

See [examples of using the csv module to parse CSV files into
Lists](Reading_and_parsing_CSV_files_in_Python#CSV_to_Lists)
and[Dictionaries](Reading_and_parsing_CSV_files_in_Python#CSV_to_Dictionaries).

## Regular Expressions module

Python, like most other high-level programming languages, provides
support for Regular Expressions. The [re module is documented
separately](Regular_expressions#Python_implementation).

## UrlLib.Request module

The urllib.request module allows your programs to include a custom-built
text-based web browser by fetching documents from the internet:

- [official
  documentation](http://docs.python.org/3/library/urllib.html#module-urllib)\]
- [how to fetch internet resources using
  urllib](http://docs.python.org/3.3/howto/urllib2.html)

### Simple example

This example program requests the text of a web page and prints it out
to the console.

```python
 #import the urllib request module
 import urllib.request

 #ask the python web server for the home page data
 f = urllib.request.urlopen('http://python.org/')

 #read the response that the web server has sent to us
 pageData = f.read()

 #print that data out
 print(pageData)
```

Once an HTML document has been retrieved from the web, it can be easily
parsed using HTML parser modules, such as [Beautiful
Soup](#Beautiful_Soup).

### Parser example

This example shows how to do a small amount of manual parsing of an HTML
document, looking for links. In most cases, programmers would use any of
a number of ready-made popular parsing modules that can do a wide
variety of parsing tasks, rather than write this code manually.

**Note:** I have not tested this example.

```python
 import urllib.request

 response = urllib.request.urlopen("http://python.org") #make a request to a web server, and store the response

 html = str(response.read()) #convert the response to a string


 startingPosition = 0
 numberOfLinks = 0
 searchTerm = "http://"

 while startingPosition >= 0:
     startingPosition = html.find(searchTerm, startingPosition + 1)
     numberOfLinks = numberOfLinks + 1

 print("Found", numberOfLinks, "links in this web page")
```

### Creating a web crawling spider

```python
 #example that crawls all NYU i6 accounts and counts how many times  a given word is mentioned

 import urllib.request

 #get a list of all the letters
 letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z" .split(" ")

 #get a list of all the numbers
 numbers = "0 1 2 3 4 5 6 7 8 9".split(" ")

 #generate all possible net ids, assuming net id is 2 letters  followed by 4 numbers
 net_ids = [] #a blank list that will hold all possible net ids

 #nested for loops!
 for l1 in letters:
     for l2 in letters:
         for n1 in numbers:
             for n2 in numbers:
                 for n3 in numbers:
                     for n4 in numbers:
                         net_id = l1 + l2 + n1 + n2 + n3 + n4
                         net_ids.append(net_id)

 #debugging
 print(net_ids)

 #count how many times the word "awesome" is used on i6 user  home pages
 page_counter = 0
 awesome_counter = 0

 #loop through all net ids and scrape their i6 pages
 for net_id in net_ids:

     #make an http request for the web page of this person
     f = urllib.request.urlopen("http://i6.cims.nyu.edu/~" +  net_id)

     #get the html code for this page
     html_code = f.read()

     #increment our page counter
     page_counter = page_counter + 1

     #you can now do any kind of analysis on these pages here
     if "awesome" in html_code:
         #increment the awesome counter
         awesome_counter = awesome_counter + 1

         #debugging
         print("Found an awesome on " + net_id + "'s page.")
```

## Beautiful Soup

The add-on module
[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
is very useful for parsing HTML code. Note that this is not included in
Python\'s standard modules, and so must be downloaded and installed in
order to be available.

### HTML parser

```python
 #import the module
 from bs4 import BeautifulSoup

 #let's say you have an HTML file you scraped off the web...
 html_doc = """
 <!doctype html>
 <html>
   <head>
     <title>Foo Bar</title>
     <script src="js/jquery-1.10.2.min.js"></script>
     <link rel="stylesheet" href="css/main.css" type="text/css"  />
   </head>
   <body>
     <div id="wrapper">
       <article>
         <h1>Redeye to go</h1>
         <p>Viennese beans, wings robust cream frappuccino  single shot.</p>
         <p>Et as, half and half dripper espresso chicory  filter pumpkin spice.</p>
       </article>
     </div>
   </body>
 </html>
 """


 #...and you want to make some sense of it
 soup = BeautifulSoup(html_doc)

 #... now you can do things like get the contents of HTML  tags...
 print("The title of the document is", soup.title.string)

 #... or find the contents of all paragraphs, for example ...
 for p in soup.find_all('p'):
     print(p.string)

 #... or get all the text without the HTML code...
 print(soup.get_text())

 #etc...  check out more: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
```
