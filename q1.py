# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
    
    if len(portfolios)<2 or max(portfolios)==0:
        answer=0
        return answer
    answer=max([portfolios[a]^portfolios[b] for a in range(len(portfolios)) for b in range(a+1, len(portfolios))])

    return answer
