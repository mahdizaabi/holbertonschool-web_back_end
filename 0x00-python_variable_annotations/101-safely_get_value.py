#!/usr/bin/env python3
"""More involved type annotations
"""


from typing import Union, Tuple, TypeVar, Sequence, Any, Mapping


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None])\
                     -> Union[Any, TypeVar('T')]:
    """ function safely_get_value """
    if key in dct:
        return dct[key]
    else:
        return default
