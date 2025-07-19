#!/usr/bin/env python3
"""
Utils module
"""
from typing import Mapping, Any, Sequence, Union
import requests


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """
    Access a nested map using a sequence of keys.
    """
    current = nested_map
    for key in path:
        if isinstance(current, Mapping):
            current = current[key]
        else:
            raise TypeError(f"{type(current).__name__} object is not subscriptable")
    return current


def memoize(method):
    """
    Decorator to cache method output
    """
    attr_name = "_{}".format(method.__name__)

    @property
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)

    return wrapper


