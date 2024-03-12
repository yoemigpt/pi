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

class ArabicFinal(mn.Scene):
    def construct(self):
        audio = mn.Tex(
            "الصوت",
            font_size=32,
            tex_template=tex_template_ar
        )
        
        audio2 = mn.Tex(
            "محمد الأمين الوقف",
            font_size=40,
            tex_template=tex_template_ar
        )
        
        script = mn.Tex(
            "الكتابة والتدقيق",
            font_size=32,
            tex_template=tex_template_ar
        )
        
        script2 = mn.Tex(
            "محمد الأمين الوقف",
            "\\\\",
            "يوسف أمين",
            "\\\\",
            "المختار باب حمدي",
            font_size=40,
            tex_template=tex_template_ar
        )
        
        montage = mn.Tex(
            "المونتاج",
            font_size=32,
            tex_template=tex_template_ar
        )
        
        montage2 = mn.Tex(
            "محمد الأمين الوقف",
            "\\\\",
            "يوسف أمين",
            font_size=40,
            tex_template=tex_template_ar
        )
        
        thanks = mn.Tex(
            "شكر خاص",
            font_size=32,
            tex_template=tex_template_ar
        )
        
        group = mn.VGroup(
            audio, audio2, script, script2, montage, montage2 # , thanks
        )
        
        group.arrange(
            mn.DOWN,
        #    aligned_edge=mn.LEFT
        )
        group.to_edge(
            mn.RIGHT,
            buff=1)
        
        pi = mn.MathTex(
            "\\pi",
            color=mn.RED,
            font_size=72,
        )
        pi.scale(5)
        pi.shift(3*mn.LEFT)
        
        
        for mobj in group:
            mobjs = mobj.submobjects[0].submobjects
            mobj.submobjects[0].submobjects = mobjs[::-1]
        
        self.play(
            mn.Write(group),
            mn.FadeIn(pi),
            run_time=4)
        self.wait(1)
        
        pi.generate_target()
        pi.target.move_to(mn.ORIGIN) # type: ignore
        pi.target.scale(1.5) # type: ignore
        
        self.play(
            mn.FadeOut(group),
            mn.MoveToTarget(pi),
            run_time=1.5)
        self.wait(1)