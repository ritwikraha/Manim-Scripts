from manim import *
import numpy as np


# manim -p -ql -i posEncoder.py Sinusdoid
class Sinusoid(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(0, 10.01, 2),
            },
            tips=False,
        )
        labels = axes.get_axis_labels(x_label="x", y_label="E(x)")

        self.play(FadeIn(axes, labels))
        self.wait(0.5)
        for L in range(5):
            def funcSin(x):
                return np.sin(2 ** L * x)

            def funcCos(x):
                return np.cos(2 ** L * x)

            text = MathTex("L = " + str(L)).shift(3 * UP).shift(2 * RIGHT)
            graphSin = axes.get_graph(funcSin, color=MAROON)
            graphCos = axes.get_graph(funcCos, color=BLUE)
            self.add(text)
            self.play(Write(text))
            self.play(Create(graphSin))
            self.play(Create(graphCos))
            self.wait(0.5)
            self.remove(text)
            self.play(Uncreate(graphSin))
            self.play(Uncreate(graphCos))
            self.wait(0.5)
        self.wait(1)
        for L in range(5):
            def funcSin(x):
                return np.sin(2 ** L * x)

            def funcCos(x):
                return np.cos(2 ** L * x)

            text = MathTex("L = 0,1,2,3,4").shift(3 * UP).shift(2 * RIGHT)
            graphSin = axes.get_graph(funcSin, color=MAROON)
            graphCos = axes.get_graph(funcCos, color=BLUE)
            self.add(text)
            self.add(graphSin, graphCos)
            self.wait(0.5)
        self.wait(0.5)
        self.play(FadeOut(axes, labels))
