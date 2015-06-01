# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Alerts(models.Model):
    resourceid = models.ForeignKey('Resources', db_column='resourceId')  # Field name made lowercase.
    description = models.TextField()
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alerts'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EncodedVideos(models.Model):
    videoid = models.ForeignKey('Videos', db_column='videoId')  # Field name made lowercase.
    akamaipath = models.CharField(db_column='akamaiPath', max_length=512, blank=True, null=True)  # Field name made lowercase.
    bitrate = models.CharField(max_length=32)
    encoded = models.IntegerField(blank=True, null=True)
    height = models.IntegerField()
    mediatype = models.CharField(db_column='mediaType', max_length=256)  # Field name made lowercase.
    name = models.CharField(max_length=256)
    uploaded = models.IntegerField(blank=True, null=True)
    width = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'encoded_videos'


class Languages(models.Model):
    code = models.CharField(primary_key=True, max_length=3)
    alt = models.CharField(max_length=2)
    name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'languages'


class Logs(models.Model):
    videoid = models.ForeignKey('Videos', db_column='videoId', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField()
    iserror = models.IntegerField(db_column='isError', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs'


class Partners(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'partners'


class Regions(models.Model):
    code = models.CharField(primary_key=True, max_length=2)
    country = models.CharField(max_length=256)
    languagecode = models.ForeignKey(Languages, db_column='languageCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'regions'


class Resources(models.Model):
    name = models.CharField(max_length=256)
    haserror = models.IntegerField(db_column='hasError', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resources'


class Roles(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'roles'


class States(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'states'


class Thumbnails(models.Model):
    videoid = models.ForeignKey('Videos', db_column='videoId')  # Field name made lowercase.
    akamaipath = models.CharField(db_column='akamaiPath', max_length=512, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField()
    localpath = models.CharField(db_column='localPath', max_length=512)  # Field name made lowercase.
    uploaded = models.IntegerField(blank=True, null=True)
    width = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'thumbnails'


class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    lastactiondate = models.DateTimeField(db_column='lastActionDate')  # Field name made lowercase.
    roleid = models.ForeignKey(Roles, db_column='roleId')  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Videos(models.Model):
    partnerid = models.ForeignKey(Partners, db_column='partnerId')  # Field name made lowercase.
    stateid = models.ForeignKey(States, db_column='stateId')  # Field name made lowercase.
    artist = models.CharField(max_length=256, blank=True, null=True)
    bitrate = models.CharField(max_length=32, blank=True, null=True)
    cleanupdate = models.DateTimeField(db_column='cleanUpDate', blank=True, null=True)  # Field name made lowercase.
    downloaddate = models.DateTimeField(db_column='downloadDate', blank=True, null=True)  # Field name made lowercase.
    arcid = models.CharField(db_column='arcId', max_length=64)  # Field name made lowercase.
    isrcdistpolicy = models.CharField(db_column='isrcDistPolicy', max_length=64)  # Field name made lowercase.
    receiptdatearc = models.DateTimeField(db_column='receiptDateArc', blank=True, null=True)  # Field name made lowercase.
    errorstatusarc = models.CharField(db_column='errorStatusArc', max_length=512, blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(blank=True, null=True)
    ftpinfolocation = models.CharField(db_column='ftpInfoLocation', max_length=512, blank=True, null=True)  # Field name made lowercase.
    genres = models.CharField(max_length=32, blank=True, null=True)
    hd = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    importationdate = models.DateTimeField(db_column='importationDate', blank=True, null=True)  # Field name made lowercase.
    infoparsedate = models.DateTimeField(db_column='infoParseDate', blank=True, null=True)  # Field name made lowercase.
    isrc = models.CharField(max_length=32, blank=True, null=True)
    mviid = models.CharField(db_column='mviId', max_length=256)  # Field name made lowercase.
    localpath = models.CharField(db_column='localPath', max_length=512)  # Field name made lowercase.
    originalfilesize = models.IntegerField(db_column='originalFileSize', blank=True, null=True)  # Field name made lowercase.
    originalname = models.CharField(db_column='originalName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    rating = models.CharField(max_length=32, blank=True, null=True)
    reported = models.IntegerField(blank=True, null=True)
    sendtoakamaidate = models.DateTimeField(db_column='sendToAkamaiDate', blank=True, null=True)  # Field name made lowercase.
    sendtoencoderdate = models.DateTimeField(db_column='sendToEncoderDate', blank=True, null=True)  # Field name made lowercase.
    sendtoumadate = models.DateTimeField(db_column='sendToUmaDate', blank=True, null=True)  # Field name made lowercase.
    sourcefolder = models.CharField(db_column='sourceFolder', max_length=512, blank=True, null=True)  # Field name made lowercase.
    sublabel = models.CharField(db_column='subLabel', max_length=256, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    territories = models.CharField(max_length=1024, blank=True, null=True)
    trackname = models.CharField(db_column='trackName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    subtitle = models.CharField(db_column='subTitle', max_length=256, blank=True, null=True)  # Field name made lowercase.
    umaid = models.CharField(db_column='umaId', max_length=512, blank=True, null=True)  # Field name made lowercase.
    upc = models.CharField(max_length=32, blank=True, null=True)
    widescreen = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.
    updateinfolocation = models.CharField(db_column='updateInfoLocation', max_length=512, blank=True, null=True)  # Field name made lowercase.
    featuredartist1 = models.CharField(db_column='featuredArtist1', max_length=256, blank=True, null=True)  # Field name made lowercase.
    featuredartist2 = models.CharField(db_column='featuredArtist2', max_length=256, blank=True, null=True)  # Field name made lowercase.
    featuredartist3 = models.CharField(db_column='featuredArtist3', max_length=256, blank=True, null=True)  # Field name made lowercase.
    grid = models.CharField(db_column='GRid', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'videos'
