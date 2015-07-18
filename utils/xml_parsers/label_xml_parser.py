__author__ = 'Hao Lin'

import xml.etree.ElementTree as ET
import datetime
from models.mvi_models import Videos, States
from utils.database.connection import Connection
import xml_parser_helper as helper


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
        isrc, duration, trackName, artist, subLabel, genres, rating
        bitrate, height, width, widescreen, originalName, sourceFolder
        upc, GRid, mviId

        , partnerId, territories,
        """
        # TODO: right now for WMG only

        # isrc
        isrc = self.root.find("./ResourceList/Video/VideoId/ISRC").text
        self.video.isrc = isrc

        # trackName
        track_name = self.root.find("./ResourceList/Video/ReferenceTitle/TitleText").text
        self.video.trackName = track_name

        # duration
        duration = self.root.find("./ResourceList/Video/Duration").text
        duration = helper.ddex_time_to_seconds(duration)
        self.video.duration = duration

        detail = self.root.find("./ResourceList/Video/VideoDetailsByTerritory")

        # artist
        artist = detail.find("./DisplayArtist/PartyName/FullName").text
        self.video.artist = artist

        # subLabel
        sub_label = detail.findall("./LabelName")[0].text
        self.video.subLabel = sub_label

        # genre
        genre = detail.find("./Genre/GenreText").text
        self.video.genre = genre

        # rating
        rating = detail.find("./ParentalWarningType").text
        self.video.rating = rating

        technical_detail = detail.find("./TechnicalVideoDetails")

        # bitrate
        bitrate_element = technical_detail.find("./OverallBitRate")
        self.video.bitrate = bitrate_element.text + " " + bitrate_element.get("UnitOfMeasure")

        # height
        height = technical_detail.find("./ImageHeight").text
        self.video.height = height

        # width
        width = technical_detail.find("./ImageWidth").text
        self.video.width = width

        # widescreen
        self.video.widescreen = helper.is_widescreen(height, width)

        file_detail = technical_detail.find("./File")

        # originalName
        original_name = file_detail.find("./FileName").text
        self.video.originalName = original_name

        # sourceFolder
        source_folder = file_detail.find("./FilePath").text
        self.video.sourceFolder = self.xml_location['remote_folder'] + source_folder

        # upc (GRid)
        upc = self.root.find("./ReleaseList/Release").find("./ReleaseId/GRid").text
        self.video.upc = upc
        self.video.GRid = upc

        # partnerId

        # mviId



        # TODO: featuredArtist

        print self.video


    def get_start_date(self):
        # TODO
        print "Not implemented"

    def get_end_date(self):
        # TODO
        print "Not implemented"

    def save_to_database(self):
        return False



location = {
    'remote_folder' : '/Fake/path/for/now/',
    'local_folder'  : '/Users/armsky/TEMP/Metadata/WMG/',
    'filename'      : 'A10302B0003031354U.xml'
}
parser = LabelXmlParser("WMG", location)
# parser.get_state()
parser.get_meta()
