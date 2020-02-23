
from itertools import combinations

# def acmTeam(topic):
#     x=[sum(a=='1' or b=='1' for a,b in zip(a,b)) for a,b in combinations(topic,2)]
#     print(x)
#     m=max(x)
#     return m,sum(m==x for x in x)

def acmTeam(topic):
    r = []
    for a,b in combinations(topic, 2):
        count = 0
        for x,y in zip(a,b):
            if(x == '1' or y =='1'):
                count +=1
        r.append(count)
    return (max(r), r.count(max(r)))

print(acmTeam(['10101', '11100', '11010', '00101']))