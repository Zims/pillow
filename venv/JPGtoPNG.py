import os
import sys
from PIL import Image
import glob

source_folder = input('Type the source folder of the files (a folder name in your main directory): ')
output_folder = input('Folder name to output the .png files (one word): ')

path_now = os.getcwd()
path_source = f"{path_now}/{source_folder}"
path = path_now + "/" + output_folder

try:
    os.mkdir(path)
except OSError:
    pass

for filename in glob.glob(f'{source_folder}/*.jpg'):  # assuming jpg
    im = Image.open(filename)
    new_name = os.path.splitext(filename)[0]
    no_prefix = new_name.split('/')[1]
    im.save(f'{output_folder}/{no_prefix}.png')
print('All done!')
