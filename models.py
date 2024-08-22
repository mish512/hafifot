# models.py
from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException


class FileUploadRequest(BaseModel):
    filename: str
    content: bytes


class FileDownloadResponse(BaseModel):
    filename: str
    message: str


class FileOperationResponse(BaseModel):
    status: str
    filename: Optional[str] = None
    path: Optional[str] = None
    detail: Optional[str] = None


class FileNotFoundError(HTTPException):
    def __init__(self, filename: str):
        super().__init__(status_code=404, detail=f"File '{filename}' not found.")


class FileOperationError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)
