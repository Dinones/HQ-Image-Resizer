###########################################################################################################################
####################################################     LIBRARIES     ####################################################
###########################################################################################################################

import os
import numpy as np
from PIL import Image
import Constants as CONST
from Utils import Colored_Strings as COLOR_str

###########################################################################################################################
#################################################     INITIALIZATIONS     #################################################
###########################################################################################################################

NEW_PIXEL_SIZE = int(CONST.NEW_MAX_SIZE * CONST.DPI / 2.54)

###########################################################################################################################
#####################################################     PROGRAM     #####################################################
###########################################################################################################################

images = [element for element in os.listdir('./Original') if 
    element.endswith('.jpg') or element.endswith('.png') or element.endswith('.jpeg')]

for image in images:
    img = Image.open(f'./Original/{image}')

    # ↓↓ Gets the original DPI, if there is not, it is set to 'CONST.DPI'
    # dpi = img.info.get("dpi", (CONST.DPI, CONST.DPI))

    # ↓↓ Gets the original aspect ratio
    aspect_ratio = img.width / img.height

    # ↓↓ Gets the new sizes. The larger side will be converted to the specified new max size
    size = [img.width, img.height]
    max_size_index = np.argmax(size)
    if max_size_index == 0: new_size = [NEW_PIXEL_SIZE, int(NEW_PIXEL_SIZE/aspect_ratio)]
    else: new_size = [int(NEW_PIXEL_SIZE*aspect_ratio), NEW_PIXEL_SIZE]

    # ↓↓ Resizes and saves the image 
    img_resized = img.resize(new_size, Image.BICUBIC)
    img_resized.info["dpi"] = CONST.DPI
    img_resized.save(f'./Resized/{image}')

    print(COLOR_str.IMAGE_RESIZED.replace('{image_name}', 'image'))