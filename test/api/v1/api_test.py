import unittest

import mock

from src.api import v1 as api

from src.ftp import Context


class ApiTestCase(unittest.TestCase):
    def test_fetch_ftp_file(self):
        ftp_provider = mock.MagicMock()
        storage_provider = mock.MagicMock()
        ctx = Context('file', 'host', 'user', 'pass')
        ftp_provider.move_file.return_value = 'test'

        api.fetch_ftp_file(ctx, ftp_provider, storage_provider)
        ftp_provider.move_file.assert_called_once_with(ctx)
        storage_provider.fetch.assert_called_once_with('test')
