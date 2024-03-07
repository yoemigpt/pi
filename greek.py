import numpy as np
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

partex = """
\\begin{itemize}
\\item محيط الدائرة أكبر من محيط الشكل الداخلي
\\item محيط الدائرة أصغر من محيط الشكل الخارجي
\\end{itemize}
"""

def reverse_mobjects(mobj):
    # reverse the order of the mobjects
    # recursively reverse the submobjects
    for mob in mobj.submobjects:
        if len(mob) > 0:
            reverse_mobjects(mob)
    mobj.submobjects = list(reversed(mobj.submobjects))


class GreekPolygon(mn.Scene):
    def construct(self):
        method = mn.Tex(
            "طريقة أرخميدس",
            font_size=60,
            tex_template=tex_template_ar
        )
        reverse_mobjects(method)
        self.play(mn.Write(method), run_time=3)
        self.wait(1)
        method.generate_target()
        method.target.to_edge(mn.UR) # type: ignore
        method.target.scale(0.5) # type: ignore
        self.play(mn.MoveToTarget(method), run_time=2)
        self.wait(2)
        
        r = 2
        circ = mn.Circle(radius=r)
        self.play(mn.Create(circ), run_time=2)
        self.wait(2)
        self.play(
            circ.animate.shift(mn.LEFT * 2),
            run_time=0.5)
        
        def inscribed(circ, n):
            points = []
            for i in range(n):
                p = circ.point_at_angle(mn.TAU * i / n)
                points.append(p)
            return points, mn.Polygon(*points)
        
        def subscribed(circ, n):
            points = []
            c = circ.get_center()
            r = circ.radius
            a = r / (np.cos(mn.TAU / (2*n)))
            for i in range(n):
                p = circ.point_at_angle(mn.TAU * i / n)
                points.append((p-c) * a / r + c)
            return points, mn.Polygon(*points)



        nc = "عدد الأضلاع: " 
        label = mn.Tex(
            nc,
            font_size=32,
            tex_template=tex_template_ar
        )
        label.to_edge(mn.UP)
        label.align_to(circ, mn.RIGHT)
        self.play(mn.Write(label), run_time=0.5)
        nk = 3
        for k in range(0, nk):
            if k == 0:
                n = 4
            else:
                n = 3 * (2**k)
            _, ins = inscribed(circ, n)
            ins.set_color(mn.BLUE)
            _, sub = subscribed(circ, n)
            sub.set_color(mn.GREEN)
            label2 = mn.Tex(
                nc,
                f"{n}",
                font_size=32,
                tex_template=tex_template_ar
            )
            label2.move_to(label)
            label2.align_to(label, mn.RIGHT)
            self.play(
                mn.TransformMatchingShapes(
                    label, label2, path_arc=0),
                mn.Create(ins),
                mn.Create(sub),
                run_time=2
            )
            label = label2
            self.wait(1)
            if k == nk-1:
                # self.play(mn.FadeOut(label), run_time=0.1)
                par = mn.Tex(
                    partex,
                    font_size=32,
                    tex_template=tex_template_ar
                )
                par.to_edge(mn.RIGHT)
                u = 34
                mobjs = par.submobjects[0].submobjects
                par.submobjects[0].submobjects = mobjs[:u][::-1] + mobjs[u:][::-1]
                self.play(mn.Write(par), run_time=3)
            else:
                self.play(
                    mn.FadeOut(ins),
                    mn.FadeOut(sub),
                    run_time=0.5
                )
                self.wait(1)
        
        self.wait(2)
        
