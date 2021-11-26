from manim import *
# manim -p -qh -i start.py BlendingImages

class BlendingImages(Scene):
    def construct(self):
        text=MathTex(
            "o = f(x,y)"
        )
        add = MathTex(
            "+"
        )

        blendText = Tex("Blended Image")
        blendText.shift(LEFT*3)




        self.play(Write(text))
        self.wait()
        lake= ImageMobject("lake.jpg")
        lake.scale(0.5)
        lake.shift(LEFT*3)

        boat= ImageMobject("lake-boat.jpg")
        boat.scale(0.5)
        boat.shift(RIGHT*3)


        blend= ImageMobject("lake-blend.jpg")
        blend.scale(0.5)
        blend.shift(RIGHT*3)



        self.play(FadeOut(text))
        self.wait(1)
        self.play(FadeIn(lake,boat))
        self.wait()
        self.play(Write(add))
        self.wait(2)
        self.remove(add)
        self.play(FadeTransform(lake,blend))
        self.play(Write(blendText))
        self.wait(2)


