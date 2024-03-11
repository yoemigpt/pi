import manim as mn
import numpy as np

preamble_ar=r"""
\usepackage{fontspec}
\usepackage{polyglossia}
\setdefaultlanguage[%
    numerals=maghrib
]{arabic}
\setotherlanguage{english}
\setmainfont{Amiri}
"""
tex_template_ar = mn.TexTemplate(
    tex_compiler="xelatex",
    output_format=".xdv",
    preamble=preamble_ar
)

def reverse_mobjects(mobj):
    # reverse the order of the mobjects
    # recursively reverse the submobjects
    for mob in mobj.submobjects:
        if len(mob) > 0:
            reverse_mobjects(mob)
    mobj.submobjects = list(reversed(mobj.submobjects))

class ArabicFirst(mn.Scene):
    def construct(self):
        text = mn.Tex(
            "تخليدا لليوم العالمي للرياضيات 14 مارس 2024",
            font_size=64,
            tex_template=tex_template_ar
        )
        mobjs = text.submobjects[0].submobjects
        text.submobjects[0].submobjects = mobjs[::-1]
        text.to_edge(mn.UP)

        text2 = mn.Tex(
            "جمعية ترقية الرياضيات",
            font_size=60,
            tex_template=tex_template_ar
        )
        mobjs = text2.submobjects[0].submobjects
        text2.submobjects[0].submobjects = mobjs[::-1]
        text2.next_to(text, mn.DOWN)
        
        logo = mn.ImageMobject(
            "assets/logos/promath.png")
        logo.scale(0.7)
        logo.next_to(text2, mn.DOWN)
        
        text3 = mn.Tex(
            "تقدم",
            font_size=50,
            tex_template=tex_template_ar
        )
        mobjs = text3.submobjects[0].submobjects
        text3.submobjects[0].submobjects = mobjs[::-1]
        text3.next_to(logo, mn.DOWN)

        
        text4 = mn.Tex(
            "فيديو عن العدد",
            " ",
            "$\\pi$",
            font_size=64,
            tex_template=tex_template_ar
        )
        mobjs = text4.submobjects[0].submobjects
        text4.submobjects[0].submobjects = mobjs[::-1]
        mobjs = text4.submobjects[1].submobjects
        text4.submobjects[1].submobjects = mobjs[::-1]
        mobjs = text4.submobjects[2].submobjects
        text4.submobjects[2].submobjects = mobjs[::-1]
        mobjs = text4.submobjects
        text4.submobjects = mobjs[::-1]
        text4.next_to(text3, mn.DOWN)
        
        self.play(
            mn.AnimationGroup(
                mn.Write(text),
                mn.Write(text2),
                mn.FadeIn(logo),
                mn.Write(text3),
                mn.Write(text4),
                lag_ratio=0.8
            ),
            run_time=4
        )
        self.wait(2)
        
        self.play(
            mn.FadeOut(text),
            mn.FadeOut(text2),
            mn.FadeOut(logo),
            mn.FadeOut(text3),
            mn.FadeOut(text4),
            run_time=1
        )
        
        self.wait(1)