class GreekPolygonExample(mn.Scene):
    def construct(self):
        title = mn.Tex(
            "مثال المربع",
            font_size=60,
            tex_template=tex_template_ar
        )
        mobjs = title.submobjects[0].submobjects
        title.submobjects[0].submobjects = mobjs[::-1]
        
        self.play(mn.Write(title), run_time=2)
        self.wait(0.5)
        
        title.generate_target()
        title.target.to_edge(mn.UR) # type: ignore
        title.target.scale(0.5) # type: ignore
        self.play(mn.MoveToTarget(title), run_time=1)
        self.wait(0.5)
        
        r = 2
        circ = mn.Circle(radius=r)
        self.play(mn.Create(circ), run_time=2)
        self.wait(0.5)
        
        text1 = mn.Tex(
            "قطر الدائرة يساوي $1 $ ",
            font_size=32,
            tex_template=tex_template_ar
        )
        mobjs = text1.submobjects[0].submobjects
        text1.submobjects[0].submobjects = mobjs[::-1]
        text1.next_to(circ, mn.UP)
        text1.shift(mn.UP)
        dashed1 = mn.DashedLine(
            circ.get_left() + 0.5 * r * mn.UP,
            circ.get_left() + 1.6 * r * mn.DOWN,
        )
        dashed2 = mn.DashedLine(
            circ.get_right() + 0.5 * r * mn.UP,
            circ.get_right() + 1.6 * r * mn.DOWN,
        )
        arrow1 = mn.DoubleArrow(
            dashed1.get_end(),
            dashed2.get_end(),
            buff=0,
            tip_length=0.15
        )
        label1 = mn.MathTex(
            "1",
            font_size=32
        )
        label1.next_to(arrow1, mn.DOWN)
        self.play(
            mn.Create(dashed1),
            mn.Create(dashed2),
            mn.Create(arrow1),
            mn.Create(label1),
            run_time=1,
        )
        self.play(mn.Write(text1), run_time=1)
        self.wait(0.5)
        
        def inscribed(circ, n):
            points = []
            for i in range(n):
                p = circ.point_at_angle(mn.TAU * i / n)
                points.append(p)
            return points, mn.Polygon(*points)
        
        _, polygon = inscribed(circ, 4)
        polygon.set_color(mn.BLUE)
        self.play(mn.Create(polygon), run_time=1)
        
        text2 = mn.Tex(
            "إذا كان ضلع المربع $c$:",
            font_size=32,
            tex_template=tex_template_ar
        )
        mobjs = text2.submobjects[0].submobjects
        text2.submobjects[0].submobjects = mobjs[::-1]
        
        text2.next_to(circ, mn.LEFT)
        text2.align_to(text1, mn.UP)
        text2.shift(0.5 * mn.LEFT)
        self.play(mn.Write(text2), run_time=1)
        self.wait(0.5)
        
        eq2 = mn.MathTex(
            "c^2",
            "+",
            "c^2",
            "=",
            "1^2",
            font_size=32
        )
        
        eq2.next_to(text2, mn.DOWN)
        self.play(mn.Write(eq2), run_time=1)
        self.wait(0.5)
        
        eq3 = mn.MathTex(
            "2c^2",
            "=",
            "1",
            font_size=32
        )
        eq3.next_to(eq2, mn.DOWN)
        self.play(
            mn.TransformMatchingShapes(
                eq2, eq3
            ),
            run_time=1
        )
        eq4 = mn.MathTex(
            "c",
            "=",
            "\\frac{1}{\\sqrt{2}}",
            font_size=32
        )
        eq4.next_to(eq3, mn.DOWN)
        self.play(
            mn.TransformMatchingShapes(
                eq3, eq4
            ),
            run_time=1
        )
        
        eq4.generate_target()
        eq4.target.next_to(text2, mn.LEFT) # type: ignore
        self.play(mn.MoveToTarget(eq4), run_time=1)
        self.wait(0.5)
        
        text3 = mn.Tex(
            "محيط المربع الداخلي يساوي $4 c$",
            font_size=32,
            tex_template=tex_template_ar
        )
        mobjs = text3.submobjects[0].submobjects
        text3.submobjects[0].submobjects = mobjs[::-1]
        text3.next_to(text2, mn.DOWN)
        text3.align_to(text2, mn.RIGHT)
        self.play(mn.Write(text3), run_time=1)
        self.wait(0.5)
        
        text4 = mn.Tex(
            "محيط المربع الداخلي يساوي $4\\frac{1}{\\sqrt{2}}$",
            font_size=32,
            tex_template=tex_template_ar
        )
        mobjs = text4.submobjects[0].submobjects
        text4.submobjects[0].submobjects = mobjs[::-1]
        text4.move_to(text3)
        text4.align_to(text3, mn.RIGHT)
        self.play(
            mn.TransformMatchingShapes(
                text3, text4
            ),
            run_time=1
        )
        self.wait(0.5)
        
        text5 = mn.Tex(
            "محيط المربع الداخلي يساوي $2\\sqrt{2}$",
            font_size=32,
            tex_template=tex_template_ar
        )
        mobjs = text5.submobjects[0].submobjects
        text5.submobjects[0].submobjects = mobjs[::-1]
        text5.move_to(text4, mn.DOWN)
        text5.align_to(text4, mn.RIGHT)
        self.play(
            mn.TransformMatchingShapes(
                text4, text5
            ),
            run_time=1
        )
        self.wait(0.5)
        eq5 = mn.MathTex(
            "\\boxed{2\\sqrt{2}\\le \\pi}",
            font_size=64
        )
        eq5.next_to(text5, mn.DOWN)
        self.play(mn.Write(eq5), run_time=1)
        self.wait(0.5)
        
        self.play(
            mn.FadeOut(text5),
            mn.FadeOut(polygon),
            mn.FadeOut(text2),
            mn.FadeOut(eq4),
            run_time=1
        )
        
        self.play(
            eq5.animate.to_edge(mn.RIGHT),
            run_time=1
        )
        
        def subscribed(circ, n):
            points = []
            c = circ.get_center()
            r = circ.radius
            a = r / (np.cos(mn.TAU / (2*n)))
            for i in range(n):
                p = circ.point_at_angle(mn.TAU * i / n)
                points.append((p-c) * a / r + c)
            return points, mn.Polygon(*points)
    
        _, polygon = subscribed(circ, 4)
        polygon.set_color(mn.GREEN)
        self.play(mn.Create(polygon), run_time=1)
        self.wait(0.5)
        
        text2 = mn.Tex(
            "إذا كان ضلع المربع $c$:",
            font_size=32,
            tex_template=tex_template_ar
        )
        mobjs = text2.submobjects[0].submobjects
        text2.submobjects[0].submobjects = mobjs[::-1]
        text2.next_to(circ, mn.LEFT)
        text2.align_to(text1, mn.UP)
        text2.shift(0.5 * mn.LEFT)
        self.play(mn.Write(text2), run_time=1)
        
        eq2 = mn.MathTex(
            "c",
            "=",
            "1",
            font_size=32
        )
        eq2.next_to(text2, mn.DOWN)
        self.play(
            polygon.animate.rotate(mn.PI / 4),
            # mn.Write(eq2),
            run_time=1)
        self.wait(0.5)
        
        self.play(mn.Write(eq2), run_time=1)
        self.wait(0.5)
        
        self.play(
            eq2.animate.next_to(text2, mn.LEFT),
            run_time=1)
        self.wait(0.5)
        
        text3 = mn.Tex(
            "محيط المربع الخارجي يساوي $4 c$",
            font_size=32,
            tex_template=tex_template_ar
        )
        mobjs = text3.submobjects[0].submobjects
        text3.submobjects[0].submobjects = mobjs[::-1]
        text3.next_to(text2, mn.DOWN)
        text3.align_to(text2, mn.RIGHT)
        self.play(mn.Write(text3), run_time=1)
        self.wait(0.5)
        
        text4 = mn.Tex(
            "محيط المربع الخارجي يساوي $4$",
            font_size=32,
            tex_template=tex_template_ar
        )
        mobjs = text4.submobjects[0].submobjects
        text4.submobjects[0].submobjects = mobjs[::-1]
        text4.move_to(text3)
        text4.align_to(text3, mn.RIGHT)
        self.play(
            mn.TransformMatchingShapes(
                text3, text4
            ),
            run_time=1
        )
        self.wait(0.5)
        
        eq3 = mn.MathTex(
            "\\boxed{4\\ge \\pi}",
            font_size=64
        )
        eq3.next_to(text4, mn.DOWN)
        self.play(mn.Write(eq3), run_time=1)
        self.wait(0.5)
        
        self.play(
            mn.FadeOut(polygon),
            mn.FadeOut(text2),
            mn.FadeOut(eq2),
            mn.FadeOut(text4),
            run_time=1
        )
        
        self.play(
            eq3.animate.next_to(eq5, mn.DOWN),
            run_time=1
        )
        
        self.wait(0.5)
        self.play(
            mn.Uncreate(circ),
            mn.Uncreate(dashed1),
            mn.Uncreate(dashed2),
            mn.Uncreate(arrow1),
            mn.Unwrite(label1),
            mn.Unwrite(text1),
            run_time=1
        )
        self.wait(0.5)
        
        eq = mn.MathTex(
            "\\boxed{",
            "2\\sqrt{2}",
            "\\le",
            "\\pi",
            "\\le 4",
            "}",
            font_size=64
        )
        self.play(
            mn.TransformMatchingShapes(
                mn.VGroup(eq5, eq3),
                eq
            ),
            run_time=1
        )
        
        self.wait(2)
        
