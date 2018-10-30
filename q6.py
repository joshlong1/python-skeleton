# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question06(numServers, targetServer, times):
    D=[0]+["inf"]*(numServers-1)
    v=range(numServers)
    visited=[]
    j=0
    while len(v)>0:
        visit = D.index(sorted(D)[j])
        j+=1
        v.remove(visit)
        
        for i in v:
            D[i]=min(D[visit]+times[visit][i],D[i])

                
    answer=D[targetServer]
    return answer
            
