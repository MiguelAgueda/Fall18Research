import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-d', '--directory',
                type=str,
                help="Path to directory with files.",
                required=True)
ap.add_argument('-D', '--destination',
                type=str,
                help="Path to destined directory.",
                required=True)
ap.add_argument('-t', '--file_type',
                type=str,
                help="File type (.png, .tif, .txt, .py, etc.)",
                required=True)
args = vars(ap.parse_args())
path = args['directory']
destination = args['destination']
file_type = args['file_type']

for filename in os.listdir(path):
    file_first_four = filename[:3] + file_type
    src = path + filename
    dst = destination + file_first_four
    os.rename(src, dst)
