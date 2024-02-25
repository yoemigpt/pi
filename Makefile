# Quality of the video.
QUALITY=-qm

# Manim command.
MANIM=manim

# Manim flags.
FLAGS=-v WARNING

all:
	$(MANIM) $(QUALITY) $(FLAGS) main.py DateToPI
	$(MANIM) $(QUALITY) $(FLAGS) main.py CirclePI
	$(MANIM) $(QUALITY) $(FLAGS) main.py ArchimedesPI
#	$(MANIM) $(QUALITY) $(FLAGS) main.py NewtonPI
