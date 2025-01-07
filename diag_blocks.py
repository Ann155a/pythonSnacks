# returns a square matrix with diagonal blocks.
def block_diag(n):
    arr = np.zeros((n, n))
    for i in range(0, n-1):
        arr[i:i+2, i:i+2] = 1
    return arr
