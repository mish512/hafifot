import os
from typing import List, Optional
import aiofiles
from config import DOWNLOAD_PATH, KILOBYTE


class FileService:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def list_files(self) -> List[str]:
        """List all files in the base directory"""
        try:
            return os.listdir(self.base_dir)
        except OSError as e:
            print(f"Error listing files {e}")
            return []

    async def download_file(self, filename: str) -> Optional[str]:
        """Download the content of a file"""
        try:
            file_path = os.path.join(self.base_dir, filename)
            async with aiofiles.open(file_path, 'rb') as source_file:
                async with aiofiles.open(DOWNLOAD_PATH, 'wb') as dest_file:
                    chunk = await source_file.read(KILOBYTE)
                    while chunk:  # as long as there is data in chunk
                        await dest_file.write(chunk)
                        chunk = await source_file.read(KILOBYTE)
            return DOWNLOAD_PATH
        except FileNotFoundError as e:
            print(f"The file was not found: {e}")
            return None
        except OSError as e:
            print(f"Error reading the file: {e}")
            return None

    async def upload_file(self, filename: str, content) -> Optional[str]:
        """Save content to a file"""
        try:
            file_path = os.path.join(self.base_dir, filename)
            async with aiofiles.open(content, 'rb') as source_file:
                async with aiofiles.open(file_path, 'wb') as dest_file:
                    chunk = await source_file.read(KILOBYTE)
                    while chunk:  # as long as there is data in chunk
                        await dest_file.write(chunk)
                        chunk = await source_file.read(KILOBYTE)

            return file_path
        except OSError as e:
            print(f"Error saving file {filename}: {e}")
            return None

    # async def upload_file(self, filename: str, content: bytes) -> Optional[str]:
    #     """Save content to a file"""
    #     try:
    #         file_path = os.path.join(self.base_dir, filename)
    #         async with aiofiles.open(file_path, 'wb') as file:
    #             await file.write(content)
    #         return file_path
    #     except OSError as e:
    #         print(f"Error saving file {filename}: {e}")
    #         return None

    def delete_file(self, filename: str) -> bool:
        """Delete a file"""
        try:
            file_path = os.path.join(self.base_dir, filename)
            os.remove(file_path)
            return True
        except FileNotFoundError:
            print(f"File not found: {filename}")
            return False
        except OSError as e:
            print(f"Error deleting file {filename}: {e}")
            return False
