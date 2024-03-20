import os

API_ID = API_ID = 90864300
API_HASH = os.environ.get("API_HASH", "50cf66c0625d75b0d2ed21ee68196370")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7101283284:AAGCMVQGcO72UHQ_0M31nQaM4q4lb0RQlNU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5148038477))

LOG = -1002098581395

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5148038477").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


