from minio import Minio
from app.core.config import settings

client = Minio("localhost:9000",
        access_key= settings.MINIO_ACCES_KEY,
    secret_key= settings.MINIO_SECRET_KEY,
    secure= False
)

bucket_name = "crud"
if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)