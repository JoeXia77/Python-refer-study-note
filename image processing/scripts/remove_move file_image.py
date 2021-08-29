## select pic of certain size

import os
from PIL import Image
import numpy as np

## path should be in raw string format: r''
old_floder_path = r'S:\BaiduNetdiskDownload\[TSDM@佐藤ひな]Genshin Impact\Genshin Impact'
new_folder_path = r'S:\BaiduNetdiskDownload\[TSDM@佐藤ひな]Genshin Impact\壁纸'

## find all the file name in a dir use: os.listdir(path)
for fname in os.listdir(old_floder_path):
    ## join two path using path.join(pathA, pathB)
    old_path = os.path.join(old_floder_path,fname)
    new_path = os.path.join(new_folder_path,fname)
    print(old_floder_path)
    print(fname)
    print(new_path)
    print("#######################")
    
    ## open image using PIL.Image.open()
    ## modify image using np.asarray(image_object)
    I = np.asarray(Image.open(old_path))
    
    rows = I.shape[0]
    columns = I.shape[1]
    rate = 1920/1080

    if rows>800 and rate-0.1<columns/rows<rate+0.1:
        os.rename(old_path,new_path)

    
    





