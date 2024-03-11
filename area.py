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


class Area(mn.Scene):
    def construct(self):
        title = mn.Tex(
            "مساحة القرص",
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
        self.play(mn.MoveToTarget(title), run_time=1)
        self.wait(1)
        
        r = 1.5
        circ = mn.Circle(
            radius=r,
            color=mn.BLUE,
        )

        self.play(mn.Create(circ))
        self.wait(1)
        self.play(circ.animate.set_fill(mn.BLUE, 0.5))
        self.wait(1)
        self.play(circ.animate.to_edge(mn.UL))
        self.wait(1)
        
        eq = mn.MathTex(
            "\\pi = \\frac{\\text{مساحة القرص}}{^2\\text{نصف قطر القرص}}",
            tex_template=tex_template_ar
        )
        mobjs = eq.submobjects[0].submobjects[2:12]
        eq.submobjects[0].submobjects[2:12] = mobjs[::-1]
        mobjs = eq.submobjects[0].submobjects[13:26]
        eq.submobjects[0].submobjects[13:26] = mobjs[::-1]

        self.play(mn.Write(eq), run_time=2)
        self.wait(1)
        
        eq.generate_target()
        eq.target.to_edge(mn.DR) # type: ignore
        # eq.target.scale(0.5) # type: ignore
        self.play(mn.MoveToTarget(eq), run_time=1)
        self.wait(1)
        
        circ.generate_target()
        circ.target.move_to(mn.ORIGIN).to_edge(mn.LEFT) # type: ignore
        self.play(mn.MoveToTarget(circ), run_time=1)
        self.wait(1)
        
        r = circ.radius
        n = 30
        dr = r/n
        dt = 0.15
        s = 110*dr
        
        lines = mn.VGroup()
        circ2 = circ.copy()
        circ2.set_color(mn.GREEN)
        for i in range(n):
            fact = (r - (i+1)*dr)/(r - i*dr)
            o = circ.get_center()
            c = mn.Circle(
                radius=r - i*dr,
                color=mn.RED,
                stroke_width=s,
                arc_center=o
            )
            p = c.get_bottom()
            l = mn.Line(
                p, p,
                stroke_width=s,
                color=mn.RED
            )
            t = mn.ValueTracker(0)
            
            # Function to update the line.
            def update_line(l):
                tv = t.get_value()
                p2 = p + (r - i*dr) * tv * mn.RIGHT
                nl = mn.Line(
                    start=p,
                    end=p2,
                    stroke_width=s,
                    color=mn.RED)
                l.become(nl)
            l.add_updater(update_line)
            # Function to update the arc.
            def update_arc(arc):
                tv = t.get_value()
                na = mn.Arc(
                    start_angle=-mn.PI/2,
                    angle=mn.TAU - tv,
                    radius=r - i*dr,
                    stroke_width=s,
                    arc_center=o,
                    color=mn.RED
                )
                na.shift(tv*(r - i*dr)*mn.RIGHT)
                arc.become(na)
            c.add_updater(update_arc)
            ta = t.animate.set_value(mn.TAU)
            b = p + mn.TAU * (r - i*dr) * mn.RIGHT
            self.add(c, l)
            self.play(
                circ2.animate.scale(fact),
                run_time=dt)
            if i < 2:
                self.play(
                    ta,
                    run_time=1.5)
            else:
                self.play(
                    ta,
                    run_time=dt)
            l.clear_updaters()
            lines.add(l)
            c.clear_updaters()

        self.wait(1)
        o = circ.get_center()
        a = circ.get_bottom()
        b = lines[0].get_end()
        
        triangle = mn.Polygon(
            o, a, b,
            color=mn.YELLOW,
            # stroke_width=0,
            # fill_opacity=0.5
        )
        self.play(mn.Create(triangle), run_time=1)
        self.wait(1)
        self.play(mn.Uncreate(lines), run_time=1)
        
        text = mn.MathTex(
            "\\text{مساحة المثلث} = \\text{مساحة القرص}",
            font_size=30,
            tex_template=tex_template_ar
        )
        text.to_edge(mn.UP)
        mobjs = text.submobjects[0].submobjects
        text.submobjects[0].submobjects = mobjs[::-1]

        self.play(
            triangle.animate.set_fill(mn.YELLOW, 0.5))
        self.wait(1)
        self.play(
            mn.Write(text),
            circ.animate.to_edge(mn.UL))
        self.wait(1)
        a1 = o + 0.2*mn.LEFT
        b1 = a + 0.2*mn.LEFT
        dashed11 = mn.DashedLine(o, a1)
        dashed12 = mn.DashedLine(a, b1)
        arrow1 = mn.DoubleArrow(
            a1, b1,
            buff=0,
            tip_length=0.15,
        )
        label1 = mn.Tex(
            "نصف قطر \\\\ القرص",
            font_size=30,
            tex_template=tex_template_ar
        )
        mobjs = label1.submobjects[0].submobjects
        label1.submobjects[0].submobjects = mobjs[::-1]
        label1.rotate(mn.PI/2)
        label1.next_to(arrow1, mn.LEFT)
        self.play(
            mn.Create(dashed11),
            mn.Create(dashed12),
            mn.Create(arrow1),
            mn.Write(label1),
            run_time=1)
        
        a2 = a + 0.2*mn.DOWN
        b2 = b + 0.2*mn.DOWN
        dashed21 = mn.DashedLine(a, a2)
        dashed22 = mn.DashedLine(b, b2)
        
        arrow2 = mn.DoubleArrow(
            a2, b2,
            buff=0,
            tip_length=0.15,
        )
        label2 = mn.Tex(
            "محيط الدائرة",
            font_size=30,
            tex_template=tex_template_ar
        )
        mobjs = label2.submobjects[0].submobjects
        label2.submobjects[0].submobjects = mobjs[::-1]
        label2.next_to(arrow2, mn.DOWN)
        self.play(
            mn.Create(dashed21),
            mn.Create(dashed22),
            mn.Create(arrow2),
            mn.Write(label2),
            run_time=1)
        self.wait(1)
        
        text1 = mn.MathTex(
            "\\text{نصف قطر القرص}\\times \\text{محيط الدائرة} \\times \\frac{1}{2} = \\text{مساحة المثلث}",
            font_size=40,
            tex_template=tex_template_ar
        )
        text1.to_edge(mn.RIGHT)
        mobjs = text1.submobjects[0].submobjects
        text1.submobjects[0].submobjects = mobjs[::-1]
        self.play(mn.Write(text1), run_time=1)
        self.wait(1)
        
        text2 = mn.MathTex(
            "^2\\text{نصف قطر القرص}\\times 2\\pi \\times \\frac{1}{2} = \\text{مساحة القرص}",
            font_size=40,
            tex_template=tex_template_ar
        )
        text2.to_edge(mn.RIGHT)
        self.play(
            mn.TransformMatchingShapes(text1, text2),
            run_time=1)
        self.wait(1)
        
        self.play(
            mn.Uncreate(dashed11),
            mn.Uncreate(dashed12),
            mn.Uncreate(arrow1),
            mn.Uncreate(label1),
            mn.Uncreate(dashed21),
            mn.Uncreate(dashed22),
            mn.Uncreate(arrow2),
            mn.Uncreate(label2),
            mn.Uncreate(triangle),
            mn.Uncreate(text),
            mn.Uncreate(circ),
            run_time=1)
        self.wait(1)
        
        text3 = mn.MathTex(
            "^2\\text{نصف قطر القرص}\\times \\pi = \\text{مساحة القرص}",
            font_size=40,
            tex_template=tex_template_ar
        )
        self.play(
            mn.TransformMatchingShapes(text2, text3),
            run_time=1)
        self.wait(1)
        
        eq.generate_target()
        eq.target.move_to(mn.ORIGIN) # type: ignore
        eq.target.scale(1.5) # type: ignore
        
        self.play(
            mn.FadeOut(text3),
            mn.MoveToTarget(eq),
            run_time=1)
        self.wait(1)
        
        self.play(
            mn.Unwrite(eq),
            run_time=1)
        self.wait(0.5)
        
        self.play(
            mn.FadeOut(title),
            run_time=0.5)
        self.wait(0.5)
        
        