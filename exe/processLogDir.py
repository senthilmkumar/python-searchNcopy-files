import os
import sys
import shutil


clear = lambda: os.system('clear')
clear()

# Execuetion 
# python processLogDir.py <src_dir> <dest_dir>

# # Use this if your running the script from logs directory
# # Getting the current work directory (cwd)
# thisdir = os.getcwd()

#  # Use this if your running the script from different directory
# thisdir = "../python-copy-files/logsdir"

# Use this if your passing directory path as param
thisdir = sys.argv[1]
print ("Searching the files in : "+thisdir)

destDir = "/path/to/your/dest/dir"
try: 
    os.makedirs(destDir)
except OSError:
    if not os.path.isdir(destDir):
        raise

search_result_files_path = []
search_result_file_names = []

# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith("-result.json"):
            print (file)
            search_result_files_path += [os.path.join(r, file)]
            search_result_file_names += [file]


for fp in search_result_files_path:
    #print (fp)
    for fn in search_result_file_names:
        #print (fn)
        src = thisdir +'/'+ fn
        dest = destDir +'/'+ fn
        #print (src)
        #print (dest)
        shutil.copy(src, destDir)
