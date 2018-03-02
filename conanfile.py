from conans import ConanFile


class nghttp2_with_conan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = \
    "zlib/1.2.11@odant/stable", \
    "openssl/1.1.0g@odant/testing", \
    "boost/1.66.0@odant/testing"

   generators = "cmake"

