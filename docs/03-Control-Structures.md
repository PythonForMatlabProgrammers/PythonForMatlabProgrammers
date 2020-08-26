<br>
<br>

# Python Control Structures

Python's core library provides a limited but versatile set of control
structures. Add-on packages provide many additional constructs, but the
following discussion will be limited to those of the core library.

### Flow Control

Python provides the usual flow control constructs, with some minor
syntax changes.

-   Here is an if-statement:

    ```python
    if x < 0:
        print('x is negative')
    elif x == 0:
        print('x is zero')
    else:
        print('x is positive')
    ```

-   Note again there's no end statement. Nor are there semicolons at the end of
    each line. Indentation is required, as it is how Python detects constructs.
    The Python style guide requests indents of four spaces, not a tab.

-   Python does not define a switch-case construct.

-   Python has only two looping constructs: the *while* construct, and the *for*
    construct. Here's a while-statement:

    ```python
    >>> x = 0
    >>> while x < 10:
    ...   print(x, end=', ')
    ...   x += 1
    ```

-   Here's a for-statement. Python will iterate over the items of any sequence,
    as discussed earlier.

    ```python
    >>> for x in 'abcd':
    ...   print(x)
    ```

    The above will print 'a', 'b', 'c', 'd' on separate lines. The same
    construct works with lists:

    ```python
    >>> names = ['Dave', 'John', 'Mark']
    >>> for x in names:
    ...   print(x)
    ```

    The above will print 'Dave', 'John', 'Mark' on separate lines.

-   The target list ('names' in the above example) is an *iterable* which serves
    up its elements one at a time. Note the similarities to MATLAB, which can
    iterate in a for-loop over a numeric array or a cell array.

-   Wondering how to use indices in a for-loop? There are several ways, and here
    is one example:

    ```python
    >>> N = len(names)
    >>> for i in range(0,N):
    ...   print(i, names[i])
    0 Dave
    1 John
    2 Mark
    ```

    The `range` function will return the sequence of values 0, 1, ..., N-1.
    We'll see later that `range` is an *iterable* object.

    Using the `enumerate` function, we can simplify the above loop and obtain
    the loop counter:

    ```python
    >> for i, v in enumerate(names):
    ...  print(i,v)
    ```

    When the list to print is instead a dictionary, an `items` method performs
    much the same role as the `enumerate` function:

    ```python
    >>> names = {1: 'Dave', 2: 'John', 3: 'Mark'}
    >>> for key, val in names.items():
    ...   print(key,val)
    ```

-   Within looping constructs, Python supports the usual `break` and `continue`
    statements.

-   Within for-loops, Python also supports an `else` clause: the else block will
    execute when the iterable has been exhausted, but not following a break
    statement. While-loops also support an else clause; here, the else block
    will execute when the while conditional becomes false.

Those are the core, familiar control constructs.  Again, the Python language is
intended to be lightweight.  Let's move on to a construct that may not be
familiar to you.

### List Comprehensions

The list data type is a key element of the Python language. Recall that a list
is similar to MATLAB's cell vector. A construct called a *list comprehension, or
listcomp,* provides a compact syntax to create one list from another, or from an
iterable.

-   List comprehensions eliminate the for-loop side-effect of creating
    an index.

-   Syntax is a bracket, followed by an expression, followed by a for-clause,
    followed by an optional if-clause and then a closing bracket.

-   Nested for- and if-clauses are allowed.  A few simple examples:

    ```python
    >>> Index = [i for i in range(10)] # Produces 0, 1, 2, ..., 9
    >>> Squares = [x**2 for x in range(10)] # Produces 0, 1, 4, ..., 81
    >>> Squares = [x**2 for x in range(10) if x != 5] # Skips x=5
    ```

-   The expression in a listcomp can be any expression, including another
    listcomp. Consider the following examples.

    ```python
    >>> x = [[0, 1, 2],
    ...      [3, 4, 5],
    ...      [6, 7, 8]]
    ```

    ```python
    >>> [row for row in x]
    [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    ```

    ```python
    >>> [row[i] for row in x for i in range(3)]
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    ```

    The above is equivalent to the following:

    ```python
    >>> out = []
    >>> for row in range(3):
    ...   for i in range(3):
    ...     out.append(x[row][i])
    ```

-   The following comprehension will transpose x. Note that the order of nesting
    is reversed with this construct. In this example, the expression is another
    listcomp, and is referred to as a listcomp inside a listcomp.

    ```python
    >>> [[row[i] for row in x] for i in range(3)]
    [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    ```

