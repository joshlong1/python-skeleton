# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question03(numNodes, edgeList):

    eList=[]
    eCont=[]
    nodes=range(1,numNodes+1)
    score=0

    for i in range(len(edgeList)):
        a=sorted(edgeList[i].values())
        if a[0]!=a[1]:
            if a not in eList:
                eList.append(a)
                eCont.extend(a)
    for i in nodes:
        if len(eCont)==0:
            answer=numNodes+score
            return answer
        
        Rem=max(eCont,key=eCont.count)
        score-=2
        eCont=[]
        eList=[edge for edge in eList if Rem not in edge]
        eCont=sum(eList,[])
                
                  
    answer=0
        
    return answer
