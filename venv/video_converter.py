import os
import sys
import glob
from converter import Converter

conv = Converter()
#
# input_folder = sys.argv[1]
# output_folder = sys.argv[2]
#
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# for filename in os.listdir(input_folder):


convert = conv.convert('test1.avi', 'test1.mp4', {
    'format': 'mp4',
    'audio': {
        'codec': 'aac',
        'samplerate': 11025,
        'channels': 2
    },
    'video': {
        'codec': 'hevc',
        'width': 720,
        'height': 400,
        'fps': 25
    }})

for timecode in convert:
    print(f'\rConverting ({timecode:.2f}) ...')