# ===
# This is the main GYP file, which builds better-sqlite3 with SQLite3 itself.
# ===

{
  'includes': ['deps/common.gypi'],
  'targets': [
    {
      'target_name': 'better_sqlite3',
      'sources': ['src/better_sqlite3.cpp'],
      'cflags': ['-std=c++14'],
      'xcode_settings': {
        'OTHER_CPLUSPLUSFLAGS': ['-std=c++14', '-stdlib=libc++'],
      },
      "conditions": [
        ["sqlite3 != 'internal' and sqlite3_libpath != ''", {
          # link to pre-built sqlite3 library
          "include_dirs": ["<(sqlite3)"],
          "libraries+": ["<(sqlite3_libpath)"]
        }, {
          # build internal / custom amalgamation
          "dependencies": ["deps/sqlite3.gyp:sqlite3"]
        }]
      ]
    },
    {
      'target_name': 'test_extension',
      "conditions": [
        ["sqlite3 != 'internal' and sqlite3_libpath != ''", {
          # link to pre-built sqlite3 library
          "include_dirs": ["<(sqlite3)"],
          "libraries+": ["<(sqlite3_libpath)"]
        }, {
          # build internal / custom amalgamation
          "dependencies": ["deps/sqlite3.gyp:sqlite3"]
        }]
      ],
      'sources': ['deps/test_extension.c'] 
    },
  ],
}
