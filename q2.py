# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question02(cashFlowIn, cashFlowOut):

    setIn=list({sum(x) for x in powerset(cashFlowIn)})
    setOut=list({sum(y) for y in powerset(cashFlowOut)})
    answer=1000*100
 
    diff={abs(i-j) for i in setIn for j in setOut if i+j!=0}
    answer=min(diff)

            
    return answer
    
def powerset(seq):

    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item
        
