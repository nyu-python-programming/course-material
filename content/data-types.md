---
layout: github
title: Data Types
permalink: /data-types
redirect_from: /data-types.md
---

# Data types

## The simplest primitive data types

Every high-level computer programming language has a built-in
understanding of a few different types of data. The differentiation in
how a computer \"understands\" data is, of course, different from how
humans think about data. Some common data types are outlined below.

### Integers

Simple numbers with no decimal place.

Examples:

- `4`
- `666`
- `-2`

### Floating point numbers

Numbers with decimal points.

Examples:

- `12.2`
- `3.14159`
- `1.0`

### Strings

Regular text is usually represented by programming languages as a
\"string of characters\" or \"string\" for short.

Most programming languages require that quotation marks be placed around
string [literals](./variables-literals-expressions) to
differentiate them from other keywords in the language. Whether to use
double or single quotes for this is dependent on which language you are
using.

Examples:

- `"money"`
- `"4"` \#note that most languages will treat this as a string, not an
  int because of the quotes
- `"12.2"` \#note that most languages will treat this as a string, not
  a float because of the quotes

See more on [Strings](./string-basics)

### Booleans

Boolean values are those propositions which the programming languages
understands to be either true or false.

Examples of Boolean values in Python:

- `True`
- `False`

Examples of Boolean values in Java:

- `true`
- `false`

See more on [Boolean logic](./boolean-logic)

## Aggregate data structures

Some data structures allow you to group together a bunch of different
pieces of data into a single aggregate data structure. These are a bit
more "high-level".

### Lists and arrays

[Lists](./list-basics), also known as arrays, are groups of single values.

- e.g. `"money", "wealth", and "peanut butter"`

### Dictionaries, associative arrays, and hash maps

[Dictionaries](./dictionary-basics), associative arrays, and hash
tables, are all data structures that hold a group of key/value pairs.

- e.g. `"my_name": "Inego Montoya", "reason_here": "to kill your father"`

## Incompatibilities among data types

When trying to perform operations on values of multiple data types, it is not uncommon to find incompatibilities among the data types. Each high-level programming language has its own limitations on how different data types can be mixed and matched in operations.

### Python examples

Example of an error:

```python
x = "my favorite number " #a string
y = 4 #an int
z = x + y #an error! you cannot add a string to an int
```

Example of a potential solution

```python
x = "my favorite number " #a string
y = 4 #an int
z = x + str(y) #fine! the int was converted to a string before adding
```

## Converting among data types

Often it is useful to translate a value from one data type into another data type. Each high-level programming language has its own techniques for how to convert data of one type to data of another type.

### Python examples

Imagine you have a variable x

`x = "4"`

Python [built-in functions](./modules):

- `int(x)` -- converts a float or string to an integer
- `float(x)` -- converts an integer or string to a float
- `str(x)` -- converts an integer or float to a string
- `bool(x)` - converts various data types to a boolean equivalent
- `list(x)` - converts any data type to a list

#### Code examples

```python
#input
x = input("What's your lucky number today?")

#processing
y = int(x) * 10

#output
msg = "Your lucky number times ten is " + str(y)
print(msg)
```

## Introspection

If you\'re not sure what data type a given value is, find out. Each high-level programming language has its own techniques for introspection, or discovering information about the system and the data stored in the system.

### Python examples

- `type(x)` -- determines what type a given piece of data is
- `dir(__builtins__)` \#shows you a list of [Python's built-in functions](http://docs.python.org/py3k/library/functions.html)
- `print(input.__doc__)` \#shows you the input() function's (or any other function's) usage documentation
- `help(input)` \#shows you the Python help for the input() function (or
  any other function)

#### Code examples

```python
if type("a haircut") == str:
  print("Hoorah!")
```
