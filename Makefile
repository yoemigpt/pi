# Quality of the video.
QUALITY=-qm

# Manim command.
MANIM=manim

# Manim flags.
FLAGS=-v WARNING

all: datetopi circlepi circle2pi archemidespi binomialpi newtonpi

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
