import math

github = [
    (0.933333, 0.933333, 0.933333),
    (0.776470, 0.894117, 0.545098),
    (0.482352, 0.788235, 0.435294),
    (0.137254, 0.603921, 0.231372),
    (0.098039, 0.380392, 0.152941),
]


def get_color(x):
    colors = github

    a = x * (len(colors) - 1)
    t = a - math.floor(a)
    c0 = colors[math.floor(a)]
    c1 = colors[math.ceil(a)]

    return ((1.0 - t) * c0[0] + t * c1[0], (1.0 - t) * c0[1] + t * c1[1],
            (1.0 - t) * c0[2] + t * c1[2])
