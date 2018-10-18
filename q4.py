# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
    
    rows=np.array(rows)
    rows[rows=='X']=0
    rows=rows.astype(int)
    S=[]
    for i in rows:
        for j in range(len(i)-numberMachines+1):
            nums=i[j:(j+numberMachines)]
            C=np.count_nonzero(nums)
            if C==numberMachines:  
                S.append(sum(nums))
    if len(S)>0:        
        answer =min(S)
    else:
        answer=0
    return answer

