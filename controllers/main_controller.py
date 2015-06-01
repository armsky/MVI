__author__ = 'Hao Lin'

from models.mvi_models import Partners
from utils.database.connection import Connection

class MainController():

    # The current Partner object
    Partner = ""

    #
    Session = Connection.create_session()

    @classmethod
    def set_partner(cls, partner):
        # is Partner object
        if isinstance(partner, Partners):
            cls.Partner = partner
        elif isinstance(partner, int):
            print cls.Session
            cls.Partner = cls.Session.query(Partners).filter_by(id=partner).first()
        elif isinstance(partner, str):
            print cls.Session
            cls.Partner = cls.Session.query(Partners).filter_by(name=partner).first()
        # else:
        #     raise Exception('Unexpected type for parameter partner. (MainController.set_partner)')
        if not isinstance(cls.Partner, Partners):
            raise TypeError("Unexpected type for parameter 'partner'. (MainController.set_partner)")

    @classmethod
    def get_partner(cls):
        if cls.Partner:
            return cls.Partner
        else:
            raise Exception("Partner hadn't been set up yet. MainController.get_partner)")


MainController.set_partner(1)
MainController.set_partner("UMG")
print MainController.Session

