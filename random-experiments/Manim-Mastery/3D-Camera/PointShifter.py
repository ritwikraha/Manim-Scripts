from manim import *
import numpy as np


# manim -p -ql -i PointShifter.py Translation
class Translation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        lab1 = axes.get_z_axis_label(Tex("$Z_w$"))
        axes2 = ThreeDAxes(x_length=2, y_length=2, z_length=2).shift([2, 2, 2]).rotate(angle=0.75*PI, axis=Y_AXIS)
        lab2 = axes2.get_z_axis_label(Tex("$Z_c$"))
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        dot = Dot([0, -1, -1])
        staticDot = Dot([0, -1, -1])
        dest = Dot([3, 3, 3], color=YELLOW)
        self.add(axes,lab1, staticDot, dot, dest, axes2, lab2)
        self.wait(1)
        self.play(dot.animate.shift(dest.get_center() - dot.get_center()))
        self.wait(1)
