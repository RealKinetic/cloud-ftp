import abc
import six


class StorageProvider(six.with_metaclass(abc.ABCMeta, object)):
    """Provides the interface into reaching out an external storage service
    and downloading a file.  This can be any service accessible from Google
    App Engine.
    """
    @abc.abstractmethod
    def fetch(self, name):
        """Fetches the file associated with the provided name.  Raises a file
        not found error if the requested file could not be found.

        :param name: name of the file
        :type name: str
        :return: file handle
        :rtype: File
        """
        pass
