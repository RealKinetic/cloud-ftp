class FileNotFoundError(Exception):
    """Raised when a requested item could not be found.
    """
    pass


class UnauthorizedError(Exception):
    """Raised when user does not have access to the specified FTP host.
    """
    pass
