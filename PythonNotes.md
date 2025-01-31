# Python
## Variables
### Creating variables
```python
my_height = 174
my_name = "Aditya"
```
### Storing Results
```python
summation = a + b  # Addition
difference = a - b # Subtraction
product = a * b    # Multiplication
quotient = a / b   # Division
```
### Negative Numbers
```python
my_negative_num = -1
```
## Comments
```python
# Single Line comment
"""
Multi-line comment
Aka Docstrings (https://peps.python.org/pep-0257/)
"""
```
## Variable Names
Variable names can _not_ have spaces, they're continuous strings of characters.

The creator of the Python language himself, [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum), [implores us](https://peps.python.org/pep-0008/#function-and-variable-names) to use `snake_case` for variable names. What _is_ snake case? It's just a style for writing variable names. See [[Different Casing Styles]]

## Basic Variable Types
```python
# Strings --> List of characters strung together
name_with_single_quotes = 'boot.dev' # not so good
name_with_double_quotes = "boot.dev" # so good       [prefered method]

# Numbers
##Integer
x = 5 # positive integer
y = -5 # negative integer
##Float
x = 5.2
y = -5.2

# Booleans
is_tall = True
is_short = False
```
## F-Strings
Create strings that contain dynamic values.
```python
num_bananas = 10
f_string = f"You have {num_bananas} bananas"
print(f_string)
# You have 10 bananas
```
## NoneType
`None` is a special value in Python that represents the absence of a value. It is _not_ the same as zero, False, or an empty string.
## Dynamic Typing
Python is [dynamically typed](https://en.wikipedia.org/wiki/Type_system#Static_and_dynamic_type_checking_in_practice), which means a variable can store any type, and that type can _change_.
```python
speed = 5
speed = "five"
```
In almost all circumstances, it's a _bad idea_ to change the type of a variable. The "proper" thing to do is to just create a new one. For example:
```python
speed = 5
speed_description = "five"
```
## Math with Strings
When working with strings the `+` operator performs a "[concatenation](https://en.wikipedia.org/wiki/Concatenation)", which is a fancy word that means "joining two strings". _Generally speaking, it's better to use string interpolation with `f-strings` over `+` concatenation_.
```python
first_name = "Adi "
last_name = "Dahake"
full_name = first_name + last_name
print(full_name)
# prints "Adi Dahake"
```
## Multi-variable Declaration
We can save space when creating many new variables by declaring them on the same line:
```python
sword_name, sword_damage, sword_length = "Excalibur", 10, 200
# same as
sword_name = "Excalibur"
sword_damage = 10
sword_length = 200
```
Any number of variables can be declared on the same line, and variables declared on the same line _should_ be related to one another in some way so that the code remains easy to understand.
We call code that's easy to understand "clean code".

## Functions
Functions allow us to reuse and organize code.
```python
# Function Definition
def area_of_circle(r):
	pi = 3.14
	result = pi * r * r
	return result

# Function Call
radius = 3
area = area_of_circle(radius) # 28.26
```
Above is a function that calculates area of a circle.
### **Multiple Parameters**
Functions can have multiple parameters ("parameter" being a fancy word for "input"). Here, `r` is a parameter.
The name of a parameter doesn't matter when it comes to which values will be assigned to which parameter. It's **position** that matters. The first parameter will become the first value that's passed in, the second parameter is the second value that's passed in, and so on.
### **Printing vs Returning**
- `print()` is a function that:
    1. Prints a value to the console
    2. Does _not_ return a value
- `return` is a keyword that:
    1. Ends the current function's execution
    2. Provides a value (or values) back to the caller of the function
    3. Does _not_ print anything to the console (unless the return value is later `print()`ed)
### **Where to Declare Functions**
Code executes in _order from top to bottom_, so a variable needs to be created before it can be used. That means that if you define a function, you can't call that function until _after_ the definition.
### **Parameters vs. Arguments**
Parameters are the names used for inputs when _defining_ a function. Arguments are the values of the inputs supplied when a function is _called_.
To reiterate, **arguments are the actual values** that go into the function, such as `42.0`, `"the dark knight"`, or `True`. **Parameters are the names** we use in the function definition to refer to those values, which at the time of writing the function, can be whatever we like.
That said, this is all semantics, and frankly developers are really lazy with these definitions. You'll often hear the words "arguments" and "parameters" used interchangeably.
### **Scope**
Scope refers to _where_ a variable or function name is available to be used. For example, when we create variables in a function (such as by giving names to our parameters), that data is _not_ available outside of that function.
```python
def subtract(x, y):
    return x - y
result = subtract(5, 3)
print(x)
# ERROR! "name 'x' is not defined"
```
#### **Global Scope**
So far we've been working in the global scope. That means that when we define a variable or a function, that name is accessible in _every other place_ in our program, even within other functions.
```python
pi = 3.14

def get_area_of_circle(radius):
    return pi * radius * **radius**
```
Because `pi` was declared in the parent "global" scope, it is usable within the `get_area_of_circle()` function.

## Computing
### Python Numbers
- **Int** - `6`
- **Float** - `6.9`

### Operations
- Addition: 2 + 2 => 3
- Subtraction: 2 - 2 => 0
- Multiplication: 2 * 2 => 4
- Division: 2 / 2 => 1 `int`
- 3 / 2 => 1.5 `float`

### Floor Division
- 2 // 2 => 1 `int`
- 3 // 2 => ~~1.5~~ 1 `int` | Floored / rounded down 

### Exponents
-> 2 ** 3 => 8 | same as 2^3

### In-place operator
ex. variable += 1
`+=`, `-=`, `*=`, `/=`

### Scientific Notation
You can add the letter `e` or `E` followed by a positive or negative integer to specify that you're using [scientific notation](https://en.wikipedia.org/wiki/Scientific_notation).
```python
print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071
```
### Readability of numbers
Python allows you to represent large numbers in the decimal format using underscores as the [delimiter](https://en.wikipedia.org/wiki/Decimal_separator#Digit_grouping) instead of commas to make it easier to read.
```python
num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000
```
### Logical Operators
```python
True and True == True
True and False == False
False and False == False

True or True == True
True or False == True
False or False == False

print(not True)
# Prints: False

print(not False)
# Prints: True
```
## Binary Numbers
[Binary numbers](https://en.wikipedia.org/wiki/Binary_number) are just "base 2" numbers. They work the same way as "normal" base 10 numbers, but with two symbols instead of ten.

- Base-2 (binary) symbols: `0` and `1`
- Base-10 (decimal) symbols: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`
![[Pasted image 20250129185226.png|900]]
Each `1` in a binary number represents an ever-greater multiple of 2. In a 4-digit number, that means you have the eights place, the fours place, the twos place, and the ones place. Similar to how in decimal you would have the thousands place, the hundreds place, the tens place, and the ones place.
### In Python
```python
print(0b0001)
# Prints 1

print(0b0101)
# Prints 5
```
## Bitwise Operators
- **AND** -> `&`
	- "*Binary "and" will always reduce the total number of ones in a binary number*"
	- It is also called **Masking** or **Filtering**.
	- Ampersand `&` is the bitwise "and" operator in Python. "And" is the _name_ of the bitwise operation, while ampersand `&` is the _symbol_ for that operation.
	- For example, `5 & 7 = 5`, while `5 & 2 = 0`.
```
0101    # 5
&
0010    # 2
=
0000    # 0
```
- OR -> `|`
	- "*Binary "or" will always have 1 in place where either of the input numbers has a 1*"
	- When two binary numbers are "or"ed together, the result has a `1` in any place where _either_ of the input numbers has a `1` in that place.
	- `|` is the bitwise "or" operator in Python.
	- Example: `5 | 7 = 7` and `5 | 2 = 7` as well!
```
0101    # 5
|
0010    # 2
=
0111    # 7
```

## Comparisons
When coding it's necessary to be able to compare two values. `Boolean logic` is the name for these kinds of comparison operations that always result in `True` or `False`.

The operators:
- `<` "less than"
- `>` "greater than"
- `<=` "less than or equal to"
- `>=` "greater than or equal to"
- `==` "equal to"
- `!=` "not equal to"
For example:
```python
5 < 6 # evaluates to True
5 > 6 # evaluates to False
5 >= 6 # evaluates to False
5 <= 6 # evaluates to True
5 == 6 # evaluates to False
5 != 6 # evaluates to True
```

## If-else
It's often useful to only execute code if a certain condition is met:
```python
if CONDITION:
	# do some stuff here
elif SOME_OTHER_CONDITION:
	# do some stuff here
elif YET_SOME_OTHER_CONDITION:
	# do some stuff here
else:
	# do some stuff here

# code after the if-else block may still run regardless
```
Here are some basic rules with if/else blocks.

- You can't have an `elif` or an `else` without an `if`
- You _**can**_ have an `else` without an `elif`
## Loops
A _"for loop"_ in Python is written like this:
```python
for i in range(0, 10):
    print(i)
```
`i` replaces the numbers `0` to `9`. In English, the code says:
1. Start with `i` equals `0`. (`i in range(0)`)
2. If `i` is not less than 10 (`range(0, 10)`), exit the loop. Else:
    - Print `i` to the console. (`print(i)`)
    - Add `1` to `i`. (`range` defaults to incrementing by 1)
    - Go back to step `2`.
The result is that the numbers `0-9` are logged to the console in order.

Python has another type of loop, the `while` loop. It's a loop that continues `while` a condition remains `True`. The syntax is simple:
```python
num = 0
while num < 3:
    num += 1
    print(num)

# prints:
# 1
# 2
# 3
# (the loop stops when num >= 3)

## INFINITE LOOP
while 1:
    print("1 evaluates to True")

# prints:
# 1 evaluates to True
# 1 evaluates to True
# (...continuing)
```
### **Range function**
- `range(start, end, step*)`
- `[start, end)`
- `step` -> optional

--
## Lists
A natural way to organize and store data is in a `List`. Some languages call them "arrays", but in Python they are just called lists.
```python
inventory = ["Iron Breastplate", "Healing Potion", "Leather Scraps"]
```
### Indexes
In the world of programming, we don't start counting at `1`, we start at `0` instead.
Each item in a list has an index that refers to its spot in the list.
Ex, `names = ['Alice', 'Bob', 'Carl', 'Dan']`
Index 0 -> `Alice`
Index 1 -> `Bob`
Index 2 -> `Carl`
Index 3 -> `Dan`
### Getting length of lists
`len()`
### Updating Items in a list
```python
inventory = ["Leather", "Iron Ore", "Healing Potion"]
inventory[0] = "Leather Armor"
#         ^ index of the item
# inventory: ['Leather Armor', 'Iron Ore', 'Healing Potion']
```
### Useful list methods
**`.append(<value>)`**
-> add items to the end of the list.
**`.pop()`**
-> removes one item from the end of the list and returns it.
-> `.pop(<index>)` => removes and returns item at the given index
### For-loops on a list
- `for i in range(0, len(<list>))`
- `for item in <list>`
- `for i, item in enumerate(<list>)`
### Slicing Lists
Python makes it easy to slice and dice lists to work only with the section you care about. One way to do this is to use the simple slicing operator, which is just a colon `:`.
Syntax: `my_list[ start : stop : step ]`
**Omitting Sections:** You can also omit various sections ("start", "stop", or "step"). For example, `numbers[:3]` means "get all items from the start up to (but not including) index 3". `numbers[3:]` means "get all items from index 3 to the end".
**Negative Indices:** Negative indices count from the end of the list. For example, `numbers[-1]` gives the last item in the list, `numbers[-2]` gives the second last item, and so on.
### List Operations
- Concatenate => `[] + []` -> returns new list with both the lists' item in that order
- Contains => `in` keyword is used to check if a value exists in a list or not.
- Deletion => `del` keyword can be used to delete specific indexes or entire slices from a list.
### **Tuples**
[Tuples](https://docs.python.org/3/library/stdtypes.html#typesseq-tuple) are collections of data that are ordered and unchangeable. You can think of a tuple as a `List` with a fixed size. Tuples are created with round brackets:
```python
my_tuple = ("this is a tuple", 45, True)
print(my_tuple[0])
# this is a tuple
print(my_tuple[1])
# 45
print(my_tuple[2])
# True
```
While it's typically considered bad practice to store items of different types in a List, it's not a problem with Tuples. Because they have a fixed size, it's easy to keep track of which indexes store which types of data.
Tuples are often used to store very small groups (like 2 or 3 items) of data. For example, you might use a tuple to store a dog's name and age.
```python
dog = ("Fido", 4)
```
_Note: There is a special case for creating single-item tuples. You must include a comma so Python knows it's a tuple and not regular parentheses._
```python
dog = ("Fido",)
```
**Tuple Unpacking:** You can easily assign the values of a tuple to variables using unpacking.
```python
dog = ("Fido", 4)
dog_name, dog_age = dog
print(dog_name)
# Fido
print(dog_age)
# 4
```
When you return multiple values from a function, you're actually returning a tuple.

## Dictionaries
[Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) in Python are used to store data values in `key` -> `value` pairs. Dictionaries are a great way to store groups of information.
```python
# use curly braces
# add key-value pairs
car = {
  "brand": "Tesla",
  "model": "3",
  "year": 2019
}

# Accessing elements
print(car["make"]) # tesla
```
If you try to use the same key twice, the first value will simply be overwritten.
### Setting, Updating and Deleting dictionary values
There is no need to create a dictionary with values already inside. It is common to create a blank dictionary then populate it later using dynamic values. The syntax is the same as getting data out of a key, just use the assignment operator (`=`) to give that key a value.
If the key is already present in the dictionary, setting it will just update the value of the key.
The `del` keyword is used to delete existing keys.
```python
planets = {
	"Pluto": True
}
# Setting
planets["Earth"] = True
print(planets["Earth"]) # True

planets["Pluto"] = False
print(planets["Pluto"]) # False

del planets["Pluto"]
print(planets) #{'Earth': True}

del planets["Pluto"] # ERROR: key dosen't exist
```
The `in` keyword can be used to see if a key exists in a dictionary. It will return a boolean.
### Iterating over a dictionary
We can iterate over a dictionary's keys using the same no-index syntax we used to iterate over the values in a list. With access to the dictionary's keys, we also have access to their corresponding values.

## Sets
[Sets](https://docs.python.org/3/tutorial/datastructures.html#sets) are _like_ Lists, but they are _unordered_ and they guarantee _uniqueness_. Only _ONE_ of each value can be in a set.
- Adding values -> use `.add(<value>)` method. *No error will be raised if item already in set* 
- Empty Set -> Because the empty bracket `{}` syntax creates an empty dictionary, to create an _empty_ set, you need to use the `set()` function.
- When iterating over a set, *The order is not guaranteed*.
- Removing values -> use `.remove(<item>)`method to remove values.
```python
fruits = {"apple", "banana", "grape"}
print(type(fruits)) # <class 'set'>
print(fruits)  # {'banana', 'grape', 'apple'}

fruits = {"apple", "banana", "grape"}
for fruit in fruits:
    print(fruit)
    # Prints:
    # banana
    # grape
    # apple

planets = set()
planets.add("Earth")
print(planets) # {'Earth'}
```

## Errors
#### **Syntax Errors**
You probably know what these are by now. A syntax error is just the Python interpreter telling you that your code isn't adhering to proper Python syntax.
#### **Exceptions**
Even if your code has the right syntax, however, it may still cause an error when an attempt is made to execute it. Errors detected during execution are called "exceptions" and can be handled gracefully by your code. You can even raise your own exceptions when bad things happen in your code.
Python uses a [try-except](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) pattern for handling errors.
```python
try:
  10 / 0
except Exception:
  print("can't divide by zero")

# If we want to access the data from the exception, we use the following syntax:
try:
	#something
except Exception as e:
	print(e)
```
Wrapping potential errors in `try/except` blocks allows the program to handle the exception gracefully without crashing.
#### Raising our own Exceptions
When something in our own code happens that isn't the "happy path", we should raise our own exceptions. For example, if someone passes some bad inputs to a function we write, we should not be afraid to raise an exception to let them know they did something wrong.
An _error_ or _exception_ is raised when something bad happens, but as long as our code handles it as users expect it to, it's _not_ a bug. A bug is when code behaves in ways our users don't expect it to.
An exception can be raised as follows:
```python
raise Exception("<error/exception message>")
```

*Note:* As a rule of thumb, you do not want to catch exceptions you raise within the same function block. Instead, the caller should handle any potential error by wrapping the function call within a try/except block.
### **Types of Exceptions**
There are different types of exceptions, and we can handle them differently depending on the situation. Some exceptions are more specific, like `ZeroDivisionError` or `IndexError`, and some are more general, like the base `Exception`.
```python
try:
    10/0
except ZeroDivisionError:
    print("0 division")
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")
except Exception as e:
    print(e)
```
If you're interested in the official documentation on all the built-in exceptions you can find a [list here](https://docs.python.org/3/library/exceptions.html).
