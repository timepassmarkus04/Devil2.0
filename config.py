import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "29350132"))

API_HASH = getenv("API_HASH", "e854995be05edb5bf21f5b84bdc0212f")

BOT_TOKEN = getenv("BOT_TOKEN", "")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", ""))

OWNER_ID = int(getenv("OWNER_ID", "6616796006"))

START_STICKER_ID = getenv("START_STICKER_ID", "CAACAgUAAxkBAAEMh05mnxmdTdD_d3MX1bvpZMBduBCQqgACxQ8AAuPNQVVKfyLFzl_KDDUE")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Amrita ^ MSN")

POWERED_BY = getenv("POWERED_BY", "‹‹‹[🢓 𝕌𝐧𝐢𝐯𝐞𝐫𝐬𝐞 𝐍𝐞𝐭-𝐖𝐨𝐫𝐤𝐬 🢓]›››")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/timepassmarkus04/Devil2.0",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MNS_botss")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/MNS_botss")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", None))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")


PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "300"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



# Get your pyrogram v2 session from @Stringene_bot on Telegram
STRING1 = getenv("STRING_SESSION", "BQG_2PQAe8wWePj7LzevRxd7DF-9KOyv8eY7mrRkinJ6g0aHm5Y8fdKvMm0Gaesu16WbplF-Lv_ec2ujmQ4PvCF0MopZp8-0pOIVa4ycFPNmpqrTSGNMoJz3Wnh1F4i_BhvVesd0k4sklF3TEx2EoNKHQ0l8jsDtwljJOxGNW3pfwqEm5zdQO0L7m6UndzTKS0hhUe7MYrrPFaT7AoZy-9uoYis5HfheyREjca4Fmv3_EaQ0rUUhTD7JFj0dgmBFUoifHJG7wadVP4AsyR1tvfd3dONHwauCGkO_hg9bpbSqxqfDsfDdWBCnDjPahcRQ-uAi_zLrvUeDxHMYtxmI2BXnkdnc3AAAAAG85SnWAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/c3847da256457f7cb057d.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/c3847da256457f7cb057d.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/af86ccd36db0028a47597.jpg"
STATS_IMG_URL = "https://telegra.ph/file/80a9ed23ef383cab9120c.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/bad08d50dd445dd12162d.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/a695a0c52b7c19c4cbf8c.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/b00af14042edff8b71f2e.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/e8819c35a316479cc3d01.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
