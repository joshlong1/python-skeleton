# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
     
    X='X'
    #rows=np.array(rows)
    S=[]
    for i in rows:
        for j in range(len(i)-numberMachines+1):
            nums=i[j:(j+numberMachines)]
            try:
                nums=map(int, nums)
                S.append(sum(nums))
            except:
                continue
            
    try:        
        answer =min(S)
    except:
        answer=0
    return answer

