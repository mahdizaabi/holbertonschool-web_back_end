#!/usr/bin/env python3
"""function
"""


from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """[summary]

    Args:
        multiplier (float): [description]
    """

    def fnx(arg: float):
        return multiplier * arg
    return fnx
