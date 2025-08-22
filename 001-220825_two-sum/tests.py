import pytest
from solution import twoSumHash, twoSumPointers

def test_basic_case():
    assert sorted(twoSumHash([2,7,11,15], 9)) == [0,1]
    assert sorted(twoSumPointers([2,7,11,15], 9)) == [0,1]

def test_duplicates():
    assert sorted(twoSumHash([3,3], 6)) == [0,1]
    assert sorted(twoSumPointers([3,3], 6)) == [0,1]

def test_negatives():
    assert sorted(twoSumHash([-1,-2,-3,-4,-5], -8)) == [2,4]
    assert sorted(twoSumPointers([-1,-2,-3,-4,-5], -8)) == [2,4]