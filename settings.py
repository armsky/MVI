__author__ = 'Hao Lin'

import os

# Database configuration
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASS = "QuantH00p!"
MYSQL_DB = "mvi_live"

# Folders paths
ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))

DB_BACKUPS_FOLDER = ROOT_FOLDER + '/Docs/SqlBackups/'
LOCAL_METADATA_FOLDER = ROOT_FOLDER + '/Inbox/Metadata/'
ARCHIVE_METADATA_FOLDER = '/mnt/Encoding/Litterbox/MVI_METADATA_ARCHIVE/'
LOCAL_VIDEOS_FOLDER = ROOT_FOLDER + '/Inbox/Videos/'
LOCAL_UMA_XML_FOLDER = ROOT_FOLDER + '/Inbox/UmaXml/'
LOCAL_UPDATE_FOLDER = ROOT_FOLDER + '/Inbox/Update/'
LOCAL_LOG_FOLDER = ROOT_FOLDER + '/Logs/'
AKAMAI_PATH_PREFIX = '/8619/_!'






# Label FTP configuration
WMG_CONF = {
    'SERVER':   'ftp.mtvintldigital.com',  # 'ftp.mtvintldigital.com'
    'USER':     'watsond',
    'PASSWORD': 'watsond789',
    'ROOT_FOLDER':  '/home/ftp/wmg/wmg/new_release/Assets_Only/',
    'LOCAL_FOLDER': LOCAL_VIDEOS_FOLDER + 'WMG/',
    'VIDEO_FILE_EXTENSION': 'mp4'
}
