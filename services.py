import os


class FileService:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def list_files(self):
        """List all files in the base directory"""
        return os.listdir(self.base_dir)

    def download_file(self, filename):
        """Download the content of a file"""
        file_path = os.path.join(self.base_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                return file.read()
        return None

    def upload_file(self, filename, content):
        """Save content to a file"""
        file_path = os.path.join(self.base_dir, filename)
        with open(file_path, 'wb') as file:
            file.write(content)
        return file_path

    def delete_file(self, filename):
        """Delete a file"""
        file_path = os.path.join(self.base_dir, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
