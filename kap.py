def kaprekarNumbers(p, q):
    result = []
    for i in range(p, q):
        sq = i*i
        str_sq = str(sq)
        length = len(str_sq)
        if length == 1:
            if sq == i:
                result.append(i)
        elif length % 2 == 0:
            temp = int(str_sq[:int(length/2)])+int(str_sq[int(length/2):])
            if temp == i:
                result.append(i)
        elif length % 2 == 1:
            temp = int(str_sq[:int((length-1)/2)])+int(str_sq[int((length-1)/2):])
            if temp == i:
                result.append(i)
    return result



print(kaprekarNumbers(1, 99999))