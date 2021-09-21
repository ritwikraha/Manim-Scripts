from manim import *
import numpy as np


# manim -p -ql -i ThetaPhi.py Visualizer
class Visualizer(ThreeDScene):
    def construct(self):
        worldAxes = ThreeDAxes()
        labelWorld = [worldAxes.get_z_axis_label(Tex("$Z_w$")),
                      worldAxes.get_x_axis_label(Tex("$X_w$").rotate(90 * DEGREES, axis=X_AXIS)),
                      worldAxes.get_y_axis_label(Tex("$Y_w$").rotate(90 * DEGREES, axis=X_AXIS))]

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES, distance=20)

        phiText = MathTex(r"\phi=75").scale(0.8).to_corner(UL)
        thetaText = MathTex(r"\theta=-45").scale(0.8).next_to(phiText, DOWN)

        updatedthetaText = MathTex(r"\theta=40").scale(0.8).next_to(phiText, DOWN)

        self.play(
            FadeIn(worldAxes, *labelWorld),
            FadeIn(self.add_fixed_in_frame_mobjects(phiText)),
            FadeIn(self.add_fixed_in_frame_mobjects(thetaText))
        )

        self.wait(2)

        self.move_camera(
            phi=75 * DEGREES,
            theta=40 * DEGREES,
            distance=20
        )
        self.play(FadeOut(thetaText))
        self.play(FadeIn(self.add_fixed_in_frame_mobjects(updatedthetaText)))
        self.wait(1)
