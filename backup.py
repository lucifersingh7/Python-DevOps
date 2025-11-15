import os
import shutil

def backup_files(source,dest) :
    backup_file_name = os.path.join(dest,"backup-sahil")
    shutil.make_archive(backup_file_name,'zip',source)

source = r"C:\Users\admin\OneDrive\Desktop\Python-For-DevOps"
destination = r"C:\Users\admin\OneDrive\Desktop\PythonBackup"

backup_files(source,destination)

