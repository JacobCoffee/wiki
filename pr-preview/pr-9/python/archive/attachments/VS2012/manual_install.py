# Nick Hilton
# 2013-10-05
#
# Installs a Python build from the Visual Studio directory to target directory
#

import glob
import os
import shutil
import sys

import os.path

from os.path import dirname
from os.path import abspath

#------------------------------------------------------------------------------
# Globals

EXTERNALS_DIR = dirname(abspath(__file__))
PYTHON_DIR = "Python-2.7.5"
TCLTK_DIR = "tcltk64"

DST_DIR = r"C:\Python27_d"
CPU = "amd64"


def make_directory(d):
    if not os.path.exists(d):
        print "Creating directory: %s" % repr(d)
        os.makedirs(d)


def copy_files(filelist, dst):

    for f in filelist:

        f = f.replace('/', '\\')

        f, ext = os.path.splitext(f)

        for ext_ in [ext, '_d' + ext]:

            f_ = f + ext_

            if os.path.isfile(f_):
                print "Copying %s --> %s" % (f_, dst)
                shutil.copy(f_, dst)

def copy_directory(src_dir, dst_dir):

    if not os.path.isdir(src_dir):
        raise RuntimeError("Oops, couldn't find path: %s" % repr(src_dir))

    if os.path.isdir(dst_dir):
        shutil.rmtree(dst_dir)

    print "Copying %s --> %s" % (src_dir, dst_dir)
    shutil.copytree(src_dir, dst_dir)


if __name__ == "__main__":

    print "EXTERNALS_DIR =", EXTERNALS_DIR
    print "PYTHON_DIR =", PYTHON_DIR
    print "TCLTK_DIR =", TCLTK_DIR

    for p in [EXTERNALS_DIR, PYTHON_DIR, TCLTK_DIR]:

        if not os.path.isdir(p):
            raise RuntimeError("Oops, could not find path: %s" % repr(p))

    #--------------------------------------------------------------------------
    # Create destination directory

    if DST_DIR is None:

        DST_DIR = r"C:\Python27_d"

        d = raw_input("Enter destination directory [%s]: " % repr(DST_DIR))

        if len(d) > 0:
            DST_DIR = d

    print "DST_DIR =", DST_DIR

    if os.path.isdir(DST_DIR):

        choice = raw_input("Destination directory exists, continue? ").upper()

        if choice not in ['Y', 'YES']:
            print "Aborting ..."
            exit(1)

    make_directory(DST_DIR)

    #--------------------------------------------------------------------------
    # copy python.exe

    SRC_DIR = os.path.join(EXTERNALS_DIR, PYTHON_DIR)

    PCBUILD_DIR = "{SRC_DIR}/PCbuild/{CPU}".format(SRC_DIR = SRC_DIR, CPU = CPU)

    filelist = """
        {py_prefix}/python.exe
        {py_prefix}/pythonw.exe
        {py_prefix}/python27.dll
    """.format(py_prefix = PCBUILD_DIR).split()

    copy_files(filelist, DST_DIR)


    #--------------------------------------------------------------------------
    # copy DLLs

    src_list = glob.glob(PCBUILD_DIR + r"\*.pyd")

    dst_dir = os.path.join(DST_DIR, "DLLs")

    make_directory(dst_dir)

    copy_files(src_list, dst_dir)

    # Tcl dlls
    src_list = glob.glob(TCLTK_DIR + r"\bin\*.dll")

    copy_files(src_list, dst_dir)

    #--------------------------------------------------------------------------
    # copy include

    src_dir = os.path.join(SRC_DIR, "Include")
    dst_dir = os.path.join(DST_DIR, "include")

    copy_directory(src_dir, dst_dir)

    src_list = ["{SRC_DIR}/PC/pyconfig.h".format(SRC_DIR = SRC_DIR)]

    copy_files(src_list, dst_dir)

    #--------------------------------------------------------------------------
    # copy Lib

    src_dir = os.path.join(SRC_DIR, "Lib")
    dst_dir = os.path.join(DST_DIR, "Lib")

    copy_directory(src_dir, dst_dir)

    #--------------------------------------------------------------------------
    # copy libs

    src_list = glob.glob(PCBUILD_DIR + r"\*.lib")

    dst_dir = os.path.join(DST_DIR, "libs")

    make_directory(dst_dir)

    copy_files(src_list, dst_dir)

    #--------------------------------------------------------------------------
    # Scripts dir

    make_directory(os.path.join(DST_DIR, "Scripts"))

    #--------------------------------------------------------------------------
    # tcl

    src_dir = os.path.join(EXTERNALS_DIR, TCLTK_DIR, "lib")
    dst_dir = os.path.join(DST_DIR, "tcl")

    copy_directory(src_dir, dst_dir)


    print "All done!"


