__author__ = 'Hao Lin'

import abstract_model


class VideoModel(abstract_model.AbstractModel):

    @staticmethod
    def save(self):
        print self.__class__.__name__
        print "this is a child class update"
        return

    @staticmethod
    def update(self):
        print self.__class__.__name__
        print "this is a update"
        return


test = VideoModel()
VideoModel.save(test)
VideoModel.update(test)