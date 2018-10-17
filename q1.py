# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
    x=range(len(portfolios))
    xor=[]

    for i in x:  
        for j in x:
                if i!=j:
                    a=portfolios[i]^portfolios[j]
                    xor.append(a)
    answer=max(xor)
    return answer
