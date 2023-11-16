from os import getenv

from dotenv import load_dotenv

load_dotenv()

# db = "mongodb://{}:{}@{}:{}/{}".format(
#     getenv("DB_USER"), getenv("DB_PASSWORD"), getenv("DB_HOST"), getenv("DB_PORT"), getenv("DB_SCHEMA")
# )

db = "mongodb://{}:{}/{}".format(
    getenv("DB_HOST"), getenv("DB_PORT"), getenv("DB_SCHEMA")
)

# db="mongodb://localhost:27017"