class GreekPolygonBounds(mn.Scene):
    def construct(self):
        title = mn.Tex(
            "حدود قيمة $\\pi$",
            font_size=60,
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
        
        sides = [4, 6, 12, 24, 48, 96]
        lowers = {
            4: "2\\sqrt{2}",
            6: "3",
            12: "12\\left(\\frac{\\sqrt{2-\\sqrt{3}}}{2}\\right)",
            24: "24\\left(\\frac{\\sqrt{2-\\sqrt{2+\\sqrt{3}}}}{2}\\right)",
            48: "48\\left(\\frac{\\sqrt{2-\\sqrt{2+\\sqrt{2+\\sqrt{3}}}}}{2}\\right)",
            96: "96\\left(\\frac{\\sqrt{2-\\sqrt{2+\\sqrt{2+\\sqrt{2+\\sqrt{3}}}}}}{2}\\right)"
        }
        uppers = {
            4: "4",
            6: "2\\sqrt{3}",
            12: "12\\left(\\frac{\\sqrt{2-\\sqrt{3}}}{\\sqrt{2+\\sqrt{3}}}\\right)",
            24: "24\\left(\\frac{\\sqrt{2-\\sqrt{2+\\sqrt{3}}}}{\\sqrt{2+\\sqrt{2+\\sqrt{3}}}}\\right)",
            48: "48\\left(\\frac{\\sqrt{2-\\sqrt{2+\\sqrt{2+\\sqrt{3}}}}}{\\sqrt{2+\\sqrt{2+\\sqrt{2+\\sqrt{3}}}}}\\right)",
            96: "96\\left(\\frac{\\sqrt{2-\\sqrt{2+\\sqrt{2+\\sqrt{2+\\sqrt{3}}}}}}{\\sqrt{2+\\sqrt{2+\\sqrt{2+\\sqrt{2+\\sqrt{3}}}}}}\\right)"
        }
        
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
        
        mid = mn.MathTex(
            "\\le",
            "\\pi",
            "\\le",
            font_size=40
        )
        low1 = mn.MathTex(
            "",
            font_size=40
        )
        up1 = mn.MathTex(
            "",
            font_size=40
        )
        low1.next_to(mid, mn.LEFT)
        up1.next_to(mid, mn.RIGHT)
        label = mn.Tex(
            "عدد الأضلاع: ",
            font_size=40,
            tex_template=tex_template_ar
        )
        label.to_edge(mn.UP)
        mobjs = label.submobjects[0].submobjects
        label.submobjects[0].submobjects = mobjs[::-1]
        self.play(mn.Write(label), run_time=0.5)
        
        label1 = mn.Tex(
            "",
            font_size=40,
            tex_template=tex_template_ar
        )
        label1.next_to(label, mn.LEFT)
        self.play(mn.Write(mid), run_time=0.5)
        for n in sides:
            label2 = mn.Tex(
                f"{n}",
                font_size=40,
                tex_template=tex_template_ar
            )
            label2.next_to(label, mn.LEFT)
            
            low2 = mn.MathTex(
                lowers[n],
                font_size=40
            )
            low2.next_to(mid, mn.LEFT)
            up2 = mn.MathTex(
                uppers[n],
                font_size=40
            )
            up2.next_to(mid, mn.RIGHT)
            self.play(
                mn.TransformMatchingShapes(
                    label1, label2
                ),
                run_time=0.5
            )
            label1 = label2
            self.play(
                mn.TransformMatchingShapes(
                    low1, low2
                ),
                mn.TransformMatchingShapes(
                    up1, up2
                ),
                run_time=1
            )
            low1 = low2
            up1 = up2
            self.wait(1)
        
        low = "3.1408"
        up = "3.1492"
        low2 = mn.MathTex(
            low,
            font_size=40
        )
        
        up2 = mn.MathTex(
            up,
            font_size=40
        )
        low2.next_to(mid, mn.LEFT)
        up2.next_to(mid, mn.RIGHT)
        self.play(
            mn.TransformMatchingShapes(
                low1, low2
            ),
            mn.TransformMatchingShapes(
                up1, up2
            ),
            run_time=1
        )
        self.wait(6)
        