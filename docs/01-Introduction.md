
# Introduction

If the title of this paper caught your eye, chances are you have
programmed in MATLAB for some time. You know the MATLAB language, the
development environment, and probably a few toolboxes. And yet you saw
the word *Python* in the title and kept reading.

Alongside MATLAB, Python has evolved into a powerful and popular
programming language. Python can interact with MATLAB, and thus could
augment or streamline some of your current MATLAB-based programming
efforts. That is, if only you knew more about the Python language.

This article's authors have more than thirty years combined programming
experience with MATLAB and numerous other languages. Over the past
several years we've also worked with Python, and we know firsthand that
there's room for the Python language in a MATLAB programmer's toolbox.
But to our knowledge nobody has written a comprehensive guide to help a
MATLAB programmer discover Python. Until now.

If you are a MATLAB programmer and you've been wondering what the
Python programming language is or if it might be of value to you, this
article is for you. If you want to learn about Python but don't want to
spend a week reading tutorials, this article is for you. We hope that by
the time you've read this article, assuming that you do, you'll agree
that we've provided a quick way to discover Python given your
background in MATLAB programming.

## Objectives of this Article

Because MATLAB and Python have many similarities, and because you
already know the former, learning about the latter should come easy. The
primary objective of this article is to provide you with a quick,
familiar way of discovering Python. We will not try to present the
entire Python language; we'll instead focus on those parts most
relevant to a person coming from your background.

In addition to presenting the Python language we'll introduce the
Python ecosystem, a set of libraries and tools that provides Python with
features and capabilities you've come to enjoy with MATLAB. The Python
ecosystem is vast, and a second objective of this article is to filter
the ecosystem to those parts that will likely be of importance to you.

A third objective is to present you with an unbiased view of both
languages. There are plenty of websites and articles that claim to prove
one language is somehow *better* than the other; we find those
discussions to be subjective, biased, and often misrepresentative of one
or both languages. We will not suggest that you switch from one language
to the other. We find tremendous value in MATLAB, but we also find value
in Python. Each language has its strengths and the two products can
interoperate. So perhaps you'll find reasons to use both languages, as
we do.

A fourth, and last objective of this article is to be as brief as
possible. Python is already well documented, so this document strives to
be a quick read.

## Contributing to this Article

