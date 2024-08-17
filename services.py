import os
from typing import List, Optional

DOWNLOAD_PATH = "/Downloads/downloaded_file.txt"


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

    # def download_file(self, filename: str) -> Optional[bytes]:
    #     """Download the content of a file"""
    #     file_path = os.path.join(self.base_dir, filename)
    #     if os.path.exists(file_path):
    #         with open(file_path, 'rb') as file:
    #             return file.read()
    #     return None

    def download_file(self, filename: str) -> Optional[bytes]:
        """Download the content of a file"""
        try:
            file_path = os.path.join(self.base_dir, filename)
            with open(file_path, 'rb') as file:
                content = file.read()
            with open(DOWNLOAD_PATH, 'wb') as downloaded_file:
                downloaded_file.write(content)
            return content
        except FileNotFoundError as e:
            print(f"The file was not found: {e}")
            return None
        except OSError as e:
            print(f"Error reading the file: {e}")
            return None

    def upload_file(self, filename: str, content: bytes) -> Optional[str]:
        """Save content to a file"""
        try:
            file_path = os.path.join(self.base_dir, filename)
            with open(file_path, 'wb') as file:
                file.write(content)
            return file_path
        except OSError as e:
            print(f"Error updating file {filename}: {e}")
            return None

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
