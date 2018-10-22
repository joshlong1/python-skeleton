# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):
    minAlloc = [0]*(totalValue+1)
    
    for i in allowedAllocations:
        try: minAlloc[i]=1
        except: continue
        
    for k in range(totalValue+1):
        #allocCount = k
        for j in [c for c in allowedAllocations if c <= k]:
            if minAlloc[k-j]+1<=k and minAlloc[k-j]>0:
                minAlloc[k] = minAlloc[k-j]+1
  
    answer=int(minAlloc[totalValue])
    return answer
