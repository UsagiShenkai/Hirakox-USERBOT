import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "27572576")) #optional
API_HASH = getenv("API_HASH", "6bc3a7b9b70d62f5fab87b196aac4ff5") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", ""5489233583).split()))
OWNER_ID = int(getenv("OWNER_ID", "5489233583"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Kazee:kaze@kazee.jpyqywq.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5569861454:AAE6FK0I7Dj9CncHxMDsWc0gtyOYILfXy50")
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/f973fcb16b21e5c8597f3.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "I am hirako")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkASV56Ga2tLkqAEI_yiUl3_NksO1n2GZPRHhAInYkvjH2P19_NSn81DhPByOnx0yYXErZxYbDz2pp7immmFfH5KNb7tqLbXFPlhA7S7erxm03wsJQq7zCVi1dw-GD2vzlTDIHlQOOPnFouy7QjICf5k84wwTcXWvcjnyGjUiegA7pAJjerfXCu65cBUhKz9YT-XtZCAd8n0muKiRt9ADFKqiQ4Cz0lMEVCnCcAmy73vvuIwB1vRB0SPp8a0qEXfEu3wP9BbU8IwvitxQ5RkvMpR2PTYY98LDJTv_gTmmTMwWvX3Dn_MVRS2yVAm6avi1F5QCx5LM4KhiYXg8yT2krZDAAAAAFHLw6vAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
