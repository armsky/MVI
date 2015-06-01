__author__ = 'Hao Lin'

from ftplib import FTP
from settings import WMG_CONF

class WmgFtpHandler():

    def __init__(self):
        print WMG_CONF['SERVER']
        self.ftp = FTP(WMG_CONF['SERVER'], WMG_CONF['USER'], WMG_CONF['PASSWORD'])
        print WMG_CONF['SERVER']
        self.ftp.login()
        self.root_folder = WMG_CONF['ROOT_FOLDER']
        self.video_extension = WMG_CONF['VIDEO_FILE_EXTENSION']

    def get_xml_list(self):
        xml_paths = []
        print "Getting WMG first level folders in "+self.root_folder
        first_level_dir = self.get_dir(self.root_folder)
        print "done"

    def get_dir(self, folder_path):
        dirs = []
        files = self.ftp.nlst()
        print files


w = WmgFtpHandler()
w.get_xml_list()
