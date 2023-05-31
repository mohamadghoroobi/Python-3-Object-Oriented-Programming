import sys
import shutil
import zipfile
from pathlib import Path
from PIL import Image


class ZipProcessor:
    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = Path(f"unzipped-{zipname[:-4]}")

    # overall manager
    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(self.temp_directory)

    # def find_replace(self):
    #     for filename in self.temp_directory.iterdir():
    #         with filename.open() as file:
    #             contents = file.read()
    #         contents = contents.replace(self.search_string, self.replace_string)
    #         with filename.open("w") as file:
    #             file.write(contents)

    def zip_files(self):
        with zipfile.ZipFile(self.zipname, "w") as file:
            for filename in self.temp_directory.iterdir():
                file.write(filename, filename.name)
        shutil.rmtree(self.temp_directory)

