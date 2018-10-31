# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
    answer=0
    portfolios=list(set(portfolios))
    L=len(portfolios)
    for i in range(L-1):
        for j in range(i+1,L):
            answer=max(portfolios[i]^portfolios[j],answer)

    return answer
