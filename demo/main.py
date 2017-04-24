import json

import webapp2

from src.api import v1 as api
from src.ftp import Context
from src.ftp.providers.cloud_function import CloudFunctionProvider
from src.storage.providers.gcs import GCSStorageProvider


class MainPage(webapp2.RequestHandler):
    """Main page for GCS demo application."""

    def post(self):
        jsonstring = self.request.body
        jsonobject = json.loads(jsonstring)

        ctx = self.make_context(**jsonobject)
        ftp = self.make_ftp_provider(**jsonobject)
        storage = self.make_storage_provider(**jsonobject)

        file = api.fetch_ftp_file(ctx, ftp, storage)
        value = ''
        for i in xrange(10):
            value += file.readline()

        file.close()

        return {'data': value}

    def make_context(self, **kwargs):
        return Context(
            kwargs.get('fileName'),
            kwargs.get('host'),
            kwargs.get('user'),
            kwargs.get('password'),
        )

    def make_ftp_provider(self, **kwargs):
        return CloudFunctionProvider(
            kwargs.get('url'),
            kwargs.get('bucket', None)
        )

    def make_storage_provider(self, **kwargs):
        return GCSStorageProvider(
            kwargs.get('bucket', None)
        )


app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
