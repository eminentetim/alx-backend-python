#!/usr/bin/env python3
'''Task 9's module.
'''
from typing import Any, Optional, List


def safe_first_element(lst: List[Any]) -> Optional[Any]:
    '''Computes the length of a list of sequences.
    '''
    if lst:
         return lst[0]
    else:
         return None

