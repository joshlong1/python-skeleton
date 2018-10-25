# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
    
    X='X'
    answer="inf"
    for i in rows:
        for j in range(len(i)-numberMachines+1):
            nums=i[j:(j+numberMachines)]
            try:
                nums=sum(nums)
                if nums<answer: 
                    answer=nums
            except:
                continue
                
    if answer=="inf":
        answer=0

    return answer
