import re, logging
from os import environ
from Script import script

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
API_ID = environ.get('API_ID', '22549633')
if len(API_ID) == 0:
    print('Error - API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get('API_HASH', '34d8c9887fe445c1dac2228cbdf9ab48')
if len(API_HASH) == 0:
    print('Error - API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('BOT_TOKEN', '6052565020:AAEE7aCx619jfFovvs7bIfbGfC9CVmvYY08')
if len(BOT_TOKEN) == 0:
    print('Error - BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', '8080'))

# Bot pics
PICS = (environ.get('PICS', 'https://telegra.ph/file/30689a75684ced43ab22c.jpg')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '2057170163')
if len(ADMINS) == 0:
    print('Error - ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1001858969618 -1001800011644').split()]
AUTH_CHANNEL = [int(auth_channels) for auth_channels in environ.get('AUTH_CHANNEL', '-1001402115130').split()]
LOG_CHANNEL = environ.get('LOG_CHANNEL', '-1001995831309')
if len(LOG_CHANNEL) == 0:
    print('Error - LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)
    
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '-1002101524343')
if len(SUPPORT_GROUP) == 0:
    print('Error - SUPPORT_GROUP is missing, exiting now')
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)
    
OPENAI_API = environ.get('OPENAI_API', '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')
if len(OPENAI_API) == 0:
    print('Warning - OPENAI_API is empty')

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "+srv://Virusbot:virus347000vmp03@cluster0.aexnusr.mongodb.net/?retryWrites=true&w=majority")
if len(DATABASE_URL) == 0:
    print('Error - DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/Virus_Botz')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/Virus_Studios')
FILMS_LINK = environ.get('FILMS_LINK', 'https://t.me/+7MJoYsTqBblmYjU9')

# Bot settings
AUTO_FILTER = is_enabled((environ.get('AUTO_FILTER', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", "True"), True)
SHORTLINK = is_enabled((environ.get('SHORTLINK', "True")), True)
DELETE_TIME = int(environ.get('DELETE_TIME', 300)) # Add time in seconds
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), False)
WELCOME = is_enabled((environ.get('WELCOME', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
LINK_MODE = is_enabled(environ.get("LINK_MODE", "True"), True)
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10))
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

# Other
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "shareus.io")
SHORTLINK_API = environ.get("SHORTLINK_API", "z8J99Nke1wNxdm3wyj1G7pWxAaI3")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = is_enabled(environ.get("IS_VERIFY", "False"), False)
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
TUTORIAL = environ.get("TUTORIAL", "https://t.me/How_To_Verify/11")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/How_To_Verify/11")
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]

# stream features vars
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1002015091563")
if len(BIN_CHANNEL) == 0:
    print('Error - BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "")
if len(URL) == 0:
    print('Error - URL is missing, exiting now')
    exit()
else:
    if URL.startswith('https://'):
        if not URL.endswith("/"):
            URL += '/'
    elif '.' in URL:
        URL = f'http://{URL}:{PORT}/'
    else:
        print('Error - URL is not valid, exiting now')
        exit()
