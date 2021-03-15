#!/usr/bin/env python3
"""duck type an iterable object
"""


from typing import List, Union, Tuple, Callable, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """[summary]

    Args:
        lst (Sequence): [description]

    Returns:
        Tuple[Sequence, int]: [description]
    """
    return [(i, len(i)) for i in lst]
