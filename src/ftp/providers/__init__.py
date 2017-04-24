"""
A collected package of generic "providers".  A provider is nothing but a service
that takes some FTP information and moves a file from an FTP server to another
service accessible from app engine.

An example is a generic HTTP provider that simply communicates with an external
service that moves a file from an FTP server to Google Cloud Storage which is
easy to access from GAE.
"""
