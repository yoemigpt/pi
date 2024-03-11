import manim as mn

preamble_ar=r"""
\usepackage{amsmath}
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

class BinomialEquation(mn.Scene):
    def construct(self):
        title = mn.Tex(
            "صيغة ثنائي نيوتن",
            font_size=72,
            tex_template=tex_template_ar
        )
        mobjs = title.submobjects[0].submobjects
        title.submobjects[0].submobjects = mobjs[::-1]
        self.play(mn.Write(title), run_time=2)
        self.wait(1)
        
        title.generate_target()
        title.target.to_edge(mn.UR) # type: ignore
        title.target.scale(0.5) # type: ignore
        self.play(mn.MoveToTarget(title), run_time=1) # type: ignore
        self.wait(1)

        eq2 = mn.MathTex(
            "(a + b)^2 = a^2 + 2ab + b^2",
        )
        self.play(mn.Write(eq2), run_time=2)
        self.wait(1)
        
        eq3 = mn.MathTex(
            "(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3",
        )
        self.play(
            mn.TransformMatchingShapes(eq2, eq3),
            run_time=2)
        self.wait(1)
        
        eqn = mn.MathTex(
            "(a+b)^n = \\sum_{k=0}^{n} \\binom{n}{k} a^{n-k} b^k",
        )
        self.play(
            mn.TransformMatchingShapes(eq3, eqn),
            run_time=1)
        self.wait(1)
        
        eqn2 = mn.MathTex(
            "(1+x)^n = \\sum_{k=0}^{n} \\binom{n}{k} x^{k}"
        )
        self.play(mn.TransformMatchingShapes(eqn, eqn2), run_time=1)
        
        eqninf = mn.MathTex(
            "(1+x)^n = \\sum_{k=0}^{\\infty} \\binom{n}{k} x^{k}"
        )
        self.play(mn.TransformMatchingShapes(eqn2, eqninf), run_time=1)
        self.wait(1)
        
        text = mn.MathTex(
            "n = \\frac12",
        )
        text.to_edge(mn.UL)
        self.play(mn.Write(text), run_time=1)
        
        eq12 = mn.MathTex(
            "(1+x)^{\\frac12} = \\sum_{k=0}^{\\infty} \\binom{\\frac12}{k} x^{k}"
        )
        self.play(
            mn.TransformMatchingShapes(eqninf, eq12), run_time=1)
            
        self.wait(3)
        
        self.play(
            mn.Unwrite(text),
            mn.Unwrite(eq12),
            run_time=0.5)
        self.wait(1)
        self.play(mn.FadeOut(title), run_time=0.5)
        self.wait(0.5)