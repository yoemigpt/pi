from pdb import run
import manim as mn
import numpy as np

PITEX = "$\pi$" # type: ignore
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
        pi = mn.Tex(f"${ds}\ldots$", font_size=fs) # type: ignore
        equal = mn.Tex("=", font_size=fs)
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

        equal.scale(s)
        equal.next_to(three14, mn.LEFT)
        pitex.scale(s)
        pitex.next_to(equal, mn.LEFT)
        self.play(mn.Write(pitex))
        self.play(mn.Write(equal))
        self.wait(1)
        
        self.play(mn.FadeOut(three14, pi, equal))
        self.wait(1)
        
        pitex.generate_target()
        pitex.target.move_to(mn.ORIGIN) # type: ignore
        pitex.target.scale(6) # type: ignore
        pitex.target.set_color(mn.RED) # type: ignore
        self.play(mn.MoveToTarget(pitex))
        self.wait(1)
        

class CirclePI(mn.Scene):
    r = 1
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
        self.play(
            mn.TransformFromCopy(circ, c)
        )
        
        circles = mn.VGroup()
        circles.add(c)
        for _ in range(3):
            c1 = c.copy()
            c1.shift(2*r*mn.RIGHT)
            tr = mn.TransformFromCopy(c, c1)
            self.play(tr)
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

class ArchimedesPI(mn.Scene):
    def inscribed(self, circ, n):
        points = []
        pr = 0.5/n
        for i in range(n):
            p = circ.point_from_proportion(pr + i/n)
            points.append(p)
        return mn.Polygon(*points)
    
    def subscribed(self, circ, n):
        a = mn.PI / n
        r = 1 / np.cos(a)
        pr = 0.5/n
        points = []
        for i in range(n):
            p = circ.point_from_proportion(pr + i/n)
            points.append(r * p)
        return mn.Polygon(*points)
    
    def construct(self):
        circ = mn.Circle(radius=1, color=mn.BLUE)
        circ.scale(3)
        self.play(mn.Create(circ))
        self.wait(1)
        
        for n in [4, 6, 8]:
            polygons = mn.VGroup()
            ins = self.inscribed(circ, n)
            ins.set_color(mn.RED)
            polygons.add(ins)
            self.play(mn.Create(ins))
            self.wait(1)
            
            subs = self.subscribed(circ, n)
            subs.set_color(mn.GREEN)
            polygons.add(subs)
            self.play(mn.Create(subs))
            self.wait(1)
            self.play(mn.FadeOut(polygons), run_time=1)
            