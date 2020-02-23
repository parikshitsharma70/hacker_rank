def move_queen(n, updated_row, updated_col, r , c, obstacles):
    p = 0
    while True:
        r = updated_row(r)
        c = updated_col(c)
        key = (r - 1) * n + c
        if (c < 1 or c > n or r < 1 or r > n) or (key in obstacles):
            return p
        p += 1
    return p

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obs):
    obstacles = {}
    for b in obs:
        obstacles[(b[0] - 1) * n + b[1]] = None
    print(obstacles)
    p = 0
    dr = [-1, -1, -1, 0, 0 , 1 , 1,1]
    dc = [0, -1, 1, 1, -1 , 0 , 1,-1]
    
    for i in range(8):
        p += move_queen(n, (lambda r: r + dr[i]), (lambda c: c + dc[i] ), r_q, c_q, obstacles)
        print(p)
    return p

print(queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]))