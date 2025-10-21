def add_filter_greedy(quanty, b50=0, b20=0, b10=0, b5=0, b2=0, b1=0, c50=0, c20=0, c10=0, c5=0, c2=0, c1=0):
    coins = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    max_coins = [b50, b20, b10, b5, b2, b1, c50, c20, c10, c5, c2, c1]
    res = []
    used = [0] * len(coins)
    i = 0
    while quanty >= 0.01 and i < len(coins):
        if coins[i] <= quanty and max_coins[i] > 0:
            res.append(coins[i])
            quanty = round(quanty - coins[i], 2)
            max_coins[i] -= 1
            used[i]+=1
        else:
            i += 1

    return res, used


