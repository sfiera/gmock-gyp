LIBGMOCK_CPPFLAGS := \
	$(LIBGTEST_CPPFLAGS) \
	-I $(GMOCK)/googletest-1.10.0/googlemock/include

LIBGMOCK_A := $(OUT)/libgmock.a
LIBGMOCK_SRCS := \
	$(GMOCK)/googletest-1.10.0/googlemock/src/gmock-all.cc \
	$(GMOCK)/googletest-1.10.0/googlemock/src/gmock-cardinalities.cc \
	$(GMOCK)/googletest-1.10.0/googlemock/src/gmock-internal-utils.cc \
	$(GMOCK)/googletest-1.10.0/googlemock/src/gmock-matchers.cc \
	$(GMOCK)/googletest-1.10.0/googlemock/src/gmock-spec-builders.cc \
	$(GMOCK)/googletest-1.10.0/googlemock/src/gmock.cc
LIBGMOCK_OBJS := $(LIBGMOCK_SRCS:%=$(OUT)/%.o)

$(LIBGMOCK_A): $(LIBGMOCK_OBJS) $(LIBGTEST_OBJS)
	$(AR) rcs $@ $+

PRIVATE_LIBGMOCK_CPPFLAGS := \
	$(PRIVATE_LIBGTEST_CPPFLAGS) \
	$(LIBGMOCK_CPPFLAGS) \
	-I $(GMOCK)/googletest-1.10.0/googlemock

$(LIBGMOCK_OBJS): $(OUT)/%.cc.o: %.cc
	@$(MKDIR_P) $(dir $@)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) $(PRIVATE_LIBGMOCK_CPPFLAGS) -c $< -o $@

-include $(LIBGMOCK_OBJS:.o=.d)
