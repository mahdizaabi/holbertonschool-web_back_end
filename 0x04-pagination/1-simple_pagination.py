#!/usr/bin/env python3
"""
1-simple_pagination.py
"""

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Paginate the Dataset and return the appropriate page
            of the dataset
        """

        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        if page_size * page > len(self.dataset()):
            return []

        indexRange = index_range(page, page_size)
        DataSet = self.dataset()
        return(DataSet[indexRange[0]:indexRange[1]])
