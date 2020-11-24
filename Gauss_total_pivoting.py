import numpy as np
import Back_substitution

def gauss_total_pivoting(n, mat, vec):
    order = [[0,0]]
    iteration = 0
    errors = []
    matrices = []

    values_A = list(map(float, mat))
    A = np.array(values_A).reshape(n, n)

    det = np.linalg.det(A)
    if(det == 0):
        errors.append(A)
        errors.append("The matrix must be non singular")
        return errors

    values_b = list(map(float, vec))
    b = np.array(values_b).reshape(n, 1)

    # Augmented matrix
    M = np.concatenate((A, b), axis=1)
    matrices.append(np.copy(M))
    iteration += 1

    for i in range(0, n-1):
        grpos = np.unravel_index(np.argmax(np.absolute(M[i:n,i:n])), np.shape(M[i:n,i:n]))

        if grpos[1]+i != i:
            order = np.append(order, [[i, grpos[1]+i]], axis=0)
            aux = np.copy(M[:, grpos[1]+i])
            M[:, grpos[1]+i] = M[:, i]
            M[:, i] = aux

        if grpos[0]+i != i:
            aux = np.copy(M[grpos[0]+i, i:n+1])
            M[grpos[0]+i, i:n+1] = M[i, i:n+1]
            M[i, i:n+1] = aux

        for j in range(i+1, n):
            if M[j,i]!=0:
                M[j,i:n+1] = np.subtract(M[j,i:n+1], np.divide(M[j,i], M[i,i])*M[i,i:n+1])

        matrices.append(np.copy(M))
        iteration += 1

    x = Back_substitution.back_subst(M, n)
    for swap in range(np.size(order, 0), 1, -1):
        aux = np.copy(x[order[swap-1, 0]])
        x[order[swap-1, 0]] = x[order[swap-1, 1]]
        x[order[swap-1, 1]] = aux

    ans = [x, matrices, n]
    return ans
