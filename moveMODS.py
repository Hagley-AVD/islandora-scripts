import os, shutil

def moveMODS(src):
    for dir in (get_immediate_subdirectories(src)):
        dstdir = os.path.join(src, dir)
        srcfile = dstdir + '.xml'
        dstfile = os.path.join(dstdir, 'MODS.xml')
        if os.path.exists(srcfile):
            shutil.copyfile(srcfile, dstfile)


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
        if os.path.isdir(os.path.join(a_dir, name))]

src = "/usr/local/fedora/xfer/test"

moveMODS(src)