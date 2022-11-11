# fixcollections

Python 3.10 broke compatibility with old versions of some libraries (some of them are very popular, like setuptools).

This provides a monkeypatch funcion that restores the compatibility shims [removed in Python 3.10](https://github.com/python/cpython/issues/81505)

Usage: 

```python
import fixcollections
fixcollections.monkeypatch()

from setuptools import setup
# etc etc
```
