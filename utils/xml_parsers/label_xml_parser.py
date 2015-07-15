__author__ = 'Hao Lin'

import xml.etree.ElementTree as ET
import datetime
from models.mvi_models import Videos, States
from utils.database.connection import Connection

class LabelXmlParser(object):

    def __init__(self, label_name, xml_location, update=False, video=None):
        """
        video is mvi_models.Videos object, if passed, cannot be None.
        """
        self.label_name = label_name
        self.xml_location = xml_location
        self.root = ET.parse(xml_location['local_folder']+xml_location['filename']).getroot()
        self.update = update
        if self.update is False:
            self.video = Videos()
        else:
            if video is None:
                raise
            self.video = video
        self.session = Connection.create_session()

    def get_state(self):
        """
        stateId
        """
        if self.update is False:
            self.video.stateId = self.session.query(States.id).filter_by(name="Metadata Imported").first()[0]
        else:
            self.video.stateId = self.session.query(States.id).filter_by(name="Video Has Metadata To Update").first()[0]

    def get_date(self):
        """
        importationDate
        updateDate
        """
        if self.update is False:
            self.video.importationDate = datetime.datetime.now()
        else:
            self.video.updateDate = datetime.datetime.now()

    def get_info_location(self):
        """
        ftpInfoLocation
        updateInfoLocation
        """
        if self.update is False:
            self.video.ftpInfoLocation = self.xml_location['remote_folder']+self.xml_location['filename']
        else:
            self.video.updateInfoLocation = self.xml_location['remote_folder']+self.xml_location['filename']

    def get_meta(self):
        """

        bitrate, originalName, sourceFolder, duration, height, width, widescreen, genres,
        rating, partner, subLabel, artist, trackName, isrc, upc, territories, mviId, GRid
        """
        # For WMG
        VideoDetailsByTerritory = self.root.findall("./ResourceList/Video/VideoDetailsByTerritory/")
        print VideoDetailsByTerritory, len(VideoDetailsByTerritory)
        for one_detail in VideoDetailsByTerritory:
            if one_detail.tag == "TechnicalVideoDetails":
                TechnicalVideoDetails = one_detail.find("TechnicalVideoDetails")
                for tech_detail in TechnicalVideoDetails:
                    if tech_detail.tag == "":
                        self.video. = one_detail.text
            elif one_detail.tag == "":
                self.video. = one_detail.text
            elif one_detail.tag == "":
                self.video. = one_detail.text
            elif one_detail.tag == "":
                self.video. = one_detail.text
            elif one_detail.tag == "":
                self.video. = one_detail.text
            elif one_detail.tag == "":
                self.video. = one_detail.text
            elif one_detail.tag == "":
                self.video. = one_detail.text
            print one_detail.tag


    def get_start_date(self):
        # TODO
        print "Not implemented"

    def get_end_date(self):
        # TODO
        print "Not implemented"

    def save_to_database(self):
        return False

location = {
    'local_folder'  : '/Users/armsky/TEMP/Metadata/WMG/',
    'filename'      : 'A10302B0003031354U.xml'
}
parser = LabelXmlParser("EMI", location)
# parser.get_state()
parser.get_meta()
