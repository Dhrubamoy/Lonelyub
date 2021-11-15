# Configs imports from here

import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from userbot.Config import Config
else:
    if os.path.exists("exampleconfig.py"):
        from exampleconfig import Development as Config

# legendbot
