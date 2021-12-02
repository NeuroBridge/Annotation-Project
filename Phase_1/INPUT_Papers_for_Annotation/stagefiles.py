# Program to stage files for upload into Inception

import os
import shutil
import sys
import logging

logging.basicConfig(filename='stagefiles.log', filemode='a', format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info("stagefiles.py started.")
logging.info("Current absolute directory: %s.", os.path.abspath(os.getcwd()))

n = len(sys.argv)
if n != 4:
    logging.error("Command line arguments incorrect.")
    logging.error("stagefile.py ended (badly).")
    raise RuntimeError("Incorrect number of command line args (specify FROM and TO dirs, & FileList).")

from_dir  = sys.argv[1]
to_dir    = sys.argv[2]
file_list = sys.argv[3]

logging.info("Input directory is:  %s.", from_dir)
logging.info("Output directory is: %s.", to_dir)
logging.info("File list is in:     %s.", file_list)

if not os.path.exists(to_dir):
    logging.info("Output directory does not exist, creating it: %s.", to_dir)
    os.mkdir(to_dir)

# The main part:

with open(file_list) as f:
    for line in f:
        try:
            src = from_dir + '\\' + line.strip() + '.txt'
            dst = to_dir
            shutil.move(src, dst)
            logging.info("Moving %s to %s.", src, dst)
        except:
            logging.warning("Ignoring %s (probably already moved?).", src)

# Wrap up

logging.info("staging.py ended.")

# EOF
