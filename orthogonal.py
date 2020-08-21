import numpy as np 

def ProjectionMatrix1D(b):
    p = (b @ b.T)/(b.T @ b)
    return p 

def Project1D(b,x):
    p = ProjectionMatrix1D(b) @ x
    return p

def ProjectionMatrixGenral(B):
    P = B @ np.linalg.inv(B.T @ B) @ (B.T)
    return P

def ProjectionGenral(B,x):
    p= ProjectionMatrixGenral(B) @ x
    return p


# ------------------------------------------------

x1 = np.array([1,2]).reshape(-1,1)
b1= np.array([2,1]).reshape(-1,1)
proj1 = Project1D(b1,x1)
print(proj1)

x2 =np.array([6,0,0]).reshape(-1,1)
B = np.array([[1,0],[1,1],[1,2]]).reshape(-1,2)
proj2 = ProjectionGenral(B,x2)
print(proj2)
m = ProjectionMatrixGenral(B)
print(m)