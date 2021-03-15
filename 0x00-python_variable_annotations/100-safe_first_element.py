#!/usr/bin/env python3
"""Duck typing - first element of a sequence
"""


from typing import List, Union, Tuple, Callable, Iterable, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """[summary]

    Args:
        lst ([type]): [description]

    Returns:
        [type]: [description]
    """
    if lst:
        return lst[0]
    else:
        return None
