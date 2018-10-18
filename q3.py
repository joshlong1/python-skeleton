# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question03(numNodes, edgeList):
    
    N=numNodes-len(edgeList)
    nums=[]
    for i in edgeList:
        for j in i:
            nums.append(j)
            
    nums=np.sort(nums)
    ct=np.zeros(numNodes)
    
    for i in range(len(nums)):
        if (nums[i]==nums[i-1]):
            ct[nums[i]-1]+=1
            N+=1
            
    for i in range(len(ct)):
        if (ct[i]!=0):
            N-=1
            print(N)
            
    print(nums)
    print(ct)



    answer = N
    return answer
