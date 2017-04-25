import json

from cloudstorage import common

import webapp2

from cloud_ftp.api import v1 as api
from cloud_ftp.ftp import Context
from cloud_ftp.ftp.providers.cloud_function import CloudFunctionProvider
from cloud_ftp.storage.providers.gcs import GCSStorageProvider


common.set_access_token('your access token here... `gsutil -d ls`')


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

        self.response.headers['Content-Type'] = 'application/json'
        obj = {
            'data': value,
        }
        self.response.out.write(json.dumps(obj))

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
