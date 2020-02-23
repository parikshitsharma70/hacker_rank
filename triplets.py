from itertools import combinations

def beautifulTriplets(d, arr):
    bt = 0
    for i in arr:
        print(i)
        if (i+d) in arr and (i+d)+d in arr:
            bt += 1
    return bt

print(beautifulTriplets(3, [1, 2, 4, 5, 7, 8, 10]))