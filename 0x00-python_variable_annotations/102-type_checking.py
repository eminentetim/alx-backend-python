from typing import List

def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Takes a list and returns a list with each item repeated 'factor' times.
    
    Args:
        lst (List[int]): List of integers to be zoomed.
        factor (int): The number of times each item should be repeated.
    
    Returns:
        List[int]: The zoomed-in list.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


# Correcting the input to use a list of integers
array = [12, 72, 91]

# Using an integer factor for correct type matching
zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Corrected the second argument to be an integer
