from typing import TypeVar, Dict, Optional

# Define a type variable that can represent any type
T = TypeVar('T')

def safely_get_value(dct: Dict[str, T], key: str, default: Optional[T] = None) -> Optional[T]:
    """
    Safely gets the value from a dictionary given a key.
    Returns a default value if the key does not exist.

    Args:
        dct (Dict[str, T]): A dictionary with string keys and values of type T.
        key (str): The key to look for in the dictionary.
        default (Optional[T]): The default value to return if the key is not found.

    Returns:
        Optional[T]: The value corresponding to the key if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

