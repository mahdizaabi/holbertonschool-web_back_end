#!/usr/bin/env python3
"""Complex types - list of floats
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """[summary]

    Args:
        input_list ([type]): [argument]

    Returns:
        float: [description]
    """
    s: float = float(0)

    for i in input_list:
        s += i
    return s
