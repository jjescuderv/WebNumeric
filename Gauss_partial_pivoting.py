import numpy as np
import Back_substitution

def gauss_partial_pivoting(n, mat, vec):
    iteration = 0
    errors = []
    matrices = []

    values_A = list(map(float, mat))
    A = np.array(values_A).reshape(n, n)

    det = np.linalg.det(A)
    if(det == 0):
        errors.append("The matrix must be non singular")
        return errors

    values_b = list(map(float, vec))
    b = np.array(values_b).reshape(n, 1)

    # Augmented matrix
    M = np.concatenate((A, b), axis=1)
    matrices.append(np.copy(M))
    iteration += 1

    for i in range(0, n-1):
        col = M[i+1:n, i]
        grpos = np.argmax(np.absolute(col))
        gr = col[grpos]

        if gr>abs(M[i,i]):
            aux = np.copy(M[grpos+i+1, i:n+1])
            M[grpos+i+1, i:n+1] = M[i, i:n+1]
            M[i, i:n+1] = aux

        for j in range(i+1, n):
            if M[j,i]!=0:
                M[j,i:n+1] = np.subtract(M[j,i:n+1], np.divide(M[j,i], M[i,i])*M[i,i:n+1])

        matrices.append(np.copy(M))
        iteration += 1

    x = Back_substitution.back_subst(M, n)

    ans = [x, matrices, n]
    return ans