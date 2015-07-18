__author__ = 'Hao Lin'

from main_controller import MainController


class IngestController(MainController):

    def __init__(self, partner, process):
        self.partner = partner
        self.process = process

    def import_metadata(self):

        from utils.processes.metadata_download import MetadataDownload

        xml_paths = MetadataDownload.get_metadata_list_from_ftp()
        new_xml_locations = MetadataDownload.filter_new_metadata(xml_paths)
        MetadataDownload.download_new_xmls(new_xml_locations)

        print "done"
