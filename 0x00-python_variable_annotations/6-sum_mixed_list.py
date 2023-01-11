#!/usr/bin/env python3
"""A type-annotation of sum_mixed_list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return sum of list."""
    return float(sum(mxd_lst))
