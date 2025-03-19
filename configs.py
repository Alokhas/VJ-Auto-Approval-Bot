# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28647200"))
    API_HASH = getenv("API_HASH", "42e71744fb1829f43010bd6003224daf")
    BOT_TOKEN = getenv("BOT_TOKEN", "6770440133:AAF-bGyAAnntFKioNs22O6M2hLieWQO4crU")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1001599827340")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "6667876837").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://ALLU:ALLU@cluster0.5blb9tp.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
