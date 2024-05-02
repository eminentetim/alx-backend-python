from typing import Any, Optional, List

def safe_first_element(lst: List[Any]) -> Optional[Any]:
    """
    Returns the first element of a list if it exists, otherwise returns None.

    Args:
        lst (List[Any]): A list of elements of any type.

    Returns:
        Optional[Any]: The first element if the list is not empty, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
