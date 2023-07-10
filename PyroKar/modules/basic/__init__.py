import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "PyroKar"])

async def join(client):
    try:
        await client.join_chat("obrolansuar")
        await client.join_chat("RuangGabutArman")
        await client.join_chat("yagitudahpokonya")
        await client.join_chat("mutualindoo")
    except BaseException:
        pass
