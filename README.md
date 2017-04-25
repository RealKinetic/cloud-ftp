## Cloud FTP

Sometimes there is a requirement to gain access to FTP files from Google App Engine.  Unfortunately, this is not natively supported leaving users to solve this problem using other mehods.

This library is a simple implementation and workaround of this limitation by utilizing other means.

The default implementations are very generic so users can customize, by example, as they see fit.  However, a simple implementation using Google Cloud Functions is included by default.

### Google Cloud Functions

A simple cloud function-based FTP provider is included.  Cloud functions are similar to AWS's lambdas in that they are deployable functions that execute on demand in a highly scalable manner.

This means that users of this default provider need to grab the cloud function at [ftp-bucket](https://github.com/RealKinetic/ftp-bucket) and follow the instructions there to deploy.

The workflow is as follows:
1. FTP Provider (cloud function) accesses and FTP server on the consumer's behalf and moves that file to GCS.
2. Storage Provider reaches out to GCS and downloads the file.

This is one possible use case, but users are free to implement FTP and Storage providers to tailor their use cases.  These interfaces (using ABC) are injected into the API layer so that piece should be reusable.

### TODO:

There is a known limitation currently regarding the cloud function returning a 500 when a requested file cannot be found.  That will be addressed shortly.

Authors:
dev@realkinetic.com
