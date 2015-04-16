__author__ = 'Hao Lin'

import abc


class AbstractModel(object):
    __metaclass__ = abc.ABCMeta

    @staticmethod
    def save(self):
        print self.__class__.__name__
        print "this is a save"
        return