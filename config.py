import os

API_ID = API_ID = 90864300
API_HASH = os.environ.get("API_HASH", "50cf66c0625d75b0d2ed21ee68196370")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6287684948:AAFl1ZfAC6McttYkYwYXNf277zu0VrazEDM")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 809150135))

LOG = -992473338

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "809150135").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


