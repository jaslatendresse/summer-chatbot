# Hello, World! 
In this section, you will learn the basics of Python such as creating a Python script, writing Python code, and executing Python code. 

I will be following the tutorial from [W3Schools](https://www.w3schools.com/python/), but I will only include what I think is relevant to this chatbot project!

<hr>

1. Create a "helloworld" project folder on your computer and open it in Visual Studio. 
2. Open a terminal window in 
3. In the folder, create a "helloworld.py" file
4. In your "helloworld.py" file, type `print('Hello, World!')` 
5. In the terminal window, execute your script with `python3 helloworld.py`

 <img width="618" alt="Capture d’écran, le 2022-07-21 à 11 11 29" src="https://user-images.githubusercontent.com/17911957/180249143-402fd346-5510-4efc-a6f5-332482b5c461.png">

## Python identation

In Python, **identation** is very important as it is used to indicate a block of code. You can use the "tab" key on your keyboard to create indentations in your Python scripts.

Try the following examples in your helloworld.py file. 

Example of correct code block:

```
if 2 > 1
    print('2 is greater than 1!')
```

Example of an incorrect code block (your interpreter will raise an error):

```
if 2 > 1
print('2 is greater than 1!')
```

## Python variables

You can create a variable and assign it a value:

```
x = 2
y = 'Hello, World!'
z = ['this', 'is', 'a', 'list', 'of', 'strings']
```

As you can see, you don't need to specify the type of value you assign to your variable (integer, string, array) in Python. The interpreter knows and will raise an error if you try to perform illegal operations on them (for example, `x + y` would not work because `x` is an integer and `y` is a string).

You can also assign a variable the result of an operation on 2 variables:

```
first_number = 1
second_number = 2
result = first_number + second_number

print(result)

>>> 3
```

## Python comments

Commenting your code is important since it allows to communicate what your code does with other collaborators. 

```
#This is a comment
print('Hello, World!')

print('Hello, World!') #This is also a comment

#This is 
#another comment
#with multiple lines
print('Hello, World!')

"""
You can also write multi-line comments
just like this!
"""
print('Hello, World!')
```

## Python data types

Data type is an important concept of programming because different data types can do different things. 
| Type           | Python type                  |
|----------------|------------------------------|
| Text type      | `str`                          |
| Numeric types  | `int`, `float`, `complex`          |
| Sequence types | `list`, `type`, `range`            |
| Mapping type   | `dict`                         |
| Set types      | `set`, `frozenset`               |
| Boolean type   | `bool`                         |
| Binary types   | `bytes`, `bytearray`, `memoryview` |
| None type      | `NoneType`                     |

You can see the data type of a variable by using the `type()` function: 

```
x = 2
print(type(x))

>>> int
```

## Python strings

Since we are working on a chatbot, we will be processing a lot of natural language. Thus, it is important to understand how strings work. 

In Python, strings are arrays of bytes representing unicode characters. A character in Python is simply a string with a length of 1. 

You can view a string as a list of characters with their own respective positions. The string position always starts at 0. 

Example: access the letter "e" in the following string

```
#Since the string position starts at 0, then the letter "e" is at position 1. 
x = 'Hello, World!'
print(x[1])

>>> 3
```

You can also access the length of a string using the `len()` function. This returns the total number of characters in a string:

```
x = 'Hello, World!'
print(len(x))

>>> 13
```

You can also concatenate strings to create another string:

```
x = 'Hello'
y = 'World'

print(x + ' ' + y)

>>> Hello World
```

## Python boolean

Programming is logic-based meaning you often need to check if an expression is `True` or `False`. Thus, a boolean is a binary value that is either `True` or `False`.

```
print(1 > 0)
>>> True

print(1 == 2)
>>> False

print(1 < 2)
>>> True
```

## Python if-else statements

Now that we have just seen booleans, we can use them in conditional statements. 

```
a = 2
b = 3

if a < b:
    print('b is greater than a')
else:
    print('b is not greather than a')
```

You can also verify multiple conditions with `elif` (else if):

```
a = 2
b = 3

if a < b:
    print('b is greater than a')
elif a == b:
    print('a is equal to b')
else:
    print('b is not greather than a')
```

You can see the use of if-else as a condition flow. We first start by evaluating the `if` statement. If the condition is met, the program stops. If the condition is not met, it moves on to the next statement (`elif` in the example above). Finally, the `else` statement is used to catch anything that isn't caught by the preceding conditions. 

## Python loops

**For loops**
`for` loops are used to iterate over a sequence (list, tuple, dictionary, set, or string). 

```
fruits = ['apple', 'banana', 'orange']
for x in fruits:
    print(x)

>>> apple
>>> banana
>>> orange
```

You can also loop through a string:
```
for x in 'apple'
    print(x)

>>> a
>>> p
>>> p 
>>> l
>>> e
```

You can use conditional statements within loops:

```
fruits = ['apple', 'banana', 'orange']
for x in fruits:
    if x == 'apple'
        print(x)
>>> apple
```

You can also `break` out of a `for` loop. This means that you can stop the loop before it has looped through all the times:

```
fruits = ['apple', 'banana', 'orange']
for x in fruits:
    print(x)
    if x == 'banana'
        break
>>> apple
```

The outcome of this code block will be different from the previous one: 

```
fruits = ['apple', 'banana', 'orange']
for x in fruits:
    if x == 'orange'
        break
    print(x)
>>> apple
>>> banana
```

You can use the `continue` statement to stop the current iteration of the loop and move to the next one: 
```
fruits = ['apple', 'banana', 'orange']
for x in fruits:
    if x == 'banana'
        continue
    print(x)
>>> apple
>>> orange
```

## Python functions

A function is a block of code that will execute only when it is called. You can create a function using the `def` keyword.

```
def my_function():
    print('Hello, World! This is from my function.')

my_function()
>>> Hello, World! This is from my function.
```

You can also pass arguments to your function.

```
def my_function(my_argument):
    print(my_argument)

my_function('Hello')
>>> Hello
    
```

You can have your function return a result:

```
def add(a, b):
    return a + b

add(1, 1)
>>> 2
```

## Using external libraries in Python

Coding is fun, but it can sometimes be tedious. This is why there exist libraries that provide functionalities for you to use in your code. 

To use an external library, you first need to install it with the `pip` command. Then, you can safely import it in your code and use its functionalities. 

Let's see an example with `pandas`, a useful library to analyze data. 

`pip3 install pandas` 

```
#You can give a custom name to the library to make it easier to use in your code. In our case, we will use pd instead of pandas.
import pandas as pd

#Next, we will use pandas to read a csv file into a dataframe, a special data structure provided by pandas. 
pd_reader = pd.read_csv('my_file.csv')
```





