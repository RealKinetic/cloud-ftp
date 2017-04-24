"""
Provides interfaces into the possible storage systems used.  Any storage system,
including home grown generic HTTP interfaces, can be used to store the file,
except FTP itself.  It must exist on one of Google's approved ports.  GCS is
simply a very simple mechanism to do this and this provider is provided by
default.
"""
