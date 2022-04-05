import os
try:
    import dotenv
except:
    print("Python-dotenv not found! Installing...")
    import os
    os.system("python3 -m pip install python-dotenv")
    import dotenv

dotenv.load_dotenv('.env')

TOKEN = os.environ['TOKEN'] #user token
DB_NAME='mydb.db'
LOG_INFO = False #False or True
NO_SCRAPE=[] #userid,userid...
GUILD_DICTIONARY = { #ID guild/id channel
    '100000000000000000':'11000000000000000', #replace this
}
BADGE = {
    131072: 'VERIFIED_DEVELOPER',
    65536: 'VERIFIED_BOT',
    16384: 'BUG_HUNTER_LEVEL_2',
    4096: 'SYSTEM',
    1024: 'TEAM_USER',
    512: 'PREMIUM_EARLY_SUPPORTER',
    256: 'HYPESQUAD_ONLINE_HOUSE_3',
    128: 'HYPESQUAD_ONLINE_HOUSE_2',
    64: 'HYPESQUAD_ONLINE_HOUSE_1',
    8: 'BUG_HUNTER_LEVEL_1',
    4: 'HYPESQUAD',
    2: 'PARTNER',
    1: 'STAFF'
}

NUM_OF_LOOP = 0 #Number of rescan 0: 1 scan, no rescan
TIME_BETWEEN_LOOP= 3600 #in seconds