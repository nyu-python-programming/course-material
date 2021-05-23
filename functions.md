# Functions

Whereas [variables](Variables_and_literals) store a piece of
data in memory,
[functions](<http://en.wikipedia.org/wiki/Function_(computer_science)>)
store a series of commands in memory to be run at a later time. Think of
a function as a block of code that performs a specific task.

## Defining a function

For example, let's say we have a function that does one thing -- outputs
a message with the word, "hello."

### in Python

`def sayHello() :`\
` print(``<font color="#008000">``)`

### in Javascript

`function sayHello() {`\
` document.write(``<font color="#008000">``);`\
`}`

### in PHP

`function sayHello() {`\
` print(``<font color="#008000">``);`\
`}`

### in Java

Java methods (a.k.a. functions) include indications of the method\'s
visibility (e.g. public, private, or protected), whether the method
belongs to an instance or to the entire class (i.e. static), and the
return type of the method (e.g. void for no return value, or the keyword
such as int indicating the return type).

`public static void sayHello() {`\
` System.out.println(``<font color="#008000">``);`\
`}`

### Explanation

Let's take this function line-by-line. We\'ll refer to the Python
version, but the main ideas apply to any high-level programming
language:

`def sayHello() :`

This line of code declares that the following block of code will be a
function by using the keyword "def". Then it defines the name of the
function as "sayHello".

` print(``<font color="#008000">``)`

This line of code calls the Python interpreter's built-in "print"
function, which will automagically output a message with the word
"hello" in it when it is run.

Notice how the print command is indented in a few spaces in from the def
command. This tells the interpreter, which is reading this code, that
the print command is "inside" of the function. If it wasn't indented
properly, the interpreter would not know which commands to store as part
of the function.

## Calling the function

It's all well and good to define a function, as we have done above. But
the interpreter does not actually perform the actions defined in the
function. It simply stores them in memory for use later.

In order to actually run the commands stored in the function, we have to
"call" the function. This usually happens somewhere else in the code,
outside of the function block.

To call the function we defined above, we would use the following code:

### in Python

`sayHello()`

### in Javascript

`sayHello();`

### in PHP

`sayHello();`

### in Java

`sayHello();`

### Explanation

This would run all the statements in the function, which in this case
simply results in the word "hello" being output.

## Passing arguments to functions

Let's say we wanted to make the message that is output more
customizable. For example, we want the message to have someone's name in
it, such as "hello, Martha" or "hello, Juan", or "hello, Fausta."

We want to be able to use this same function to say hello to all these
people. How do we do it?

We could just write a separate function for each person, like this
(Python code is displayed for example, although the same concepts apply
to all high-level programming languages):

`def sayHelloToMartha() :`\
` print(``<font color="#008000">``)`\
\
`def sayHelloToJuan() :`\
` print(``<font color="#008000">``)`\
\
`def sayHelloToFausta() :`\
` print(``<font color="#008000">``)`

and whenever we want to output a message for Martha we call her function
in our code:

`sayHelloToMartha()`

and when we want to pop up a message for Juan, we call his function:

`sayHelloToJuan()`

...and so on.

However, this can become very inefficient if there are lots of
variations on the same basic function. That's a lot of redundant code.
There is an easier way, using function parameters.

We can design a version of our original function that takes one
"parameter" or input. When we call the function, we tell the function
the name of the person to whom to say hello, and it outputs a message
customized to that person.

Here is what our function will look like:

### in Python

` def sayHello(``<font color="#993300"> ``) :`\
` print(``<font color="#008000">``)`

### in Javascript

` function sayHello(``<font color="#993300"> ``) {`\
` document.write(``<font color="#008000">``);`\
`}`

### in PHP

` function sayHello(``<font color="#993300"> ``) {`\
` print(``<font color="#008000">``);`\
`}`

### in Java

` public static void sayHello(``<font color="#993300"> ``) {`\
` System.out.println(``<font color="#008000">``);`\
`}`

### Explanation

This single function can say hello to just about anybody we tell it to.
Let's take the Python version of this function line by line in order to
understand:

` def sayHello(``<font color="#993300"> ``) :`

This first line, known as the function signature, declares that we are
defining a function named "sayHello" and that it accepts one parameter,
which we call "person".

**Note:** Anytime you see words in between the parentheses of a function
definition, they indicate parameters that the function accepts as input
when it is called.

` print(``<font color="#008000">``)`

Here we are again using the interpreter's built-in "print" function in
order to output a message. However, the message we are outputting is no
longer just a simple "hello". The message we are outputting (i.e. the
stuff between the parentheses of the print function call) is now:

`<font color="#008000">`

This takes the word "hello," and glues it to the name we will use as a
parameter when we called the function. The word "hello", in this case,
is a string literal, which we saw in the discussion on variables. You
can tell this because it is text surrounded by quotes. The term "person"
is a variable name, which you can tell because it is text not surrounded
by quotes in the code.

So the word "hello" is concatenated with, or glued onto, whatever word
is stored in the parameter variable named "person".

If we call the function and pass it the word "Martha" as a parameter,
the function takes the word, "Martha", stores it in a variable named
"person", and concatenates this variable with the word "hello". Then it
outputs the combined message, which contains the words, "hello, Martha".

Calling the function with the word "Martha" as a parameter looks like
this:

` sayHello(``<font color="#008000"> ``)`

If we pass it the word "Simon", it will say "hello, Simon":

` sayHello(``<font color="#008000"> ``)`

If we pass it the word, "Susan", it will pop up "hello, Susan":

` sayHello(``<font color="#008000"> ``)`

...and so on.

## More about parameters and variable scope

Functions are not limited to just accepting one parameter as input.
Functions can take as many parameters as you want them to when you
design them. Some examples in Python (the same concepts apply to all
high-level programming languages):

` def doSomething(``<font color="#800000"> ``) :`

In any function definition, the stuff between the parentheses is a
comma-delimited list of parameters. Parameters are values that the
function will accept when it is called. They are variables that
automatically hold the values that were passed to the function when it
was called.

When we call a function, we supply it with a list of arguments. These
can be either variables or literals. In the following example function
call we're using two literals, but these arguments could just as easily
be variables: the two are interchangeable as far as the code is
concerned, and it really depends on what you're trying to achieve which
one you use.

` doSomething(``<font color="#008000"> ``)`

When we call the function this way, the argument "hello" is stored in
the function's first parameter variable, "parameter1″. The second
argument, 100, is stored in the function's second parameter variable,
"parameter2″.

Within the function block (any code indented directly beneath the
function signature) , the variable "parameter1″ holds the value "hello",
and "parameter2″ holds the value 100. These parameter variables only
exist within that function, and are said to have a local
[scope](<http://en.wikipedia.org/wiki/Scope_(programming)>) to that
function. Referring to the variable named "parameter1″ outside of the
function is meaningless.

So the term "arguments" refers to values that are supplied to a function
when that function is called somewhere in your code. Parameters are the
flip-side of arguments -- the term "parameters" refers to the values
that the function accepts and stores in variables when it is called.
Whatever you supply as arguments to a function are then stored
temporarily in that function's parameters.

## Return values

Some functions have return values. This means that when the function is
called, it takes some kind of input, performs a specific function on
that input, and then returns the results of that process to the code
that called it.

This is probably best illustrated with an example:

### in Python

`def addOne(someNumber) :`\
` newNumber = someNumber + 1`\
` return newNumber`

### in Javascript

`function addOne(someNumber) {`\
` newNumber = someNumber + 1;`\
` return newNumber;`\
`}`

### in PHP

`function addOne($someNumber) {`\
` $newNumber = $someNumber + 1;`\
` return $newNumber;`\
`}`

### in Java

`public static int addOne(int someNumber) {`\
` int newNumber = someNumber + 1;`\
` return newNumber;`\
`}`

### Explanation

This function defines a block of code that takes some number and adds
one to it. Then it returns the new number.

So if we call this number, and give it the number 10 as an argument, we
will get the number 11 back. This is how we'd call the function and
supply it with the argument, 10. The following code is in Python,
although the same concepts apply to all high-level programming
languages.

`addOne(10)`

But in order to see that this works, we would have to do something we
the number we get back, like, for example, popping it up in an alert
message. So let's first store the returned value in a variable, and then
output the contents of that variable.

`result = addOne(10)`\
`print(result)`

So we can see that the return value of the function was 11. If we
supplied the function with the parameter 3, the return value would be 4,
and so on.

## Function names

Like variable names, function names must not have any spaces or special
characters in them, although they can use the underscore ("\_")
character. They also often use [lower camel case or upper camel case
conventions](Variables,_literals,_and_expressions#Common_variable_naming_conventions).
