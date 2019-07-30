# create a book structure for ingest into islandora: https://github.com/Islandora/islandora_book_batch
# thanks ned, the first foldercreator.py is here https://github.com/digitalutsc/folderCreator/blob/master/folderCreator.py
# os.listdir (just the list), copytree (copies tree folder structure), shutil copy (copies files)
# os.path.exists will also return True if there's a regular file with that name.
# os.path.isdir will only return True if that path exists and is a directory.

import os, shutil

def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(src).st_mtime - os.stat(dst).st_mtime > 1:
                sweetfoldername = os.path.splitext(d)[0]
                if not os.path.exists(sweetfoldername):
                    os.mkdir(sweetfoldername)
                if d.endswith(".tif"):
                    shutil.move(s, sweetfoldername)
                elif d.endswith(".xml"):
                    shutil.move(s, sweetfoldername) #if there's just xml and no matching it takes out the extension
                else:
                    print("NOT FOR INGEST") , d

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
        if os.path.isdir(os.path.join(a_dir, name))]

src = "T:/RUNBOOKBATCH/Compound/"
dst = "T:/RUNBOOKBATCH/BATCH/"

for dir in (get_immediate_subdirectories(src)):
    copytree(src + dir, dst + dir)