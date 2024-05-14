{
  "variables": {
    "mediasoup_build_type%": "Release"
  },
  "targets": [
    {
      "target_name": "worker-channel",
      "sources": [
        "src/binding.cpp",
        "src/workerChannel.cpp"
      ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'include_dirs': [
        "<!@(node -p \"require('node-addon-api').include\")",
        "<!(pwd)/../../worker/include",
      ],
      "libraries": [
        "<!(pwd)/../../worker/out/<(mediasoup_build_type)/build/libmediasoup-worker.a"
      ],
      'dependencies': ["<!(node -p \"require('node-addon-api').gyp\")"],
      'conditions': [
        ['OS=="win"', {
          "msvs_settings": {
            "VCCLCompilerTool": {
              "ExceptionHandling": 1
            }
          }
        }],
        ['OS=="mac"', {
          "xcode_settings": {
            "CLANG_CXX_LIBRARY": "libc++",
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            # TODO: This should be the same as the one used for libmediasoup
            # Is it really needed?
            'MACOSX_DEPLOYMENT_TARGET': '14'
          }
        }]
      ]
    }
  ]
}
