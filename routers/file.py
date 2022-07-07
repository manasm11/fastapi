import os
import shutil

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse

router = APIRouter(prefix="/file", tags=["File"])


@router.post("/upload")
def upload_file(upload_file: UploadFile = File(...)):
    if not os.path.exists("files/"):
        os.mkdir("files/")
    path = f"files/{upload_file.filename}"
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return {"filename": path, "type": upload_file.content_type}


@router.get("/download/{filename}", response_class=FileResponse)
def download_file(filename: str):
    return f"files/{filename}"
