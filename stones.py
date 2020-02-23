from itertools import combinations

def stones(n, a, b):
    print(" ".join(map(str, sorted({x*a+(n-1-x)*b for x in range(n)}))))


stones(3, 1, 2)