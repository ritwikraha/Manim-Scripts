from manim import *
import numpy as np


# manim -p -ql -i ThetaPhi.py Visualizer
class Visualizer(ThreeDScene):
    def construct(self):
        worldAxes = ThreeDAxes()
        labelWorld = [worldAxes.get_z_axis_label(Tex("$Z_w$")),
                      worldAxes.get_x_axis_label(Tex("$X_w$").rotate(90 * DEGREES, axis=X_AXIS)),
                      worldAxes.get_y_axis_label(Tex("$Y_w$").rotate(90 * DEGREES, axis=X_AXIS))]

        self.set_camera_orientation(phi=75 * DEGREES, theta=0 * DEGREES, distance=20)

        tracker = ValueTracker(0)

        phiText = MathTex(r"\phi=75").scale(0.8).to_corner(UL)
        thetaText = MathTex(r"\theta=").scale(0.8).to_corner(UL).shift(0.5*DOWN)

        numbers = DecimalNumber(0, num_decimal_places=0)
        point = Dot3D([1.0,1.0,1.0], color=BLUE)

        def numbers_updater(m):
            m.set_value(tracker.get_value())
            self.add_fixed_in_frame_mobjects(m)

        numbers.add_updater(numbers_updater)
        numbers.scale(0.8).next_to(thetaText)

        self.play(
            FadeIn(worldAxes, *labelWorld),
            FadeIn(self.add_fixed_in_frame_mobjects(phiText)),
            FadeIn(self.add_fixed_in_frame_mobjects(thetaText)),
            Create(point)
        )

        self.wait(2)
        self.play(
            FadeIn(numbers)
        )

        self.begin_ambient_camera_rotation(about="theta",rate=0.38)
        self.play(tracker.animate.set_value(360), run_time=16)
        self.wait(1)
