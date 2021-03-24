#!/usr/bin/env python3
"""
Main file
"""


def index_range(page, page_size):
    """return the index range of the data List to pgainate
        Current Index = nombre of previous pages * page_size
        last index on the current page = Current Index + page_size
    """

    currentListIndex = (page - 1) * page_size

    return(currentListIndex, currentListIndex + page_size)
