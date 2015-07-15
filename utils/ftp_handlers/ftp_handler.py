__author__ = 'Hao Lin'
import time
import sys
import os.path
import abc
import paramiko
# paramiko is used to establish SFTP connection (since regular FTP not work)
# See docs: http://paramiko-docs.readthedocs.org/en/latest/api/sftp.html
# TODO: TEST_WMG_CONF need to be deleted after local test done
from settings import WMG_CONF, TEST_WMG_CONF, MOST_RECENT_DAYS

WMG_CONF = TEST_WMG_CONF

class FtpHandler(object):
    __metaclass__ = abc.ABCMeta

    seconds_from_now = 24*60*60 * MOST_RECENT_DAYS

    def get_new_xml_list(self):
        """Get NewRelease XMLs from label FTP"""
        return self.get_xml_list(False)

    def get_update_xml_list(self):
        """Get Update XMLs from label FTP, based on update_flag=True"""
        return self.get_xml_list(update=True)

    @abc.abstractmethod
    def get_xml_list(self, update=False):
        """Implemented by each Label Ftp Handler"""
        return


class WmgFtpHandler(FtpHandler):
    def __init__(self):
        self.root_folder = WMG_CONF['ROOT_FOLDER']
        self.local_video_folder = WMG_CONF['LOCAL_VIDEO_FOLDER']
        self.local_meta_folder = WMG_CONF['LOCAL_META_FOLDER']
        self.archive_meta_folder = WMG_CONF['ARCHIVE_METADATA_FOLDER']
        self.video_extension = WMG_CONF['VIDEO_FILE_EXTENSION']
        transport = paramiko.Transport((WMG_CONF['SERVER'], WMG_CONF['PORT']))
        transport.connect(username=WMG_CONF['USER'], password=WMG_CONF['PASSWORD'])
        sftp = paramiko.SFTPClient.from_transport(transport)
        self.sftp = sftp

    def __str__(self):
        return "WMG FTP Handler"

    def get_xml_list(self, update=False):
        """
        Get a list of paths of NewRelease or Update XMLs
        :param update: Boolean
        :return: list of XML paths
        """
        xml_paths = []
        print "Getting WMG first level folders in " + self.root_folder
        first_level_dir_attrs = self.sftp.listdir_attr(self.root_folder)
        # Example of a dir_attr: <SFTPAttributes: [ size=4096 uid=518 gid=509 mode=042770 atime=1434509348 mtime=1423883137 ]>
        for first_level_dir_attr in first_level_dir_attrs:
            if first_level_dir_attr.filename not in ['reports']:
                if abs(int(time.time()) - first_level_dir_attr.st_mtime) < FtpHandler.seconds_from_now:
                    print "Getting WMG second level folders in "+first_level_dir_attr.filename
                    second_level_dirs = self.sftp.listdir(os.path.join(self.root_folder, first_level_dir_attr.filename))
                    for second_level_dir in second_level_dirs:
                        # Make sure it's a folder not a BatchComplete xml
                        if ".xml" not in second_level_dir:
                            print "Getting xml from ", second_level_dir
                            folder_path = os.path.join(self.root_folder, first_level_dir_attr.filename, second_level_dir)
                            if update is False:
                                xml_path = self.get_xml_path(folder_path)
                            elif update is True:
                                xml_path = self.get_xml_path(folder_path, update)
                            # If it is a valid path, append it to list
                            if xml_path:
                                xml_paths.append(xml_path)
                else:
                    print "Folder "+first_level_dir_attr.filename+" exceeds "+str(MOST_RECENT_DAYS)+" days... Skip!"

        return xml_paths

    def get_xml_path(self, folder_path, update=False):
        """
        Get the full path of xml. If the update flag is False, the xml is a NewRelease xml. otherwise it's a Update xml.
        :param folder_path:
        :param update: Boolean
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
    def create_handler(label):
        if label.upper() == "WMG" or int(label) == 1:
            return WmgFtpHandler()
        elif label.upper() == "UMG" or int(label) == 3:
            return UmgFtpHandler()
        elif label.upper() == "SONY" or int(label) == 4:
            return SonyFtpHandler()
        elif label.upper() == "EMI" or int(label) == 5:
            return EmiFtpHandler()
        elif label.upper() == "VPL" or int(label) == 10:
            return VplFtpHandler()
        else:
            print "Not a valid handler. See FtpHandlerFactory.create_handler()"
            sys.exit()


def main():
    handler = FtpHandlerFactory.create_handler("WMG")
    print handler
    print handler.get_update_xml_list()

if __name__ == "__main__":
    main()
