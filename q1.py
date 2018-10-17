# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
    Max=2**16
    pairs=[]
    while(Max>0):
        Max-=1
        for i in portfolios:
            p=i^Max
            pairs.append(p)
        for x in pairs:
            for y in portfolios:
                if x==y:
                    answer = Max
                    print(x)
                    print(x^Max)
                    return answer
