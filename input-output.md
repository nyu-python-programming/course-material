# Input & output

## Receiving input from the user

Many programs receive input from the person using the program. This \"user input\" can come from any input device that a user has access to, such as computer\'s keyboard, microphone, camera, oystick, trackpad, etc.

For simple programs, the input usually comes from the keyboard.

### Python examples

- the [input() function](http://docs.python.org/py3k/library/functions.html#input)

#### Code example

`wealth = input("How many `[` Dentalium`` ``shells `](https://wikipedia.org/Dentalium_shell)` do you have?")`

## Sending output to the user

Many programs send output to the person using the program. This output can be displayed by any output device that the user has access to, such as the computer\'s display or speakers. Output sent to the computer\'s display can usually either be displayed as plain text, or as graphics.

For simple programs, the output is usually plain text output to a console.

### Python examples

- the [print() function](http://docs.python.org/py3k/library/functions.html#print)

#### Code examples

`print("this that the other")` #outputs 'this that the other\n'

`print("this", "this", "the other" sep="-")` #outputs 'this-that-the other\n'

```python
print("this", end="-")
print("that", end="-")
print("the other")
#outputs 'this-that-the other\n'
```

`print("this", "that", "the other" sep="-", end="?")` #outputs 'this-that-the other?'
