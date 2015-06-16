__author__ = 'Hao Lin'
import time
import sys
import os.path
import paramiko
# paramiko is used to establish SFTP connection (since regular FTP not work)
# See docs: http://paramiko-docs.readthedocs.org/en/latest/api/sftp.html
from settings import WMG_CONF, MOST_RECENT_DAYS

class FtpHandler(object):

    seconds_from_now = 24*60*60 * MOST_RECENT_DAYS

    def __init__(self):
        self._new_xml_list = []
        self._update_xml_list = []

    def get_xml_list(self):
        return self._new_xml_list

    def get_update_xml_list(self):
        return self._update_xml_list


class WmgFtpHandler(FtpHandler):
    def __init__(self, update=False):
        self.root_folder = WMG_CONF['ROOT_FOLDER']
        self.video_extension = WMG_CONF['VIDEO_FILE_EXTENSION']
        transport = paramiko.Transport((WMG_CONF['SERVER'], WMG_CONF['PORT']))
        transport.connect(username=WMG_CONF['USER'], password=WMG_CONF['PASSWORD'])
        sftp = paramiko.SFTPClient.from_transport(transport)
        self.sftp = sftp
        if update is False:
            self._new_xml_list = self.get_xml_list()
        else:
            self._update_xml_list = self.get_xml_list(update=True)
        self._name = "WMG FTP Handler"

    def get_xml_list(self, update=False):
        xml_paths = []
        print "Getting WMG first level folders in " + self.root_folder
        first_level_dir_attrs = self.sftp.listdir_attr(self.root_folder)
        # Example of a dir_attr: (drwxrws---   1 518      509          4096 13 Feb 22:05 20150214023209453)
        for first_level_dir_attr in first_level_dir_attrs:

            if abs(int(time.time()) - first_level_dir_attr.st_mtime) < FtpHandler.seconds_from_now:
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
            else:
                print "Folder "+first_level_dir_attr.filename+" exceeds "+str(MOST_RECENT_DAYS)+" days... Skip!"

        return xml_paths

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



class UmgFtpHandler(FtpHandler):
    def __init__(self):

        self._name = "UMG FTP Handler"


class SonyFtpHandler(FtpHandler):
    def __init__(self):

        self._name = "SONY FTP Handler"


class EmiFtpHandler(FtpHandler):
    def __init__(self):

        self._name = "EMI FTP Handler"


class VplFtpHandler(FtpHandler):
    def __init__(self):

        self._name = "VPL FTP Handler"


class FtpHandlerFactory(object):
    @staticmethod
    def create_handler(label, update=False):
        if label == "WMG" or label == "1" or label == 1:
            return WmgFtpHandler(update)
        elif label == "UMG" or label == "3" or label == 3:
            return UmgFtpHandler(update)
        elif label == "SONY" or label == "4" or label == 4:
            return SonyFtpHandler(update)
        elif label == "EMI" or label == "5" or label == 5:
            return EmiFtpHandler(update)
        elif label == "VPL" or label == "10" or label == 10:
            return VplFtpHandler(update)
        else:
            sys.exit()

handler = FtpHandlerFactory.create_handler("WMG", update=False)
print handler.get_xml_list()
