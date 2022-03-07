import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 8989465))
    API_HASH = os.environ.get("API_HASH", "936001c6daa3264b59759b813b645e59")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2099275683:AAFcFqODyad3tHK57PlaNMlTrVcgtBX2350")
    SESSION_NAME = os.environ.get("SESSION_NAME", "akrenamerbot")
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
    BOT_OWNER = os.environ.get("BOT_OWNER", 2097398523)
    CAPTION = "Rename Bot by @{}\n\nMade by @ncarun1999"
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001653651182")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001659818664))
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://akrenamerbot:akrenamerbot@cluster0.h8k1x.mongodb.net/akrenamerbot?retryWrites=true&w=majority")
    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    ONE_PROCESS_ONLY = bool(os.environ.get("ONE_PROCESS_ONLY", False))
    START_TEXT = """
I am Telegram Files Rename Bot.

Send me a File to Rename.
    """
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
    """
