# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
    
    xor=[]
    answer=0
    for i in range(len(portfolios)):
        b=portfolios[0]
        portfolios.remove(b)
        for j in portfolios:
            a=b^j
            if a>answer:
                answer=a
          
    return answer
