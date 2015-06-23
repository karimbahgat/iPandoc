try: from setuptools import setup
except: from distutils.core import setup

setup(	long_description=open("README.rst").read(), 
	name="""iPandoc""",
	license="""MIT""",
	author="""Karim Bahgat""",
	author_email="""karim.bahgat.norway@gmail.com""",
	py_modules=['ipandoc'],
	url="""http://github.com/karimbahgat/iPandoc""",
	version="""0.1.0""",
	keywords="""pandoc document format conversion rst markdown docverter API""",
	classifiers=['License :: OSI Approved', 'Programming Language :: Python', 'Development Status :: 4 - Beta', 'Intended Audience :: Developers', 'Intended Audience :: Science/Research', 'Intended Audience :: End Users/Desktop'],
	description="""Pure Python bindings to the online Docverter Pandoc document format conversion API.""",
	)
