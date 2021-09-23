from manim import *


# manim -p -ql -i DragonFractal.py Fractalify

class Fractalify(MovingCameraScene):
    CONFIG = {
        "colors": [RED, ORANGE, GREEN_B, BLUE_D, BLUE]
    }

    def construct(self):


        line = Line(DOWN, UP).scale(0.004)
        self.offset = 1.4

        self.dragon = VMobject()
        self.dragon.set_stroke(width=20)
        self.dragon.set_points(line.get_points())

        self.frame = self.camera.frame
        self.frame.set_height(self.dragon.get_height() * self.offset)
        self.frame.move_to(self.dragon.get_center())

        self.last_point = self.dragon.get_last_point()

        self.play(Create(self.dragon.copy()))

        for _ in range(10):
            self.copy_and_rotate()
        self.wait()

    def copy_and_rotate(self):
        dragon = self.dragon.copy()
        dragon.generate_target()
        dragon.target.rotate(PI / 2, about_point=self.last_point)

        self.bring_to_back(dragon)
        self.dragon.set_points(
            np.vstack((self.dragon.get_points(), dragon.target.get_points()))
        )

        self.play(
            MoveToTarget(dragon, path_arc=PI / 2),
            run_time=1.5,
            rate_func=linear,
        )

        self.last_point = self.dragon.get_points()[len(self.dragon.get_points()) // 2]