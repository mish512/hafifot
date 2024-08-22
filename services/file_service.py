import os
from typing import List, Optional
import aiofiles
from utils import utility_functions

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

    async def download_file(self, filename: str) -> Optional[str]:
        """Download the content of a file"""
        try:
            file_path = os.path.join(self.base_dir, filename)
            async with aiofiles.open(file_path, 'rb') as source_file:
                async with aiofiles.open(config['DOWNLOAD_PATH'], 'wb') as dest_file:
                    chunk = await source_file.read(config['KILOBYTE'])
                    while chunk:  # as long as there is data in chunk
                        await dest_file.write(chunk)
                        chunk = await source_file.read(config['KILOBYTE'])
            return config['DOWNLOAD_PATH']
        except FileNotFoundError as e:
            logger.error(f"The file was not found: {e}")
            return None
        except OSError as e:
            logger.error(f"The file was not found: {e}")

            return None

    async def upload_file(self, filename: str, content) -> Optional[str]:
        """Save content to a file"""
        try:
            file_path = os.path.join(self.base_dir, filename)
            async with aiofiles.open(content, 'rb') as source_file:
                async with aiofiles.open(file_path, 'wb') as dest_file:
                    chunk = await source_file.read(config['KILOBYTE'])
                    while chunk:  # as long as there is data in chunk
                        await dest_file.write(chunk)
                        chunk = await source_file.read(config['KILOBYTE'])

            return file_path
        except OSError as e:
            logger.error(f"Error saving file {filename}: {e}")
            return None

    def delete_file(self, filename: str) -> bool:
        """Delete a file"""
        try:
            file_path = os.path.join(self.base_dir, filename)
            os.remove(file_path)
            return True
        except FileNotFoundError:
            logger.error(f"File not found: {filename}")
            return False
        except OSError as e:
            logger.error(f"Error deleting file {filename}: {e}")
            return False
