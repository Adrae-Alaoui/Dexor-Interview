from minio import Minio
from minio.error import S3Error
import os
import psycopg2

access_key= "gamma"
secret_key= "1e56abe075d2912c9358dab75c12c9a1"
client = Minio("minio.dexor.de", access_key=access_key, secret_key=secret_key, region="eu")

con = psycopg2.connect(
    name= "gamma_photos",
    user= "gamma",
    password= "8ebe63401e50bb351f508d4480753cad",
    host= "db.dexor.de",
    port= 5432)


for file in os.listdir():
    if '.json' in file:
    client.put_object("photos", "gamma", file)

con.close()
