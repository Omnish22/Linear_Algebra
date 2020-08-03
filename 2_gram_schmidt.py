import numpy as np 

def gsbasis(A):
    ''' this function will take a matix of vectors and output a matix whose columns are
    orthonormal vectors '''
    small_number= 1e-14
    # copy the input matrix    
    B= np.array(A,dtype= np.float_)
    print(f'shape of matrix {B.shape[1]}')

    for i in range(B.shape[1]): # i is for current columns
        for j in range(i): # j is for perivous columns
            B[:,i] = B[:,i] - np.dot(B[:,j],B[:,i]) * B[:,j]

        if np.sqrt((np.dot(B[:,i],B[:,i]))) > small_number:  # normalize the column and 
            B[:,i] = B[:,i] / np.sqrt((np.dot(B[:,i],B[:,i])))  # save it to B
        else:
            B[:,i] = np.zeros_like(B[:,i])                                                         
    return B








V = np.array([[1,0,2,6],
              [0,1,8,2],
              [2,8,3,1],
              [1,-6,2,3]], dtype=np.float_)

print('\n')
print("V")
print(gsbasis(V))



A = np.array([[3,2,3],
              [2,5,-1],
              [2,4,8],
              [12,2,1]], dtype=np.float_)

# what happens when we have one vector that is a
#  linear combination of the others.
C = np.array([[1,0,2],
              [0,1,-3],
              [1,0,2]], dtype=np.float_)

print('\n')
print("C")
print(gsbasis(C))