# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
    
    xor=[]

    for i in portfolios:  
        for j in portfolios:
            a=i^j
            xor.append(a)
            
    answer=max(xor)
    return answer
