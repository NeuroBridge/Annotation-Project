# FAR - Filter and Rename
#
# Collect, rename, and place somewhere more useful the output from Inception. Run from the directory
# above the output from Inception and the target directory for the final results. Not much help or
# detailed guidance for this one.
#
# 2021.10.28
# MDT

# Constants & Setup

import os
import shutil
import sys
import glob
import logging

logging.basicConfig(filename='far.log', filemode='a', format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info("far started.")
logging.info("Current absolute directory: %s.", os.path.abspath(os.getcwd()))

new_extension = ".wtsv"

# Parse the command line to get the IN and OUT directories:

n = len(sys.argv)
if n != 3:
    logging.error("Command line arguments incorrect.")
    logging.error("far ended (badly).")
    raise RuntimeError("Incorrect number of command line arguments (specify IN and OUT dirs).")

input_dir  = sys.argv[1]
output_dir = sys.argv[2]

logging.info("Input directory is:    %s.", input_dir)
logging.info("Output directory is:   %s.", output_dir)

# Check that the OUT directory exists:

if not os.path.exists(output_dir):
    logging.info("Output directory does not exist, creating it: %s.", output_dir)
    os.mkdir(output_dir)

# Hard Part
#
# Go through the subdirectories, find the .tsv file from CURATION_USER.tsv, copy it
# to the new location, and give it the new name...

for folder in os.listdir(input_dir):
    #folder_path = os.path.abspath(os.path.join(input_dir, folder))
    folder_path = os.path.join(input_dir, folder)
    output_file_name = folder.split(sep='.')[0] + new_extension
    src = glob.glob(folder_path + '\\CURATION_USER.tsv')[0]
    dst = output_dir + "\\" + output_file_name
    logging.info("Copying %s to %s.", src, dst)
    shutil.copyfile(src, dst)

# Wrap up

logging.info("far ended.")

# EOF
