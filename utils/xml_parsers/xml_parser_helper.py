__author__ = 'Hao Lin'

import settings
import re


def is_widescreen(height, width):
    if int(width) / int(height) >= settings.MIN_WIDESCREEN_RATIO:
        return 1
    else:
        return 0


def ddex_time_to_seconds(ddex_time):
    """
    Convert a ddex time string to seconds, round to nearest integer.
    :param ddex_time:
    :return: int
    """
    result = re.search(r"^PT((?P<hour>\d+)H)?(?P<minute>\d+)M(?P<second>\d+(\.\d+)?)S$", ddex_time)
    if result.group("hour"):
        hour = int(result.group("hour"))
    else:
        hour = 0
    if result.group("minute"):
        minute = int(result.group("minute"))
    else:
        minute = 0
    second = int(round(float(result.group("second"))))
    return second + minute*60 + hour*3600
