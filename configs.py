# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "25603034"))
	API_HASH = os.environ.get("API_HASH", "294a7bf4488b21609436de1cdd05c316")
	
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "5983400035:AAHuXglu4ch9pnS89JQObVi57aeoBVuC6sQ")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "storedbbot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001577667595"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL',"api.shareus.io")
	SHORTLINK_API = os.environ.get('SHORTLINK_API',"uMqvZtYEWAM8uoQigOVX5HOPh253")
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5791145987 5764988016"))
	DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://xajay10997:Xr1p2CNHjIJLrHl8@cluster0.bjsdwy9.mongodb.net/?retryWrites=true&w=majority')
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "streaamdb")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", -1001953206885)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", 0))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Developer:** [Predator HackerzZ](https://t.me/OwnYourBotz) 
│
├🔹 **Bot Support:** [Support Group](https://t.me/TeleRoid14)
│
├🔸 **Bot Updates:** [Bots Channel](https://t.me/TeleRoidGroup)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [@PredatorHackerzZ](https://github.com/PredatorHackerzZ)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/DonateXrobot) or ```MrAbhi2k3@apl```
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
