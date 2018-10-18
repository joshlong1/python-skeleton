# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
    

    S=[]
    for i in rows:
        i=np.array(i)
        i[i=='X']=0
        i=i.astype(int)
        for j in range(len(i)-numberMachines+1):
            nums=i[j:(j+numberMachines)]
            C=np.count_nonzero(nums)
            if C==numberMachines:  
                S.append(sum(nums))
    try:       
        answer =min(S)
    except:
        answer=0
    return answer


