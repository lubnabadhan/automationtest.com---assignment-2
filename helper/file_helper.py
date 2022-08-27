import os

class FileHelper():
    
    def get_relative_file_path(self, file_path):
        return os.path.abspath(file_path)