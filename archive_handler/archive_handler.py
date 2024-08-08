#Make archive

import shutil 
import pathlib

BACKUP_FOLDER = "backup_data"
FORMAT = "zip"

shutil.make_archive(base_name="backup_data", format="zip", root_dir="Compendium")

print("Backup")

shutil.unpack_archive(filename=f"{BACKUP_FOLDER}.{FORMAT}")







