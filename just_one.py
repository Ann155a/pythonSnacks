# returns true if this matrix is ​​made of all 0s except one cell with a 1.
def just_one(arr):
    ones = np.sum(arr == 1)
    values = np.all((arr == 1) | (arr == 0))
    return ones == 1 and values
