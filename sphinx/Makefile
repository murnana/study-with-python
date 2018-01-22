# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =-d _build/doctrees
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = study_with_python
SOURCEDIR     = .
BUILDDIR      = ../docs

# Put it first so that "make" without argument is like "make help".
.PHONY: Makefile html
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	
# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@  $(SPHINXOPTS) "$(SOURCEDIR)" "$(BUILDDIR)"

