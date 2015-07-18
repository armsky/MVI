__author__ = 'Hao Lin'

from pprint import pprint
from utils.database.connection import Connection
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


engine = Connection.get_engine()
metadata = MetaData()
Base = declarative_base()


class Videos(Base):
    """

    """
    __tablename__ = 'videos'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    id = Column(Integer, primary_key=True)
    thumbnails = relationship('Thumbnails', backref=backref('videos'))
    encoded_videos = relationship('EncodedVideos', backref=backref('videos'))

    partnerId = Column(Integer, ForeignKey('partners.id'))
    stateId = Column(Integer, ForeignKey('states.id'))

    artist = Column(String(256))
    bitrate = Column(String(32))
    cleanUpDate = Column(DateTime, default=func.now())
    downloadDate = Column(DateTime, default=func.now())
    arcId = Column(String(64))
    isrcDistPolicy = Column(String(64))
    receiptDateArc = Column(DateTime, default=func.now())
    errorStatusArc = Column(String(512))
    duration = Column(Integer)
    ftpInfoLocation = Column(String(512))
    genres = Column(String(32))
    hd = Column(Boolean)
    height = Column(Integer)
    importationDate = Column(DateTime, default=func.now())
    infoParseDate = Column(DateTime, default=func.now())
    isrc = Column(String(32))
    mviId = Column(String(256))
    localPath = Column(String(512))
    originalFileSize = Column(Integer)
    originalName = Column(String(256))
    rating = Column(String(32))
    reported = Column(Boolean)
    sendToAkamaiDate = Column(DateTime, default=func.now())
    sendToEncoderDate = Column(DateTime, default=func.now())
    sendToUmaDate = Column(DateTime, default=func.now())
    sourceFolder = Column(String(512))
    subLabel = Column(String(256))
    subTitle = Column(String(256))
    startDate = Column(Date)
    endDate = Column(Date)
    territories = Column(String(1024))
    trackName = Column(String(256))
    umaId = Column(Integer)
    upc = Column(String(32))
    widescreen = Column(Boolean)
    width = Column(Integer)
    updateDate = Column(DateTime, default=func.now())
    updateInfoLocation = Column(String(512))
    featuredArtist1 = Column(String(256))
    featuredArtist2 = Column(String(256))
    featuredArtist3 = Column(String(256))
    GRid = Column(String(256))

    def __str__(self):
        attrs = vars(self)
        return "\n\t" + "\n\t".join("%s: %s" % item for item in attrs.items())


class EncodedVideos(Base):
    """

    """
    __tablename__ = 'encoded_videos'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    id = Column(Integer, primary_key=True)

    videoId = Column(Integer, ForeignKey('videos.id', onupdate='cascade', ondelete='cascade'))
    video = relationship('Videos', backref=backref('EncodedVideos', lazy='dynamic'))

    width = Column(Integer)
    height = Column(Integer)
    name = Column(String(256))
    mediaType = Column(String(256))
    bitrate = Column(String(32))
    akamaiPath = Column(String(512), nullable=True)
    uploaded = Column(Boolean, nullable=True)
    encoded = Column(Boolean, nullable=True)


class Thumbnails(Base):
    """

    """
    __tablename__ = 'thumbnails'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    id = Column(Integer, primary_key=True)

    videoid = Column(Integer, ForeignKey('videos.id', onupdate='cascade', ondelete='cascade'))
    video = relationship('Videos', backref=backref('Thumbnails', lazy='dynamic'))

    width = Column(Integer)
    height = Column(Integer)
    localPath = Column(String(512))
    akamaiPath = Column(String(512), nullable=True)
    uploaded = Column(Boolean, nullable=True)


class States(Base):
    """

    """
    __tablename__ = 'states'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)


class Partners(Base):
    """

    """
    __tablename__ = 'partners'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)


Base.metadata.create_all(engine, checkfirst=True)
