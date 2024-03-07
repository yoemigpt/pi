# Quality of the video.
QUALITY=-qm

# Manim command.
MANIM=manim

# Manim flags.
FLAGS=-v WARNING

all: intro circum greek

intro:
	$(MANIM) $(QUALITY) $(FLAGS) intro.py ArabicFirst
	$(MANIM) $(QUALITY) $(FLAGS) intro.py ArabicSecond

circum:
	$(MANIM) $(QUALITY) $(FLAGS) circum.py Circumference

greek:
#	$(MANIM) $(QUALITY) $(FLAGS) greek.py GreekPolygon
#	$(MANIM) $(QUALITY) $(FLAGS) greek.py GreekPolygonExample
	$(MANIM) $(QUALITY) $(FLAGS) greek.py GreekPolygonBounds

datetopi:
	$(MANIM) $(QUALITY) $(FLAGS) main.py DateToPI

circlepi:
	$(MANIM) $(QUALITY) $(FLAGS) main.py CirclePI
	
circle2pi:
	$(MANIM) $(QUALITY) $(FLAGS) main.py Circle2PI
	
archemidespi:
	$(MANIM) $(QUALITY) $(FLAGS) main.py ArchimedesPI
	
binomialpi:
	$(MANIM) $(QUALITY) $(FLAGS) main.py BinomialPI
	
newtonpi:
	$(MANIM) $(QUALITY) $(FLAGS) main.py NewtonPI
