import math
import itertools

def encryption(s):
    s = s.replace(" ", "")
    r = math.floor(math.sqrt(len(s)))
    c = math.ceil(math.sqrt(len(s)))
    arr = [s[i:i+c] for i in range(0, len(s), c)]
    tup = list(filter(None, pair) for pair in itertools.zip_longest(*arr))
    resArr = []
    for t in tup:
        tempStr = "".join(t)
        resArr.append(tempStr)
    resStr = " ".join(resArr)
    return resStr

print(encryption('feedthedog'))