class ArabicSecond(mn.Scene):
    def construct(self):
        
        # Write the date in Arabic.
        text = mn.Tex(
            "14",
            " "
            "مارس",
            font_size=84,
            tex_template=tex_template_ar
        )
        reverse_mobjects(text)
        self.play(mn.Write(text), run_time=3)
        self.wait(2)
        
        # Write the date in English.
        text2 = mn.MathTex(
            "03",
            "/",
            "14",
            font_size=84
        )
        text2.move_to(text)
        text2.align_to(text, mn.RIGHT)
        self.play(
            mn.TransformMatchingShapes(
                text, text2
            ),
            run_time=2
        )
        self.wait(2)
        
        text3 = mn.MathTex(
            "3",
            "/",
            "14",
            font_size=84
        )
        text3.move_to(text2)
        text3.align_to(text2, mn.RIGHT)
        
        self.play(
            mn.TransformMatchingShapes(
                text2, text3
            ),
            run_time=1
        )
        self.wait(1)
        
        text4 = mn.MathTex(
            "3",
            ".",
            "14",
            font_size=84
        )
        
        text4.move_to(text3)
        text4.align_to(text3, mn.RIGHT)
        
        self.play(
            mn.TransformMatchingTex(
                text3, text4,
                transform_mismatches=True,
            ),
            run_time=2
        )
        self.wait(1)
        
        text5 = mn.MathTex(
            "\\pi",
            "\\approx",
            "3",
            ".",
            "14",
            font_size=84
        )
        text5.move_to(text4)
        text5.align_to(text4, mn.RIGHT)
        self.play(
            mn.TransformMatchingTex(
                text4, text5,
                transform_mismatches=True,
            ),
            run_time=2
        )
        self.play(
            text5.animate.to_edge(mn.LEFT)
        )
        
        text6 = mn.MathTex(
            "\\pi",
            "\\approx",
            "3",
            ".",
            "14",
            "159265358979323846264",
            "\\ldots",
            font_size=84
        )
        text6.move_to(text5)
        text6.align_to(text5, mn.LEFT)
        self.play(
            mn.TransformMatchingShapes(
                text5, text6,
            ),
            run_time=3
        )
        self.wait(2)
        
        text7 = mn.MathTex(
            "\\pi",
            font_size=84
        )
        
        text7.move_to(text6)
        text7.align_to(text6, mn.LEFT)
        
        self.play(
            mn.TransformMatchingShapes(
                text6, text7,
            ),
            run_time=2
        )
        
        text7.generate_target()
        
        text7.target.move_to(mn.ORIGIN) # type: ignore
        text7.target.scale(5) # type: ignore
        text7.target.set_color(mn.RED) # type: ignore
        
        self.play(
            mn.MoveToTarget(text7),
            run_time=2
        )
        self.wait(9)
        self.play(
            mn.FadeOut(text7),
            run_time=2
        )
        self.wait(1)
        
        
class ArabicIntro(mn.Scene):
    def construct(self):
        squares = [mn.Square(side_length=3) for _ in range(3)]
        mn.VGroup(*squares).set_x(0).arrange(buff=1)
        
        self.play(mn.GrowFromPoint(squares[0], mn.ORIGIN))
        self.play(mn.GrowFromPoint(squares[1], [-2, 2, 0]))
        self.play(mn.GrowFromPoint(squares[2], [3, -2, 0]))
        self.wait(1)

        
        def inscribed(circ, n):
            points = []
            for i in range(n):
                p = circ.point_at_angle(mn.TAU * i / n)
                points.append(p)
            return mn.Polygon(*points)
        
        def subscribed(circ, n):
            points = []
            c = circ.get_center()
            r = circ.radius
            a = r / (np.cos(mn.TAU / (2*n)))
            for i in range(n):
                p = circ.point_at_angle(mn.TAU * i / n)
                points.append((p-c) * a / r + c)
            return mn.Polygon(*points)
        
        n = 6
        circ = mn.Circle(radius=1)
        circ.move_to(squares[1].get_center())
        
        ins = inscribed(circ, n)
        sub = subscribed(circ, n)
        
        eq = mn.MathTex(
            "\\sum_{n=0}^\\infty \\frac1{k^2} = \\frac{\\pi^2}{6}",
        )
        eq.move_to(squares[2].get_center())
        eq.scale(0.5)
        
        eq2 = mn.MathTex(
            "e^{i\\pi} + 1 = 0",
        )
        eq2.move_to(squares[0].get_center())
        
        self.play(
            mn.Write(eq2),
            mn.Create(circ),
            mn.Write(eq),
            run_time=1)
        
        nt = 7
        for _ in range(nt):
            self.play(
                mn.Write(eq2),
                mn.Create(ins),
                mn.Create(sub),
                mn.Write(eq),
                run_time=1
            )
            self.wait(0.5)
        self.wait(1)