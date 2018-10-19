# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question03(numNodes, edgeList):
    
    L=len(edgeList)
    N=numNodes-L
    nums=np.zeros(2*L)
    
    for i in range(L):
            nums[2*i]=int(edgeList[i].get('edgeA'))
            nums[2*i+1]=int(edgeList[i].get('edgeB'))
          
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
