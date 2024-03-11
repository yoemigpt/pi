from pdb import run
from turtle import color
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

class Circumference(mn.Scene):
    def construct(self):
        title = mn.Tex(
            "تعريف $\\pi$",
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

        r = 1
        s = 0.2
        circ = mn.Circle(radius=r)
        self.play(mn.Create(circ))
        self.play(circ.animate.to_edge(mn.UL))
        
        n = 2
        a = mn.ORIGIN + n * 2 * r * mn.LEFT
        points = []
        for i in range(2*n + 1):
            p = a + i * 2 * r * mn.RIGHT
            points.append(p)

        bars = mn.VGroup()
        for i, p in enumerate(points):
            o = p + s * mn.UP
            q = p + s * mn.DOWN
            bar = mn.Line(o, q)
            bars.add(bar)
        
        c = circ.copy()
        self.add(c)        
        a = a + r*mn.RIGHT
        
        self.play(c.animate.move_to(a), run_time=0.5)
        self.play(mn.Create(bars[0]), run_time=0.5)
        
        for i in range(1, len(bars)):
            self.play(mn.Create(bars[i]),
                      run_time=0.5)
            if i == len(bars) - 1:
                self.play(mn.FadeOut(c),
                          run_time=0.5)
                self.remove(c)
            else:
                self.play(
                    c.animate.shift(2*r*mn.RIGHT),
                    run_time=0.5)
        
        labels = mn.VGroup()
        arrows = mn.VGroup()
        for i in range(len(bars)-1):
            arrow = mn.DoubleArrow(
                bars[i].get_end(),
                bars[i+1].get_end(),
                buff=0,
                tip_length=0.15
            )
            label = mn.Tex(
                "قطر الدائرة",
                font_size=24,
                tex_template=tex_template_ar
            )
            label.next_to(arrow, mn.DOWN)
            labels.add(label)
            arrows.add(arrow)
            
        self.play(
            mn.Create(arrows),
            mn.Create(labels)
        )
        self.wait(0.5)
        
        circ.generate_target()
        a = bars[0].get_center()
        circ.target.move_to(a) # type: ignore
        circ.target.shift(r*mn.UP) # type: ignore
        self.play(mn.MoveToTarget(circ), run_time=0.5)
        self.wait(0.5)
        
        t = mn.ValueTracker(0)
        def update_arc(arc):
            tv = t.get_value()
            narc = mn.Arc(
                start_angle=-mn.PI/2,
                angle=mn.TAU - tv,
                radius=r,
                arc_center=a + r*tv*mn.RIGHT,
                color=mn.RED,
                # stroke_width=4
            )
            narc.shift(r*mn.UP)
            arc.become(narc)
        
        def update_line(line):
            tv = t.get_value()
            nline = mn.Line(
                a, a + r*tv*mn.RIGHT,
                color=mn.RED,
            )
            line.become(nline)
        
        arc = circ.copy()
        line = mn.Line(a, a)
        self.add(arc)
        self.add(line)
        self.remove(circ)
        
        line.add_updater(update_line)
        arc.add_updater(update_arc)
        
        ta = t.animate.set_value(mn.TAU)
        self.play(ta, run_time=3)
        self.wait(0.5)
        
        line.clear_updaters()
        arc.clear_updaters()
        
        b = line.get_end()
        bar = mn.Line(
            b + s*mn.UP,
            b + s*mn.DOWN
        )
        self.play(mn.Create(bar), run_time=0.5)
        arrow = mn.DoubleArrow(
            bars[0].get_start(),
            bar.get_start(),
            buff=0,
            # stroke_width=1,
            tip_length=0.15
        )
        label = mn.Tex(
            "محيط الدائرة",
            font_size=24,
            tex_template=tex_template_ar
        )
        label.next_to(arrow, mn.UP)
        self.play(
            mn.Create(arrow),
            mn.Create(label),
            run_time=0.5
        )
        self.wait(0.5)
        
        eq = mn.MathTex(
            "\\pi",
            "=",
            "\\frac{\\text{محيط الدائرة}}{\\text{قطر الدائرة}}",
            font_size=72,
            tex_template=tex_template_ar
        )
        
        u = 11
        i = 2
        mobjs = eq.submobjects[i].submobjects
        eq.submobjects[i].submobjects = mobjs[:u][::-1] + [mobjs[u]] + mobjs[u+1:][::-1]
        eq.to_edge(mn.UP)
        self.play(mn.Write(eq), run_time=5)
        self.wait(3)
        
        self.play(
            mn.Uncreate(bar),
            mn.Uncreate(arrow),
            mn.Uncreate(label),
            mn.Uncreate(bars),
            mn.Uncreate(arrows),
            mn.Uncreate(labels),
            mn.Uncreate(line),
            mn.Unwrite(eq),
            run_time=1)
        self.play(mn.FadeOut(title), run_time=0.5)
        self.wait(0.5)