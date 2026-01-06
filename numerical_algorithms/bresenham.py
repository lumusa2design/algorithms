def bresenham_algorithm(x1, y1, x2, y2):
    dx = (x2 - x1)
    dy = (y2 - y1)
    
    if  dy >= 0:
        inc_yi=1
    else:
        dy = -dy
        inc_yi=-1
    if dx >= 0:
        inc_xi=1
    else:
        dx = -dx
        inc_xi=-1
    if dx >= dy:
        inc_y_r = 0
        inc_x_r = inc_xi
    else:
        inc_y_r = inc_yi
        inc_x_r = 0
        dx, dy = dy, dx
    X = x1
    Y = y1
    aVR = 2*dy
    av = aVR - dx
    avL = av - dx
    points = []
    for _ in range(dx + 1):
        points.append((X, Y))
        if av >= 0:
            X += inc_xi
            Y += inc_yi
            av += avL
        else:
            X += inc_x_r
            Y += inc_y_r
            av += aVR