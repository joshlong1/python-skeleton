# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
    
    answer = 0
    for i in range(17)[::-1]:
        answer <<= 1
        prefixes = {num >> i for num in portfolios}
        answer += any(answer^1 ^ p in prefixes for p in prefixes)
    return answer
