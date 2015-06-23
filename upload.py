import pypi
 
packpath = "ipandoc.py"
pypi.define_upload(packpath,
                   author="Karim Bahgat",
                   author_email="karim.bahgat.norway@gmail.com",
                   license="MIT",
                   name="iPandoc",
                   description="Pure Python bindings to the online Docverter Pandoc document format conversion API.",
                   url="http://github.com/karimbahgat/iPandoc",
                   keywords="pandoc document format conversion rst markdown docverter API",
                   classifiers=["License :: OSI Approved",
                                "Programming Language :: Python",
                                "Development Status :: 4 - Beta",
                                "Intended Audience :: Developers",
                                "Intended Audience :: Science/Research",
                                'Intended Audience :: End Users/Desktop'],
                   )

pypi.generate_docs(packpath)
#pypi.upload_test(packpath)
pypi.upload(packpath)

