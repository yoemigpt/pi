import manim as mn
import numpy as np

PITEX = "$\\pi$"
PIDIGITS = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337863849961244352961"

class DateToPI(mn.Scene):
    def construct(self):
        fs = 128
        s = 0.5
        d = "14/03/2024"
        t14 = "3.14"
        ds = PIDIGITS[3:31]

        date = mn.Text(d, font_size=fs)
        date2 = mn.Text(d[:5], font_size=fs)
        three14 = mn.Tex(f"${t14}$", font_size=fs)
        pi = mn.Tex(f"${ds}\\ldots$", font_size=fs)
        eq = mn.Tex("=", font_size=fs)
        pitex = mn.Tex(PITEX, font_size=fs)
        
        self.play(mn.Write(date))
        self.wait(1)
        
        self.play(mn.Transform(date, date2))
        self.wait(1)
        
        self.play(mn.Transform(date, three14, replace_mobject_with_target_in_scene=True))
        self.wait(1)
        
        three14.generate_target()
        three14.target.shift(4*mn.LEFT) # type: ignore
        three14.target.scale(s) # type: ignore
        self.play(mn.MoveToTarget(three14))
        self.wait(1)

        pi.scale(s)
        pi.next_to(three14, mn.RIGHT)
        pi.shift(0.225*mn.LEFT)
        self.play(mn.Write(pi))
        self.wait(1)

        eq.scale(s)
        eq.next_to(three14, mn.LEFT)
        pitex.scale(s)
        pitex.next_to(eq, mn.LEFT)
        self.play(mn.Write(pitex))
        self.play(mn.Write(eq))
        self.wait(1)
        
        self.play(mn.FadeOut(three14, pi, eq))
        self.wait(1)
        
        pitex.generate_target()
        pitex.target.move_to(mn.ORIGIN) # type: ignore
        pitex.target.scale(6) # type: ignore
        pitex.target.set_color(mn.RED) # type: ignore
        self.play(mn.MoveToTarget(pitex))
        self.wait(1)
        

class CirclePI(mn.Scene):
    r = 1
    
    def labels(self, dots, label, a):
        labels = mn.VGroup()
        dasheds = mn.VGroup()
    
        for dot in dots:
            p = dot.get_center()
            q = p + a*mn.DOWN
            dashed = mn.DashedLine(p, q)
            dasheds.add(dashed)
        
        lines = mn.VGroup()
        for i in range(len(dots) - 1):
            p = dasheds[i].get_center()
            q = dasheds[i+1].get_center()
            l = mn.DoubleArrow(p, q,
                               buff=0,
                               tip_length=0.2)
            labels.add(mn.Tex(label))
            labels[i].next_to(l, mn.DOWN, buff=0.1)
            lines.add(l)

        group = mn.VGroup()
        group.add(dasheds)
        for line, label in zip(lines, labels):
            group.add(line)
            group.add(label)
        return group
    
    def construct(self):
        r = self.r
        u = 3*r*mn.LEFT + 4*r*mn.DOWN
        circ = mn.Circle(
            radius=r,
            color=mn.BLUE
        )
        self.add(circ)
        self.wait(1)
        self.play(circ.animate.shift(2.5*r*mn.UP))
        
        c = circ.copy()
        c.shift(u)
        self.play(mn.TransformFromCopy(circ, c))
        
        circles = mn.VGroup()
        circles.add(c)
        for _ in range(3):
            c1 = c.copy()
            c1.shift(2*r*mn.RIGHT)
            self.play(mn.TransformFromCopy(c, c1))
            c = c1
            circles.add(c)
        self.wait(1)
        
        # Create dots on each left side
        # of the circle:
        dots = mn.VGroup()
        c = circles[0].get_left()
        for i in range(5):
            dot = mn.Dot(c+2*i*r*mn.RIGHT)
            dots.add(dot)
        self.play(mn.Create(dots), run_time=2)
        self.wait(1)

        # Remove circles.
        self.play(mn.FadeOut(circles))
        self.wait(1)
        
        self.play(dots.animate.shift(r*mn.UP))
        self.wait(1)
        
        group = self.labels(dots, '$d$', 0.5)
        self.play(mn.Create(group), run_time=3)
        self.wait(1)

        # Move the circle to the first dot.
        c = dots[0].get_center()
        q = c + r*mn.UP
        self.play(circ.animate.move_to(q))
        
        t = mn.ValueTracker(0)
        p = circ.get_bottom()
        line = mn.Line(start=p, end=p)
        
        self.add(line)
        
        # Function to update the line.
        def update_line(l):
            tv = t.get_value()
            p2 = p + r * tv * mn.RIGHT
            nl = mn.Line(start=p, end=p2, color=mn.RED)
            l.become(nl)
        
        # Function to update the arc.
        def update_arc(arc):
            tv = t.get_value()
            na = mn.Arc(
                start_angle=-mn.PI/2,
                angle=mn.TAU - tv,
                radius=r,
                arc_center=q,
                color=mn.RED
            )
            na.shift(tv*r*mn.RIGHT)
            arc.become(na)

        circ.add_updater(update_arc)
        line.add_updater(update_line)
        
        ta = t.animate.set_value(mn.TAU)
        self.play(ta, run_time=6)
        self.wait(1)
        
        p = dots[0].get_center()
        q = p + mn.TAU * r * mn.RIGHT
        
        dasheds = mn.VGroup()
        a = p + 0.5*r*mn.UP
        b = q + 0.5*r*mn.UP
        
        dashed = mn.DashedLine(p, a, color=mn.RED)
        dasheds.add(dashed)
        dashed = mn.DashedLine(q, b, color=mn.RED)
        dasheds.add(dashed)
        self.play(mn.Create(dasheds))
        
        a = dasheds[0].get_center()
        b = dasheds[1].get_center()
        
        l = mn.DoubleArrow(a, b, buff=0, tip_length=0.2, color=mn.RED)
        label = mn.Tex("$\pi d$", color=mn.RED) # type: ignore
        label.next_to(l, mn.UP, buff=0.1)
        self.play(mn.Create(l), mn.Create(label))
        self.wait(1)
        
        approx = mn.Tex("$\\approx 3.14 d$", color=mn.RED) # type: ignore
        approx.next_to(label, mn.RIGHT, buff=0.1)
        self.play(mn.Write(approx))
        
