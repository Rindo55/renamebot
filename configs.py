# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = 3845818
    API_HASH = "95937bcf6bc0938f263fc7ad96959c6d"
    BOT_TOKEN = "5426835246:AAGpWNE1EQF5_t56BmcdD8QWSJhCtynh3gk"
    DOWNLOAD_DIR = "./downloads"
    LOGGER = logging
    OWNER_ID = 1443454117
    PRO_USERS = 1443454117
    MONGODB_URI = "mongodb+srv://720p:hevc@cluster0.fw3dwgb.mongodb.net/?retryWrites=true&w=majority"
    LOG_CHANNEL = int("-1001730306649")
    BROADCAST_AS_COPY = bool("False")
