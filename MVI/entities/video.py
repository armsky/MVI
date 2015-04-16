__author__ = 'Hao Lin'


from django.db import models


class Video(models.Model):

    artist = models.CharField(max_length=256)
    bitrate = models.Char.Field(max_length=32)