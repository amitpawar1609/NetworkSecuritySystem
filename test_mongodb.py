
from pymongo import MongoClient
uri = "mongodb+srv://amitpawar16902_db_user:<@password@>@cluster0.tivftua.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)


