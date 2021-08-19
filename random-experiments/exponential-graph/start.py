from manim import *
import numpy as np

# manim -p -ql -i start.py ExponentialPlot

class ExponentialPlot(GraphScene):
       def construct(self):
        ax = Axes(
            x_range=[-10, 10], y_range=[0, 100, 10], axis_config={"include_tip": True}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="exp(-x)")

        t = ValueTracker(-10)

        def func(x):
            return np.exp(-x)
        graph = ax.get_graph(func, color=MAROON)

        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point)

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        x_space = np.linspace(*ax.x_range[:2],200)
        minimum_index = func(x_space).argmin()

        self.add(ax, labels, graph, dot)
        self.play(t.animate.set_value(x_space[minimum_index]))
        self.wait()