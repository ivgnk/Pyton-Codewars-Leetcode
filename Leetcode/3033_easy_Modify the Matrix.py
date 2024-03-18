import numpy as np

# Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix called answer.
# Make answer equal to matrix, then replace each element
# with the value -1 with the maximum element in its respective column.
#
# Return the matrix answer.

def modifiedMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    a = np.array(matrix)
    ncol = len(a[0])
    for i in range(ncol):
        b = a[:,i]
        b[b==-1]=np.max(b)
        a[:, i]=b
    return a.tolist()


# print(modifiedMatrix([[1,2,3],[4,5,6],[7,8,9]]))
print(modifiedMatrix([[1,2,-1],[4,-1,6],[7,8,9]]))
