TECTONIC := tectonic
SRCS := activity1.tex activity2.tex
PDFS := $(SRCS:.tex=.pdf)

.PHONY: all clean

all: $(PDFS)

%.pdf: %.tex preamble.tex
	$(TECTONIC) $<

clean:
	rm -f $(PDFS)
