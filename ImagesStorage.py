from minio import Minio
from dotenv import load_dotenv
from minio.error import S3Error


access_key= "gamma"
secret_key= "1e56abe075d2912c9358dab75c12c9a1"
client = Minio("minio.dexor.de", access_key=access_key, secret_key=secret_key, region="eu",secure=True)
client.make_bucket("photos")
