TECTONIC := tectonic
SRCS := JR_230557T.tex
PDFS := $(SRCS:.tex=.pdf)

.PHONY: all clean

all: $(PDFS)

%.pdf: %.tex
	$(TECTONIC) $<

clean:
	rm -f $(PDFS)
