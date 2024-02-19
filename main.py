import manim as mn

class AnimatedPI(mn.Scene):
    def construct(self):
        pi = mn.Tex(
            "$\pi$",
            font_size=256,
            color=mn.RED
        )
        self.play(mn.Write(pi))
        
        text = mn.Tex(
            "3.141592653589793238462643383279502",
            font_size=24
        ).next_to(pi, mn.DOWN)
        self.play(mn.Write(text))

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