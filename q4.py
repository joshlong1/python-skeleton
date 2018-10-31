# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):

    answer=0
    for r in rows:
        window=[]
        if r.count("X")<=(len(r)-numberMachines):
            for j in r:
                if j=="X":
                    window=[]
                else:
                    window+=[int(j)]
                    if (len(window)==numberMachines):
                        ans=sum(window)
                        answer=ans if answer==0 else min(ans,answer)
                        window=window[1:]
                    
    return answer
