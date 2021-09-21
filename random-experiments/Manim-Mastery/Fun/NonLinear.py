from manim import *
import numpy as np


# manim -p -ql -i NonLinear.py Grid
class Grid(Scene):
    def construct(self):
        title1 = Tex(r"What happens when you apply this equation")
        eqn = MathTex(r"xsin(x)",color=MAROON)
        title2 = Tex(r"to points on a circle?")
        VGroup(title1, eqn, title2).arrange(DOWN)
        title3 = Tex(r"You get an arc")
        title4 = Tex(r"of unit length")

        VGroup(title3,title4).arrange(DOWN)

        self.play(
            Write(title1),
            Write(title2),
            FadeIn(eqn)
        )
        self.wait(3)
        self.play(
            FadeOut(title1),
            FadeOut(title2),
            FadeOut(eqn, run_time=2, lag_ratio=0.1)
        )

        circle = Circle(color=MAROON)
        grid = NumberPlane()
        self.add(grid)

        self.play(
            Create(grid, run_time=3),
        )
        self.play(
            Create(circle, run_time=3),
        )
        self.wait()
        # grid.prepare_for_nonlinear_transform()
        self.play(
            circle.animate.apply_function(
                lambda p: p * np.sin(p)
            ),
            run_time=3,
        )
        self.wait(1)

        self.play(
            Uncreate(circle, runtime=2),
            FadeOut(grid, run_time=3)
        )
        self.wait(1)
        self.play(
            Write(title3),
            FadeIn(title4, run_time=2, lag_ratio=0.1),
        )
        self.wait()

