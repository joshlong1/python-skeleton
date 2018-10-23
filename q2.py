# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question02(cashFlowIn, cashFlowOut):

    setIn=[sum(x) for x in powerset(cashFlowIn)]
    setOut=[sum(y) for y in powerset(cashFlowOut)]
    answer=1000*100
 
    for i in setIn:
        for j in setOut:
            diff=abs(i-j)
            if i+j==0:
                continue
            if diff<answer:
                answer=diff
                if answer==0:
                    return answer
    return answer
    
def powerset(seq):

    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item
        
