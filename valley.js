function queensAttack(n, k, r_q, c_q, obstacles) {
    var obs = {}
    for(var el in obstacles){
        var temp = obstacles[el]
        obs[(temp[0]-1)*n + temp[1]] = 0
    }
    console.log(obs)
}

queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]])