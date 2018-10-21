# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question02(cashFlowIn, cashFlowOut):
    MaxIn=max(sum(cashFlowIn),sum(cashFlowOut))

    lenIn=len(cashFlowIn)
    lenOut=len(cashFlowOut)

    
    subIn=[]
    subOut=[]
    
    for i in range(MaxIn+1):
        subIn.append([0])
        for j in range(lenIn):
            subIn[i].append(0)
    subIn[0]=[1 for x in range(lenIn+1)]
            
    subIn=np.array(subIn)
    for j in range(1,lenIn+1):
        for i in range(1,MaxIn+1):
            if (i<cashFlowIn[j-1]):
                subIn[i,j]=subIn[i,j-1]
            if (i>=cashFlowIn[j-1]):
                subIn[i,j]=subIn[i-cashFlowIn[j-1],j-1] or subIn[i,j-1]
                           
    for i in range(MaxIn+1):
        subOut.append([0])
        for j in range(lenOut):
            subOut[i].append(0)
    subOut[0]=[1 for x in range(lenOut+1)]
            
    subOut=np.array(subOut)
    for j in range(1,lenOut+1):
        for i in range(1,MaxIn+1):
            if (i<cashFlowOut[j-1]):
                subOut[i,j]=subOut[i,j-1]
            if (i>=cashFlowOut[j-1]):
                subOut[i,j]=subOut[i-cashFlowOut[j-1],j-1] or subOut[i,j-1]


    subIn=subIn[1:,lenIn]
    subOut=subOut[1:,lenOut]
    match=0
    answer=min(cashFlowIn+cashFlowOut)
    
    for i in range(len(subIn)):
        for j in range(len(subOut)):
        
            if (subIn[i] and subOut[j]):
                a=abs(i-j)
                if a<answer:
                    answer=a
    
    return answer
