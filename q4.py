# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
    
    rows=np.array(rows)
    S=[]
    for i in rows:
        for j in range(len(i)-numberMachines+1):
            nums=i[j:(j+numberMachines)]
            try:
                nums=nums.astype(int)
                S.append(sum(nums))
            except:
                continue
            
    try:        
        answer =min(S)
    except:
        answer=0
    return answer

