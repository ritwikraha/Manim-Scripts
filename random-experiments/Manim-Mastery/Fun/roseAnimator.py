import random

from manim import *
import numpy as np


# manim -p -ql -i roseAnimator.py Rose
class Rose(Scene):
    def construct(self):
        t = PI * 0.5

        # self.play(FadeIn(axes))
        self.wait(0.5)
        for L in range(1, 10):
            if L % 2 == 0:
                f = RIGHT
            else:
                f = LEFT
            circle = Circle().shift(0.5*L * f)
            circle2 = circle.copy().shift(circle.get_end() *1/L*UP).scale(1 / L).set_color(ORANGE)
            #line = Line().rotate(2 ** L * random.uniform(0, 1) * t)
            self.add(circle)
            self.play(Create(circle))
            self.add(circle2)
            self.play(Create(circle2))
        self.wait(1)
