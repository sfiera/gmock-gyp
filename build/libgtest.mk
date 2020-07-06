LIBGTEST_CPPFLAGS := \
	-I $(GMOCK)/googletest-1.10.0/googletest/include \
	-I /usr/include/libcxxabi

LIBGTEST_A := $(OUT)/libgtest.a
LIBGTEST_SRCS := \
	$(GMOCK)/googletest-1.10.0/googletest/src/gtest-all.cc \
	$(GMOCK)/googletest-1.10.0/googletest/src/gtest-death-test.cc \
	$(GMOCK)/googletest-1.10.0/googletest/src/gtest-filepath.cc \
	$(GMOCK)/googletest-1.10.0/googletest/src/gtest-matchers.cc \
	$(GMOCK)/googletest-1.10.0/googletest/src/gtest-port.cc \
	$(GMOCK)/googletest-1.10.0/googletest/src/gtest-printers.cc \
	$(GMOCK)/googletest-1.10.0/googletest/src/gtest-test-part.cc \
	$(GMOCK)/googletest-1.10.0/googletest/src/gtest-typed-test.cc \
	$(GMOCK)/googletest-1.10.0/googletest/src/gtest.cc
LIBGTEST_OBJS := $(LIBGTEST_SRCS:%=$(OUT)/%.o)

$(LIBGTEST_A): $(LIBGTEST_OBJS)
	$(AR) rcs $@ $+

PRIVATE_LIBGTEST_CPPFLAGS := \
	$(LIBGTEST_CPPFLAGS) \
	-I $(GMOCK)/googletest-1.10.0/googletest

$(LIBGTEST_OBJS): $(OUT)/%.cc.o: %.cc
	@$(MKDIR_P) $(dir $@)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) $(PRIVATE_LIBGTEST_CPPFLAGS) -c $< -o $@

-include $(LIBGTEST_OBJS:.o=.d)
