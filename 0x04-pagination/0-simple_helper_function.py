#!/usr/bin/env python3
"""
Main file
"""


def index_range(page, page_size):
    """return list parameters for pagination"""

    previousPagesContent = (page - 1) * page_size

    return(previousPagesContent, previousPagesContent + page_size)
