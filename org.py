def organizingContainers(container):
    storage = []
    balls = []
    for i in range(0, len(container)):
        storage.append(sum(container[i]))
        temp = 0
        for j in range(0, len(container)):
            temp += container[j][i]
        balls.append(temp)
    storage.sort()
    balls.sort()
    if storage == balls:
        return "Possible"
    else:
        return "Impossible"


print(organizingContainers([[1, 3, 1], [2, 1, 2], [3, 3, 3]]))