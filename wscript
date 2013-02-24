# -*- mode: python -*-

def common(ctx):
    ctx.default_sdk = "10.6"
    ctx.default_compiler = "gcc"
    ctx.load("compiler_cxx")
    ctx.load("core", "ext/waf-sfiera")

def options(opt):
    common(opt)

def configure(cnf):
    common(cnf)
    cnf.check(lib="pthread", uselib_store="gmock/system/pthread")

def build(bld):
    common(bld)

    bld.stlib(
        target="gmock/gmock-main",
        features="universal",
        source="gmock-1.6.0/src/gmock_main.cc",
        use="gmock/gmock",
    )

    bld.stlib(
        target="gmock/gmock",
        features="universal",
        source=[
            "gmock-1.6.0/src/gmock-cardinalities.cc",
            "gmock-1.6.0/src/gmock-internal-utils.cc",
            "gmock-1.6.0/src/gmock-matchers.cc",
            "gmock-1.6.0/src/gmock-spec-builders.cc",
            "gmock-1.6.0/src/gmock.cc",
        ],
        includes="gmock-1.6.0 gmock-1.6.0/include",
        export_includes="gmock-1.6.0/include",
        use="gmock/gtest",
    )

    bld.stlib(
        target="gmock/gtest",
        features="universal",
        source=[
            "gmock-1.6.0/gtest/src/gtest-death-test.cc",
            "gmock-1.6.0/gtest/src/gtest-filepath.cc",
            "gmock-1.6.0/gtest/src/gtest-port.cc",
            "gmock-1.6.0/gtest/src/gtest-printers.cc",
            "gmock-1.6.0/gtest/src/gtest-test-part.cc",
            "gmock-1.6.0/gtest/src/gtest-typed-test.cc",
            "gmock-1.6.0/gtest/src/gtest.cc",
        ],
        includes="gmock-1.6.0/gtest gmock-1.6.0/gtest/include",
        export_includes="gmock-1.6.0/gtest/include",
        use="gmock/system/pthread",
    )
