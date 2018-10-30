# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question06(numServers, targetServer, times):
  # modify and then return the variable below
    for node in times:
        if min(node)<times[targetServer][0]:
            for t in range(len(node)):
                dist=node[0]+node[t]
                if dist<times[t][0]:
                    times[t][0]=dist
            
    answer = times[targetServer][0]
    return answer
            
