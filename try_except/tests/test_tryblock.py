#
# Unit tests for tryblock.py
#

import pytest
from tryblock import func


def test_func_raise():
    val = func(True)
    assert val == 67

def test_func_no_raise():
    val = func(False)
    assert val == 65
