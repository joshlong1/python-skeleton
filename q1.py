# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
    

    answer=0
    
    answer=max([portfolios[i]^portfolios[j] for i in range(len(portfolios)) for j in range(i+1, len(portfolios))])

    return answer
