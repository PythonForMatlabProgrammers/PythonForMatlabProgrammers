<br>
<br>

# Object-Oriented Programming in Python

At this point of the article we'll dive a bit deeper into the Python programming
language. We'll discuss namespaces, scopes, and then classes. Each of these
differs from the MATLAB model, and you need to be aware of the changes.

### Namespaces and Scopes

Let's start with Namespaces and scopes, as these concepts are important
prerequisites for understanding classes.

-   A *namespace* is a mapping from names to objects, typically implemented as a
    dictionary. Examples include built-in names, exception names, global names
    of a module, and local names of a function.

-   Namespaces are implemented (currently, anyway) as dictionaries. The
    dictionary keys are variable names, and the associated values are the
    objects that the names point to.

-   In Python, a *global* namespace refers to the top-level space of a single
    module. The global namespaces of two or more modules are not shared.

-   Attributes of an object are effectively a namespace.

-   A *scope* is a textual region of a program where a namespace is directly
    accessible.

-   At any time during program execution, at least three scopes are in
    effect. From the innermost scope to the outermost, these are:

    1.  The innermost scope is that of any embedded function (a function embedded in an
        enclosing function). When Python is trying to resolve a
        reference, this innermost scope of local names is searched
        first.

    2.  The scopes of enclosing functions, containing non-local, but
        also non-global names is the second-most inner scope. When resolving references, this scope is
        searched second.

    3.  The next to last scope (the *middle,* or *global scope*)
        contains a module's global names.

    4.  The outermost scope (searched last) is the namespace containing
        built-in names.

-   Variables can be declared *global*, in which case they will reside
    in the middle scope.  These variables  will not be shared across modules.

-   Within the four scopes, variables flow from the outer scopes into the inner
    scopes.  That is, a variable declared in an outer scope can be referenced in
    an inner scope.  The converse is not true; variables defined in an inner scope
    cannot be referenced in an outer scope.  To alter this latter behaviour, variables
    in an inner scope can be declared *nonlocal*, whereby they will pass by reference
    into any outer scope.

### Classes

For programming projects of non-trivial size, the use of classes is considered
standard practice. MATLAB provides a sophisticated class model that, while
offering programmers tremendous capabilities, is difficult to learn. Python's
class model is much simpler, offers fewer capabilities, but is easier to learn.
Let's have a look.

In the following, we'll make no attempt to explain object-oriented programming;
we are instead assuming you have covered this topic elsewhere. We'll provide an
outline of what Python offers, from as usual, the perspective of a MATLAB
programmer.

In Python *everything* is an object; in MATLAB most but not all things are
objects.

Let's look at a few simple Python examples of variables. Consider the following:
```python
>>> x = []
>>> x?
Type: list
String form: []
Length: 0
Docstring: Built-in mutable sequence.
```

As the above shows, even the [] construct creates an object.  In this case,
variable x is a list object. Or consider how a variable containing an integer
has a class attribute:
```python
>>> x = 5
>>> x.__class__
<class 'int'>
```

-   Classes are defined with a straightforward syntax. In the following
    example code, we define a class, a docstring, an instantiation method,
    and then two class methods:
    ```python
    class MyClass:
            """A sample class definition"""         # Like MATLAB's H1 line

            def __init__(self):      # A constructor
                self.mydata = []

            def method1(self):
                self.mydata = 3.14159

            def method2(self):
                self.mydata = 3.14159 / 2
    ```

-   Class objects support only two kinds of operations: attribute references and
    instantiation. Let's look first at attribute references. Consider the
    following class definition which defines one attribute and one method:
    ```python
    class MyClass:
            """Doc String"""
            x = 3.140

            def f(self,StringToPrint):
            print(StringToPrint)
    ```
    You'll need to save the above into a .py file.  You can choose any name for the
    file; let's use simple.py.  Back in the Python console window, we can type the
    following:

    ```python
    >>> import simple
    >>> obj = simple.MyClass()
    >>> obj.x
    3.14
    >>> obj.f('test')
    'test'
    ```
    Both the attribute and the method are referenced with the same
    notation. Use of the variable 'self' as the first argument to the
    above method is only a convention; this is, however, the standard
    convention.

-   Now let's look at an instantiation operation. Python uses a
    specifically named method for instantiation, called
    `__init__`, as per the following example:
    ```python
    def __init__(self, day, activity):
        self.weekday = day
        self.activity = activity
    ```
    When an `__init__` method is placed into a class definition, it is
    automatically invoked when the class is first instantiated.

-   Python supports class inheritance. The syntax is simply:
    ```python
    class SubClassName(BaseClassName):
    ```
    In the above, BaseClassName must be in scope. If it is not, one can
    instead use:
    ```python
    class SubClassName(ModuleName.BaseClassName):
    ```
    Subclass methods may either override or extend base class methods of the same
    name. To call a super-class method from a subclass, use super(). For example, if
    a parent class has a method called invite(), the subclass can reference the
    method with super().invite().

