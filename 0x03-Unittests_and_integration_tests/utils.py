from typing import Mapping, Any, Sequence
import requests


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """
    Access a nested map using a sequence of keys.

    Args:
        nested_map (Mapping): A nested dictionary.
        path (Sequence): A sequence of keys to access the nested values.

    Returns:
        Any: The value found at the end of the path.

    Raises:
        KeyError: If a key in the path is not present in the nested map.
    """
    current = nested_map
    for key in path:
        try:
            current = current[key]
        except KeyError:
            raise
        except TypeError:
            # إذا current ماشي Mapping، نرفع KeyError باش يتوافق مع التستات
            raise KeyError(key)
    return current


def get_json(url: str) -> dict:
    """
    Fetch JSON content from a given URL.

    Args:
        url (str): The URL to fetch the JSON from.

    Returns:
        dict: The JSON content.
    """
    response = requests.get(url)
    return response.json()


def memoize(method):
    """
    Memoization decorator. Caches the result of a method.

    Args:
        method: The method to cache.

    Returns:
        Cached function result.
    """
    attr_name = f"_{method.__name__}"

    @property
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)

    return wrapper
