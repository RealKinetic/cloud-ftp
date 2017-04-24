def fetch_ftp_file(ctx, ftp_provider, storage_provider):
    """Retrieves an FTP file using a two step process:
    1) Uses the FTP provider to move the FTP file from an FTP server to a GAE
    compatible data store.
    2) Uses the storage provider to reach out to that data store to retrieve
    the file.

    :param ctx: information about the request
    :type ctx: src.ftp.Context
    :param ftp_provider: ftp interface
    :type ftp_provider: src.ftp.FTPProvider
    :param storage_provider: storage interface
    :type storage_provider: src.storage.StorageProvider
    :return: file interface, this interface *must* be closed when done
    :rtype: File
    """
    name = ftp_provider.move_file(ctx)
    return storage_provider.fetch(name)
