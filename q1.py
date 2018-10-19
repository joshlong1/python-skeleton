# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
    
    xor=[]
    answer=0

    for i in portfolios:  
        for j in portfolios:
            a=i^j
            if a>answer:
                answer=a
          
    return answer
