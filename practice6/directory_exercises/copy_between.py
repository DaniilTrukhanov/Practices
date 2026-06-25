import shutil
import os

if os.path.exists("folder/file_copy.txt"):
    os.remove("folder/file_copy.txt")
else:
    shutil.copy(
    "folder/inafolder/inanotherfolder/file.txt",
    "folder/file_copy.txt")