import os
from typing import List, Optional
import aiofiles
from utils import utility_functions
from models import FileUploadRequest, FileDownloadResponse, FileOperationResponse
from models import FileNotFoundError, FileOperationError

logger = utility_functions.create_logger()
config = utility_functions.load_config()


class FileService:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def list_files(self) -> List[str]:
        """List all files in the base directory"""
        try:
            return os.listdir(self.base_dir)
        except OSError as e:
            logger.error(f"Error listing files {e}")
            return []

    async def download_file(self, filename: str) -> Optional[FileDownloadResponse]:
        """Download the content of a file"""
        file_path = os.path.join(self.base_dir, filename)
        if not os.path.exists(file_path):
            logger.error(f"File '{filename}' not found.")
            raise FileNotFoundError(filename)
        try:
            async with aiofiles.open(file_path, 'rb') as source_file:
                async with aiofiles.open(config['DOWNLOAD_PATH'], 'wb') as dest_file:
                    chunk = await source_file.read(config['KILOBYTE'])
                    while chunk:
                        await dest_file.write(chunk)
                        chunk = await source_file.read(config['KILOBYTE'])
            return FileDownloadResponse(filename=filename, message="downloaded")

        except OSError as e:
            logger.error(f"Error downloading file '{filename}': {e}")
            raise FileOperationError(f"Error downloading file '{filename}'.")

    async def upload_file(self, request: FileUploadRequest) -> Optional[FileOperationResponse]:
        """Save content to a file"""
        file_path = os.path.join(self.base_dir, request.filename)
        try:
            async with aiofiles.open(request.content, 'rb') as source_file:
                async with aiofiles.open(file_path, 'wb') as dest_file:
                    chunk = await source_file.read(config['KILOBYTE'])
                    while chunk:  # as long as there is data in chunk
                        await dest_file.write(chunk)
                        chunk = await source_file.read(config['KILOBYTE'])
            return FileOperationResponse(status="success", filename=request.filename, path=file_path)
        except OSError as e:
            logger.error(f"Error saving file {request.filename}: {e}")
            raise FileOperationError(f"Error saving file '{request.filename}'.")

    def delete_file(self, filename: str) -> FileOperationResponse:
        """Delete a file"""
        file_path = os.path.join(self.base_dir, filename)
        if not os.path.exists(file_path):
            logger.error(f"File '{filename}' not found.")
            raise FileNotFoundError(filename)
        try:
            os.remove(file_path)
            return FileOperationResponse(status="success", filename=filename)

        except OSError as e:
            logger.error(f"Error deleting file {filename}: {e}")
            raise FileOperationError(f"Error deleting file '{filename}'.")
