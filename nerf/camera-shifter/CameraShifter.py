from manim import *
import numpy as np


# manim -p -qh -i CameraShifter.py Translation
class Translation(ThreeDScene):

    def construct(self):
        worldAxes = ThreeDAxes(x_length=4, y_length=4, z_length=4)
        labelWorld = [worldAxes.get_z_axis_label(Tex("$Z_w$")),
                      worldAxes.get_x_axis_label(Tex("$X_w$").rotate(90 * DEGREES, axis=X_AXIS)),
                      worldAxes.get_y_axis_label(Tex("$Y_w$").rotate(90 * DEGREES, axis=X_AXIS))]

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES, distance=20)
        worldPoint = Dot3D([0.0, 1.0, 2.0], color=RED)

        origin = Dot3D([0.0, 0.0, 0.0])
        X_W = Arrow3D(origin.get_center(), worldPoint.get_center(), color=WHITE)
        x_w_Label = MathTex("X_W").next_to(X_W, RIGHT).rotate(90 * DEGREES, axis=X_AXIS)

        secondAxesPosition = [0.0, 5.0, 0.0]
        secondAxesLabelPosition = [0.0, 2.5, 0.0]
        secondAxesLabelZPosition = [0.0, 1.5, 0.0]
        secondAxisScaler = 0.9
        cameraImage = ImageMobject("assets/video-camera.png").shift(secondAxesPosition).scale(0.25).flip(
            axis=Y_AXIS)

        cameraAxes = (ThreeDAxes(x_length=3, y_length=3, z_length=3).scale(secondAxisScaler)
                      .shift(secondAxesPosition))

        labelCamera = [cameraAxes.get_z_axis_label(Tex("$Z_c$")).shift(secondAxesLabelZPosition),
                       cameraAxes.get_x_axis_label(Tex("$X_c$").rotate(90 * DEGREES, axis=X_AXIS)).shift(
                           secondAxesLabelZPosition),
                       cameraAxes.get_y_axis_label(Tex("$Y_c$").rotate(90 * DEGREES, axis=X_AXIS)).shift(
                           secondAxesLabelPosition)]

        X_C = Arrow3D(secondAxesPosition, worldPoint.get_center(), color=YELLOW)
        x_c_Label = MathTex("X_C", color=YELLOW).next_to(X_C, RIGHT).rotate(90 * DEGREES, axis=X_AXIS).flip(
            axis=Z_AXIS)

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
            distance=20
        )
        self.wait(0.5)
        self.remove(X_W)
        self.remove(x_w_Label)
        self.wait(0.5)
        self.add(X_C)
        self.play(Create(X_C, run_time=1))
        self.add(x_c_Label)
        self.wait(1)
