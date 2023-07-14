import os

API_ID = API_ID = 23739388

API_HASH = os.environ.get("API_HASH", "0f8772e5e06adc997427b2d8048cc510")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6054754530:AAEreKb8JAbOtA_q9wt3e2EWQHT19PLPL08")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5596869249))

LOG = -1001590232792

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5596869249").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)

