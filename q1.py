# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
        result = 0
        for i in reversed(xrange(16)):
            result <<= 1
            prefixes = set()
            for n in portfolios:
                prefix.add(n >> i)
            for p in prefix:
                if (result | 1) ^ p in prefix:
                    result += 1
                    break

        return result
