__author__ = 'Hao Lin'

import sys
sys.path.append("..")
from utils.celery.tasks import add

add.delay(3,4)
add.delay(3,5)
add.delay(3,6)
add.delay(3,7)
add.delay(3,8)
add.delay(3,9)
add.delay(3,41)
add.delay(3,42)
add.delay(3,43)
add.delay(3,44)
add.delay(3,45)
add.delay(3,46)
add.delay(3,47)


