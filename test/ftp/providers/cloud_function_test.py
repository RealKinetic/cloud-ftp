import json
import unittest

import mock

from src.cloud_ftp.ftp import Context
from src.cloud_ftp.ftp.providers.cloud_function import CloudFunctionProvider


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

    def test_verify_error(self):
        ctx = Context('file', 'host', 'user', 'pass')
        p = CloudFunctionProvider('url', bucket_name='bucket')
        response = mock.MagicMock()
        response.status_code = 404

        self.assertRaises(ValueError, p.verify_response, ctx, response)

    @mock.patch('src.cloud_ftp.ftp.providers.cloud_function.urlfetch')
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
        )
