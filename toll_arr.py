#CHECK IF 2 ARRAYS ARE CLOSE WITHIN THE TOLERANCE
def toll(arrx, arry, eps = 1e-6):
    return np.all(np.abs(arrx - arry) < eps)
