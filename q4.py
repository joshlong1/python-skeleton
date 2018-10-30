# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
    
    X='X'
    sums=[sum(i[j:(j+numberMachines)]) for i in rows for j in range(len(i)-numberMachines+1) if X not in i[j:(j+numberMachines)]]
    if sums==[]:
        return 0
    answer=min(sums)
    
    return answer
