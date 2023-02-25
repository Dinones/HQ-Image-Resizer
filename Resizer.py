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

# ↓↓ Checks the Constants format
if type(CONST.DPI) != int or type(CONST.NEW_MAX_SIZE) != int: 
    exit(print(COLOR_str.WRONG_FORMAT.replace('{constant}', 'DPI, NEW_MAX_SIZE').replace('{type}', 'integers')))

# ↓↓ Checks if the necessary folders exist. If not, creates them
if not os.path.exists(CONST.RESIZED_FOLDER_PATH): os.mkdir(CONST.RESIZED_FOLDER_PATH)
if not os.path.exists(CONST.ORIGINAL_FOLDER_PATH): os.mkdir(CONST.ORIGINAL_FOLDER_PATH)

NEW_PIXEL_SIZE = int(CONST.NEW_MAX_SIZE * CONST.DPI / 2.54)

###########################################################################################################################
#####################################################     PROGRAM     #####################################################
###########################################################################################################################

images = [element for element in os.listdir(CONST.ORIGINAL_FOLDER_PATH) if 
    element.endswith('.jpg') or element.endswith('.png') or element.endswith('.jpeg')]

if not images: exit(print(COLOR_str.NO_IMAGES_FOUND.replace('{folder}', CONST.ORIGINAL_FOLDER_PATH)))

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

    img_resized = img.resize(new_size, Image.BICUBIC)
    img_resized.info["dpi"] = CONST.DPI

    if not CONST.OUTPUT_FORMAT:
        img_resized.save(f'{CONST.RESIZED_FOLDER_PATH}/{image}')
    else:
        # ↓↓ Creates a blank image with the size of the resized one
        pdf = Image.new("RGB", img_resized.size, (255, 255, 255))
        # ↓↓ If image has transparent background, else will raise the except
        try: pdf.paste(img_resized, (0, 0), img_resized)
        except: pdf.paste(img_resized, (0, 0))
        # ↓↓ Saves as '.pdf' keeping the resolution
        pdf.save(f"{CONST.RESIZED_FOLDER_PATH}/{'.'.join(image.split('.')[:-1])}.pdf", "PDF", resolution = CONST.DPI)

    print(COLOR_str.IMAGE_RESIZED.replace('{image_name}', image))

print(COLOR_str.ALL_IMAGES_RESIZED.replace('{images}', str(len(images))))