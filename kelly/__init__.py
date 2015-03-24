# coding: utf-8
import os
import time

os.environ['TZ'] = 'America/Los Angeles'
time.tzset()

from flask import Flask

# Setup application
app = Flask(__name__)

# wsgi.SETTINGS tells us which settings file to load for this env
from wsgi import SETTINGS
settings = __import__('kelly.settings.%s' % SETTINGS,
                      fromlist=['DEBUG', 'SECRET'])

app.debug = settings.DEBUG
app.config['SECRET_KEY'] = settings.SECRET

try:
    CSE_ID = settings.CSE_ID
    GOOGLE_DEV_KEY = settings.GOOGLE_DEV_KEY
except KeyError:
    pass

from kelly import views
