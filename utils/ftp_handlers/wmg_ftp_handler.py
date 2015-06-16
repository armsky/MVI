__author__ = 'Hao Lin'

from ftplib import FTP
import time
import os.path
import paramiko
# paramiko is used to establish SFTP connection (since regular FTP not work)
# See docs: http://paramiko-docs.readthedocs.org/en/latest/api/sftp.html
from settings import WMG_CONF, MOST_RECENT_DAYS

class WmgFtpHandler:

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
                second_level_dirs = self.sftp.listdir(os.path.join(self.root_folder, first_level_dir_attr.filename))
                for second_level_dir in second_level_dirs:
                    # Make sure it's a folder not a BatchComplete xml
                    if ".xml" not in second_level_dir:
                        print "Getting xml from ", second_level_dir
                        xml_path = self.get_xml_path(os.path.join(self.root_folder,
                                                                  first_level_dir_attr.filename, second_level_dir))
                        if xml_path:
                            xml_paths.append(xml_path)
                            print xml_paths
            else:
                print "Folder "+first_level_dir_attr.filename+" exceeds "+str(MOST_RECENT_DAYS)+" days... Skip!"

    def get_xml_path(self, folder_path, update=False):
        """
        Get the full path of xml. If the update flag is False, the xml is a NewRelease xml. otherwise it's a Update xml.
        :param folder_path:
        :param update:
        :return: xml_path or False
        """
        has_video = False
        has_xml = False
        contents = self.sftp.listdir(folder_path)
        for content in contents:
            print os.path.join(folder_path, content)

            if ".xml" in content:
                has_xml = True
                xml_path = os.path.join(folder_path, content)
            elif "resources" in content:
                resources = self.sftp.listdir(os.path.join(folder_path, content))
                for resource in resources:
                    if self.video_extension in resource:
                        has_video = True
        if update is False:
            if has_video and has_xml:
                return xml_path
            else:
                return False
        # Find the update xml
        else:
            if has_xml and has_video is False:
                return xml_path
            else:
                return False


w = WmgFtpHandler()
w.get_xml_list()
