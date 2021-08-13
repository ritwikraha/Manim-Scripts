from manim import *
# manim -p -ql -i start.py DirectedAcyclicGraph
class DirectedAcyclicGraph(Scene):
	def construct(self):
		vertices=['X','Z','W','Y']
		edges1 = [('W','Y'),('Z','X'),('W','X'),('X','Y')]
		edges2 = [('W','Y'),('X','Y')]

		g1 = Graph(vertices, edges1, layout="planar", layout_scale=5, labels=True,
			vertex_config={'X': {"fill_color": BLUE}},
			edge_type=Arrow,
			edge_config={('X', 'Y'): {"stroke_width": 0.25},
                               ('W', 'Y'): {"stroke_width": 0.25},
                               ('Z','X'): {"stroke_width": 0.25},
                               ('W','X'): {"stroke_width": 0.25}})
		g2 = Graph(vertices, edges2, layout="planar", layout_scale=5, labels=True,
			vertex_config={'X': {"fill_color": BLUE}},
			edge_type=Arrow,
			edge_config={('X', 'Y'): {"stroke_width": 0.25},
                               ('W', 'Y'): {"stroke_width": 0.25}})

		self.play(Create(g1))
		self.wait()
		self.play(Uncreate(g1))
		self.play(Create(g2))
		self.wait()
