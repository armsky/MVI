__author__ = 'Hao Lin'

import os

# Database configuration
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASS = "QuantH00p!"
MYSQL_DB = "mvi_live"

# Folders paths
ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
temp_download_folder = '/Users/armsky/TEMP'

DB_BACKUPS_FOLDER = ROOT_FOLDER + '/Docs/SqlBackups/'
LOCAL_METADATA_FOLDER = ROOT_FOLDER + '/Inbox/Metadata/'
ARCHIVE_METADATA_FOLDER = '/mnt/Encoding/Litterbox/MVI_METADATA_ARCHIVE/'
LOCAL_VIDEOS_FOLDER = ROOT_FOLDER + '/Inbox/Videos/'
LOCAL_UMA_XML_FOLDER = ROOT_FOLDER + '/Inbox/UmaXml/'
LOCAL_UPDATE_FOLDER = ROOT_FOLDER + '/Inbox/Update/'
LOCAL_LOG_FOLDER = ROOT_FOLDER + '/Logs/'
AKAMAI_PATH_PREFIX = '/8619/_!'

# Search most recent xmls in FTP (in days)
MOST_RECENT_DAYS = 3
# Delete old contents in FTP (in days)
TO_DELETE_DAYS = 120



# Label FTP configuration
WMG_CONF = {
    'SERVER':   'ftp.mtvintldigital.com',  # 'ftp.mtvintldigital.com'
    'USER':     'watsond',
    'PASSWORD': 'watsond789',
    'PORT': 22,
    'ROOT_FOLDER':  '/home/ftp/wmg/wmg/new_release/Assets_Only/',
    'LOCAL_VIDEO_FOLDER': LOCAL_VIDEOS_FOLDER + 'WMG/',
    'LOCAL_META_FOLDER': LOCAL_METADATA_FOLDER + 'WMG/',
    'ARCHIVE_METADATA_FOLDER': ARCHIVE_METADATA_FOLDER + 'WMG/',
    'VIDEO_FILE_EXTENSION': 'mp4'
}
TEST_WMG_CONF = {
    'SERVER':   'ftp.mtvintldigital.com',  # 'ftp.mtvintldigital.com'
    'USER':     'watsond',
    'PASSWORD': 'watsond789',
    'PORT': 22,
    'ROOT_FOLDER':  '/home/ftp/wmg/wmg/new_release/Assets_Only/',
    'LOCAL_VIDEO_FOLDER': '/Users/armsky/TEMP/Videos/WMG/',
    'LOCAL_META_FOLDER': '/Users/armsky/TEMP/Metadata/WMG/',
    'ARCHIVE_METADATA_FOLDER': '/Users/armsky/TEMP/Archive/WMG/',
    'VIDEO_FILE_EXTENSION': 'mp4'
}

MIN_WIDESCREEN_RATIO = 1.6
