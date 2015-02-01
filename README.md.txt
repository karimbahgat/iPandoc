# iPandoc

Pure Python bindings to the online Docverter Pandoc document format conversion API.
This way, you get access to the power of Pandoc from anywhere, without having to meddle 
with installing anything. 

www.docverter.com

Karim Bahgat (2015)

## Usage

Usage is pretty simple, there is only one function, which converts a piece of text to another document format. 

This can be pretty useful, especially for dynamically converting a project README file, typically in markdown format for displaying at GitHub, over to ReStructured text for displaying at PyPi (e.g. in your project's setup.py file). 

```python

import ipandoc
markdown = open("README.md").read()
rst = ipandoc.convert(text=markdown, fromformat="markdown", toformat="rst")

```

## Documentation

```python

def convert(text, fromformat, toformat, **options):
    """
    - text: The text to be converted to another language format. If converting file use open(filepath).read(). Text should be encoded as raw byte string (e.g. "yourtext".encode(...)". 
    - fromformat: From language format. FORMAT can be markdown (markdown), textile (Textile), rst (reStructuredText), html (HTML), docbook (DocBook XML), or latex (LaTeX).
    - toformat: To language format. FORMAT can be markdown (markdown), rst (reStructuredText), html (XHTML 1), latex (LaTeX), context (ConTeXt), mediawiki (MediaWiki markup), textile (Textile), org (Emacs Org-Mode), texinfo (GNU Texinfo), docbook (DocBook XML), docx (Word docx), epub (EPUB book), mobi (Kindle book), asciidoc (AsciiDoc), or rtf (rich text format).
    - **options: Supply any additional Pandoc options for the conversion process. Note: Options that are only meant to be set on or off should be specified as strings "true" or "false". See docverter api website for more details on options: http://www.docverter.com/api
    """

```