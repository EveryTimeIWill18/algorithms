#!/Users/williamrobertmurphy/anaconda3/envs/env36/bin/python3.6
import os
import sys
import abc
import re
import math
import collections
import numpy as np
import pandas as pd

def bubble_sort(l):
    """
    bubble sort algorithm:
    Time Complexity: O(n^2)
    """
    j = 0
    for i in range(len(l)-1):
        j = i+1
        while j < len(l):
            if l[i] > l[j]:
                temp = l[j]
                l[j] = l[i]
                l[i] = temp
            j += 1
    return l

def merge(L: list, R: list, A: list):
    nL = len(L)
    nR = len(R)
    i = 0
    j = 0
    k = 0
    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1
    return A

def merge_sort(l):
    """
    merge sort algorithm
    Time Complexity: O(nlogn)
    """
    n = len(l)
    if n < 2:
        return
    mid = math.floor(n/2)
    left = [i for i in l[:mid]]
    right = [i for i in l[mid:]]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, l)
    return merge(left, right, l)