class Circle2PI(mn.Scene):
    def construct(self):
        r = 1.5
        circ = mn.Circle(
            radius=r,
            color=mn.BLUE,
            fill_opacity=1
        )
        self.play(mn.Create(circ))
        self.wait(1)
        
        self.play(
            circ.animate
            .shift(5*mn.LEFT)
            .shift(2*mn.UP))
        
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
                ta,
                run_time=dt)
            l.clear_updaters()
            lines.add(l)
            c.clear_updaters()

        self.wait(1)
        
        f = 2.25
        self.play(lines.animate.shift(f*mn.RIGHT))
        
        o = circ.get_center()
        b = circ.get_bottom()
        
        doto = mn.Dot(o, color=mn.WHITE)
        dotb = mn.Dot(b, color=mn.WHITE)
        self.play(mn.Create(doto), mn.Create(dotb))
        self.wait(1)
        self.play(
            doto.animate.shift(f*mn.RIGHT),
            dotb.animate.shift(f*mn.RIGHT))
        self.wait(1)
        
        o = doto.get_center()
        b = dotb.get_center()
        a = b + mn.TAU * r * mn.RIGHT
        dota = mn.Dot(a, color=mn.WHITE)
        self.play(mn.Create(dota))
        triangle = mn.Polygon(o, b, a, color=mn.WHITE)
        self.play(mn.Create(triangle))
        self.wait(1)
        self.play(
            mn.FadeOut(dota),
            mn.FadeOut(dotb),
            mn.FadeOut(doto),
            mn.FadeOut(lines))
        
        arrow = mn.DoubleArrow(
            circ.get_center(),
            circ.get_bottom(),
            buff=0,
            tip_length=0.2,
            color=mn.WHITE
        )
        label = mn.Tex("$r$", color=mn.WHITE)
        label.next_to(arrow, mn.LEFT)
        self.play(mn.Create(arrow), mn.Write(label))
        
        arrow1 = mn.DoubleArrow(
            o, b,
            buff=0, 
            tip_length=0.2)
        arrow1.shift(0.15*mn.LEFT)
        label1 = mn.Tex("$r$")
        label1.next_to(arrow1, mn.LEFT)
        arrow2 = mn.DoubleArrow(
            b, a,
            buff=0, 
            tip_length=0.2
        )
        arrow2.shift(0.15*mn.DOWN)
        label2 = mn.Tex("$2\\pi r$")
        label2.next_to(arrow2, mn.DOWN)
        self.play(
            mn.Create(arrow1),
            mn.Write(label1))
        self.play(
            mn.Create(arrow2),
            mn.Write(label2))
        
        text = mn.Tex(
            "$A =\\frac12\\times 2\\pi r \\times r$",
            font_size=64
        )
        text.next_to(label2, mn.DOWN)
        self.play(mn.Write(text))
        self.wait(1)
        
        text2 = mn.Tex(
            "$A =\\pi r^2$",
            font_size=64
        )
        text2.move_to(text)
        self.play(
            mn.Transform(text, text2),
            replace_mobject_with_target_in_scene=True
        )
        self.wait(1)
        
        text = mn.Tex(
            "$r = 1 \\quad \\implies \\quad A = \\pi$",
            font_size=64
        )
        text.move_to(text2)
        self.play(mn.Transform(text2, text))
        self.wait(2)
        
