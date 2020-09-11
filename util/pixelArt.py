# avatar for the Assistant

def pikachu():
    # palette
    b = blue = (29, 39, 86)
    y = yellow = (255, 255, 0)
    g = gold = (255, 162, 0)
    m = marrom = (182, 76, 38)
    r = red = (255, 0, 55)
    d = dark = (0, 0, 0)

    avatar = [
        d, b, b, d, d, d, d, b,
        d, d, y, g, d, d, d, g,
        d, d, d, y, y, y, y, g,
        g, g, d, y, d, y, y, d,
        g, g, d, r, y, y, y, g,
        d, g, d, y, g, g, g, d,
        d, g, y, g, y, g, y, d,
        d, d, y, g, m, m, g, d
    ]
    return avatar


def kirby():
    # palette
    p = pink = (255, 101, 165)
    u = purple = (136, 13, 83)
    r = red = (255, 0, 55)
    d = dark = (0, 0, 0)
    w = white = (255, 255, 255)

    avatar = [
        d, d, d, d, d, d, d, d,
        d, d, p, p, p, p, d, d,
        d, p, p, w, p, w, p, d,
        p, p, p, d, p, d, p, p,
        p, p, r, p, p, p, r, p,
        u, u, p, p, u, p, p, u,
        r, r, r, p, p, p, u, d,
        r, r, r, r, p, p, p, p,
    ]
    return avatar


def snake():
    # palette
    b = blue = (73, 95, 121)
    g = green = (0, 160, 77)
    r = red = (255, 0, 0)
    o = black = (0, 0, 0)

    avatar = [
        o, o, o, o, o, o, o, g,
        o, g, g, g, g, g, g, g,
        o, g, o, o, o, o, o, o,
        o, g, g, g, g, g, o, o,
        o, o, o, o, o, g, o, o,
        b, g, b, g, g, g, o, o,
        g, g, g, o, o, o, o, o,
        r, o, o, o, o, o, o, o,
    ]
    return avatar


def snake2():
    # palette
    b = blue = (73, 95, 121)
    g = green = (0, 160, 77)
    r = red = (255, 0, 0)
    o = black = (0, 0, 0)

    avatar = [
        o, g, o, o, o, o, o, o,
        o, g, g, g, g, g, g, o,
        o, o, o, o, o, o, g, o,
        o, g, g, g, g, g, g, o,
        o, g, g, g, o, o, o, o,
        o, o, b, g, b, o, o, o,
        o, o, g, g, g, o, o, o,
        o, o, r, o, o, o, o, o,
    ]
    return avatar


def snakeExclam():
    # palette
    b = blue = (73, 95, 121)
    g = green = (0, 160, 77)
    r = red = (255, 0, 0)
    o = black = (0, 0, 0)

    avatar = [
        o, o, o, g, g, o, o, o,
        o, o, o, g, g, o, o, o,
        o, o, o, g, g, o, o, o,
        o, o, o, g, g, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, b, g, b, o, o, o,
        o, o, g, g, g, o, o, o,
        o, o, r, o, o, o, o, o,
    ]
    return avatar


def snakeQuestion():
    # palette
    b = blue = (73, 95, 121)
    g = green = (0, 160, 77)
    r = red = (255, 0, 0)
    o = black = (0, 0, 0)

    avatar = [
        o, o, g, g, g, g, g, o,
        o, o, o, o, o, o, g, o,
        o, o, o, g, g, g, g, o,
        o, o, o, g, o, o, o, o,
        o, o, o, o, o, o, o, o,
        o, o, b, g, b, o, o, o,
        o, o, g, g, g, o, o, o,
        o, o, r, o, o, o, o, o,
    ]
    return avatar
