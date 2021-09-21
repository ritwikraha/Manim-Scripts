from manim import *
import numpy as np


# manim -p -qh -i RayGenerator.py Shooter
class Shooter(ThreeDScene):
    def construct(self):
        worldAxes = ThreeDAxes()
        labelWorld = [worldAxes.get_z_axis_label(Tex("$Z_w$")),
                      worldAxes.get_x_axis_label(Tex("$X_w$").rotate(90 * DEGREES, axis=X_AXIS)),
                      worldAxes.get_y_axis_label(Tex("$Y_w$").rotate(90 * DEGREES, axis=X_AXIS))]

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        cameraPoint = Dot3D([1.0, 0.0, 2.0], color=BLUE)
        cameraLabel = Text("Camera").scale(0.3).next_to(cameraPoint).rotate(90 * DEGREES, axis=X_AXIS)

        imagePoint = Dot3D([1.0, 1.0, 2.0], color=RED)
        extendedPoint = Dot3D([1.0, 3.0, 2.0])
        grid = NumberPlane(x_length=2, y_length=2, background_line_style={
            "stroke_color": BLUE_D,
            "stroke_width": 1,
            "stroke_opacity": 0.4,
        }).rotate(90 * DEGREES, axis=X_AXIS).shift(imagePoint.get_center())
        imageLabel = Text("Image").scale(0.3).next_to(grid).rotate(90 * DEGREES, axis=X_AXIS)

        dirVec = Arrow3D(cameraPoint.get_center(), imagePoint.get_center(), color=YELLOW)
        extendVec = Arrow3D(cameraPoint.get_center(), extendedPoint.get_center(), color=YELLOW_A)
        vecLabel = Tex(r"$\vec{r}$").scale(0.7).next_to(extendedPoint).rotate(90 * DEGREES, axis=X_AXIS)

        self.play(
            FadeIn(worldAxes, *labelWorld),
            Create(cameraPoint),
            Create(cameraLabel),
            FadeIn(grid),
            Create(imageLabel)
        )

        self.wait(1)
        self.play(
            Create(imagePoint)
        )
        self.wait(1)
        self.play(
            Create(dirVec)
        )
        self.play(
            Create(extendVec),
            Create(vecLabel)
        )
        self.wait(1)
        self.move_camera(
            phi=75 * DEGREES,
            theta=0 * DEGREES,
            distance=20
        )
        self.wait(1)
        self.move_camera(
            phi=75 * DEGREES,
            theta=45 * DEGREES,
            distance=20
        )
        self.wait()
