#!/bin/python3

import math
import os
import random
import re
import sys

#
#  the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        hashes = "#" * i
        print(spaces + hashes)
