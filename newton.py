import manim as mn
import numpy as np

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

tex = r"""
\begin{itemize}
\item مساحة الشكل الأزرق هي المتكاملة $\int_0^1 f(x) \, dx$
\item مساحة الشكل الأزرق تساوي ربع دائرة نصف قطرها $1$. و بالتالي تساوي $\frac{\pi}{4}$
\end{itemize}
"""
            

class Integral(mn.Scene):
    def construct(self):
        title = mn.Tex(
            "التكامل و التفاضل",
            font_size=72,
            tex_template=tex_template_ar
        )
        mobjs = title.submobjects[0].submobjects
        title.submobjects[0].submobjects = mobjs[::-1]
        self.play(mn.Write(title), run_time=1)
        self.wait(1)
        
        title.generate_target()
        title.target.to_edge(mn.UR) # type: ignore
        title.target.scale(0.5) # type: ignore
        self.play(mn.MoveToTarget(title), run_time=1)
        self.wait(1)
        
        ax = mn.Axes(
            x_range=[-0.2, 1.2],
            y_range=[-0.2, 1.2],
            x_length=4,
            y_length=4,
            # tips=False,
            axis_config={
                "include_numbers": True,
                "tip_shape": mn.StealthTip
            },
        ).add_coordinates()
        ax_labels = ax.get_axis_labels(
            x_label=mn.Tex("$x$"),
            y_label=mn.Tex("$y$")
        )
        self.play(
            mn.Create(ax),
            mn.Create(ax_labels))
        group = mn.VGroup(ax, ax_labels)

        self.wait(1)
        
        def f(x):
            return np.sqrt(1-x**2)
        
        eq = mn.MathTex(
            "x^2 + y^2 = 1",
        )
        eq.to_edge(mn.LEFT)
        
        graph = ax.plot(
            f, x_range=[0, 1, 0.001],
            use_smoothing=True,
            color=mn.BLUE)
        group.add(graph)
        self.play(
            mn.Write(eq),
            mn.Create(graph))
        self.wait(1)
        
        eq2 = mn.MathTex(
            "y^2 = 1 - x^2",
        )
        eq2.to_edge(mn.LEFT)
        self.play(
            mn.TransformMatchingShapes(eq, eq2),
            run_time=1)
        self.wait(1)
        
        eq3 = mn.MathTex(
            "y = \\sqrt{1 - x^2}",
        )
        eq3.to_edge(mn.LEFT)
        self.play(
            mn.TransformMatchingShapes(eq2, eq3),
            run_time=1)
        self.wait(1)
        
        eq4 = mn.MathTex(
            "y = f(x) = \\left(1 - x^2\\right)^{\\frac{1}{2}}",
        )
        eq4.to_edge(mn.LEFT)
        self.play(
            mn.TransformMatchingShapes(eq3, eq4),
            run_time=1)
        
        eq5 = mn.MathTex(
            "f(x) = \\left(1 - x^2\\right)^{\\frac{1}{2}}",
        )
        eq5.to_edge(mn.LEFT)
        self.play(
            mn.TransformMatchingShapes(eq4, eq5),
            run_time=1)
        
        self.play(eq5.animate.to_edge(mn.UP))
        self.wait(1)
        
        area = ax.get_area(
            graph,
            (0, 1),
            color=mn.BLUE,
            opacity=0.5)
        group.add(area)
        
        self.play(mn.Create(area))
        self.wait(1)

        text1 = mn.Tex(
            tex,
            font_size=30,
            tex_template=tex_template_ar
        )
        self.play(group.animate.to_edge(mn.LEFT))
        text1.to_edge(mn.RIGHT)
        text1.shift(1.5*mn.UP)
        mobjs = text1.submobjects[0].submobjects
        text1.submobjects[0].submobjects = mobjs[:37][::-1] + mobjs[37:][::-1] 
        self.play(mn.Write(text1), run_time=2)
        self.wait(4)
        
        eq6 = mn.MathTex(
            "\\int_0^1 f(x) \\, dx = \\frac{\\pi}{4}",
            font_size=64,
        )
        eq6.next_to(text1, mn.DOWN)
        self.play(mn.Write(eq6), run_time=2)
        self.wait(1)
        
        self.play(
            mn.FadeOut(text1),
            mn.FadeOut(group),
        )
        self.wait(1)
        
        eq6.generate_target()
        eq6.target.to_edge(mn.DL) # type: ignore
        eq6.target.scale(0.5) # type: ignore
        self.play(mn.MoveToTarget(eq6), run_time=1)

        eq5.generate_target()
        eq5.target.move_to(mn.ORIGIN) # type: ignore
        # eq5.target.scale(1.5) # type: ignore
        self.play(mn.MoveToTarget(eq5), run_time=1)
        
        text3 = mn.Tex(
            "باستخدام الصيغة الثنائية للنيوتن",
            font_size=34,
            tex_template=tex_template_ar
        )
        mobjs = text3.submobjects[0].submobjects
        text3.submobjects[0].submobjects = mobjs[::-1]
        text3.to_edge(mn.RIGHT)
        text3.shift(1.5*mn.UP)
        self.play(mn.Write(text3), run_time=1)
        
        eq7 = mn.MathTex(
            "f(x) = \\sum_{n=0}^\\infty \\binom{\\frac{1}{2}}{n} (-x)^{2n}",
        )
        eq7.align_to(eq5, mn.LEFT)
        
        self.play(
            mn.TransformMatchingShapes(eq5, eq7),
            run_time=1)
        self.wait(1)
        
        eq8 = mn.MathTex(
            "f(x) = \\sum_{n=0}^\\infty (-1)^n \\binom{\\frac{1}{2}}{n} x^{2n}",
        )
        eq8.align_to(eq7, mn.LEFT)
        self.play(
            mn.TransformMatchingShapes(eq7, eq8),
            run_time=1)
        self.wait(1)

        self.play(mn.FadeOut(text3))
        
        eq9 = mn.MathTex(
            "\\int_0^1 f(x)dx = \\sum_{n=0}^\\infty (-1)^n\\binom{\\frac{1}{2}}{n}\\int_0^1x^{2n}dx",
        )
        # eq9.align_to(eq8, mn.LEFT)
        self.play(
            mn.TransformMatchingShapes(eq8, eq9),
            run_time=1)
        self.wait(1)
        
        eq10 = mn.MathTex(
            "\\int_0^1 f(x)dx = \\sum_{n=0}^\\infty (-1)^n \\binom{\\frac{1}{2}}{n} \\frac{1}{2n+1}",
        )
        self.play(
            mn.TransformMatchingShapes(eq9, eq10),
            run_time=1)
        self.wait(1)
        
        eq11 = mn.MathTex(
            "\\frac{\\pi}{4}=\\sum_{n=0}^\\infty (-1)^n \\binom{\\frac{1}{2}}{n} \\frac{1}{2n+1}",
        )
        self.play(
            mn.FadeOut(eq6),
            mn.TransformMatchingShapes(eq10, eq11),
            run_time=1)
        self.wait(1)

        eq12 = mn.MathTex(
            "\\pi=4\\sum_{n=0}^\\infty \\frac{(-1)^n}{2n+1} \\binom{\\frac{1}{2}}{n}",
        )
        self.play(
            mn.TransformMatchingShapes(eq11, eq12),
            run_time=1)
        self.wait(1)
        
        eq12.generate_target()
        eq12.target.to_edge(mn.UL) # type: ignore
        eq12.target.scale(0.5) # type: ignore
        self.play(mn.MoveToTarget(eq12), run_time=1)
        self.wait(1)
        
        def binom(r, k):
            kk = np.arange(k)
            return np.prod((r-kk)/(k-kk))
            
        def an(n):
            return 4*(-1)**n/(2*n+1)*binom(1/2, n)
        
        def Sn(n):
            if n == 0:
                return 4
            else:
                return Sn(n-1) + an(n)

        t = mn.ValueTracker(1)
        eq = mn.MathTex(
            "",
        )
        def update_eq(e):
            tv = t.get_value()
            ne = mn.MathTex(
                "\\pi\\approx 4\\sum_{n=0}^{" + str(int(tv)) + "} \\frac{(-1)^n}{2n+1} \\binom{\\frac{1}{2}}{n}= " + f"{Sn(int(tv)):.6f}",
            )
            e.become(ne)
        
        eq.add_updater(update_eq)
        self.add(eq)
        self.play(t.animate.set_value(20), run_time=5)
        eq.clear_updaters()
        
        self.wait(2)
        self.play(
            mn.Unwrite(eq12),
            mn.FadeOut(eq),
            run_time=1)
        
        self.wait(1)
        self.play(mn.FadeOut(title), run_time=0.5)
        self.wait(1)
        
        
class Newton(mn.Scene):
    pass