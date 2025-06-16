def greedy(num):
    coins = [50,20,10,5,2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    res = []
    i = 0
    while num >= 1e-2:
        if coins[i] >= num:
            i+=1
        else:
            res.append(coins[i])
            num -= coins[i]
    return res
