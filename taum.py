def taumBday(b, w, bc, wc, z):
    if b > w:
        cost = min(b*bc+w*wc, b*bc+w*bc+w*z)
    if w > b:
        cost = min(w*wc+b*bc, w*wc+b*wc+b*z)
    if w == b:
        cost = min(w*wc+b*bc, b*bc+w*bc+w*z, w*wc+b*wc+b*z)
    print(cost)
    return cost


taumBday(3, 3, 1, 9, 2)