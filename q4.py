# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
    X='X'
    answer=0
    for r in rows:
        window=[]
        for j in range(len(r)):
            if r[j]==X:
                window=[]
            else:
                window+=[int(r[j])]
                if len(window)==numberMachines:
                    ans=sum(window)
                    if ans<answer or answer==0: 
                        answer=ans
                    window=window[1:]
                    
    return answer
