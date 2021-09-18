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
        #
        # axes2.generate_target()

        self.add(worldAxes,
                 *labelWorld,
                 worldPoint,
                 X_W,
                 cameraAxes,
                 *labelCamera)
        self.wait(1)
        self.move_camera(
            phi=75 * DEGREES,
            theta=40 * DEGREES,
            rate=0.5
        )
        self.add(X_C)
        self.wait(1)
