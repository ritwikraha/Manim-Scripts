from manim import *
import numpy as np


# manim -p -ql -i CameraShifter.py Translation
class Translation(ThreeDScene):
    def construct(self):
        worldAxes = ThreeDAxes()
        labelWorld = [worldAxes.get_z_axis_label(Tex("$Z_w$")),
                      worldAxes.get_x_axis_label(Tex("$X_w$").rotate(90 * DEGREES, axis=X_AXIS)),
                      worldAxes.get_y_axis_label(Tex("$Y_w$").rotate(90 * DEGREES, axis=X_AXIS))]

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        worldPoint = Dot3D([0.0, 1.0, 2.0], color=RED)

        origin = Dot3D([0.0, 0.0, 0.0])
        X_W = Arrow3D(origin.get_center(), worldPoint.get_center(), color=WHITE)
        x_w_Label = MathTex("X_W").next_to(X_W, RIGHT).rotate(90 * DEGREES, axis=X_AXIS)

        secondAxesPosition = [3.0, 3.0, 3.0]
        secondAxisScaler = 0.3

        cameraAxes = (ThreeDAxes(x_length=5, y_length=5, z_length=5).scale(secondAxisScaler)
                      .shift(secondAxesPosition))

        labelCamera = [cameraAxes.get_z_axis_label(Tex("$Z_c$").scale(secondAxisScaler)),
                       cameraAxes.get_x_axis_label(Tex("$X_c$")
                                                   .scale(secondAxisScaler)
                                                   .rotate(90 * DEGREES, axis=X_AXIS)),
                       cameraAxes.get_y_axis_label(Tex("$Y_c$")
                                                   .scale(secondAxisScaler)
                                                   .rotate(90 * DEGREES, axis=X_AXIS))]

        X_C = Arrow3D(secondAxesPosition, worldPoint.get_center(), color=YELLOW)
        x_c_Label = MathTex("X_C", color=YELLOW).next_to(worldPoint, RIGHT).rotate(90 * DEGREES, axis=X_AXIS).flip(axis=Z_AXIS)

        self.add(worldAxes, *labelWorld)
        self.play(FadeIn(worldAxes, *labelWorld))
        self.wait(0.5)
        self.add(cameraAxes, *labelCamera)
        self.play(FadeIn(cameraAxes, *labelCamera))
        self.wait(0.5)
        self.add(worldPoint)
        self.play(FadeIn(worldPoint))
        self.wait(0.5)
        self.add(X_W)
        self.play(Create(X_W, run_time=1))
        self.wait(0.5)
        self.add(x_w_Label)
        self.wait(0.5)
        self.move_camera(
            phi=75 * DEGREES,
            theta=40 * DEGREES,
            rate=0.5
        )
        self.wait(0.5)
        self.remove(X_W)
        self.remove(x_w_Label)
        self.wait(0.5)
        self.add(X_C)
        self.play(Create(X_C, run_time=1))
        self.add(x_c_Label)
        self.wait(1)
