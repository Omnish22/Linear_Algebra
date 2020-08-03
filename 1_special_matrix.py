import numpy as np 

def singular(A):
    # first row 
    if A[0,0] == 0:
        A[0] = A[0] + A[1]
    if A[0,0] == 0:
        A[0] = A[0] + A[2]
    if A[0,0] == 0:
        A[0] = A[0] + A[3]
    if A[0,0] == 0:
        return f'{A}\n matrix is singular'
    A[0] = A[0] / A[0,0] 


    # second row
    A[1] = A[1] - A[1,0] * A[0]

    if A[1,1] == 0 :
        A[1] = A[1] + A[2]
    if A[1,1] == 0:
        A[1] = A[1] + A[3] 
    if A[1,1] == 0:
        return f'{A}\n matrix is singular'
    A[1] = A[1] / A[1,1]
    A[0] = A[0] - A[0,1] * A[1]

    # third 
    if A[2,2] == 0:
        A[2] = A[2] + A[3]
    if A[2,2] == 0:
        return f'{A}\n matrix is singular'

    A[2] = A[2] - A[2,0] * A[0]
    A[2] = A[2] - A[2,1] * A[1]
 
    A[2] = A[2] / A[2,2]

    A[1]=A[1] - A[1,2] * A[2] 
    A[0]=A[0] - A[0,2] * A[2] 

    # fourth 
    if A[3,3] == 0:
        return f'{A}\n matrix is singular'
    
    A[3] = A[3] - A[3,0] * A[0]
    A[3] = A[3] - A[3,1] * A[1]
    A[3] = A[3] - A[3,2] * A[2]

    A[3] = A[3] / A[3,3] 

    A[0]=A[0] - A[0,3] * A[3] 
    A[1]=A[1] - A[1,3] * A[3] 
    A[2]=A[2] - A[2,3] * A[3] 

    return A



A = np.array([
        [0, 7, -5, 3],
        [2, 8, 0, 4],
        [3, 12, 0, 5],
        [1, 3, 1, 8]
    ], dtype=np.float_)


print(singular(A))

from datetime import datetime 
print(datetime.now())

print(set([3,4,0]))