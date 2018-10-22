# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):
    if (totalValue==0):
        return 0
    answer=minAllocation(allowedAllocations,totalValue)
    return answer
    
def minAllocation(alloc,tot):
    res=tot
    for c in alloc:
        if (c<=tot):
            sub_res=minAllocation(alloc,tot-c)
            if sub_res+1<res:
                res=sub_res+1
    return res
