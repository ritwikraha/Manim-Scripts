from manim import *
import cmath
import numpy as np


X_LIMITS = (-0.4, 1.2)
Y_LIMITS = (-0.4, 0.7)


# manim -p -ql -i DragonFractal.py Fractalify      |_|


def compute_new(z1, z2, up):

    v = (z2 - z1) / 2  # v is the 'vector' from z1 to the middle of the segment [z1, z2]
    v_mod, v_phas = cmath.polar(v)  # using the polar form to make some homothety and translation
    v_mod *= np.sqrt(2)  # homothety

    if up:
        rot = 1j ** 0.5
    else:
        rot = -1j ** 1.5

    return cmath.rect(v_mod, v_phas) * rot  # translation


def partial_dragon_curve(T):
    '''
    Generates the next generation of the fractal curve algorithm. For each pair of consecutive points of T
    that make a vertice, we add between those two points the new point(s) generated by the "compute_new"
    method.
    Parameters
    ----------
    T : list[complex]
        the current state of the algorithm.
    Returns
    -------
    res : list[complex]
        The next step of the algorithm.
    '''

    res = []
    for i in range(len(T) - 1):
        res.append(T[i])
        res.append(T[i] + compute_new(T[i], T[i + 1], i % 2 == 0))
    res.append(T[-1])
    return res


def dragon_curve(n):
    '''
    Recursive method to build the final fractal curve of degree n.
    Parameters
    ----------
    n : int
        The degree of the fractal curve to build.
    Returns
    -------
    list[complex]
        The list of complex numbers that represent the n-th degree fractal curve.
    '''

    if n == 0:
        return [complex(0, 0), complex(1, 0)]
    else:
        return partial_dragon_curve(dragon_curve(n - 1))


def pts_num(n):
    '''
    Optional function that returns the amount of points in the n-th generation of the algorithm.
    Parameters
    ----------
    n : int
        The degree of the fractal curve.
    Returns
    -------
    int
        The number of vertices needed to build the n-th degree fractal curve.
    '''

    n0 = 2
    return (2 ** n) * (n0 - 1) + 1


#  _            _
# | |          | |
# | |_ ___  ___| |_ ___
# | __/ _ \/ __| __/ __|
# | ||  __/\__ \ |_\__ \
#  \__\___||___/\__|___/

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    N = 15
    D = dragon_curve(N)
    Dr = [el.real for el in D]
    Di = [el.imag for el in D]
    plt.plot(Dr, Di, lw=np.exp(-N / 10))