#!/usr/bin/env python

# Ned's FolderCreator 9000 
# will copy all files into folders with the same name
# will break if filenames exceed maximum characters permited for folder names 
# destination folder must be different from source folder

import os, shutil

# Function for creating folders and copying/moving files
def createFolder():
  n = 0
  for dirpath, dirs, files in os.walk(src):
    for file in files:
      try:
	Dir = file.split("-")[0]
	newDir = os.path.join(dest, Dir)
	os.mkdir(newDir)
	# change shutil.copy to shutil.move if you want to move the files instead of copying them
	shutil.copy(os.path.join(dirpath, file), newDir)
	n = n + 1
      except OSError:
	break
  print ""
  print "Process complete:",n,"folder(s) created."
  print ""

src = ""
dest = ""
menu = True

# Menu
while menu:
  print("\n *** Ned's Folder Creator 9000 ***")
  print("\n Current source: "), src
  print(" Current destination: "), dest
  print("""
    1. Set source folder
    2. Set destination folder
    3. Run
    4. Quit
    """)   
  menu = raw_input("\n What would you like to do? ")
  if menu == "1":
    src = raw_input("\n Enter path to source folder: ")
  if menu == "2":
    dest = raw_input("\n Enter path to destination folder (must be different from source): ")
  if menu == "3":
    createFolder()
  if menu == "4":
    print("\n Goodbye")
    print ""
    menu = None
