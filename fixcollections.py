""" This must be imported early, e.g. before setuptools 

It restores compatibility shims removed by https://github.com/python/cpython/issues/81505

License: MIT

"""
try:
    # Python < 3.10
    from collections import MutableMapping
except:
    # Python >= 3.10
    import collections.abc
    import collections
    collections.MutableMapping = collections.abc.MutableMapping
    collections.Iterable = collections.abc.Iterable