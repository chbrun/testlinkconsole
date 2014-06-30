from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name    = 'testlinkconsole',
    version = '0.1',
    author = "Christophe Brun",
    author_email = "christophe.brun.cl194@gadz.org",
    description = ("Testlink Console "),
    license = "BSD",
    keywords = "console testlink",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=find_packages(),
    classifiers=[
            "Development Status :: 3 - Alpha",
            "Topic :: Utilities",
            "License :: OSI Approved :: BSD License",
            ],


)
