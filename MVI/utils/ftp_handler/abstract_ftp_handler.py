__author__ = 'Hao Lin'

import abc
from ftplib import FTP


class AbstractFtpHandler:
    __metaclass__ = abc.ABCMeta

    _ftp = None
    _root_folder = None

    @abc.abstractmethod
    def get_xml_list(self):
        return

    @abc.abstractmethod
    def get_ftp(self):
        return self._ftp

    @abc.abstractmethod
    def get_root_folder(self):
        return self._root_folder
