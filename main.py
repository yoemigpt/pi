from textwrap import fill
import manim as mn

class AnimatedCircle(mn.Scene):
    def construct(self):
        circle = mn.Circle(
            radius=2,
            fill_color=mn.BLUE,
            fill_opacity=0.5,
            stroke_color=mn.RED,
        )
        text = mn.Text("Voici un cercle", font_size=24).next_to(circle, mn.UP)
        self.play(mn.Create(circle), mn.Write(text))