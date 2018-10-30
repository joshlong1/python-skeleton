# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question06(numServers, targetServer, times):
    D=[0]+["inf"]*(numServers-1)
    v=range(numServers)
    visited=[]
    j=0
    print D
    while len(v)>0:
        visit = D.index(sorted(D)[j])
        j+=1
        v.remove(visit)
        
        for i in v:
            dist=D[visit]+times[visit][i]
            if dist<D[i]:
                D[i]=dist

                
    answer=D[targetServer]
    return answer
            
