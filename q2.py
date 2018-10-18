# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question02(cashFlowIn, cashFlowOut):
    MaxIn=sum(cashFlowIn)

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

    Diff=0
    subIn=subIn[1:,lenIn]
    subOut=subOut[1:,lenOut]
    match=0
    cashFlowIn=np.array(cashFlowIn)
    Srt=np.min(cashFlowIn[np.nonzero(cashFlowIn)])
    
    for j in range(Srt):
        for i in range(MaxIn-1):
            match=subIn[i] and subOut[i]
            
            if (match==1):
                answer=Diff
                return answer
    
        subIn=subIn[1:]
        subIn=np.append(subIn,[0])
        Diff+=1
    
    
    answer=Srt
    return answer
