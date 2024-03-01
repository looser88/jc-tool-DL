from os import environ
import os
import logging
from logging.handlers import RotatingFileHandler


#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "10755921"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d5e49fd3637cba407f17807d31c77977")

#Bot token @Botfather
# TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5872747581:AAH7_XPCOCEVfbgUhepjJWlcOmj8wjDTjBk") #url_v3
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5906626853:AAFzimXzHM4oV1QCT2xvkadzjvjRti7NMBk") #drm


#Your db channel Id
# CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001693231644"))

# Your log channel Id
LOG_ID = int(os.environ.get("LOG_ID", "-1001956515516"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1061576483"))

# #shortenr
# API = environ.get('API','eedc409c6457b8c783019e990dde8fd531b58eca')

#Port
PORT = os.environ.get("PORT", "8080")

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1061576483").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Database 
# DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Jayanna:Jayanna2023@yash.tm1c2bd.mongodb.net/?retryWrites=true&w=majority")
# DB_NAME = os.environ.get("DATABASE_NAME", "New_Divya_Spandana")

# #force sub channel id, if you want enable force sub
# FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

# TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "10"))

# #start message
# START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")