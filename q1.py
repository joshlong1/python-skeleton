# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
    
    xor=[]
    answer=0
    L=len(portfolios)

    for i in range(L):
        for j in range(i+1,L):
            a=portfolios[i]^portfolios[j]
            if a>answer:
                answer=a
          
    return answer
