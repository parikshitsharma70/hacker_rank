from itertools import combinations

# x=[sum(a=='1' or b=='1' for a,b in zip(a,b)) for a,b in combinations(topic,2)]

def func(topic):
    print(list(combinations(topic, 2)))

func(['10101', '11100', '11010', '00101'])
