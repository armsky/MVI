__author__ = 'Hao Lin'

from ftplib import FTP
import time
import paramiko
# paramiko is used to establish SFTP connection (since regular FTP not work)
# See docs: http://paramiko-docs.readthedocs.org/en/latest/api/sftp.html
from settings import WMG_CONF, MOST_RECENT_DAYS

class WmgFtpHandler():

    def __init__(self):

        self.root_folder = WMG_CONF['ROOT_FOLDER']
        self.video_extension = WMG_CONF['VIDEO_FILE_EXTENSION']

        transport = paramiko.Transport((WMG_CONF['SERVER'], WMG_CONF['PORT']))
        transport.connect(username=WMG_CONF['USER'], password=WMG_CONF['PASSWORD'])
        sftp = paramiko.SFTPClient.from_transport(transport)
        self.sftp = sftp
        print "connected"

    def get_xml_list(self):
        xml_paths = []
        seconds_from_now = 24*60*60 * MOST_RECENT_DAYS
        print "Getting WMG first level folders in " + self.root_folder
        first_level_dir_attrs = self.sftp.listdir_attr(self.root_folder)
        # Example of a dir_attr: (drwxrws---   1 518      509          4096 13 Feb 22:05 20150214023209453)
        for first_level_dir_attr in first_level_dir_attrs:
            if abs(int(time.time()) - first_level_dir_attr.st_mtime) < seconds_from_now:
                print "Getting WMG second level folders in "+first_level_dir_attr.filename

                print first_level_dir_attr.filename, first_level_dir_attr.st_mtime, int(time.time())

            else:
                print "Folder "+first_level_dir_attr.filename+" exceeds "+MOST_RECENT_DAYS+" days... Skip!"

    def get_xml_path(self, folder_path, update=False):
        # Determine to get the xml or not based on the Flag:update
        print "wooow"


w = WmgFtpHandler()
w.get_xml_list()
