import manim as mn

from pidigits import piGenerator

mypi = piGenerator()

PITEX = "$\\pi$"
PIDIGITS = [next(mypi) for _ in range(1000)]
PIDIGITS = "".join(map(str, PIDIGITS))

preamble_ar = r"""
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


class PIAnimation(mn.Scene):
    def construct(self):
        title = mn.Tex(
            "أين نحن اليوم؟",
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
        self.play(mn.FadeOut(title), run_time=1)

        L = 52
        R = 12
        
        prev = None
        for i in range(R):
            if prev is None:
                text = mn.MathTex(
                    PIDIGITS[0] + "." +
                    PIDIGITS[1:(i+1)*L],
                    font_size=50,
                )
                text.to_edge(mn.LEFT)
                text.to_edge(mn.UP)
            else:
                text = mn.MathTex(
                    PIDIGITS[i*L:(i+1)*L],
                    font_size=50,
                )
                text.next_to(prev, mn.DOWN)
                text.to_edge(mn.LEFT)
            
            prev = text    
            self.play(mn.Write(text), run_time=1.5)