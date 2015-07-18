__author__ = 'Hao Lin'

import sys
import time
from controllers.main_controller import MainController
from utils.ftp_handlers import ftp_handler
from utils.database.connection import Connection
from models.mvi_models import Videos


class MetadataDownload(object):

    partner = MainController.get_partner()
    print type(partner.name), partner.name
    handler = ftp_handler.FtpHandlerFactory.create_handler(partner.name)
    print handler

    @classmethod
    def get_metadata_list_from_ftp(cls):
        try:
            start_time = time.time()
            print "start"
            xml_paths = cls.handler.get_new_xml_list()
            end_time = time.time()
            print "\n===get_metadata_list_from_ftp Elapsed Time: "+str(int(end_time-start_time))+" seconds==="
            return xml_paths
        except:
            raise

    @classmethod
    def filter_new_metadata(cls, xml_paths):
        new_xml_locations = []
        session = Connection.create_session()
        stored_paths = [seq[0] for seq in session.query(Videos.ftpInfoLocation).filter_by(partnerId=cls.partner.id).all()]
        for xml_path in xml_paths:
            if xml_path not in stored_paths:
                xml_location = {}
                filename = xml_path.split('/')[-1]
                xml_location['remote_folder'] = xml_path[:-len(filename)]
                xml_location['local_folder'] = cls.handler.local_meta_folder
                xml_location['archive_folder'] = cls.handler.archive_meta_folder
                xml_location['filename'] = filename
                new_xml_locations.append(xml_location)
        print new_xml_locations

    @classmethod
    def download_new_xmls(cls, xml_locations):
        try:
            start_time = time.time()
            if xml_locations:
                if cls.partner.name == "UMG":
                    # TODO: UMG does not need ftp
                    print "nah..."
                else:
                    for xml_location in xml_locations:
                        sys.stdout.write("Downloading: %s" % xml_location['remote_folder']+xml_location['filename'])
                        try:
                            cls.handler.sftp.get(xml_location['remote_folder']+xml_location['filename'],
                                                 xml_location['local_folder']+xml_location['filename'])
                            sys.stdout.write("      Success.\n")
                        except:
                            sys.stdout.write("      Failed...skip\n")
                            xml_locations.remove(xml_location)
            else:
                print "No new XMLs need to be downloaded for "+cls.partner.name
            end_time = time.time()
            print "\n===download_new_xmls Elapsed Time: "+str(int(end_time-start_time))+" seconds==="
            return
        except:
            raise


# MetadataDownload.get_metadata_list_from_ftp()
# xml_locations = ['/home/ftp/wmg/wmg/new_release/Assets_Only/20150618190943831/A10306F0000002WJQD/A10306F0000002WJQD.xml']
# MetadataDownload.filter_new_metadata(xml_paths)
# MetadataDownload.download_new_xmls(xml_paths)
