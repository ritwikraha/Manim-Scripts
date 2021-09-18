from manim import *


# manim -p -qh -i start.py ThreeDWorld

class ThreeDWorld(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        whiteDot = Dot(color=WHITE)
        text = Text("P")
        # self.add_fixed_in_frame_mobjects(point)
        self.add(whiteDot, text)
        whiteDot.to_corner(UR)
        text.to_corner(UR).next_to(whiteDot, DOWN)
        self.add(axes)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.move_camera(phi=75 * DEGREES, theta=60 * DEGREES)
        self.wait()
