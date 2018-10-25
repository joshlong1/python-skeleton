# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
    
    X='X'
    answer="inf"
    for i in rows:
        for j in range(len(i)-numberMachines+1):
            nums=i[j:(j+numberMachines)]
            if X in nums:
                continue
            t=sum(nums)
            if t<answer: 
                    answer=t
    if answer=="inf": answer=0
    return answer
