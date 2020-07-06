all:

OUT ?= out/cur
GMOCK ?= .

CPPFLAGS ?= -MMD -MP
CXXFLAGS ?= -std=c++11 -stdlib=libc++
MKDIR_P ?= mkdir -p

include $(GMOCK)/build/targets.mk

all: $(LIBGTEST) $(LIBGMOCK) $(LIBGMOCK_MAIN)

.PHONY: clean
clean:
	$(RM) -r $(OUT)
