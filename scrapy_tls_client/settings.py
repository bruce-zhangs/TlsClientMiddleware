# -*- coding: utf-8 -*-

# You can also use the following as `client_identifier`:
# Chrome --> chrome_103, chrome_104, chrome_105, chrome_106, chrome_107, chrome_108, chrome_109, Chrome_110,
#            chrome_111, chrome_112
# Firefox --> firefox_102, firefox_104, firefox108, Firefox110
# Opera --> opera_89, opera_90
# Safari --> safari_15_3, safari_15_6_1, safari_16_0
# iOS --> safari_ios_15_5, safari_ios_15_6, safari_ios_16_0
# iPadOS --> safari_ios_15_6
# Android --> okhttp4_android_7, okhttp4_android_8, okhttp4_android_9, okhttp4_android_10, okhttp4_android_11,
#             okhttp4_android_12, okhttp4_android_13
# CLIENT_IDENTIFIER = 'chrome_112'
CLIENT_IDENTIFIER = None

# Set JA3 --> TLSVersion, Ciphers, Extensions, EllipticCurves, EllipticCurvePointFormats
# Example:
# JA3_STRING = '771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0'
JA3_STRING=None

# HTTP2 Header Frame Settings
# Possible Settings:
# HEADER_TABLE_SIZE
# SETTINGS_ENABLE_PUSH
# MAX_CONCURRENT_STREAMS
# INITIAL_WINDOW_SIZE
# MAX_FRAME_SIZE
# MAX_HEADER_LIST_SIZE
#
# Example:
# H2_SETTINGS = {
#     "HEADER_TABLE_SIZE": 65536,
#     "MAX_CONCURRENT_STREAMS": 1000,
#     "INITIAL_WINDOW_SIZE": 6291456,
#     "MAX_HEADER_LIST_SIZE": 262144
# }
H2_SETTINGS=None

# HTTP2 Header Frame Settings Order
# H2_SETTINGS_ORDER = [
#     "HEADER_TABLE_SIZE",
#     "MAX_CONCURRENT_STREAMS",
#     "INITIAL_WINDOW_SIZE",
#     "MAX_HEADER_LIST_SIZE"
# ]
H2_SETTINGS_ORDER=None

# Supported Signature Algorithms
# Possible Settings:
# PKCS1WithSHA256
# PKCS1WithSHA384
# PKCS1WithSHA512
# PSSWithSHA256
# PSSWithSHA384
# PSSWithSHA512
# ECDSAWithP256AndSHA256
# ECDSAWithP384AndSHA384
# ECDSAWithP521AndSHA512
# PKCS1WithSHA1
# ECDSAWithSHA1
#
# Example:
# SUPPORTED_SIGNATURE_ALGORITHMS = [
#     "ECDSAWithP256AndSHA256",
#     "PSSWithSHA256",
#     "PKCS1WithSHA256",
#     "ECDSAWithP384AndSHA384",
#     "PSSWithSHA384",
#     "PKCS1WithSHA384",
#     "PSSWithSHA512",
#     "PKCS1WithSHA512",
# ]
SUPPORTED_SIGNATURE_ALGORITHMS=None

# Supported Delegated Credentials Algorithms
# Possible Settings:
# PKCS1WithSHA256
# PKCS1WithSHA384
# PKCS1WithSHA512
# PSSWithSHA256
# PSSWithSHA384
# PSSWithSHA512
# ECDSAWithP256AndSHA256
# ECDSAWithP384AndSHA384
# ECDSAWithP521AndSHA512
# PKCS1WithSHA1
# ECDSAWithSHA1
#
# Example:
# SUPPORTED_DELEGATED_CREDENTIALS_ALGORITHMS = [
#     "ECDSAWithP256AndSHA256",
#     "PSSWithSHA256",
#     "PKCS1WithSHA256",
#     "ECDSAWithP384AndSHA384",
#     "PSSWithSHA384",
#     "PKCS1WithSHA384",
#     "PSSWithSHA512",
#     "PKCS1WithSHA512",
# ]
SUPPORTED_DELEGATED_CREDENTIALS_ALGORITHMS=None

# Supported Versions
# Possible Settings:
# GREASE
# 1.3
# 1.2
# 1.1
# 1.0
#
# Example:
# SUPPORTED_VERSIONS = [
#     "GREASE",
#     "1.3",
#     "1.2"
# ]
SUPPORTED_VERSIONS=None

# Key Share Curves
# Possible Settings:
# GREASE
# P256
# P384
# P521
# X25519
#
# Example:
# KEY_SHARE_CURVES = [
#     "GREASE",
#     "X25519"
# ]
KEY_SHARE_CURVES=None

# Cert Compression Algorithm
# Examples: "zlib", "brotli", "zstd"
# CERT_COMPRESSION_ALGO = 'brotli'
CERT_COMPRESSION_ALGO = None

# Additional Decode
# Make sure the go code decodes the response body once explicit by provided algorithm.
# Examples: null, "gzip", "br", "deflate"
# ADDITIONAL_DECODE = 'gzip'
ADDITIONAL_DECODE = None

# Pseudo Header Order (:authority, :method, :path, :scheme)
# Example:
# PSEUDO_HEADER_ORDER = [
#     ":method",
#     ":authority",
#     ":scheme",
#     ":path"
# ]
PSEUDO_HEADER_ORDER=None

# Connection Flow / Window Size Increment
# Example:
# CONNECTION_FLOW = 15663105
CONNECTION_FLOW = None

# Example:
# PRIORITY_FRAMES = [
#   {
#     "streamID": 3,
#     "priorityParam": {
#       "weight": 201,
#       "streamDep": 0,
#       "exclusive": False
#     }
#   },
#   {
#     "streamID": 5,
#     "priorityParam": {
#       "weight": 101,
#       "streamDep": False,
#       "exclusive": 0
#     }
#   }
# ]
PRIORITY_FRAMES=None

# Order of your headers
# Example:
# [
#   "key1",
#   "key2"
# ]
# HEADER_ORDER = [
#         "accept",
#         "user-agent",
#         "accept-encoding",
#         "accept-language"
#     ]
HEADER_ORDER = None

# Header Priority
# Example:
# HEADER_PRIORITY = {
#   "streamDep": 1,
#   "exclusive": True,
#   "weight": 1
# }
HEADER_PRIORITY = None

# randomize tls extension order
RANDOM_TLS_EXTENSION_ORDER = False

# force HTTP1
FORCE_HTTP1 = False

# catch panics
# avoid the tls client to print the whole stacktrace when a panic (critical go error) happens
CATCH_PANICS = False

# raw_response_parser
# HtmlResponse TextResponse
RAW_RESPONSE_TYPE = 'HtmlResponse'
