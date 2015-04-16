__author__ = 'Hao Lin'

import abc


class AbstractController(object):
    __metaclass__ = abc.ABCMeta

    partner = None

    @staticmethod
    def set_partner(partner):
        """
            Set the current partner.
        """
        