class ArchimedesPI(mn.Scene):
    def inscribed(self, circ, n):
        points = []
        pr = 0.5/n
        for i in range(n):
            p = circ.point_from_proportion(pr + i/n)
            points.append(p)
        return mn.Polygon(*points), points
    
    def subscribed(self, circ, n):
        a = mn.PI / n
        r = 1 / np.cos(a)
        pr = 0.5/n
        points = []
        c = circ.get_center()
        for i in range(n):
            p = circ.point_from_proportion(pr + i/n)
            points.append(r * (p-c) + c)
        return mn.Polygon(*points), points
    
    def construct(self):
        circ = mn.Circle(radius=1, color=mn.BLUE)
        circ.scale(3)
        self.play(mn.Create(circ))
        self.wait(1)
        
        for n in [4, 6, 12]:
            polygons = mn.VGroup()
            ins, _ = self.inscribed(circ, n)
            ins.set_color(mn.RED)
            polygons.add(ins)
            self.play(mn.Create(ins))
            self.wait(1)
            
            subs, _ = self.subscribed(circ, n)
            subs.set_color(mn.GREEN)
            polygons.add(subs)
            self.play(mn.Create(subs))
            self.wait(1)
            self.play(mn.FadeOut(polygons), run_time=1)

        self.play(
            circ.animate
            .scale(0.5)
            .shift(5*mn.LEFT), run_time=1)
        
        
        a = circ.get_left()
        b = circ.get_right()
        
        arrow = mn.DoubleArrow(
            a, b,
            buff=0, 
            tip_length=0.2)
        label = mn.Tex("$d=1$")
        label.next_to(arrow, mn.UP, buff=0.1)
        self.play(
            mn.FadeIn(arrow),
            mn.Write(label))
        self.wait(2)
        
        text2 = mn.Tex("$d=1\\quad\\implies\\quad P=\\pi$")
        text2.shift(3*mn.UP)
        self.play(mn.Write(text2))
        self.wait(2)
        
        self.play(
            mn.FadeOut(arrow),
            mn.FadeOut(label))
        
        n = 4
        ins, vertices = self.inscribed(circ, n)
        ins.set_color(mn.RED)
        self.play(mn.Create(ins), run_time=1)
        self.wait(1)
        
        divider1 = mn.Line(
            start=mn.ORIGIN,
            end=mn.ORIGIN + 2*mn.RIGHT,
            color=mn.RED
        )
        divider1.next_to(text2, mn.DOWN)
        divider1.align_to(text2, mn.LEFT)
        
        dashed1 = mn.DashedLine(
            vertices[0],
            vertices[0] + mn.UP,
            color=mn.RED
        )
        dashed2 = mn.DashedLine(
            vertices[1],
            vertices[1] + mn.UP,
            color=mn.RED
        )
        arrow1 = mn.DoubleArrow(
            dashed1.get_center(),
            dashed2.get_center(),
            buff=0,
            tip_length=0.2,
            color=mn.RED
        )
        
        label1 = mn.Tex("$c$", color=mn.RED)
        label1.next_to(arrow1, mn.UP, buff=0)
        
        self.play(
            mn.Create(dashed1),
            mn.Create(dashed2))
        self.play(
            mn.Create(arrow1),
            mn.Write(label1))
        self.wait(1)
        
        text3 = mn.Tex("$P_L = 4c$") # type: ignore
        text3.next_to(divider1, mn.DOWN)
        text3.align_to(divider1, mn.LEFT)
        self.play(mn.Write(text3))
        self.wait(1)
        
        arrow2 = mn.DoubleArrow(
            vertices[0],
            vertices[2],
            buff=0,
            tip_length=0.2
        )
        label2 = mn.Tex("$d$")
        label2.rotate(0.25*mn.PI)
        label2.move_to(arrow2.get_center())
        label2.shift(0.2*mn.LEFT)
        label2.shift(0.2*mn.UP)
        
        self.play(mn.Create(arrow2))
        self.play(mn.Write(label2))
        self.wait(1)
        
        text4 = mn.Tex("$c^2 + c^2 = d^2$")
        text4.next_to(text3, mn.DOWN)
        text4.align_to(text3, mn.LEFT)
        self.play(mn.Write(text4), run_time=2)
        
        text5 = mn.Tex("$2c^2 = d^2$")
        text5.next_to(text3, mn.DOWN)
        text5.align_to(text3, mn.LEFT)
        self.play(
            mn.Transform(text4, text5),
            replace_mobject_with_target_in_scene=True)
        
        text4 = mn.Tex("$c = \\frac{d}{\\sqrt{2}}$")
        text4.next_to(text3, mn.DOWN)
        text4.align_to(text3, mn.LEFT)
        self.play(
            mn.Transform(text5, text4),
            replace_mobject_with_target_in_scene=True)
        
        text5 = mn.Tex("$c = \\frac{1}{\\sqrt{2}}$")
        text5.next_to(text3, mn.DOWN)
        text5.align_to(text3, mn.LEFT)
        self.play(
            mn.Transform(text4, text5),
            replace_mobject_with_target_in_scene=True)
        
        text4 = mn.Tex("$P_L = 4\\times\\frac{1}{\\sqrt{2}} = 2\\sqrt{2}$")
        text4.next_to(divider1, mn.DOWN)
        text4.align_to(divider1, mn.LEFT)
        
        self.play(
            mn.Transform(text3, text4),
            replace_mobject_with_target_in_scene=True)
        self.wait(1)

        self.play(
            mn.FadeOut(arrow1),
            mn.FadeOut(label1),
            mn.FadeOut(dashed1),
            mn.FadeOut(dashed2),
            mn.FadeOut(arrow2),
            mn.FadeOut(label2),
            mn.FadeOut(text5))
        
        text6 = mn.Tex("$P\\geq P_L$") # type: ignore
        text6.next_to(text4, mn.DOWN)
        text6.align_to(text4, mn.LEFT)
        self.play(mn.Write(text6))
        self.wait(1)
        
        text7 = mn.Tex("$\\quad\\implies\\quad\\pi\\geq 2\\sqrt{2}$")
        text7.next_to(text6, mn.RIGHT)
        self.play(mn.Write(text7))
        
        self.play(
            mn.FadeOut(ins),
            mn.FadeOut(text3),
            mn.FadeOut(text4),
            mn.FadeOut(text6),
            mn.FadeOut(text7))
    
        text83leqpi = mn.Tex("$2\\sqrt{2} \\leq \\pi$")
        text83leqpi.shift(3*mn.UP).shift(5*mn.RIGHT)
        self.play(mn.Write(text83leqpi))
        self.wait(1)
        
        n = 4
        subs, vertices = self.subscribed(circ, n)
        subs.set_color(mn.RED)
        self.play(mn.Create(subs), run_time=1)
        self.wait(1)
        
        dashed1 = mn.DashedLine(
            vertices[0],
            vertices[0] + mn.UP,
            color=mn.RED)
        dashed2 = mn.DashedLine(
            vertices[1],
            vertices[1] + mn.UP,
            color=mn.RED)
        arrow1 = mn.DoubleArrow(
            dashed1.get_center(),
            dashed2.get_center(),
            buff=0,
            tip_length=0.2,
            color=mn.RED)
        label1 = mn.Tex("$d$", color=mn.RED)
        label1.next_to(arrow1, mn.UP, buff=0.1)
        
        self.play(
            mn.Create(dashed1),
            mn.Create(dashed2))
        self.play(
            mn.Create(arrow1),
            mn.Write(label1))
        self.wait(1)
        
        textPU4d = mn.Tex("$P_U = 4d$")
        textPU4d.next_to(divider1, mn.DOWN)
        textPU4d.align_to(divider1, mn.LEFT)
        self.play(mn.Write(textPU4d))
        self.wait(1)
        
        textPU4 = mn.Tex("$P_U = 4$")
        textPU4.next_to(divider1, mn.DOWN)
        textPU4.align_to(divider1, mn.LEFT)
        self.play(
            mn.Transform(textPU4d, textPU4),
            replace_mobject_with_target_in_scene=True)
        self.wait(1)
        
        text3 = mn.Tex("$P_U\\geq P$")
        text3.next_to(textPU4, mn.DOWN)
        text3.align_to(textPU4, mn.LEFT)
        self.play(mn.Write(text3))
        self.wait(1)
        
        text4 = mn.Tex("$\\quad\\implies \\quad\\pi\\leq4$")
        text4.next_to(text3, mn.RIGHT)
        self.play(mn.Write(text4))
        self.wait(1)
        
        self.play(
            mn.FadeOut(text3),
            mn.FadeOut(text4))        
        textPiLeq4 = mn.Tex("$\\pi\\leq4$") 
        textPiLeq4.next_to(text83leqpi, mn.DOWN)
        textPiLeq4.align_to(text83leqpi, mn.LEFT)
        self.play(
            mn.FadeOut(textPU4),
            mn.FadeOut(textPU4d))
        self.wait(1)
        
        self.play(mn.Write(textPiLeq4))
        self.wait(1)
        
        self.play(
            mn.FadeOut(subs),
            mn.FadeOut(arrow1),
            mn.FadeOut(label1),
            mn.FadeOut(dashed1),
            mn.FadeOut(dashed2),
            mn.FadeOut(text2),
            mn.FadeOut(text83leqpi),
            mn.FadeOut(textPiLeq4),
        )
        
        #########################
        top = mn.Tex("Archimedes' method")
        top.shift(3*mn.UP).shift(1.5*mn.RIGHT)
        self.play(circ.animate.scale(1.75).shift(1.25*mn.RIGHT))
        prev = top
        
        lowers = {
            4: "2\\sqrt{2}",
            6: "3",
            12: "12\\left[\\frac{\\sqrt{2-\\sqrt{3}}}{2}\\right]",
            24: "24\\left[\\frac{\\sqrt{2-\\sqrt{2+\\sqrt{3}}}}{2}\\right]"
        }
        uppers = {
            4: "4",
            6: "2\\sqrt{3}",
            12: "12\\left[\\frac{\\sqrt{2-\\sqrt{3}}}{\\sqrt{2+\\sqrt{3}}}\\right]",
            24: "24\\left[\\frac{\\sqrt{2-\\sqrt{2+\\sqrt{3}}}}{\\sqrt{2+\\sqrt{2+\\sqrt{3}}}}\\right]"
        }
        labels = mn.VGroup()
        for n in [4, 6, 12, 24]:
            ins, _ = self.inscribed(circ, n)
            ins.set_color(mn.RED)
            subs, _ = self.subscribed(circ, n)
            subs.set_color(mn.GREEN)
            label = mn.Tex(
                f"$n={n}:\\quad\\quad{lowers[n]}\\leq \\pi\\leq {uppers[n]}$",
                font_size=32)
            label.next_to(prev, mn.DOWN)
            label.align_to(prev, mn.LEFT)
            self.play(
                mn.Create(ins),
                mn.Create(subs),
                mn.Write(label),
                run_time=1
            )
            prev = label
            labels.add(label)
            self.wait(1)
            self.play(mn.FadeOut(ins), mn.FadeOut(subs))
            self.wait(1)
        
        self.wait(1)
        self.play(mn.FadeOut(labels))
        self.play(mn.FadeOut(circ))
        
        text = mn.Tex(
            "$n=96$",
            font_size=64
        )
        self.play(mn.Write(text))
        text.generate_target()
        text.target.move_to(mn.ORIGIN + 4*mn.LEFT + 3*mn.UP) # type: ignore
        text.target.scale(0.5) # type: ignore
        self.play(mn.MoveToTarget(text))
        
        low = "96\\left[\\frac{\\sqrt{2-\\sqrt{2+\\sqrt{2+\\sqrt{2 + \\sqrt{3}}}}}}{2}\\right]"
        up = "96\\left[\\frac{\\sqrt{2-\\sqrt{2+\\sqrt{2+\\sqrt{2 + \\sqrt{2+\\sqrt{3}}}}}}}{\\sqrt{2+\\sqrt{2+\\sqrt{2+\\sqrt{2 + \\sqrt{3}}}}}}\\right]"
        equation = mn.Tex(
            f"${low}\\leq \\pi \\leq {up}$",
            font_size=32
        )
        self.play(mn.Write(equation))
        self.wait(1)
        
        low2 = 3.14103195
        up2 = 3.14271460
        equation2 = mn.Tex(
            f"${low2}\\leq \\pi \\leq {up2}$",
            font_size=32
        )
        self.play(
            mn.Transform(equation, equation2)
        )
        self.wait(4)

