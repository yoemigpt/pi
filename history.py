import manim as mn

preamble_ar = r"""
\usepackage{amsmath}
\usepackage{fontspec}
\usepackage{polyglossia}
\setmainlanguage[
    numerals=maghrib,   
]{arabic}
\setotherlanguage{english}
\newfontfamily\arabicfont[Script=Arabic]{Amiri}
"""

tex_template_ar = mn.TexTemplate(
    preamble=preamble_ar,
    tex_compiler="xelatex",
    output_format=".xdv",
)



class History1(mn.Scene):
    def construct(self):
        title = mn.MathTex(
            "\\text{عبر التاريخ}\\; \\pi",
            tex_template=tex_template_ar,
            font_size=72,
        )
        mobjs = title.submobjects[0].submobjects
        title.submobjects[0].submobjects = mobjs[::-1]
        self.play(mn.Write(title))
        self.wait(1)
        
        title.generate_target()
        title.target.scale(0.5) # type: ignore
        title.target.to_edge(mn.UP) # type: ignore
        self.play(mn.MoveToTarget(title))
        self.wait(1)
        
        a = 20
        line = mn.Line(
            mn.ORIGIN-8*mn.RIGHT,
            mn.ORIGIN+8*mn.RIGHT,
            # stroke_width=2,
            # color=mn.RED,
        )
        
        dot = mn.Dot(mn.ORIGIN)
        self.play(mn.Create(line))
        self.wait(1)
        self.play(mn.Create(dot))
        self.wait(1)
        group = mn.VGroup(dot)
        groupl = mn.VGroup()
        groupu = mn.VGroup()
        
        textu = mn.Tex(
            "المصريون القدماء",
            tex_template=tex_template_ar,
        )
        mobjs = textu.submobjects[0].submobjects
        textu.submobjects[0].submobjects = mobjs[::-1]
        groupu.add(textu)
        groupu.next_to(dot, mn.UP)
        
        textl = mn.MathTex(
            "\\pi\\approx 3.12"
        )
        groupl.add(textl)
        groupl.next_to(dot, mn.DOWN)
        self.play(
            mn.Write(groupu),
            mn.Write(groupl)
        )
        self.wait(1)
        
        
        group.add(groupu, groupl)
        
        group.generate_target()
        group.target.shift(a*mn.LEFT) # type: ignore

        dot1 = mn.Dot(mn.ORIGIN+a*mn.RIGHT)
        group1 = mn.VGroup(dot1)
        group1u = mn.VGroup()
        group1l = mn.VGroup()
        
        text1u = mn.Tex(
            r"اليونانيون القدماء",
            tex_template=tex_template_ar,
        )
        mobjs = text1u.submobjects[0].submobjects
        text1u.submobjects[0].submobjects = mobjs[::-1]
        group1u.add(text1u)
        group1u.next_to(dot1, mn.UP)
        
        text1l1 = mn.MathTex(
            "\\pi\\approx 3.14",
        )
        text1l2 = mn.Tex(
            "عن طريق حساب محيطات الأشكال",
            tex_template=tex_template_ar,
        )
        text1l1.next_to(dot1, mn.DOWN)
        text1l2.next_to(text1l1, mn.DOWN)
        group1l.add(text1l1, text1l2)
        group1.add(group1u, group1l)
        
        group1.generate_target()
        group1.target.shift(a*mn.LEFT) # type: ignore

        self.play(
            mn.MoveToTarget(group),
            mn.MoveToTarget(group1)
        )
        self.wait(2)
        
        dot2 = mn.Dot(mn.ORIGIN+a*mn.RIGHT)
        group2 = mn.VGroup(dot2)
        group2u = mn.VGroup()
        group2l = mn.VGroup()
        text2u = mn.Tex(
            "الحضارة الصينية",
            tex_template=tex_template_ar,
        )
        mobjs = text2u.submobjects[0].submobjects
        text2u.submobjects[0].submobjects = mobjs[::-1]
        group2u.add(text2u)
        group2u.next_to(dot2, mn.UP)

        text2l1 = mn.MathTex(
            "\\pi\\approx 3.14159",
        )
        text2l2 = mn.Tex(
            "عن طريق حساب مساحات الأشكال",
            tex_template=tex_template_ar,
        )
        text2l1.next_to(dot2, mn.DOWN)
        text2l2.next_to(text2l1, mn.DOWN)
        group2l.add(text2l1, text2l2)
        group2.add(group2u, group2l)
        
        group1.target.shift(a*mn.LEFT) # type: ignore

        group2.generate_target()
        group2.target.shift(a*mn.LEFT) # type: ignore
        
        self.play(
            mn.MoveToTarget(group1),
            mn.MoveToTarget(group2),
            run_time=2
        )
        self.wait(2)
        
        dot3 = mn.Dot(mn.ORIGIN+a*mn.RIGHT)
        group3 = mn.VGroup(dot3)
        group3u = mn.VGroup()
        group3l = mn.VGroup()
        
        text3u1 = mn.Tex(
            "الحضارة الإسلامية",
            tex_template=tex_template_ar,
        )
        mobjs = text3u1.submobjects[0].submobjects
        text3u1.submobjects[0].submobjects = mobjs[::-1]
        group3u.add(text3u1)
        group3u.next_to(dot3, mn.UP)
        
        text3l1 = mn.Tex(
            "اختراع الأرقام العربية",
            tex_template=tex_template_ar,
        )
        mobjs = text3l1.submobjects[0].submobjects
        text3l1.submobjects[0].submobjects = mobjs[::-1]
        
        text3l2 = mn.Tex(
            "والعمليات الحسابية",
            tex_template=tex_template_ar,
        )
        mobjs = text3l2.submobjects[0].submobjects
        text3l2.submobjects[0].submobjects = mobjs[::-1]
        text3l2.next_to(text3l1, mn.DOWN)
        
        text3l3 = mn.Tex(
            "والجبر",
            tex_template=tex_template_ar,
        )
        mobjs = text3l3.submobjects[0].submobjects
        text3l3.submobjects[0].submobjects = mobjs[::-1]
        text3l3.next_to(text3l2, mn.DOWN)
        
        group3l.add(text3l1, text3l2)
        group3l.add(text3l3)
        group3l.next_to(dot3, mn.DOWN)
        group3.add(group3u, group3l)
        group2.target.shift(a*mn.LEFT) # type: ignore
        group3.generate_target()
        group3.target.shift(a*mn.LEFT) # type: ignore

        self.play(
            mn.MoveToTarget(group2),
            mn.MoveToTarget(group3),
            run_time=2,
        )
        self.wait(3)
        
        dot4 = mn.Dot(mn.ORIGIN+a*mn.RIGHT)
        group4 = mn.VGroup(dot4)
        group4u = mn.VGroup()
        group4l = mn.VGroup()
        
        text4u = mn.Tex(
            "الحضارة الأوروبية",
            tex_template=tex_template_ar,
        )
        group4u.add(text4u)
        group4u.next_to(dot4, mn.UP)
        
        text4l1 = mn.Tex(
            "حساب التكامل",
            tex_template=tex_template_ar,
        )
        mobjs = text4l1.submobjects[0].submobjects
        text4l1.submobjects[0].submobjects = mobjs[::-1]
        
        text4l2 = mn.Tex(
            "حساب اللانهايات",
            tex_template=tex_template_ar,
        )
        mobjs = text4l2.submobjects[0].submobjects
        text4l2.submobjects[0].submobjects = mobjs[::-1]
        text4l2.next_to(text4l1, mn.DOWN)
        group4l.add(text4l1, text4l2)
        
        group4l.next_to(dot4, mn.DOWN)
        group4.add(group4u, group4l)
        group3.target.shift(a*mn.LEFT) # type: ignore
        group4.generate_target()
        group4.target.shift(a*mn.LEFT) # type: ignore
        
        self.play(
            mn.MoveToTarget(group3),
            mn.MoveToTarget(group4),
            run_time=3,
        )   
        self.wait(3)
        
        text4 = mn.Tex(
            "توصلنا لمعرفة أكثر من ألف رقم بعد العلامة العشرية",
            tex_template=tex_template_ar
        )
        mobjs = text4.submobjects[0].submobjects
        text4.submobjects[0].submobjects = mobjs[::-1]
        text4.next_to(title, mn.DOWN)
        
        self.play(mn.Write(text4), run_time=3)
        self.wait(2)
        
        self.play(
            mn.Unwrite(text4),
            mn.Uncreate(line),
            mn.FadeOut(title),
            mn.FadeOut(group4),
            run_time=2)
        self.wait(1)

