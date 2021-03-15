#!/usr/bin/env python3
"""Complex types - mixed list
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """[summary]

    Args:
        mxd_lst (List): List of integers and floats
    Returns:
        float: Sum of the list
    """
    s: float = float(0)
    for i in mxd_lst:
        s += i
    return float(s)