class BinomialPI(mn.Scene):
    def construct(self):
        eq = mn.Tex("$=$", font_size=64)
        eq.shift(2*mn.LEFT)
        eq.shift(1.5*mn.UP)
        
        lhs1 = mn.Tex(
            "$\\left(1+x\\right)^2$",
            font_size=64
        )
        rhs1 = mn.Tex(
            "$1+2x+x^2$",
            font_size=64
        )
        lhs1.next_to(eq, mn.LEFT)
        rhs1.next_to(eq, mn.RIGHT)
        self.play(mn.Write(lhs1))
        self.play(mn.Write(eq))
        self.wait(1)
        self.play(mn.Write(rhs1))
        
        self.play(
            mn.FadeOut(lhs1),
            mn.FadeOut(eq),
            mn.FadeOut(rhs1)
        )
        
        lhs2 = mn.Tex(
            "$\\left(1+x\\right)^3$",
            font_size=64
        )
        rhs2 = mn.Tex(
            "$1+3x+3x^2+x^3$",
            font_size=64
        )
        lhs2.next_to(eq, mn.LEFT)
        rhs2.next_to(eq, mn.RIGHT)
        
        self.play(mn.Write(lhs2))
        self.play(mn.Write(eq))
        self.wait(1)
        self.play(mn.Write(rhs2))
        self.wait(1)
        
        self.play(
            mn.FadeOut(lhs2),
            mn.FadeOut(eq),
            mn.FadeOut(rhs2)
        )
        
        lhsn = mn.Tex(
            "$\\left(1+x\\right)^n$",
            font_size=64
        )
        rhsn = mn.Tex(
            "$\\sum_{k=0}^{n} \\binom{n}{k} x^k$",
            font_size=64
        )
        lhsn.next_to(eq, mn.LEFT)
        rhsn.next_to(eq, mn.RIGHT)
        self.play(mn.Write(lhsn))
        self.play(mn.Write(eq))
        self.wait(1)
        
        self.play(mn.Write(rhsn))
        self.wait(1)
        
        binom_n = mn.Tex(
            "$\\binom{n}{k} = \\frac{n\\times (n-1) \\times \\cdots\\times (n-k+1)}{k\\times(k-1)\\times \\cdots \\times 1},$",
            font_size=64
        )
        
        k_n = mn.Tex(
            "$k=0,\\ldots,n, \\; n\\in\\mathbb N$",
            font_size=52)
        
        binom_n.next_to(eq, mn.DOWN)
        binom_n.shift(mn.DOWN).shift(mn.RIGHT)
        k_n.next_to(binom_n, mn.DOWN)
        k_n.align_to(binom_n, mn.RIGHT)
        self.play(mn.Write(binom_n))
        self.play(mn.Write(k_n))
        self.wait(1)
        
        self.play(
            mn.FadeOut(lhsn),
            mn.FadeOut(eq),
            mn.FadeOut(rhsn)
        )
        
        lhsr = mn.Tex(
            "$\\left(1+x\\right)^r$",
            font_size=64
        )
        rhsr = mn.Tex(
            "$\\sum_{k=0}^{\\infty} \\binom{r}{k} x^k$",
            font_size=64
        )
        lhsr.next_to(eq, mn.LEFT)
        rhsr.next_to(eq, mn.RIGHT)
        self.play(mn.Write(lhsr))
        self.play(mn.Write(eq))
        self.wait(1)
        self.play(mn.Write(rhsr))
        self.wait(1)
        
        self.play(
            mn.FadeOut(binom_n),
            mn.FadeOut(k_n),
        )
        
        binom_r = mn.Tex(
            "$\\binom{r}{k} = \\frac{r\\times (r-1) \\times \\cdots\\times (r-k+1)}{k\\times(k-1)\\times \\cdots \\times 1},$",
            font_size=64
        )
        k_r = mn.Tex(
            "$k=0,1,2,\\ldots, \\; r\\in\\mathbb R$",
            font_size=52)
        
        binom_r.next_to(eq, mn.DOWN)
        binom_r.shift(mn.DOWN).shift(mn.RIGHT)
        k_r.next_to(binom_r, mn.DOWN)
        k_r.align_to(binom_r, mn.RIGHT)
        self.play(mn.Write(binom_r))
        self.play(mn.Write(k_r))
        self.wait(1)

