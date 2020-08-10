import os


class FileService:
    @staticmethod
    def delete_all_static_files():
        path = os.getcwd()
        static_path = os.path.join(path, "static")
        filelist = os.listdir(static_path)
        for file in filelist:
            os.remove(os.path.join(static_path, file))
