from manim import *


class FixedInFrameMObjectTest(ThreeDScene):
    """helps generate the scene for ray-shooting from a 2d image
    Usage:
    manim -p -ql -i start.py FixedInFrameMObjectTest
    #a.animate.shift(2*LEFT)
    """
    def construct(self):
        # adding list of arrows on the right
        # construct axes
        axes = ThreeDAxes()
        labels = axes.get_axis_labels().set_color(BLUE)
        numberplane = NumberPlane()
        numberplane.rotate(90 * DEGREES, LEFT)

        image = ImageMobject('square-keras.png')
        image.rotate(90 * DEGREES, LEFT)
        arrows = []
        dots = []
        for x in range(-2, 3):
            for y in range(-2, 3):
                arrows.append(
                    Arrow([x, 0, y], [x, 2, y], color=YELLOW)
                )

        self.add(axes, labels, image, numberplane, *dots, *arrows)
        self.set_camera_orientation(phi=45 * DEGREES, theta=45 * DEGREES)

        arrows_animate = [ScaleInPlace(a, 8.5) for a in arrows]
        self.move_camera(phi=90 * DEGREES, theta=90 * DEGREES)
        self.play(*arrows_animate)
        self.wait()
