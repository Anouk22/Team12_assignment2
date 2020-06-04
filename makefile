all: analysis data-preparation

.PHONY: all data-preparation analysis

data-preparation:
	$(MAKE) -C src/data-preparation


wipe:
	$(MAKE) wipe -C src/data-preparation
