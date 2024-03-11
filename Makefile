# Quality of the video.
QUALITY=-qh

# Manim command.
MANIM=manim

# Manim flags.
FLAGS=-v WARNING

all: intro circum greek area binom newton pianimation history final

intro:
	$(MANIM) $(QUALITY) $(FLAGS) intro.py ArabicFirst
	$(MANIM) $(QUALITY) $(FLAGS) intro.py ArabicSecond
	$(MANIM) $(QUALITY) $(FLAGS) intro.py ArabicIntro

circum:
	$(MANIM) $(QUALITY) $(FLAGS) circum.py Circumference

area:
	$(MANIM) $(QUALITY) $(FLAGS) area.py Area

greek:
	$(MANIM) $(QUALITY) $(FLAGS) greek.py GreekPolygon
	$(MANIM) $(QUALITY) $(FLAGS) greek.py GreekPolygonExample
	$(MANIM) $(QUALITY) $(FLAGS) greek.py GreekPolygonBounds

binom:
	$(MANIM) $(QUALITY) $(FLAGS) binom.py BinomialEquation

newton:
	$(MANIM) $(QUALITY) $(FLAGS) newton.py Integral
	$(MANIM) $(QUALITY) $(FLAGS) newton.py Newton

pianimation:
	$(MANIM) $(QUALITY) $(FLAGS) today.py PIAnimation

history:
	$(MANIM) $(QUALITY) $(FLAGS) history.py History1
	$(MANIM) $(QUALITY) $(FLAGS) history.py History2

final:
	$(MANIM) $(QUALITY) $(FLAGS) final.py ArabicFinal