iPandoc
=======

Pure Python bindings to the online Docverter Pandoc document format
conversion API. This way, you get access to the power of Pandoc from
anywhere, without having to meddle with installing anything. Useful for
lightweight applications or when you want to avoid the overhead of a
full pandoc installation.

See: http://www.docverter.com/

Platforms
---------

Tested on Python version 2.x and 3.4.

Dependencies
------------

Pure Python, no dependencies.

Installing it
-------------

iPandoc is installed with pip from the commandline:

::

    pip install ipandoc

Usage
-----

iPandoc is very simple to use. There is only one function, which
converts a piece of text to another document format.

This can be pretty useful, especially for dynamically converting a
project README file, which some people write in markdown format for
displaying at GitHub, over to ReStructured text for displaying at PyPi
(e.g. in your project's setup.py file).

::

    import ipandoc
    markdown = open("README.md").read()
    rst = ipandoc.convert(text=markdowntext,
                          fromformat="markdown",
                          toformat="rst")

Of course, there are many other text formats you can convert between.
See API documentation link for more details on usage and options.

More Information:
-----------------

-  `Home Page <http://github.com/karimbahgat/iPandoc>`__
-  `API Documentation <http://pythonhosted.org/iPandoc>`__

License:
--------

This code is free to share, use, reuse, and modify according to the MIT
license, see license.txt

Credits:
--------

Karim Bahgat (2015)
