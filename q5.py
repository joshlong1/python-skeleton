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
                minAlloc[k] = min(minAlloc[k-j]+1, minAlloc[k]) 

    answer=0 if minAlloc[totalValue]>9*totalValue else minAlloc[totalValue]
    
    return answer
