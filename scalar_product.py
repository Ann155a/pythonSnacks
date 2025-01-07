# Implement scalar product without packages
def prod_scalare_np(lstx, lsty):
    somma = sum([x * y for x, y in zip(lstx, lsty)])
    return somma
