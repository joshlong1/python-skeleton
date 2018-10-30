# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question06(numServers, targetServer, times):
  # modify and then return the variable below
    for node in times:
        for t in range(len(node)):
            dist=node[0]+node[t]
            times[t][0]=min(dist, times[t][0])
            
    answer = times[targetServer][0]
    return answer
            