class NewtonPI(mn.Scene):
    def construct(self):
        def f(x):
            return np.sqrt(1-x**2)

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
        ax.to_edge(mn.UL)
        ax_labels = ax.get_axis_labels(
            x_label=mn.Tex("$x$"),
            y_label=mn.Tex("$y$")
        )
        group = mn.VGroup(ax, ax_labels)
        
        graph = ax.plot(
            f, x_range=[0, 1, 0.001],
            use_smoothing=True,
            color=mn.BLUE)
        group.add(graph)
        
        f1 = mn.MathTex(
            "f(x)", "=", "\\sqrt{1-x^2}"
        ).to_edge(mn.UP)
        
        self.play(
            mn.DrawBorderThenFill(ax),
            mn.Write(ax_labels),
            run_time=2)
        self.play(
            mn.Create(graph),
            mn.Write(f1),
            run_time=2)
        self.wait(1)
        
        area = ax.get_area(
            graph, x_range=(0, 1),
            color=mn.GREEN, opacity=0.5)
        group.add(area)

        F1 = mn.MathTex(
            "\\int\\limits_0^1", "f(x)", "\\,", "\\mathrm dx", "=", "\\frac{\\pi}{4}",
        ).next_to(ax, mn.DOWN)
        
        self.play(
            mn.Create(area),
            mn.Write(F1),
            run_time=3)
        self.wait(1)
        
        f2 = mn.MathTex(
            "f(x)", "=", "\\left(1-x^2\\right)^{\\frac12}"
        ).move_to(f1).align_to(f1, mn.LEFT)
        
        self.play(
            mn.TransformMatchingTex(
                f1, f2, 
                transform_mismatches=True
            ),
            run_time=2)
        
        f3 = mn.MathTex(
            "f(x)", "=", "\\left(1-x^2\\right)^{\\frac12}", "=", "\\sum_{n=0}^\\infty", "\\binom{\\frac12}{n} (-x^2)^n"
        ).move_to(f2).align_to(f2, mn.LEFT)
        
        self.play(
            mn.TransformMatchingTex(f2, f3,
            transform_mismatches=True),
            run_time=2)
        
        f4 = mn.MathTex(
            "f(x)", "=", "\\left(1-x^2\\right)^{\\frac12}", "=", "\\sum_{n=0}^\\infty", "(-1)^n\\binom{\\frac12}{n} x^{2n}"
        ).move_to(f2).align_to(f2, mn.LEFT)
        
        self.play(
            mn.TransformMatchingTex(
                f3, f4,
                transform_mismatches=True),
            run_time=2)
        
        f5 = mn.MathTex(
            "f(x)", "=", "\\sum_{n=0}^\\infty", "(-1)^n\\binom{\\frac12}{n} x^{2n}").move_to(f2).align_to(f2, mn.LEFT)
        self.play(
            mn.TransformMatchingTex(f4, f5, fade_transform=False),
            run_time=2)
        
        self.play(
            mn.FadeOut(group))
        
        f6 = f5.copy()
        f6.to_edge(mn.UL)
        
        self.play(
            f5.animate.to_edge(mn.UL).shift(0.5*mn.DOWN))
        self.play(
            F1.animate.next_to(f5, mn.DOWN))
        
        F2 = mn.MathTex(
            "\\pi",
            "=",
            "4",
            "\\int\\limits_0^1",
            "f(x)",
            "\\mathrm dx"
        ).move_to(F1)
        
        self.play(
            mn.TransformMatchingTex(
                F1, F2,
                transform_mismatches=True),
            run_time=2)
        self.wait(1)
        
        F3 = mn.MathTex(
            "\\pi",
            "=",
            "4",
            "\\int\\limits_0^1",
            "\\sum_{n=0}^\\infty",
            "(-1)^n\\binom{\\frac12}{n}",
            "x^{2n}",
            "\\mathrm dx"
        ).move_to(F1)
        
        self.play(
            mn.TransformMatchingTex(
                F2, F3,
                transform_mismatches=True),
            run_time=2)
        
        F4 = mn.MathTex(
            "\\pi",
            "=",
            "4",
            "\\sum_{n=0}^\\infty",
            "(-1)^n\\binom{\\frac12}{n}",
            "\\int\\limits_0^1",
            "x^{2n}",
            "\\mathrm dx"
        ).move_to(F1)
        
        self.play(
            mn.TransformMatchingTex(
                F3, F4,
                fade_transform_mismatches=True),
            run_time=2)
        
        F5 = mn.MathTex(
            "\\pi",
            "=",
            "4",
            "\\sum_{n=0}^\\infty",
            "(-1)^n\\binom{\\frac12}{n}",
            "\\frac{1}{2n+1}"
        ).move_to(F1)
        
        self.play(
            mn.TransformMatchingTex(
                F4, F5,
                transform_mismatches=False),
            run_time=2)
        self.play(F5.animate.to_edge(mn.LEFT))

        divider = mn.Line(
            start=F5.get_left(),
            end=F5.get_right(),
            color=mn.WHITE
        )
        divider.next_to(F5, mn.DOWN)
        self.play(mn.Create(divider))

        def binom(r, k):
            rr = r - np.arange(k)
            kk = k - np.arange(k)
            return np.prod(rr) / np.prod(kk)

        def fSn(n):
            if n == 0: return 1
            else:
                an = (-1)**n * 1/(2*n+1) * binom(0.5, n)
                return fSn(n-1) + an
        
        n = 0
        g = mn.MathTex(
            "N", "=", f"{n}", ":",
            "\\;", "\\pi",
            "\\approx", f"{4*fSn(n):.5f}"
        ).next_to(divider, mn.DOWN).to_edge(mn.LEFT)
        self.play(mn.Write(g))
        self.wait(1)

        for n in range(1, 21):
            gg = mn.MathTex(
                "N", "=", f"{n}", ":",
                "\\;", "\\pi",
                "\\approx", f"{4*fSn(n):.5f}"
            ).move_to(g).to_edge(mn.LEFT)
            self.play(
                mn.TransformMatchingTex(g, gg,
                transform_mismatches=False),
                run_time=0.5)
            g = gg
            self.wait(1)
        
        self.wait(1)
        self.play(
            mn.FadeOut(g),
            mn.FadeOut(divider),
            mn.FadeOut(F5),
            mn.FadeOut(f5))
        
        group = mn.VGroup()
        ax.to_edge(mn.UP)
        ax_labels = ax.get_axis_labels(
            x_label=mn.Tex("$x$"),
            y_label=mn.Tex("$y$")
        )
        group.add(ax, ax_labels)
        self.play(
            mn.DrawBorderThenFill(ax),
            mn.Write(ax_labels),
            run_time=2)
        
        graph = ax.plot(
            f, x_range=[0, 1, 0.001],
            use_smoothing=True,
            color=mn.BLUE)
        self.play(mn.Create(graph), run_time=2)
        group.add(graph)
        
        x = 0.5
        dot = ax.coords_to_point(x, 0)
        dot1 = mn.Dot(dot, color=mn.WHITE)
        onehalf = mn.Tex(
            "$\\frac12$",
            font_size=30,
            color=mn.WHITE)
        onehalf.next_to(dot, mn.DOWN)
        dot = ax.coords_to_point(0, f(x))
        dot2 = mn.Dot(dot, color=mn.WHITE)
        sqrtthreehalf = mn.Tex(
            "$\\frac{\\sqrt3}{2}$",
            font_size=30,
            color=mn.WHITE)
        sqrtthreehalf.next_to(dot, mn.LEFT)
        group.add(dot1, dot2, onehalf, sqrtthreehalf)
        # line = ax.plot_line_graph(
        #    [0, x], [0, f(x)],
        #    line_color=mn.WHITE)
        graph2 = ax.plot(
            lambda t: f(x) * t / x,
            x_range=[0, x, 0.001],
            color=mn.WHITE)
        self.play(
            mn.Create(dot1),
            mn.Create(dot2),
            mn.Write(onehalf),
            mn.Write(sqrtthreehalf),
            mn.Create(graph2))
        self.wait(1)
        group.add(graph2)

        area1 = ax.get_area(
            graph2,
            x_range=(0, x),
            color=mn.RED,
            opacity=0.5)
        self.play(mn.Create(area1))
        self.wait(1)
        
        A1 = mn.MathTex(
            "A_1",
            "=",
            "\\frac12",
            "\\times",
            "\\frac{1}{2}",
            "\\times",
            "\\frac{\\sqrt3}{2}",
            font_size=42)
        A1.next_to(ax, mn.DOWN)
        self.play(mn.Write(A1))
        
        A2 = mn.MathTex(
            "A_1",
            "=",
            "\\frac{\\sqrt3}{8}",
            font_size=42)
        A2.next_to(ax, mn.DOWN)
        self.play(
            mn.TransformMatchingTex(A1, A2,
            transform_mismatches=True),
            run_time=2)
        self.wait(1)
        
        A2.generate_target()
        A2.target.move_to(mn.ORIGIN) # type: ignore
        A2.target.to_edge(mn.UP) # type: ignore
        self.play(mn.MoveToTarget(A2))
        self.wait(1)
        self.play(mn.FadeOut(area1))

        area2 = ax.get_area(
            graph, x_range=(0, x),
            bounded_graph=graph2,
            color=mn.YELLOW, opacity=0.5)
        self.play(mn.Create(area2))
        self.wait(1)

        B1 = mn.MathTex(
            "A_2",
            "=",
            "\\frac{\\pi}{12}",
            font_size=42)
        B1.next_to(ax, mn.DOWN)
        
        self.play(mn.Write(B1))
        self.wait(1)
        
        B1.generate_target()
        B1.target.next_to(A2, mn.DOWN) # type: ignore
        self.play(mn.MoveToTarget(B1))
        self.wait(1)
        
        self.play(mn.FadeIn(area1))
        
        C1 = mn.MathTex(
            "A_1",
            "+",
            "A_2",
            "=",
            "\\int\\limits_0^{\\frac12}",
            "f(x)",
            "\\mathrm dx",
        ).next_to(ax, mn.DOWN)
        
        self.play(mn.Write(C1))
        self.play(
            mn.FadeOut(area1),
            mn.FadeOut(area2))
        self.play(mn.FadeOut(group))
        self.wait(1)
        
        C1.generate_target()
        C1.target.next_to(B1, mn.DOWN) # type: ignore
        C1.target.align_to(B1, mn.LEFT) # type: ignore
        self.play(mn.MoveToTarget(C1))
        
        C2 = mn.MathTex(
            "\\frac{\\pi}{12}",
            "+",
            "\\frac{\\sqrt3}{8}",
            "=",
            "\\int\\limits_0^{\\frac12}",
            "f(x)",
            "\\mathrm dx",
        ).move_to(C1).align_to(C1, mn.LEFT)
        
        self.play(
            mn.FadeOut(A2),
            mn.FadeOut(B1),
            mn.TransformMatchingTex(C1, C2,
            transform_mismatches=True),
            run_time=2)
        
        C3 = mn.MathTex(
            "\\frac{\\pi}{12}",
            "=",
            "\\int\\limits_0^{\\frac12}",
            "f(x)",
            "\\mathrm dx",
            "-",
            "\\frac{\\sqrt3}{8}",
        ).move_to(C2).align_to(C2, mn.LEFT)
        
        self.play(
            mn.TransformMatchingTex(C2, C3,
            transform_mismatches=True),
            run_time=2)
        self.wait(1)
        
        C4 = mn.MathTex(
            "\\pi",
            "=",
            "12\\int\\limits_0^{\\frac12}",
            "f(x)",
            "\\mathrm dx",
            "-",
            "\\frac{3}{2}\\sqrt3",
        ).move_to(C2).align_to(C2, mn.LEFT)
        self.play(
            mn.TransformMatchingTex(C3, C4,
            transform_mismatches=True),
            run_time=2)
        self.play(C4.animate.move_to(mn.ORIGIN))
        
        C5 = mn.MathTex(
            "\\pi",
            "=",
            "12\\int\\limits_0^{\\frac12}",
            "\\sum",
            "_{n=0}",
            "^\\infty",
            "(-1)^n",
            "\\binom{\\frac12}{n}",
            "x^{2n}",
            "\\mathrm dx",
            "-",
            "\\frac{3}{2}\\sqrt3",
        ).move_to(C4).align_to(C4, mn.LEFT)
        
        self.play(mn.TransformMatchingTex(C4, C5, transform_mismatches=True))
        self.wait(1)
        
        C6 = mn.MathTex(
            "\\pi",
            "=",
            "12\\sum",
            "_{n=0}",
            "^\\infty",
            "(-1)^n",
            "\\binom{\\frac12}{n}",
            "\\int\\limits_0^{\\frac12}",
            "x^{2n}",
            "\\mathrm dx",
            "-",
            "\\frac{3}{2}\\sqrt3",
        ).move_to(C4).align_to(C4, mn.LEFT)
        
        self.play(mn.TransformMatchingTex(C5, C6, transform_mismatches=True))
        self.play(C6.animate.to_edge(mn.LEFT))
        
        C7 = mn.MathTex(
            "\\pi",
            "=",
            "12\\sum",
            "_{n=0}",
            "^\\infty",
            "(-1)^n",
            "\\binom{\\frac12}{n}",
            "\\frac{1}{2n+1}",
            "\\left(\\frac12\\right)^{2n+1}",
            "-",
            "\\frac{3}{2}\\sqrt3",
        ).move_to(C6).align_to(C6, mn.LEFT)
        self.play(mn.TransformMatchingTex(C6, C7, transform_mismatches=True))
        
        self.play(C7.animate.to_edge(mn.UP))
        self.wait(1)
        
        divider = mn.Line(
            start=C7.get_left(),
            end=C7.get_right(),
            color=mn.WHITE
        )
        divider.next_to(C7, mn.DOWN)
        self.play(mn.Create(divider))
        
        def gSn(n):
            if n == 0: return (1/2)
            else:
                an = (-1)**n * 1/(2*n+1) * binom(0.5, n) * (1/2)**(2*n+1)
                return gSn(n-1) + an
        
        d = (3/2) * np.sqrt(3)
        n = 0
        g = mn.MathTex(
            "N", "=", f"{n}", ":",
            "\\;", "\\pi",
            "\\approx", f"{(12*gSn(n)-d):.5f}"
        ).next_to(divider, mn.DOWN).to_edge(mn.LEFT)
        
        for n in range(1, 21):
            gg = mn.MathTex(
                "N", "=", f"{n}", ":",
                "\\;", "\\pi",
                "\\approx", f"{(12*gSn(n)-d):.5f}"
            ).move_to(g).to_edge(mn.LEFT)
            self.play(
                mn.TransformMatchingTex(g, gg,
                transform_mismatches=False),
                run_time=0.5)
            g = gg
            self.wait(1)
        