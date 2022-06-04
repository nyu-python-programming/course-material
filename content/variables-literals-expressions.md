---
layout: github
title: Variables, Literals, and Expressions
permalink: /variables-literals-expressions
redirect_from: /variables-literals-expressions.md
---

# Variables, literals, & expressions

In all [high-level programming
languages](http://en.wikipedia.org/wiki/High-level_programming_language),
we have access to some of the computer\'s memory. At any point in our
code, we can store things in memory that we want to use later on. It may
not be clear at the moment why we would want to use memory, but it will
come into play in everything we do as programmers.

The same principles we will go over here will apply to just about any
high-level programming language you will learn in the future. So
although these examples may seem abstract at first, it is imperative
that you follow the concepts and understand how they are being used.

## Variables are symbols that represent data

The simplest way of storing data is with what is termed a
[variable](http://en.wikipedia.org/wiki/Variable). If you remember basic
algebra, you may recall that you encountered formulas where some of the
values were replaced with variables. In algebra, a variable is a symbol
that represents a number.

For example, imagine a variable named x that is defined to represent the
number 3.

`x = 3`

The way these variable assignment statements work, the value on the
right side of the equals sign is placed in the memory represented by the
variable on the left side of the equals sign. So the number 3 is stored
in a spot of memory labeled \'x\'.

Now say we take a simple formula for a straight line that looks
something like this:

`y = x + 1`

If you imagine that x is replaced with the number 3, as we defined it
above, then your formula would become:

`y = 3 + 1`

and since hopefully you remember that 3 + 1 = 4, then that formula is
equivalent to saying:

`y = 4`

In this example, the letter \'x\' is a variable. It is a placeholder
for, or a reference to, some data stored in memory. In this example, you
\'remember\' that x has the value 3, so everywhere you see the letter
\'x\', you know that internally, in the guts of the computer, it is
being replaced by the number 3. But you could just as easily use the
same formula for other values of x. For example, if x=5, then following
the formula, y=5+1, which means y=6.

## Variables in programming languages come in a variety of data types

In most programming languages, unlike algebra, not all variables hold
numbers. Some can hold text or more complicated [types of
data](Data_types). For example, to hold some text in a
variable, we can do something like this:

`my_name = "Inego Montoya"`

And now, imagine we had a formula that assembles a sentence:

`introduction = "Hello, my name is " + my_name + "."`

You remember that \"name\" is a variable that refers to the name,
\"Inego Montoya\". So you can see that:

`introduction = "Hello, my name is " + "Inego Montoya" + "."`

which, if you use the plus sign to
[concatenate](./string-basics.md#concatenating-strings) the two
bits of text, means that:

`introduction = "Hello, my name is Inego Montoya."`

So here we have examples that deal with variables that refer to textual
data, not numbers. In programming parlance, variables, like this, that
hold text are called \"[strings](string-basics)\", as in a string
of characters.

## Defining variables

In each of the languages below, we show how to perform the following
tasks:

1.  [declare](<http://en.wikipedia.org/wiki/Declaration_(computer_science)>)
    (assigned a name to) a variable \'x\'
2.  assign that variable \'x\' the value 3, which tells the computer to
    store the integer 3 in the piece of memory we have symbolically
    referred to as \'x\'.

We also:

1.  declare the variable \'y\'
2.  assign it the value of x+1, which in this case tells the computer to
    first evaluate the expression x+1, realize that it is equal to 4
    (since x=3), and then store the number 4 in the piece of memory
    named \'y\'.

### In Python

In Python, you can define variables as follows:

`x = 3`\
`y = x + 1`

### In Javascript

`var x = 3;`\
`var y = x + 1;`

### In Java

`int x = 3;`\
`int y = x + 1;`

### In C

`int x = 3;`\
`int y = x + 1;`

### In PHP

`$x = 3;`\
`$y = $x + 1;`

\... you get the idea

## Common variable naming conventions

Most of popular programming languages do not allow the usage of spaces
or special characters inside identifiers, including variables and
function names. So, there are common ways that programmers create
variable or function names without spaces:

### Upper Camel Case

Examples:

- `LuckyNumberFromUser`
- `TheSecretToWealthAndHappiness`

### Lower Camel Case

Examples:

- `luckyNumberFromUser`
- `theSecretToWealthAndHappiness`

### Underscore

Examples:

- `lucky_number_from_user`
- `the_secret_to_wealth_and_happiness`

## Variables vs. Literals

There are ways to write values of the primitive data types directly.
These values are referred to as literals if written in this way.

### Integer literals

Numbers written in code are always literals:

In the following example, the number 4 is written literally using the
symbol 4:

`lucky_number = `**`4`**

In the following example, the number 666 is written by literally writing
the symbols 666:

`print(lucky_number + `**`666`**`)`

### Integer variables

Variables are keywords that can refer to numbers:

This example defines a variable named `lucky_number` that is set to refer
to the integer 4

`lucky_number = 4`\

This example refers to the integer 4 value by writing lucky_number

`print(`**`lucky_number`**` + 666)`

This example defines a variable named x that refers to the integer 100:

`x = 100`

This example refers to the integer 100 value by writing x

`one_hundred_and_one = `**`x`**` + 1`

### Float literals

Numbers in code are always literals:

`#refer to the floating point number 12.2 directly by literally writing it`\
`12.2`

`#refer to the floating point number 3.14 by literally writing it`\
`3.14`

### Float variables

Variables are keywords that can refer to numbers:

`#define a variable named x that refers to the floating point number 12.2`\
`x = 12.2`\
\
`#refer to the floating point number 12.2 value by writing x`\
`print(x)`

`#define a variable named y that refers to the floating point number 3.14`\
`y = 3.14`\
\
`#refer to the floating point number 3.14 value by writing y`\
`print(x)`

### String literals

Text in quotes is always a literal:

`#refer to the string "money" by literally writing it`\
`"money"`

`#refer to the string 'a haircut' by literally writing it`\
`'a haircut'`

### String variables

Variables are keywords that can refer to strings:

`#define a variable named x that refers to the string "money"`\
`x = "money"`\
\
`#refer to the string "money" value by writing x`\
`print(x)`

`#define a variable named y that refers to the string "a haircut"`\
`y = 'a haircut'`\
\
`#refer to the string 'a haircut' value by writing y`\
`print(x)`

### Boolean literals

The words True and False are the only Boolean literals:

`#refer to the boolean True value by literally writing it`\
`True`

`#refer to the boolean False value by literally writing it`\
`False`

### Boolean variables

Variables are keywords that can refer to boolean values:

`#define a variable named x that refers to the boolean True value`\
`x = True`\
\
`#refer to the boolean True value by writing x`\
`print(x)`

`#define a variable named y that refers to the boolean False value`\
`y = False`\
\
`#refer to the boolean False value by writing y`\
`print(y)`

### More explanation

In the following line of code, 1 is an integer literal, while x and y
are both variables:

`y = x + 1`

There are two variables in this line: \'x\' and \'y\'. There is also the
number 1. Whenever we use a raw value, rather than a variable, it is
known as a
\'[literal](<http://en.wikipedia.org/wiki/Literal_(computer_science)>)\'.
So 1, in this case, is a literal. It refers to exactly (literally) what
it looks like, not to some other value stored in memory. The same
concept applies to variables that hold other types of data, such as
strings:

`my_name = "Inego Montoya"`\
`y = "Hello, my name is " + my_name + "."`

In the second line of code in this example, \'Hello\' is a literal,
whereas \'my_name\' is a variable. In Python, literals that are numbers
do not need quotes around them. But all literals that are strings must
be surrounded by quotes. It doesn\'t matter whether you use single or
double quotes, so long as you start with the same kind of quote that you
end with.

## Expression

An expression is any code that evaluates to a single value.

An expression could be as simple as a literal, which is literally a
single value:

`5`

An expression can be as simple as a variable, which may be a reference
to a single value:

`x`

An expression can involve an operator performing an operation that
results in one value:

`5 + x`

An expression may involve a call to a [function](functions)
that returns a single value:

`do_something()`

Or any combination of the above:

`do_something() + 5 / x`

## Dynamic variable typing

Unlike most traditional programming languages, variables in some
languages, including Python, Javascript, and PHP are
\'dynamically-typed\'. This means you do not have to explicitly state
what type of data the variable will hold when you define it. For
example, a variable that previously held an integer can be later used to
hold a string:

### Python example

`#hold an integer value in a variable`\
`i = 100 `\
\
`#reassign the same variable to hold a different data type (in this case a string value)`\
`i = "this is not a number anymore!"`

In many other statically-typed languages, this would produce an error.
But in these dynamically-typed languages, it\'s fine. This is often
confusing to people who have previous experience programming more
\'strict\' languages like C, C++, or Java. See the note on static typing
below to understand what these programmers are used to.

## Static variable typing

In statically-typed programming languages, like Java, C, or C++,
variables are stuck as the original data type they were initially
defined as.

### Java example

`#hold an integer value in a variable`\
`int i = 100;`

`#you cannot reassign the same variable to hold a value of a different data type (in this case a string value)`\
`i = "this will cause an error!";`
