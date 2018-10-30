# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
    
    X='X'
    answer=0
    for i in rows:
        if len(i)>=numberMachines:  
            for j in range(len(i)-numberMachines+1):
                nums=i[j:(j+numberMachines)]
                try:
                    nums=sum(map(int, nums))
                    if nums<answer or answer==0: 
                        answer=nums
                except:
                    continue

    return answer
