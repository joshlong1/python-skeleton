# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):

    answer=0
    for r in rows:
        window=[]
        for j in range(len(r)):
            if r[j]=="X":
                window=[]
            else:
                window+=[int(r[j])]
                if (len(window)==numberMachines):
                    ans=sum(window)
                    answer=ans if answer==0 else min(ans,answer)
                    window=window[1:]
                    
    return answer
