MODULE = src
GIT_DESCRIBE_VER = $(shell git describe --tags | sed -E -e 's/^v//' -e 's/(.*)-.*/\1/')
GIT_TAG_VER = $(shell git describe --abbrev=0)
BUMP = $(shell python3 versionbump.py --$(1) $(call GIT_TAG_VER))
NEXT_VER = $(shell git tag $(call BUMP,$(1)) -m "$(2)"; $(MAKE) ${MODULE}/_version.py)

.PHONY: help
help:
	@echo "Update app version for pip along with git tags."
	@echo
	@echo "Usage:"
	@echo
	@echo "\tmake [major|minor|patch] m='MESSAGE'"
	@echo
	@echo "\tm (required) - a message to be added with new git tag."
	@echo "\tDon't foget to put it in quotes!"

.PHONY: ${MODULE}/_version.py
${MODULE}/_version.py:
	echo '__version__ = "$(call GIT_DESCRIBE_VER)"' > $@

.PHONY: patch minor major
major minor patch:
	$(call NEXT_VER,$@,$$m)
