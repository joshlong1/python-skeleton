# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):
    
    if totalValue<=0:
        return 0
    
    minAlloc=[0]*(totalValue+1)
    
    for i in allowedAllocations:
        try: minAlloc[i]=1
        except: continue
        
    for k in range(min(allowedAllocations),totalValue+1):
        for j in [c for c in allowedAllocations if c <= k]:
            if minAlloc[k-j]>0:
                if minAlloc[k-j]+1<minAlloc[k] or minAlloc[k]==0:
                    minAlloc[k] = minAlloc[k-j]+1

    
    answer=minAlloc[totalValue]
    return answer
