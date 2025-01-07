# returns a square matrix with diagonal blocks. k = size of blocks
def block_k(n, k):
    arr = np.zeros((n, n))
    for i in range(0, n):
        arr[i:i+k, i:i+k] = 1
    return arr
