import aiofiles
from fastapi import FastAPI, HTTPException, UploadFile, File, Depends
from services.file_service import FileService
from typing import List
from utils import utility_functions

config = utility_functions.load_config()
app = FastAPI()


def get_file_service() -> FileService:
    return FileService(base_dir=config['BASE_DIR'])


@app.get("/files/")
def list_files(file_service: FileService = Depends(get_file_service)) -> List[str]:
    """List all files"""
    return file_service.list_files()


@app.get("/files/{filename}")
async def download_file(filename: str, file_service: FileService = Depends(get_file_service)) -> dict:
    """Download a file"""
    content = await file_service.download_file(filename)
    if content is None:
        raise HTTPException(status_code=404, detail="File not found")
    return {"message": "downloaded", "filename": filename}


@app.post("/files/{filename}")
async def upload_file(filename: str, file: UploadFile = File(...),
                      file_service: FileService = Depends(get_file_service)) -> dict:
    """Upload a file"""
    file_path = await file_service.upload_file(filename, file.file)  # file.file is the object inside file
    if not file_path:
        raise HTTPException(status_code=500, detail="File could not be saved")
    return {"status": "success", "filename": filename, "path": file_path}


@app.delete("/files/{filename}")
def delete_file(filename: str, file_service: FileService = Depends(get_file_service)) -> dict:
    """Delete a file"""
    if file_service.delete_file(filename):
        return {"status": "success"}
    raise HTTPException(status_code=404, detail="File not found")
