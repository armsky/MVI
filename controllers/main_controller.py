__author__ = 'Hao Lin'

from models.mvi_models import Partners
from utils.database.connection import Connection


class MainController(object):
    __shared_state = {}


    def __init__(self):
        self.__dict__ = self.__shared_state

    # The current Partner object
    Partner = None

    Session = Connection.create_session()

    @classmethod
    def set_partner(cls, partner):
        """
        Set current partner
        :param partner: Partner object or int (partner_id) or string (partner_name)
        :return: Partner object
        """
        # is Partner object
        if isinstance(partner, Partners):
            cls.Partner = partner
        elif isinstance(partner, int):
            # print cls.Session
            cls.Partner = cls.Session.query(Partners).filter_by(id=partner).first()
        elif isinstance(partner, str):
            # print cls.Session
            cls.Partner = cls.Session.query(Partners).filter_by(name=partner).first()
        else:
            cls.Partner = None

        if not isinstance(cls.Partner, Partners):
            raise TypeError("Unexpected type for parameter 'partner'. (MainController.set_partner)")

        return cls.Partner

    @classmethod
    def get_partner(cls):
        if cls.Partner:
            return cls.Partner
        else:
            raise Exception("Partner hadn't been set up yet. (MainController.get_partner)")

    # def import_metadata(self):
    #     MetadataDownload.get_metadata_list_from_ftp()

