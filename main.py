from fastapi import FastAPI, HTTPException, UploadFile, File, Response
from services import FileService
import uvicorn

BASE_DIR = "./files"
app = FastAPI()
file_service = FileService(BASE_DIR)


@app.get("/files/")
def list_files():
    """List all files"""
    return file_service.list_files()


@app.get("/files/{filename}")
def download_file(filename: str):
    """Download a file"""
    content = file_service.download_file(filename)
    if content is None:
        raise HTTPException(status_code=404, detail="File not found")
    return {"message": "downloaded", "filename": filename}


@app.post("/files/{filename}")
def upload_file(filename: str, file: UploadFile = File(...)):
    """Upload a file"""
    content = file.file.read()
    file_path = file_service.upload_file(filename, content)
    return {"status": "success", "filename": filename, "path": file_path}


@app.delete("/files/{filename}")
def delete_file(filename: str):
    """Delete a file"""
    if file_service.delete_file(filename):
        return {"status": "success"}
    raise HTTPException(status_code=404, detail="File not found")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
