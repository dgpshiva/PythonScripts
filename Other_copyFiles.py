# Use the built-in version of scandir/walk if possible, otherwise
# use the scandir module version
import os
try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk

import shutil

destDir = r"D:\ManualUploadFiles"

for entry in scandir(r"D:\AutoUploadProcessor\Success"):
    try:
        filename =  os.path.basename(entry.path)
        if (os.path.splitext(filename)[1] == ".cfw"):
            shutil.copy(entry.path, destDir)
    except Exception, ex:
        print str(ex)

