import pytest
from solution import (
    mergeUntilMedian,
    BinarySearchSolution,
)

def test_example1_merge():
    nums1 = [1, 3]
    nums2 = [2]
    assert mergeUntilMedian(nums1, nums2) == 2.0

def test_example1_binary():
    nums1 = [1, 3]
    nums2 = [2]
    assert BinarySearchSolution(nums1, nums2) == 2.0

def test_example2_merge():
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert mergeUntilMedian(nums1, nums2) == 2.5

def test_example2_binary():
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert BinarySearchSolution(nums1, nums2) == 2.5

def test_single_merge():
    nums1 = []
    nums2 = [1]
    assert mergeUntilMedian(nums1, nums2) == 1.0

def test_single_binary():
    nums1 = []
    nums2 = [1]
    assert BinarySearchSolution(nums1, nums2) == 1.0

def test_odd_length_merge():
    nums1 = [0, 0]
    nums2 = [0, 0, 0]
    assert mergeUntilMedian(nums1, nums2) == 0.0

def test_odd_length_binary():
    nums1 = [0, 0]
    nums2 = [0, 0, 0]
    assert BinarySearchSolution(nums1, nums2) == 0.0
