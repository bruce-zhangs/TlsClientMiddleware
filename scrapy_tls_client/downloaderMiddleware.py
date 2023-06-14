# -*- coding: utf-8 -*-

import tls_client
from scrapy import signals
from scrapy.http import HtmlResponse, TextResponse
from twisted.internet.threads import deferToThread
from twisted.internet import defer
from twisted.internet.error import (
    ConnectError,
    ConnectionDone,
    ConnectionLost,
    ConnectionRefusedError,
    DNSLookupError,
    TCPTimedOutError,
    TimeoutError,
)
from twisted.web.client import ResponseFailed
from scrapy.core.downloader.handlers.http11 import TunnelError
from scrapy.utils.python import global_object_name
from scrapy.utils.response import response_status_message
from scrapy_tls_client.settings import *
import logging
logger = logging.getLogger('TlsClientDownloaderMiddleware')


class TlsClientDownloaderMiddleware:

    EXCEPTIONS_TO_RETRY = (
        defer.TimeoutError,
        TimeoutError,
        DNSLookupError,
        ConnectionRefusedError,
        ConnectionDone,
        ConnectError,
        ConnectionLost,
        TCPTimedOutError,
        ResponseFailed,
        IOError,
        TunnelError,
    )

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        settings = crawler.settings
        s = cls()
        cls.client_identifier = settings.get('CLIENT_IDENTIFIER', CLIENT_IDENTIFIER)
        cls.ja3_string = settings.get('JA3_STRING', JA3_STRING)
        cls.h2_settings = settings.get('H2_SETTINGS', H2_SETTINGS)
        cls.h2_settings_order = settings.get('H2_SETTINGS_ORDER', H2_SETTINGS_ORDER)
        cls.supported_signature_algorithms = settings.get('SUPPORTED_SIGNATURE_ALGORITHMS',
                                                        SUPPORTED_SIGNATURE_ALGORITHMS)
        cls.supported_delegated_credentials_algorithms = settings.get('SUPPORTED_DELEGATED_CREDENTIALS_ALGORITHMS',
                                                                    SUPPORTED_DELEGATED_CREDENTIALS_ALGORITHMS)
        cls.supported_versions = settings.get('SUPPORTED_VERSIONS', SUPPORTED_VERSIONS)
        cls.key_share_curves = settings.get('KEY_SHARE_CURVES', KEY_SHARE_CURVES)
        cls.cert_compression_algo = settings.get('CERT_COMPRESSION_ALGO', CERT_COMPRESSION_ALGO)
        cls.additional_decode = settings.get('ADDITIONAL_DECODE', ADDITIONAL_DECODE)
        cls.pseudo_header_order = settings.get('PSEUDO_HEADER_ORDER', PSEUDO_HEADER_ORDER)
        cls.connection_flow = settings.get('CONNECTION_FLOW', CONNECTION_FLOW)
        cls.priority_frames = settings.get('PRIORITY_FRAMES', PRIORITY_FRAMES)
        cls.header_order = settings.get('HEADER_ORDER', HEADER_ORDER)
        cls.header_priority = settings.get('HEADER_PRIORITY', HEADER_PRIORITY)
        cls.random_tls_extension_order = settings.get('RANDOM_TLS_EXTENSION_ORDER', RANDOM_TLS_EXTENSION_ORDER)
        cls.force_http1 = settings.get('FORCE_HTTP1', FORCE_HTTP1)
        cls.catch_panics = settings.get('CATCH_PANICS', CATCH_PANICS)
        cls.retry_enabled = settings.getbool('RETRY_ENABLED')
        cls.max_retry_times = settings.getint('RETRY_TIMES')
        cls.retry_http_codes = set(int(x) for x in settings.getlist('RETRY_HTTP_CODES'))
        cls.priority_adjust = settings.getint('RETRY_PRIORITY_ADJUST')
        cls.raw_response_type = settings.get('RAW_RESPONSE_TYPE', RAW_RESPONSE_TYPE)
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def _retry(self, request, reason, spider):

        if not self.retry_enabled:
            return None

        retry_times = request.meta.get('retry_times', 0) + 1
        max_retry_times = self.max_retry_times

        if 'max_retry_times' in request.meta:
            max_retry_times = request.meta['max_retry_times']

        stats = spider.crawler.stats
        if retry_times <= max_retry_times:
            logger.debug("Retrying %(request)s (failed %(retry_times)d times): %(reason)s",
                         {'request': request, 'retry_times': retry_times, 'reason': reason},
                         extra={'spider': spider})
            new_request = request.copy()
            new_request.meta["retry_times"] = retry_times
            new_request.dont_filter = True
            new_request.priority = request.priority + self.priority_adjust

            if callable(reason):
                reason = reason()
            if isinstance(reason, Exception):
                reason = global_object_name(reason.__class__)

            stats.inc_value('retry/count')
            stats.inc_value('retry/reason_count/%s' % reason)
            return new_request
        else:
            stats.inc_value('retry/max_reached')
            logger.error("Gave up retrying %(request)s (failed %(retry_times)d times): %(reason)s",
                         {'request': request, 'retry_times': retry_times, 'reason': reason},
                         extra={'spider': spider})
            return None

    def _process_request(self, request, spider):
        if self.client_identifier:
            tls_session = tls_client.Session(
                client_identifier=self.client_identifier,
                additional_decode=self.additional_decode,
                header_order=self.header_order,
                random_tls_extension_order=self.random_tls_extension_order,
                force_http1=self.force_http1,
                catch_panics=self.catch_panics
            )
        else:
            tls_session = tls_client.Session(
                ja3_string=self.ja3_string,
                h2_settings=self.h2_settings,
                h2_settings_order=self.h2_settings_order,
                supported_signature_algorithms=self.supported_signature_algorithms,
                supported_delegated_credentials_algorithms=self.supported_delegated_credentials_algorithms,
                supported_versions=self.supported_versions,
                key_share_curves=self.key_share_curves,
                cert_compression_algo=self.cert_compression_algo,
                additional_decode = self.additional_decode,
                pseudo_header_order=self.pseudo_header_order,
                connection_flow=self.connection_flow,
                priority_frames=self.priority_frames,
                header_order=self.header_order,
                header_priority=self.header_priority,
                force_http1=self.force_http1,
                catch_panics=self.catch_panics
            )
        method = request.method
        url = request.url
        headers = request.headers.to_unicode_dict()
        params = request.meta.get('params', None)
        data = request.meta.get('data', None)
        cookies = request.meta.get('cookies', None)
        json = request.meta.get('json', None)
        allow_redirects = request.meta.get('allow_redirects', False)
        insecure_skip_verify = request.meta.get('insecure_skip_verify', False)
        timeout_seconds = request.meta.get('timeout_seconds', None)
        proxy = request.meta.get('proxy', None)
        try:
            response = tls_session.execute_request(method=method, url=url, params=params, data=data,
                                                   headers=headers, cookies=cookies,
                                                   json=json, allow_redirects=allow_redirects,
                                                   insecure_skip_verify=insecure_skip_verify,
                                                   timeout_seconds=timeout_seconds, proxy=proxy)
        except Exception as e:
            return None

        if self.raw_response_type == 'HtmlResponse':
            new_response = HtmlResponse(url=request.url, status=response.status_code, headers=response.headers,
                                        body=response.text, request=request, encoding='utf-8')
        elif self.raw_response_type == 'TextResponse':
            new_response = TextResponse(url=request.url, status=response.status_code, headers=response.headers,
                                        body=response.text, request=request, encoding='utf-8')
        else:
            logger.error(f'RAW_RESPONSE_TYPE must be HtmlResponse or TextResponse, but {self.raw_response_type} was given')
            return None
        return new_response

    def process_request(self, request, spider):
        logger.debug('tls client handle request %s', request)
        return deferToThread(self._process_request, request, spider)

    def process_response(self, request, response, spider):
        if request.meta.get("dont_retry", False):
            return response
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            return self._retry(request, reason, spider) or response
        return response

    def process_exception(self, request, exception, spider):
        if isinstance(exception, self.EXCEPTIONS_TO_RETRY) and not request.meta.get(
                "dont_retry", False
        ):
            return self._retry(request, exception, spider)

    def spider_opened(self, spider):
        spider.logger.info("TlsClientDownloaderMiddleware enabled")

    def spider_closed(self, spider):
        spider.logger.info("Spider closed: %s" % spider.name)
