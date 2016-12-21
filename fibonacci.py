def fibonacci (i):
    c = 2
    x = 0
    y = 1
    if i == 1:
        return [x]
    elif i == 2:
        return [x,y]
    else:
        f = [x, y]
        while c != i:
            z = x + y
            f.append(z)
            x = y
            y = z
            c += 1
        return f