As just mentioned, we have a goal of keeping this article brief.  However,
we've received suggestions of additional material for the article, and 
we value those suggestions.  In March 2019 we published the article to a [GitHub public
repository](https://github.com/apjanke/PythonForMatlabCoders) under a 
[Creative Commons Attribution ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

Readers are encouraged to edit or add material by submitting pull requests from the GitHub repository.  If
you are not comfortable doing so but have corrections, additions, suggestions, criticisms, etc.
please direct them to the authors.  We will give proper acknowledgement to all who contribute to
this article.

Let's get started.

## Conventions

We will use only a few conventions in this document, again in the name
of simplicity. Code that you would enter in a Python console is prefaced
by the standard `>>>` Python prompt. Continuation lines are
prefaced by the standard `...` continuation marks.

On the rare occasion that we reference an operating system, we reference
only Windows even though Python also runs on Macintosh and Linux. We
believe that the Windows-based references are clear enough that
translating to the other operating systems will be straightforward.

# MATLAB and Python, at a High Level

Like MATLAB[^1], Python is an interpreted, interactive, object-oriented
programming language. MATLAB was first released in 1983; Python in
1991.  Both are extensible and designed for use by a wide audience.

You already know MATLAB's key characteristics. Let's assess, in as
non-subjective manner as possible, the high-level similarities of MATLAB
and Python.

-   Both languages are interpreted.

-   Both languages can be used in either interactive or batch mode.

-   Both languages have high-level data types, such as arrays and
    classes.

-   Both languages incorporate dynamic, run-time variable typing.

-   Both languages and associated ecosystems are well documented.

-   Both languages are extensible in C and C++. Both can also be used as
    an extension to other languages.

-   Both languages can call one another.

Clearly the two languages have numerous similarities. But these are
different languages, designed by different people with different design
objectives and different target audiences. Each language has its own set
of strengths and weaknesses. Some of the key differences between the two
languages are as follows; again, we will strive to be as objective as
possible.

-   MATLAB is targeted to an audience of engineers and scientists;
    Python is more closely targeted to a computer science crowd.

-   Once installed, MATLAB provides not just a programming language; it
    offers also a complete programming environment. Python is more
    modular: once installed, you'll need to go shopping for supporting
    modules and an Integrated Development Environment.

-   MATLAB expresses linear algebra and array computations with notation
    that mimics mathematical formulas. This is quite powerful for
    scientists and engineers. In contrast, the Python language does not
    offer a mathematics-based language. But the Python language is
    elegant, terse and very readable.

-   MATLAB has an extensive library of built-in functions, control
    structures, and a sophisticated object model. Python, in contrast,
    has fewer built-in functions and control structures, and a simpler
    object model. Which is better? One is more powerful out of the box;
    the other is easier to learn. You get to choose.

-   In contrast, Python has more sophisticated features for exception
    handling. Again, more powerful is good, but a shorter learning curve
    is too.

-   Both languages have numerous add-on libraries (Toolboxes or
    Modules).  Python has more add-on libraries, but the MATLAB
    libraries are commercially developed, integrated with one another,
    fully tested and documented, and supported by dedicated teams.
    Python libraries are developed in an open source environment; such
    development efforts can produce excellent software, but users need
    to verify the quality of the software they are considering.

The list goes on. Assuming you have access to both languages, you can
use both to extract the best of each. Let's look at a few more
differences that you'll eventually want to consider.

-   One major difference between MATLAB and Python is in their
    respective licensing models. MATLAB is commercial software and can
    be obtained only by paying a license fee. Python is copyrighted but
    is open source and free for both personal and commercial use.

-   As already mentioned, MATLAB installs as a complete programming
    environment. But Python is a component of a larger ecosystem. 
    Python can be used for system admin, network admin, building web
    pages, and more.

-   Python is at home on the web; that is, Python apps are easily hosted
    as web apps.  MATLAB apps can also be hosted as web apps, but this
    requires more work.

-   Like MATLAB, Python supports single- and multi-dimensional arrays,
    and has extensive functionality to perform numerical and scientific
    computing. But unlike MATLAB this support is not part of the core
    product. Python obtains this support from add-on libraries.

-   Unlike MATLAB, Python is multi-threaded.  The core Python language
    is single-threaded but module support of coarse-grain
    multi-threading is available.

Lastly, let's consider the two languages from the point of view of a
typical MATLAB programmer (assuming we can stereotype here). Each
product supports timeseries data and has several date and time-specific
data types. Each provides extensive mathematical and scientific
libraries. Each provides access to a wide collection of linear algebra
algorithms. Each provides extensive charting capabilities, including
geospatial charting. Each can compile source code to P-code. This list
too, goes on.

In the end, MATLAB and Python differ in many implementation details but
provide many common capabilities.

# Installation

Python is available for the Windows, MacIntosh and Linux operating
systems. The installation process is simple: just
[download](https://www.python.org/downloads/) the installer and click
through its prompts. Note that both x86 and x86-64 versions are
available. Grab whatever latest version is appropriate for your
computer.

# Integrated Development Environments (IDEs)

You may eventually want an IDE, and there are numerous to choose from.
The [Wiki
pages](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments)
at python.org list approximately twenty IDEs. One that will likely be of
interest to you is [Spyder](https://www.spyder-ide.org/), which provides
a programming environment similar to MATLAB's. Be aware that some
Python IDEs are quite sophisticated and are not trivial to learn. For
the purpose of running this article's code snippets, you have two
simpler options.

First, an IDE called IDLE ships with the Python download. This IDE is
limited in functionality but sufficient for our present needs. To run,
first install Python as per the above instructions. Then open a command
window and enter *idle*. There's some trial and error in learning how
to enter commands and code blocks into IDLE, but you'll catch on
quickly.

Alternatively, you can skip the Python install and run Python commands
online at any of a number of websites that provide a Python engine. One
such website is [Repl.it](https://repl.it/repls/SlategreyGloomyLava).
The learning curve is shorter with this approach, and no installations
are required.

For the moment, we recommend that you either use an online Python
engine, or simply postpone your decision until later. We will return to
the IDE topic in the chapter titled, *The Python Ecosystem*. At that
time, you'll understand why we suggest you delay this decision.

# Python Modules and Packages

Python uses *modules* and *packages* in the same way that MATLAB uses
M-files and toolboxes. A module is a file of Python code with a file
name that ends with suffix .py; a package is a directory of modules.
There are so many modules and packages publicly available that
discovering them requires an investment of your time.

A list of public modules is available at the PSF [Module
Index](https://docs.python.org/3/py-modindex.html). A searchable list of
packages is available at the [Python Package Index](https://pypi.org/).
How many packages are available, you ask? Nearly 150,000 as of late 2018.
Again, the Python ecosystem is quite large. From the PSF website,
the most commonly used packages include:

-   [NumPy](http://www.numpy.org/): a library which provides arrays to
    support advanced calculations

-   [SciPy](https://www.scipy.org/): a library for mathematical,
    scientific, and engineering computations

-   [Pandas](http://pandas.pydata.org/): a library for data structures
    and data analysis

-   [Matplotlib](https://matplotlib.org/): a 2-d plotting library with a
    MATLAB-like interface

-   [TKinter](https://wiki.python.org/moin/TkInter): de-facto GUI
    building interface

-   [IPython](http://ipython.org/): an interactive console, and tools
    for parallel and distributed computing

Most (perhaps all) of the MATLAB toolboxes have been reproduced as
Python packages. Even the MathWorks' flagship product Simulink has a
companion Python package called [bms](https://pypi.org/project/bms/). On
the Package Index website, you'll find packages for curve fitting,
statistics, mapping, analyzing text, AI, image processing, among
hundreds of topics.

Be aware that Python packages are developed in an open source
environment. Generally, these efforts produce quality software but there
are no guarantees. In contrast, MATLAB toolboxes are written by
professional software developers at the MathWorks, and the quality of
their software is usually excellent. When selecting Python packages,
it's a good practice to look for the project's development page to
gauge its member involvement, project maturity, and bug reports. Most
Python projects are hosted on [GitHub](https://github.com/).

To register a module in the current workspace, Python uses an *import*
statement. Importing a module is similar to adding a folder to the
MATLAB path: each process makes additional definitions and logic
available to the current workspace. We'll discuss the importing of
modules and packages in great detail later on. For the moment, just know
that when you see an import statement in the following examples, we're
registering Python files in the current workspace.

# The Python Style Guide

Python is a terse, whitespace-sensitive language. A key objective of the
language is to be readable, and toward that goal the language adheres to
[PEP8: The Style Guide for Python Code](https://pep8.org/). Here, PEP is
an acronym for *Python Enhancement Proposal*. Many languages have
preferred styles, but Python demands many of its style specifications.
Blank lines and indentations are important, and their proper use is not
optional. Eventually you will want to read the style guide, but early on
you can also allow an IDE to enforce the required conventions.

# Getting Help

There will be times when reading this document that you'll want
additional information on a data type, function or class. Python gives
you several sources of help. Suppose you want information about the
int() function. From a Python console you can type:

```python
int?
help(int)
```

The first command will provide you with a brief overview of the
function. The second command will provide a broader discussion. If you
are using an IDE which is IPython-based, you can also enter the
following:

```python
int?? # More details on the int() function

? # Help on IPython itself

%quickref # Quick reference on IPython
```

And of course, you can find online help at
[python.org](https://www.python.org/) or any of many Python-focused
websites.

[![Next Section](media/next.png)](02-Python-Types.md)

[^1]: MATLAB® and Simulink are registered trademarks of The MathWorks,
    Inc. 
