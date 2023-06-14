# Scrapy Tls Client Downloader Middleware

This package will make scrapy support tls_client. Everything is same with tls_client, but needed 
to specify in settings.py.

## Installation

```shell script
pip3 install scrapy-tls-client
```

## Usage

After add this middleware, all requests will be sent by tls_client.

The usage is very simple, for tls client session, just add params in settings.py in scrapy project, 
for request, specify params in meta. 

PLEASE NOTE YOU DO NOT NEED TO SPECIFY ALL PARAMS SHOWS BELOW, JUST SPECIFY REQUIRED.

For the preset usage of tls_client:

### Settings for Tls_Client Session

```python
CLIENT_IDENTIFIER = 'chrome_112'
RANDOM_TLS_EXTENSION_ORDER = True
FORCE_HTTP1 = False #default False
CATCH_PANICS = False #default False
RAW_RESPONSE_TYPE = 'HtmlResponse' #HtmlResponse or TextResponse, default HtmlResponse
```

For the custom usage:

```python
JA3_STRING = '771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0'
H2_SETTINGS = {
    "HEADER_TABLE_SIZE": 65536,
    "MAX_CONCURRENT_STREAMS": 1000,
    "INITIAL_WINDOW_SIZE": 6291456,
    "MAX_HEADER_LIST_SIZE": 262144
}
H2_SETTINGS_ORDER = [
    "HEADER_TABLE_SIZE",
    "MAX_CONCURRENT_STREAMS",
    "INITIAL_WINDOW_SIZE",
    "MAX_HEADER_LIST_SIZE"
]
SUPPORTED_SIGNATURE_ALGORITHMS = [
    "ECDSAWithP256AndSHA256",
    "PSSWithSHA256",
    "PKCS1WithSHA256",
    "ECDSAWithP384AndSHA384",
    "PSSWithSHA384",
    "PKCS1WithSHA384",
    "PSSWithSHA512",
    "PKCS1WithSHA512",
]
SUPPORTED_DELEGATED_CREDENTIALS_ALGORITHMS = [
    "ECDSAWithP256AndSHA256",
    "PSSWithSHA256",
    "PKCS1WithSHA256",
    "ECDSAWithP384AndSHA384",
    "PSSWithSHA384",
    "PKCS1WithSHA384",
    "PSSWithSHA512",
    "PKCS1WithSHA512",
]
SUPPORTED_VERSIONS = [
    "GREASE",
    "1.3",
    "1.2"
]
KEY_SHARE_CURVES = [
    "GREASE",
    "X25519"
]
CERT_COMPRESSION_ALGO = 'brotli'
ADDITIONAL_DECODE = 'gzip'
PSEUDO_HEADER_ORDER = [
    ":method",
    ":authority",
    ":scheme",
    ":path"
]
CONNECTION_FLOW = 15663105
PRIORITY_FRAMES = [
  {
    "streamID": 3,
    "priorityParam": {
      "weight": 201,
      "streamDep": 0,
      "exclusive": False
    }
  },
  {
    "streamID": 5,
    "priorityParam": {
      "weight": 101,
      "streamDep": False,
      "exclusive": 0
    }
  }
]
HEADER_ORDER = [
        "accept",
        "user-agent",
        "accept-encoding",
        "accept-language"
    ]
HEADER_PRIORITY = {
  "streamDep": 1,
  "exclusive": True,
  "weight": 1
}
FORCE_HTTP1 = False #default False
CATCH_PANICS = False #default False
RAW_RESPONSE_TYPE = 'HtmlResponse' #HtmlResponse or TextResponse, default HtmlResponse
```

### Settings for Request

```python
params = {
    'key1': 'value1',
    'key2': 'value2',
}
data = {
    'key1': 'value1',
    'key2': 'value2',
}
# turn cookie jar into dict, and remove the " mark, use ' mark
cookies = {
    'key1': 'value1',
    'key2': 'value2',
}
payload = {
    'key1': 'value1',
    'key2': 'value2'
}
proxy = 'http://username:password@ip:port' # https also works
meta_data = {
    'params': params,
    'data': data,
    'cookies': cookies,
    'json': payload,
    'allow_redirects': False,
    'insecure_skip_verify': False,
    'timeout_seconds': 10,
    'proxy': proxy
}
yield scrapy.Request(url=url, headers=headers, meta=meta_data)
```

And you also need to enable `TlsClientDownloaderMiddleware` in `DOWNLOADER_MIDDLEWARES`:

```python
DOWNLOADER_MIDDLEWARES = {
    'scrapy_tls_client.downloaderMiddleware.TlsClientDownloaderMiddleware': 543,
}
```