class History2(mn.Scene):
    def construct(self):
        img1 = mn.ImageMobject(
            "assets/images/old-pi.png")
        img1.scale(2)
        self.play(mn.FadeIn(img1), run_time=4)
        self.wait(2)
        self.play(mn.FadeOut(img1), run_time=3)
        self.wait(1)
        
        img2 = mn.ImageMobject(
            "assets/images/euclid.png")
        img2.scale(1.5)
        self.play(mn.FadeIn(img2), run_time=4)
        self.play(mn.FadeOut(img2), run_time=1)
        
        img3 = mn.ImageMobject(
            "assets/images/archimedes.png")
        img3.scale(0.2)
        
        self.play(mn.FadeIn(img3), run_time=4)
        self.wait(1)
        self.play(mn.FadeOut(img3), run_time=1)
        self.wait(1)
        
class History3(mn.Scene):
    def construct(self):
        img1 = mn.ImageMobject(
            "assets/images/links-pi.jpeg")
        
        img1.scale(0.5)
        self.play(mn.FadeIn(img1), run_time=3)
        self.wait(2)
        self.play(mn.FadeOut(img1), run_time=1)
        
        eq1 = mn.MathTex(
            "\\left(\\nabla^2 - \\frac{1}{c^2} \\frac{\\partial^2}{\\partial t^2}\\right)\\vec{E} = 0",
            font_size=72,
        )
        
        self.play(mn.Write(eq1), run_time=2)
        
        # Scroll to the right
        eq1.generate_target()
        eq1.target.scale(0.5) # type: ignore
        eq1.target.shift(16 * mn.RIGHT) # type: ignore
        
        eq2 = mn.MathTex(
            "\\vec{E} = \\vec{E}_0 e^{i(kx - \\omega t)} \\quad \\implies \\quad \\omega = kc = 2\\pi f",
            font_size=72,
        )
        eq2.submobjects[0].submobjects[-2].set_color(mn.RED)

        eq2.generate_target()
        eq2.target.move_to(mn.ORIGIN) # type: ignore

        eq2.shift(30*mn.LEFT)
        self.play(
            mn.MoveToTarget(eq1),
            mn.AnimationGroup(
                mn.FadeIn(eq2),
                mn.MoveToTarget(eq2),
                lag_ratio=1.0
            ),
            run_time=3)
        self.wait(1)
        self.play(
            mn.Unwrite(eq2),
            run_time=1)
        
        img2 = mn.ImageMobject(
            "assets/images/solar.png")
        
        self.play(mn.GrowFromCenter(img2), run_time=3)
        self.wait(1)
        self.play(mn.FadeOut(img2), run_time=2)
        self.wait(1)

        
class History4(mn.Scene):
    def construct(self):
        group = mn.VGroup()
        square = mn.Square()
        circ = mn.Circle()
        polygon = mn.RegularPolygon(6)
        group.add(square, circ, polygon)
        
        group.arrange(mn.RIGHT)
        
        group.move_to(mn.ORIGIN)
        self.play(mn.Create(group), run_time=1)
        self.wait(2)
        
        integral = mn.MathTex(
            "\\int",
            font_size=72,
        )
        
        diff = mn.MathTex(
            "\\frac{d}{dx}",
            font_size=72,
        )
        
        suminf = mn.MathTex(
            "\\sum_{n=1}^{\\infty}",
            font_size=72,
        )
        
        group2 = mn.VGroup(integral, diff, suminf)
        group2.arrange_in_grid(1, 3, buff=1)
        
        group2.move_to(mn.ORIGIN)
        
        self.play(
            mn.FadeOut(group),
            mn.Create(group2),
            run_time=2)
        self.wait(1)
        self.play(mn.FadeOut(group2), run_time=1)