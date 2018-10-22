# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):
    
    if totalValue<=0:
        return 0
    
    minAlloc=np.zeros(totalValue+1)
    allowedAllocations=sorted(allowedAllocations,reverse=1)
    
    for i in allowedAllocations:
        try: minAlloc[i]=1
        except: continue
    
    if minAlloc[totalValue]==1: return 1
        
    for k in range(allowedAllocations[-1],totalValue+1):
        for j in allowedAllocations:
            if k-j>0:
                a=minAlloc[k-j]
                if 1<a+1<minAlloc[k] or minAlloc[k]==0:
                    minAlloc[k] = a+1
                    if minAlloc[totalValue]==2:return 2

    
    answer=int(minAlloc[totalValue])
    return answer
