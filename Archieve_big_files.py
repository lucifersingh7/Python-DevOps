#python program to create a backup of a folder to a new folder

import os
import shutil

def archieve_files(source,dest):
    backup_file_name = os.path.join(dest,'sahils-backup')
    shutil.make_archive(backup_file_name,'zip',source)

source =r'C:\Users\admin\Downloads\Automation Testing'
dest =r'D:\Backup'

archieve_files(source,dest)