-   Dictionaries can also be assigned with list comprehensions:

    ```python
    >>> {x: x**2 for x in (2,4,6)}
    {2: 4, 4: 16, 6: 36}
    ```

-   Lastly, it is possible to employ an if-else in list comprehensions. This is
    achieved though Python's [ternary
    conditional](https://docs.python.org/3/reference/expressions.html#conditional-expressions),
    an expression which takes the form:

    ```python
    >>> x if C else y # C is a conditional expression
    ```

    For example, suppose you have a dictionary d with a mix of integers, doubles
    and strings. If you want to convert all of the numeric types to type double,
    but leave the strings alone, the following will work:

    ```python
    >>> d = {x: (float(d[x]) if d[x]*0 == 0 else d[x]) for x in d.keys()}
    ```

List comprehensions are a powerful feature of the Python language.  They are
memory efficient, fast, and terse.

### Iterables and Iterators

In Python every data type, whether built-in or user-defined, is a class. Some
classes have special capabilities, such as the ability of an object to produce
its data set one element at a time. Such an object is called an *iterable*.

-   An iterable is an object which can return successive items of a
    sequence created by or stored inside the object.

-   All sequence types are iterables. These include the types list, range,
    string, and tuple.

-   Sets and dictionaries are also iterables.

-   User-defined classes can be made iterable.

-   Iterables produce *iterators*.  The iterator is what produces an
    object's elements.

-   Iterators have several methods defined for them, but the one you should know
    about is the `next` method, which returns the next item in a list. Once a
    list's elements are exhausted, `next` will issue an exception.

-   For example, let's create an iterator from a list, and then produce
    the list's elements.

    ```python
    >>> x = [0, 1, 2] # A list, which is an iterable
    >>> it = iter(x)  # An iterator
    >>> next(it)
    0
    >>> next(it)
    1
    >>> next(it)
    2
    >>> next(it)
    Traceback (most recent call last):
    ```

-   Some functions return an iterable. The range() function, for example,
    creates an iterable. We saw this earlier when discussing for-loops.

-   The function call `range(0,5)` creates an iterable object that will
    return [0, 1, 2, 3, 4] one element at a time.

    ```python
    >>> range(5) # This returns the object, an iterable
    range(0, 5)
    ```

    ```python
    >>> list(range(5)) # This converts the iterable into a list
    [0, 1, 2, 3, 4]
    ```

    ```python
    >>> it = iter(range(5)) # This converts the iterable into an
    iterator
    ```

-   We also introduced the enumerate() function when discussing for-loops. The
    enumerate function returns an iterable that produces a list of tuples.
    Recall from our earlier example that the first element of each tuple will be
    a counter, and the second the value obtained from the iterable. E.g.,

    ```python
    >>> x = ['a', 'b', 'c']
    >>> list(enumerate(x))
    [(0, 'a'), (1, 'b'), (2, 'c')]
    ```

Iterables and iterators are pervasive in the Python language, as they provide
memory efficient lists. You might not use them directly, deferring instead to
for- and while-loops, but knowing how such constructs are implemented will be
valuable to you.

### Generators

As mentioned in the previous section, user-defined classes can be made iterable.
This is, however, not Python's preferred way of creating an iterator. There's
quite a bit of coding involved with iterables, and computational overhead too.
*Generators* are the preferred way of creating iteration-enabled objects. There
are two types of generators.

-   First is a *generator function*, which is a user-defined function that
    provides a sequence much like an iterable does. In deference to space
    contraints, we'll skip an example here, and just describe what a generator
    function does.

    A typical function performs computations and then returns a result.  A
    generator function is nearly identical in structure, but ends with a *yield*
    statement rather than a *return* statement.  The yield statement interrupts
    a loop, e.g., a for-loop or a while-loop, and returns one item of a
    sequence.  The function state is held in memory; any subsequent call to the
    function produces the next item of that sequence.  This process of
    generating sequence items continues until the sequence is exhausted.
    Generator functions are useful because they are highly efficient both in
    computational performance and memory usage.

-   The second type of generator is the *generator expression*. These employ
    list comprehensions and iterables to create an expression which can later be
    executed.

    In the following example, the first line produces, but does not execute, a
    generator object. The second line executes the generator object, saving the
    results as a list.

    ```python
    >>> squares = (x*x for x in range(1,5))
    >>> list(squares)
    [1, 4, 9, 16]
    ```

    The first line of the above code looks like a listcomp, but it uses ()
    rather than [], and that tells Python to create a generator. As before with
    iterators, we can iterate through a generator:

    ```python
    >>> squares = (x*x for x in range(1,3))
    >>> next(squares)
    1
    >>> next(squares)
    4
    ```

Generators are essentially lists that are awaiting completion. They are memory
efficient, and they are easy to store and to pass to methods and functions.

### Lists, Revisited

Learning Python is a nonlinear process. As we learn more and more about the
language, we need to revisit earlier topics. Now that you know about iterables,
we should revisit list construction. Lists can be constructed in multiple ways:

-   Using square brackets, a literal, as discussed before. E.g., `x = [1, 2, 3]`.

-   Using a list comprehension. E.g., `y = [x for x in range(4)]`.

-   Deferring construction with a generator. E.g., `gen = (x for x in
    range(4))`.

<!-- TODO: add example here -->
-   Using a constructor, as in the following examples:
    ```python
    >>> list('abc') # Strings are iterables
    ['a', 'b', 'c']
    ```
    ```python
    >>> list( (1, 2, 3) ) # Tuples are iterables
    [1, 2, 3]
    ```
    ```python
    >>> list( (x*x for x in range(1,5)) ) # Generators are memory-efficient
    [1, 4, 9, 16]
    ```

Keep in mind that user-defined objects can be made iterable. We have not covered
such objects yet, but once we do, you'll see that their contents can be
converted into list objects.

### Functions

Python functions are similar to MATLAB functions, although Python signatures are
more versatile. Also, there are some interesting ways to use and reuse functions
in Python.

-   The basic structure of a function is:
    ```python
    def fun(arg1,arg2):
      """doc string""" # A doc string (like a MATLAB H1 line)
      # Blank line before code begins
      code
      # Blank line to end the function
    ```

-   Function arguments are always *call by reference*. Python does not
    support *call by value*.<sup>[2]</sup>

-   To return a value(s), Python does not support an `out = fun()` construct.
    Instead, Python uses `return var` at the end of the function.

-   If a function returns no value, the built-in value `None` is returned by
    default. The value `None` has a type of `NoneType`.

-   Function arguments can be given default values. E.g.,
    ```python
    def input_name (prompt, retries=4, reminder='Please try again!'):
      """ doc string """
      # we'll skip the function's code for now
    ```

    Default values are evaluated only once, and only at the point of the
    function definition. As in the above, the arguments with default values must
    follow any positional arguments. When defaults are given, those arguments
    become optional for the caller.

-   Functions can be called with keyword arguments. E.g., to call the function
    just defined we could type:
    ```python
    >>> input_name(prompt='Your name?', retries=10, reminder='Try again')
    ```

    Once a keyword argument is provided, all remaining arguments (if provided)
    must also be keyword arguments.

-   Function signatures are quite robust. Following positional arguments and
    arguments with defaults, one can pass an arbitrary number of arguments with
    the following construct:
    ```python
    def fun(arg1, arg2='test', *args):
    ```
    This is similar to MATLAB's vararg input. In the caller, following the
    positional and keyword arguments, one can pass an arbitrary set of
    comma-separated values. Inside the called function, the `*args` inputs will
    automatically be packed into a tuple named `args` (in this example).

-   Expanding upon the above signature, one can also specify that a function is
    to receive an arbitrary number of keyword arguments:
    ```python
    def fun(arg1, arg2='test', *args, **kwargs):
    ```
    The above listed order of arguments is required.  If provided, the trailing
    keyword arguments will automatically be packed into a dictionary inside the
    function.

    Suppose we wish for the above function to print its arguments.  We'd have
    the following:
    ```python
    def fun(arg1, arg2='test', *args, **kwargs):
        print(f'arg1: {arg1}')
        print(f'arg2: {arg2}')
        print(f'*args: {args}')

        for kw in kwargs:
            print(f'{kw}: {kwargs[kw]}')
    ```
    Now call the function, as below, with the following outputs:
    ```python
    >>> fun(5, 'foo', 10, 15, a=20, b=25)
    arg1: 5
    arg2: foo
    *args: (10, 15)
    a: 20
    b: 25
    ```
-   If a function signature requires individual arguments but the calling
    workspace has a list or tuple, the latter can be unpacked on the fly with a
    star ('\*') syntax. For example:
    ```python
    >>> list(range(0, 3))
    [0, 1, 2]
    ```
    The above is equivalent to
    ```python
    >>> x = [0, 3]
    >>> list(range(*x))
    ```
    Dictionaries can also be unpacked, and that syntax uses a double star.

-   The execution of a function introduces a new symbol table used for the local
    variables of the function. Variable references in a function first look in
    the local symbol table, then in the local symbol tables of enclosing
    functions, then in the global symbol table, and finally in the table of
    built-in names.

-   Like everything else with Python, a function is represented internally as an
    object. That means you can do some interesting things with functions, like
    pass them into other functions. Consider the following simple example:
    ```python
    >>> def f(x): # Trivial function
    ...   return x+1
    ```
    The function f(x) is not just a function sitting in memory waiting to be
    invoked; it is an object in the workspace that can be passed around.
    ```python
    >>> f?
    Signature: f(x)
    Docstring: <no docstring>
    File: c:usersownerdocumentspython...
    Type: function
    ```

    Define a second function, which accepts the first function (or any function)
    as an argument:
    ```python
    >>> def g(fun, x): # Pass a function into a function
    ...   return 2*fun(x)
    ```
    It's a trivial example, but here's how the two functions work together:
    ```python
    >>> f(5)
    6
    >>> g(f,5)
    12
    ```

-   Anonymous (unnamed) functions are created with the `lambda` keyword. E.g.,
    ```python
    >>> f = lambda x,y: x/y
    >>> f(x=10, y=2)
    5
    >>> f(1000, 10)
    100
    ```
    Such functions are commonly referred to as *lambda functions* or *lambda
    expressions*. As with nested functions, lambda functions can reference
    variables of the containing scope:
    ```python
    >>> def divideby(x):
    ...   return lambda y: x/y
    ```
    The above function returns a lambda object:
    ```python
    >>> divide10by = divideby(x=10)
    >>> divide10by(5)
    2
    ```

    As mentioned earlier, functions are objects and can be passed around like
    data. This is powerful, and it will take some getting used to. Consider the
    following example, where we have a list of strings and we want to sort them,
    ascending order, by the number of unique characters in each string.
    ```python
    >>> str = ['cook', 'zoo', 'ohnoooh']
    >>> str.sort(key=lambda x: len(set(x)))
    >>> str
    ['zoo', 'cook', 'ohnoooh']
    ```

    How did the above work? First, strings are a class, and that class has a
    `sort` method associated with it. The `sort` method allows a key argument,
    and we passed a `lambda` function as the value of that argument. In other
    words, we defined, on the fly, a function and then passed that function to
    the `sort` method. For each element in variable str, the lamba function
    converted the string into a set, thereby removing duplicate letters, and
    then computed the length of the remaining characters. The length of the
    unique characters in each string then became the key by which to sort the
    list of strings.

    The above is equivalent to:
    ```python
    >>> [str[i] for i in [1, 0, 2]]
    ```
    This is equivalent, but assumes that we somehow know the sort order.
    Using the `sort` method and a `lambda` function in the first example, we
    were able to determine the sort order on the fly.

### Warnings

As with MATLAB, Python has facilities for warnings and exceptions (errors). In
fact, Python has sophisticated facilities for these.

Warnings are objects and derive from a Warning class. A list of built-in Warning
subclasses is available in the [Python Standard Library
documentation](https://docs.python.org/2/library/warnings.html). Users can
create their own warning classes, derived from the built-in classes. A warning
filter allows a user to process a warning through a sequence of pre-defined
categories of warnings, processing any match that is found with specific
actions. The filter can suppress a warning, escalate it to an exception, or
print it. For all the sophistication, warnings can also be very simple:

```python
>>> import warnings
>>> warnings.warn('Something seems wrong')
__main__:1: UserWarning: Something seems wrong
```

<br><br>

### Exceptions

Python's exceptions are a lot like MATLAB's error facility, but more powerful.
The syntax is similar, and we'll point out the differences.

Inside a program, a user might want to manually check for an error and if
encountered, issue an exception. Suppose you are about to compute the standard
deviation of a list of values, but you want to enforce a minimum length to the
list, e.g., ten data points. Your code would look something like:

```python
if len(x) <= 10:
  raise Exception('Too few data points')
```

The above block would raise (throw, in MATLAB terms) an exception.

Whereas MATLAB has try-catch blocks, Python defines try-except blocks. Here's a
quick summary:

-   Like warnings, each Python exception is a class. E.g., NameError or
    TypeError. There are dozens of built-in exception classes; you'll find a
    complete list in the [Python Standard Library
    documentation](https://docs.python.org/3/library/exceptions.html).

-   Exceptions can be user-defined and will derive from the built-in
    *Exception* class.

-   Try-except blocks have added functionality compared to MATLAB. The outline
    of a try-except block looks like:
    ```python
    try:
      # code
    except NameError:
      raise Exception('Name is not defined.')
    except ValueError:
      raise Exception('Value is not valid.')
    else:
      # Code that is always executed if no exception is raised.
      # Useful for code that should not be part of the try-block.
    finally:
      # Cleanup code that is always executed, regardless of whether an
      # exception was encountered.
    ```
-   As in MATLAB, it is not necessary to specify the class of error.
    E.g., the following is permissible:
    ```python
    try:
      x = y / z
    except:
      raise Exception('Looks like z was equal to zero')
    ```
    However, when you are monitoring for and handling specific types of errors,
    use of a built-in or user-defined exception class is recommended. E.g.,
    ```python
    try:
      x = y / z
    except ArithmeticError:
      raise Exception('Looks like z was equal to zero')
    ```

-   As with MATLAB's throw() function, use Python's raise() function to issue an
    exception. Any associated arguments are available to the exception instance.

-   While Python provides a long list of built-in exceptions you can catch,
    there will be times when you won't be able to anticipate a specific error
    type.  Perhaps you are interacting with the operating system, or a database,
    and the possible exceptions are too broad in type to catch with a
    narrowly-focused built-in exception.  For these instances you can use an
    exception base class.  E.g.,
    ```python
    try:
      x = some_function()
    except BaseException as e:
      raise(e)
    ```

-   If you desire a stack trace and/or logging into a log file, use Python's
    logging module. E.g.,
    ```python
    import logging
    try:
      y = 5 / 0
    except:
      logging.exception('Division by zero')
    ```

-   Some objects have pre-defined clean-up actions that can occur regardless of
    any exception thrown (or not). An example is the opening of a file. A
    [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
    statement will ensure that pre-defined actions occur even if not explicitly
    requested. For example:
    ```python
    with open('some_file.csv') as file:
      for line in file:
        print(line)
    ```
    Following execution of this block of code, the opened file will be closed
    regardless of whether an exception was raised. The `with` statement is just
    shorthand notation for a try-except block, but useful and convenient.

### Listing the Python Version

You'll need, from time to time, to know the version of Python that you are
using.

Here's how to get the version number from Python itself:
```python
>>> import sys
>>> sys.version
3.7.0 (v3.7.0:1, Aug 27 2018, 04:59:51) [MSC v.1914 64 bit]
```

And from a shell window, simply enter `python -V`.

### Interacting with the Operating System

Eventually you'll want to interact with the host computer's operating system.
Here's a sample of what you can do:

```python
>>> import os
>>> os.getcwd()
>>> os.listdir()
```

You can change environment variables this way, change to a new directory, etc.
To see a list of all of the methods in the os module, use `dir(os)`.
<br><br>

### Miscellaneous

If you have been entering the above commands into a Python console window, you
might be wondering how to perform a few basic maintenance operations, like
listing or clearing the workspace variables. Python itself does not provide
these features, although you can certainly code your own version of `whos` or
`clear`. However, if you are using IPython or an IDE built on IPython, you will
have access to [magic
commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html),
commands that will be familiar to you except that they are prefixed by a '%'.
Try the following:

```python
>>> %who
>>> %whos
>>> %reset # Equivalent to MATLAB's *clear* command
```

There are a *lot* of magic commands, so you'll eventually want to review those
at the above link. You can also get magic command help from the Python console
with the following command:

```python
>>> %magic
```

In addition to the magic commands, the IPython console (we're assuming you'll
eventually use this) provides an introspection facility that helps you quickly
examine any variable you have defined. For example,

```python
>>> x = list(range(5))
>>> x? # Can also use >>> ?x

Type: list
String form: [0, 1, 2, 3, 4]
Length: 5
Docstring:
Built-in mutable sequence.
```

Introspection works with objects, built-in functions and user-defined functions.

[2]: Strictly speaking, Python always passes a function argument using
    *call by value*. However, the value passed is an object reference,
    not the object itself. Therefore, in MATLAB terminology Python
    passes function arguments using *call by reference*.
