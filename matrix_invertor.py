from matrix import Matrix
from non_square_matrix import NonSquareMatrix


class MatrixInverter:
    @staticmethod
    def invert_bordering(matrix):
        if matrix.size == 1:
            return Matrix([[1/matrix.data[0][0]]])

        submatr_inv = NonSquareMatrix(MatrixInverter.invert_bordering(matrix[:-1]))
        V = NonSquareMatrix(matrix).get_submatrix(slice(-1, None, 1), slice(-1))
        U = NonSquareMatrix(matrix).get_submatrix(slice(-1), slice(-1, None, 1))
        alpha = matrix.data[-1][-1] - (V * submatr_inv * U).data[0][0]
        r = submatr_inv * U * (-1 / alpha)
        q = V * submatr_inv * (-1 / alpha)
        B_inv = Matrix((submatr_inv - (submatr_inv*U)*q).data)
        A_inv = B_inv.add_border(q, r, 1/alpha)
        return A_inv

    @staticmethod
    def invert_cells(matrix):
        if matrix.size == 1:
            return Matrix([[1/matrix.data[0][0]]])
        t = matrix.size
        p = int(t/2)
        ns_matrix = NonSquareMatrix(matrix)
        A = ns_matrix.get_submatrix(slice(p), slice(p))
        B = ns_matrix.get_submatrix(slice(p), slice(p, t))
        C = ns_matrix.get_submatrix(slice(p, t), slice(p))
        D = ns_matrix.get_submatrix(slice(p, t), slice(p, t))
        D_inv = NonSquareMatrix(MatrixInverter.invert_cells(Matrix(D.data)).data)
        X = B*D_inv
        Y = D_inv*C
        K = NonSquareMatrix(MatrixInverter.invert_cells(Matrix((A-X*C).data)).data)
        L = K*X*(-1)
        M = Y*K*(-1)
        N = D_inv - Y*L
        return K.merge(L, M, N)
