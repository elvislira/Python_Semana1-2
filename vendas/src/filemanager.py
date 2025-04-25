# Context Maneger para manipulação segura de arquivos
class FileManager:
    def __init__(self, file_path, mode='r'):
        self._file_path = file_path
        self._mode = mode
        self._file = None
    
    def __enter__(self):
        self._file = open(self._file_path, self._mode)

        return self._file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file:
            self._file.close()