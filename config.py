import os

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6101033089:AAEZ6ObvNn87UusS3YDpj9cTQejRs_cVXdc")
API_ID = int(os.environ.get("API_ID", "10010060"))
PASS_DB = int(os.environ.get("PASS_DB", "721"))
FR_TOKEN = os.environ.get("FR_TOKEN", "f0907b55-922e-414a-8d21-47c1887bb90d")
API_KEY = os.environ.get("API_KEY", "09869712-a3ff-40c4-b1f4-3c3966250da6")
API_HASH = os.environ.get("API_HASH", "807495c78593302dd5008b4775e9b01b")
ADMINS = int(os.environ.get("ADMINS", "1503980120"))
LOG = [int(chat) for chat in os.getenv("LOG", "-1001746027817").split(",") if chat != ""]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
