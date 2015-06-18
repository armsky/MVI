__author__ = 'Hao Lin'

import sys
import time
from controllers.main_controller import MainController
from utils.ftp_handlers import ftp_handler
from utils.database.connection import Connection
from models.mvi_models import Videos

# TODO: test only, need to remove this
MainController.set_partner(1)

class MetadataDownload(object):

    partner = MainController.get_partner()
    handler = ftp_handler.FtpHandlerFactory.create_handler(partner.name)

    @classmethod
    def get_metadata_list_from_ftp(cls):
        try:
            start_time = time.time()
            xml_paths = cls.handler.get_new_xml_list()
            end_time = time.time()
            print "\n===get_metadata_list_from_ftp Elapsed Time: "+str(int(end_time-start_time))+" seconds==="
            return xml_paths
        except:
            raise

    @classmethod
    def filter_new_metadata(cls, xml_paths):
        new_xml_paths = []
        session = Connection.create_session()
        stored_paths = [seq[0] for seq in session.query(Videos.ftpInfoLocation).filter_by(partnerId=cls.partner.id).all()]
        for xml_path in xml_paths:
            if xml_path not in stored_paths:
                new_xml_paths.append(xml_path)
        print new_xml_paths

    @classmethod
    def download_new_xmls(cls, xml_paths):
        try:
            start_time = time.time()
            if xml_paths:
                if cls.partner.name == "UMG":
                    # TODO: UMG does not need ftp
                    print "nah..."
                else:
                    for xml_path in xml_paths:
                        filename = xml_path.split('/')[-1]
                        sys.stdout.write("Downloading: %s" % xml_path)
                        try:
                            cls.handler.sftp.get(xml_path, cls.handler.local_meta_folder+filename)
                            sys.stdout.write("      Success.\n")
                        except:
                            sys.stdout.write("      Failed...skip\n")
                            xml_paths.remove(xml_path)
            else:
                print "No new XMLs need to be downloaded for "+cls.partner.name
            end_time = time.time()
            print "\n===download_new_xmls Elapsed Time: "+str(int(end_time-start_time))+" seconds==="
            return
        except:
            raise


# MetadataDownload.get_metadata_list_from_ftp()
xml_paths = ['/home/ftp/wmg/wmg/new_release/Assets_Only/20150618190943831/A10306F0000002WJQD/A10306F0000002WJQD.xml']
# MetadataDownload.filter_new_metadata(xml_paths)
MetadataDownload.download_new_xmls(xml_paths)
