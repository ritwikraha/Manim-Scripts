from manim import *
import numpy as np


# manim -p -qh -i continous-graph.py Curve
class Curve(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES, distance=9)
        self.add(axes)

        curve = ParametricFunction(lambda t: np.array([
            np.cos(t), np.sin(t), t
        ]), color=RED, t_range = np.array([-TAU, TAU, 0.01]))

        self.begin_ambient_camera_rotation(rate=0.9)
        self.play(Create(curve), runtime=8)

        self.wait(10)
