import numpy as np

array = np.zeros(5)

a = np.full(10,6.1)

print(a)

b = np.array([1,2,5,7,12])

print(b[2])

print(np.arange(3,10))

print(np.linspace(0,1,11)) #Literally like Matlab

np.zeros((5,2))

twoarray = np.array([
                    [1,2,3],
                    [4,5,6],
                    [7,8,9]
                     ])
print(twoarray)

print(twoarray[:2,2])

np.random.seed(2)
print(np.random.randint(low=0, high=100, size=10))

u = np.array([1,2,4])
w = np.array([5,2,9])

print(u.dot(w))

def matrix_vector_multiplication(m, v):
    assert m.shape[1] == v.shape[0]
    res = np.zeros(m.shape[0])

    for i in range(m.shape[0]):
        res[i] = m[i].dot(v)
    return res
U = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

V = np.eye(3)
def matrix_matrix_multiplication(U,V):
    assert U.shape[1] == V.shape[0]

    num_rows = U.shape[0]
    num_cols = V.shape[1]

    result = np.zeros((num_rows,num_cols))
    for i in range(num_cols):
        vi = V[:,i]
        Uvi = matrix_vector_multiplication(U, vi)
        result[:,i] = Uvi
    return result

print(matrix_matrix_multiplication(U, V))

Vinv = np.linalg.inv(V)

print(Vinv == V)



