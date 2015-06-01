__author__ = 'Hao Lin'

from controllers.main_controller import MainController

class MetadataDownload():

    @staticmethod
    def get_file_list_from_ftp():
        partner = MainController.get_partner()