-   Python supports both class (static) and instance variables. The location
    where variables are defined in a class, rather than the use of keywords,
    dictates whether a variable is a class variable or instance variable. E.g.,

    ```python
    def MyClass:
        ClassVar = 3.14     # Class, or static variable

    def __init__(self):
        self.InstanceVar = 3.14159     # Instance variable
    ```

-   Static variables should be used with care.  If you create two instances of
    the above class and use one of them to alter the value of ClassVar, that
    value will then appear also in the second instance.

-   Python also supports static methods. This introduces the topic of Python's
    *class decorators*, which we consider to be an advanced topic best saved for
    later. But for now, know that Python supports both static and instance
    methods.

-   In MATLAB, a class resides in a file of the same name. In Python, multiple
    classes can be defined in one file, and that file can take any name. More
    generally, a class can be defined anywhere, e.g., inside of a function or an
    if statement (not that you would do that, of course). Classes can be
    embedded within one another, with the inner class having access to the outer
    class namespace. The author of Python, Guido van Rossum, maintains a blog
    where he has an [interesting
    discussion](http://python-history.blogspot.com/2009/03/how-everything-became-executable.html)
    of this topic.

-   There are some significant differences between the MATLAB object
    model and Python's. Here are the biggest ones:

    -   MATLAB provides private attributes (for both properties and
        methods); Python does not.

    -   Further, MATLAB provides numerous property attributes such as
        Abstract=true. Python offers none of these.

    -   MATLAB also offers object events, or listeners; Python does not.

    -   MATLAB requires that a file can hold only one class; Python has
        no such restriction.

-   There are many more differences between the MATLAB and Python object
    models. In general, the Python model chooses simplicity over
    sophistication; vice-versa for MATLAB. Which model is the best
    choice will depend upon your programming needs.

### Mutability

Python considers everything to be an object. Once initiated, some objects allow
their state to be changed, meaning they are mutable. Other objects prohibit
state changes; these objects are immutable. Knowing which classes are mutable
and which are not is important. Here's a reference list:

-   Mutable classes: list, set, dict and byte array

-   Immutable classes: bool, complex, float, int, str, tuple and
    frozenset

It may seem strange that Python defines so many immutable classes. But beyond
the primitive data types (bool, complex, float and int) only three classes are
immutable. And of those three, the tuple class allows its contents to contain
mutable objects.

### Copy That

To close out this chapter, let's discuss an interesting, and likely unexpected,
feature of Python: the language provides *three* mechanisms for copying
variables. We think it's best to inform you of this now, so that you don't learn
about this after tripping over it.

Suppose you have a list referenced by the variable x. If you then create a new
variable y with the operation y=x, the new variable y simply points to the original
list; the variable y does not reference a new copy of the list. This is an
important concept to master as it effects all Python data types. On assignment,
Python will *bind* two objects together rather than make a copy. Consider the
following:
```python
>>> x = [0, 1, 2, 3]
>>> y = x
>>> x[0] = 99
>>> y
[99, 1, 2, 3]
```

By updating x we also updated y, because y was *bound* to x. From the MATLAB
perspective, x and y are similar to handle objects; unlike MATLAB, Python
defaults to this behavior.

When necessary Python will allow you to make a true copy. But there are two
flavors of true copies. The first is called a [shallow
copy](https://docs.python.org/3/library/copy.html). For simple objects like a
list that don't contain nested objects, the shallow copy is all you need.
```python
>>> import copy
>>> x = [0, 1, 2, 3]
>>> y = x.copy()
>>> x[0] = 99
>>> y
[0, 1, 2, 3]
```

When you are trying to copy more complex objects, such as a user-defined object
whose attributes reference other objects, you will need a [deep
copy](https://docs.python.org/3/library/copy.html) of the list. In this third
case, use x.deepcopy() instead of x.copy().

An important exception to binding is in making array slices. When an array is
sliced, the returned object is a new object, not a view into the original
object. E.g.,
```python
>>> a = list(range(5))
>>> b = a[2]     # A slice, which is not bound to variable 'a'.
>>> b
2
>>> b = 99     # Change the value of b.
>>> a
[0, 1, 2, 3, 4]     # Variable a is unaffected.
```

### Biggest Differences

Now that you've seen Python's primary data types and control structures, let's
catalog the major differences between the Python and MATLAB languages. Here are
the items that made our list. If you are going to program in the Python
language, you'll want to spend some time studying these topics further.

-   Python array indexing: zero-based rather than one-based, and square
    brackets rather than parentheses.

-   List comprehensions: there's really no equivalent in MATLAB.

-   Iterables, iterators and generators: an important feature of the
    Python language. MATLAB does not offer the feature, although you can
    code it yourself.

-   Mutability: this is an important concept in Python. This same
    concept exists in MATLAB, but programmers are largely shielded from
    and thus often unaware of it.

-   Bindings, shallow copies and deep copies: by default Python treats
    objects like MATLAB handle objects.

We have now covered the primary Python data types and control structures. In the
third and last chapter of this article, we'll look at the expansive Python
ecosystem.
