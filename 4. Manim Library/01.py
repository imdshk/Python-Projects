from manim import *


class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        self.add(square)

        self.play(FadeIn(square))

        self.play(Rotate(square, PI/4))

        self.play(FadeIn(square.set_fill(WHITE, opacity=0.8)))

        self.wait(1)

        self.play(Rotate(square, PI/4))
