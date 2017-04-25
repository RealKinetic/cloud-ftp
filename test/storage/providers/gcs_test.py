import unittest

import cloudstorage

import mock

from cloud_ftp import error
from cloud_ftp.storage.providers.gcs import GCSStorageProvider


class GCSTestCase(unittest.TestCase):
    def test_path(self):
        p = GCSStorageProvider(bucket='bucket')
        path = p.create_path('name')
        self.assertEqual('/bucket/name', path)

    @mock.patch('cloud_ftp.storage.providers.gcs.cloudstorage')
    def test_fetch_ok(self, gcs):
        p = GCSStorageProvider(bucket='bucket')
        gcs.open.return_value = 5

        result = p.fetch('name')
        self.assertEqual(5, result)
        gcs.open.assert_called_once_with(
            p.create_path('name'),
        )

    @mock.patch('cloud_ftp.storage.providers.gcs.cloudstorage')
    def test_fetch_not_found(self, gcs):
        gcs.open.side_effect = cloudstorage.errors.NotFoundError()
        p = GCSStorageProvider(bucket='bucket')

        self.assertRaises(
            error.FileNotFoundError,
            p.fetch,
            'name',
        )
