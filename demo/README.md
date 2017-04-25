## Demo

This offers a demo of the cloud ftp workflow.  You can run this locally, but you'll need an external cloud function and gcs bucket.  To use Google's cloud storage you need to set an access token or it will only hit up a local stub.

### Setting up GCS
To get a local access token:
```sh
$ gsutil -d ls
```

Scroll down and get the string after `Bearer`.

Copy that string into the `set_access_token` call in `main.py`.

This will ensure the remote GCS service is used.

### Setting up cloud functions

Go to [ftp-bucket](https://github.com/RealKinetic/ftp-bucket) and follow the instructions to set up a cloud function.

This function will move a file from an FTP server to your GCS bucket for later access.

### Start the local server

Two commands:
```sh
$ make install
```

Will install all of the dependencies into a folder called `libs`.

```sh
$ make run
```

Will start the local development server.

### Access the API

I use a tool like Postman just to make this easy.  In summary, you need to `POST` the following payload to `http://localhost:8080/`
```
{
	"fileName": "<your filename here>",
	"user": "<optional ftp username>",
	"password": "<optional password>",
	"host": "ftp hostname",
	"url": "<cloud function url, you got this when you deployed the cloud function>",
	"bucket": "<name of the bucket you created above>"
}
```

### Limitations

Currently, if a file is not found the server returns a 500.  That's a limitation of the importFTP cloud function that will eventually be fixed.