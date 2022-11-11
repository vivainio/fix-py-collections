# fixcollections

Python 3.10 broke compatibility with old versions of some libraries (some of them are very popular, like setuptools).

This provides a monkeypatch function that restores the compatibility shims [removed in Python 3.10](https://github.com/python/cpython/issues/81505)

Installation:

```
$ pip install fixcollections
```

Usage: 

```python
import fixcollections
fixcollections.monkeypatch()

from setuptools import setup
# etc etc
```

If you see this exception, you either need to do this monkeypatching or migrate to newer version of your library (like setuptools):

```
Traceback (most recent call last):
  File "C:\p\fix-py-collections\setup.py", line 5, in <module>
    from setuptools import setup
  File "C:\Users\villevai\AppData\Local\Programs\Python\Python310\lib\site-packages\setuptools\__init__.py", line 10, in <module>
    from setuptools.extern.six.moves import filter, map
  File "C:\Users\villevai\AppData\Local\Programs\Python\Python310\lib\site-packages\setuptools\extern\__init__.py", line 1, in <module>
    from pkg_resources.extern import VendorImporter
  File "C:\Users\villevai\AppData\Local\Programs\Python\Python310\lib\site-packages\pkg_resources\__init__.py", line 77, in <module>
    __import__('pkg_resources.extern.packaging.requirements')
  File "C:\Users\villevai\AppData\Local\Programs\Python\Python310\lib\site-packages\pkg_resources\_vendor\packaging\requirements.py", line 9, in <module>
    from pkg_resources.extern.pyparsing import stringStart, stringEnd, originalTextFor, ParseException
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 672, in _load_unlocked
  File "<frozen importlib._bootstrap>", line 632, in _load_backward_compatible
  File "C:\Users\villevai\AppData\Local\Programs\Python\Python310\lib\site-packages\pkg_resources\extern\__init__.py", line 43, in load_module
    __import__(extant)
  File "C:\Users\villevai\AppData\Local\Programs\Python\Python310\lib\site-packages\pkg_resources\_vendor\pyparsing.py", line 943, in <module>
    collections.MutableMapping.register(ParseResults)
AttributeError: module 'collections' has no attribute 'MutableMapping'
```
