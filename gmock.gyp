{ "targets":
  [ { "target_name": "gmock_main"
    , "type": "static_library"
    , "sources": ["gmock-1.6.0/src/gmock_main.cc"]
    , "dependencies": ["gmock"]
    , "export_dependent_settings": ["gmock"]
    }

  , { "target_name": "gmock"
    , "type": "static_library"
    , "sources":
      [ "gmock-1.6.0/src/gmock-cardinalities.cc"
      , "gmock-1.6.0/src/gmock-internal-utils.cc"
      , "gmock-1.6.0/src/gmock-matchers.cc"
      , "gmock-1.6.0/src/gmock-spec-builders.cc"
      , "gmock-1.6.0/src/gmock.cc"
      ]
    , "include_dirs":
      [ "gmock-1.6.0"
      , "gmock-1.6.0/include"
      ]
    , "dependencies": ["gtest"]
    , "export_dependent_settings": ["gtest"]
    , "direct_dependent_settings":
      { "include_dirs": ["gmock-1.6.0/include"]
      }
    }

  , { "target_name": "gtest"
    , "type": "static_library"
    , "sources":
      [ "gmock-1.6.0/gtest/src/gtest-death-test.cc"
      , "gmock-1.6.0/gtest/src/gtest-filepath.cc"
      , "gmock-1.6.0/gtest/src/gtest-port.cc"
      , "gmock-1.6.0/gtest/src/gtest-printers.cc"
      , "gmock-1.6.0/gtest/src/gtest-test-part.cc"
      , "gmock-1.6.0/gtest/src/gtest-typed-test.cc"
      , "gmock-1.6.0/gtest/src/gtest.cc"
      ]
    , "defines": ["GTEST_USE_OWN_TR1_TUPLE=1"]
    , "include_dirs":
      [ "gmock-1.6.0/gtest"
      , "gmock-1.6.0/gtest/include"
      ]
    , "direct_dependent_settings":
      { "defines": ["GTEST_USE_OWN_TR1_TUPLE=1"]
      , "include_dirs": ["gmock-1.6.0/gtest/include"]
      }
    , "link_settings":
      { "libraries":
        [ "-lpthread"
        ]
      }
    }
  ]
}
# -*- mode: python; tab-width: 2 -*-
