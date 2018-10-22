# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question06(numServers, targetServer, times):
  # modify and then return the variable below
    times=np.array(times)
    for node in times:
        for t in range(len(node)):
            dist=node[0]+node[t]
            if dist<times[t,0]:
                times[t,0]=dist
            
    print times
    answer = times[targetServer,0]
    return answer
