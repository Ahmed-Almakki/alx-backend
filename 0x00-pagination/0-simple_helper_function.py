#!/usr/bin/env python3
""" A helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ takes two argument page and page_size
        Return:
            a tuple of size two containing start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
