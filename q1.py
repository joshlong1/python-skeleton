# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
    answer=0
    if len(portfolios)<2:
        return 0
    portfolios=list(set(portfolios))
    portfolios=sorted(portfolios,reverse=True)
    bitLengths=[M.bit_length() for M in portfolios]
    L=bitLengths.count(bitLengths[0])
    if L<len(portfolios):
        for i in portfolios[:L]:
            for j in portfolios[L:]:
                a=i^j
                if a>answer:
                    answer=a
    else:
        for i in range(L-1):
            for j in range(i+1,L):
                a=portfolios[i]^portfolios[j]
                if a>answer:
                    answer=a

    return answer
