# Copyright 2017 Real Kinetic, LLC. All Rights Reserved.

import json
import unittest

import mock

from cloud_ftp import error
from cloud_ftp.ftp import Context
from cloud_ftp.ftp.providers.cloud_function import CloudFunctionProvider, DEFAULT_DEADLINE


class CloudFunctionTestCase(unittest.TestCase):
    def test_make_data(self):
        ctx = Context('file', 'host', 'user', 'pass')
        bucket = 'bucket'
        expected = {
            'bucketName': bucket,
            'host': 'host',
            'user': 'user',
            'password': 'pass',
            'fileName': 'file',
        }
        p = CloudFunctionProvider('url', bucket_name=bucket)
        self.assertEqual(json.dumps(expected), p.make_data(ctx))

    def test_verify_response_ok(self):
        ctx = Context('file', 'host', 'user', 'pass')
        p = CloudFunctionProvider('url', bucket_name='bucket')
        response = mock.MagicMock()
        response.status_code = 200

        result = p.verify_response(ctx, response)
        self.assertEqual('file', result)

    def test_verify_not_found_error(self):
        ctx = Context('file', 'host', 'user', 'pass')
        p = CloudFunctionProvider('url', bucket_name='bucket')
        response = mock.MagicMock()
        response.status_code = 404

        self.assertRaises(
            error.FileNotFoundError, p.verify_response, ctx, response
        )

    def test_verify_generic_error(self):
        ctx = Context('file', 'host', 'user', 'pass')
        p = CloudFunctionProvider('url', bucket_name='bucket')
        response = mock.MagicMock()
        response.status_code = 500

        self.assertRaises(
            ValueError, p.verify_response, ctx, response
        )

    @mock.patch('cloud_ftp.ftp.providers.cloud_function.urlfetch')
    def test_move_file(self, url_fetch):
        ctx = Context('file', 'host', 'user', 'pass')
        p = CloudFunctionProvider('url', bucket_name='bucket')
        response = mock.MagicMock()
        response.status_code = 200
        url_fetch.fetch.return_value = response

        self.assertEqual('file', p.move_file(ctx))
        url_fetch.fetch.assert_called_once_with(
            'url',
            payload=p.make_data(ctx),
            headers={"Content-Type": "application/json"},
            deadline=DEFAULT_DEADLINE,
            method=url_fetch.POST,
        )
