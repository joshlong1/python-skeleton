# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):
    
    if totalValue<=0:
        return 0
    
    allowedAllocations=list(set(allowedAllocations))
    minAlloc=[10*totalValue]*(totalValue+1)
    minAlloc[0]=0
        
    for k in range(min(allowedAllocations),totalValue+1):
        for j in [c for c in allowedAllocations if c <= k]:
                if minAlloc[k-j]+1<minAlloc[k]:
                    minAlloc[k] = minAlloc[k-j]+1

    if minAlloc[totalValue]>9*totalValue:
        return 0
    else:
        answer=minAlloc[totalValue]
    
    return answer
