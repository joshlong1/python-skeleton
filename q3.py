# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question03(numNodes, edgeList):
    
    eList=[]

#Filter data for repeats/errors
    for i in range(len(edgeList)):
        a=sorted(edgeList[i].values())
        if a[0]!=a[1]:
            if a not in eList:
                eList.append(a)
            
    L=len(eList)
    N=numNodes-L

    nums=[]
    
    for i in range(L):
        nums.extend(eList[i])
          
    nums=np.sort(nums)
    ct=np.zeros(numNodes)

    for i in range(len(nums)):
        if (nums[i]==nums[i-1]):
            ct[int(nums[i]-1)]=1
            N+=1
            
    for i in range(numNodes):
        if (ct[i]!=0):
            N-=1

    answer = N
    return answer
