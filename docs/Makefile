
chapters = 00-Preface.md 01-Introduction.md 02-Python-Types.md \
  03-Control-Structures.md 04-Plotting.md 05-Classes.md 06-Ecosystem.md \
  07-Conclusion.md

.PHONY: all
all: PythonForMatlabProgrammers.md pdf

PythonForMatlabProgrammers.md: $(chapters)
	cat $(chapters) > PythonForMatlabProgrammers.md

.PHONY: pdf
pdf: PythonForMatlabProgrammers.md
	bundle exec jekyll build
	rm -f _site/PythonForMatlabProgrammers
	cd _site && ln -s . PythonForMatlabProgrammers
	python3 convert_html_to_pdf.py

