import io
from fastapi import APIRouter,UploadFile,File
from minio import S3Error
from app.minio.client import client
from app.minio.client import bucket_name


minio_router = APIRouter(
    prefix="/minio",
    tags=["minio"]
)



@minio_router.post("/")
async def upload_file(file: UploadFile = File(...)):
   
    try:
        file_content = await file.read()
        
        client.put_object(
            bucket_name,
            file.filename,
            io.BytesIO(file_content),
            len(file_content)
        )
        return {"message": f"Файл {file.filename} успешно загружен."}
    except S3Error as e:
        return {"error": str(e)}