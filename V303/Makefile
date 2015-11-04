all: V303.tex

V303.tex: plot2u.pdf plot2low.pdf plot3u.pdf plot3low.pdf plot4.pdf

plot3u.pdf plot3low.pdf: plot3.py
	python plot3.py

plot2u.pdf plot2low.pdf: plot2.py
	python plot2.py

plot4.pdf: plot4.py
	python plot4.py
