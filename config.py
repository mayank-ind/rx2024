import os

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6101033089:AAEZ6ObvNn87UusS3YDpj9cTQejRs_cVXdc"")
API_ID = int(os.environ.get("API_ID", "10010060"))
PASS_DB = int(os.environ.get("PASS_DB", "721"))
FR_TOKEN = os.environ.get("FR_TOKEN", "f0907b55-922e-414a-8d21-47c1887bb90d"))
API_KEY = os.environ.get("API_KEY", " "))
API_HASH = os.environ.get("API_HASH", "807495c78593302dd5008b4775e9b01b")
ADMINS = int(os.environ.get("ADMINS", "1503980120"))
GROUPS = [int(chat) for chat in os.getenv("GROUPS", "-1001927764573").split(",") if chat != ""]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
