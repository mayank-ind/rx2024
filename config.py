import os

API_ID = API_ID = 10010060

API_HASH = os.environ.get("API_HASH", "807495c78593302dd5008b4775e9b01b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6101033089:AAEZ6ObvNn87UusS3YDpj9cTQejRs_cVXdc")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1503980120))

LOG = -1001927764573

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1503980120").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)

