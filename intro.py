import manim as mn

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
            "يوم العدد",
            " ",
            "$\\pi$",
            font_size=84,
            tex_template=tex_template_ar
        )
        reverse_mobjects(text)
        self.play(mn.Write(text), run_time=3)
        self.wait(2)
        self.play(mn.FadeOut(text), run_time=2)

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
        self.wait(7)
        self.play(
            mn.FadeOut(text7),
            run_time=1
        )
        self.wait(1)
        
        



