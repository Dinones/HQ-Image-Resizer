###########################################################################################################################
####################################################     LIBRARIES     ####################################################
###########################################################################################################################

import os
import numpy as np
from PIL import Image
import Constants as CONST

###########################################################################################################################
#################################################     INITIALIZATIONS     #################################################
###########################################################################################################################

SUPPORTED_FORMATS = ('.png', '.jpg', '.jpeg', '.webp')

print()
# ↓↓ Checks the Constants format
if not all(isinstance(parameter, int) and parameter > 0 for parameter in (CONST.DPI, CONST.NEW_MAX_SIZE)):
    exit(print("[χ] Parameters 'DPI' and 'NEW_MAX_SIZE' must be positive integers: Check the format in "\
        "'Constants.py' file.\n"))

if not isinstance(CONST.PDF_OUTPUT, bool):
    exit(print("[χ] Parameter 'PDF_OUTPUT' must be a boolean: Check the format in 'Constants.py' file.\n"))

if not all(isinstance(parameter, str) for parameter in (CONST.ORIGINAL_FOLDER_PATH, CONST.RESIZED_FOLDER_PATH)):
    exit(print("[χ] Parameter 'ORIGINAL_FOLDER_PATH' and 'RESIZED_FOLDER_PATH' must be strings: "\
        "Please, check the format in 'Constants.py' file.\n"))

# ↓↓ Checks if the necessary folders exist. If not, creates them
if not os.path.exists(CONST.ORIGINAL_FOLDER_PATH): 
    os.mkdir(CONST.ORIGINAL_FOLDER_PATH); print(f"[♦️] Created '/{CONST.ORIGINAL_FOLDER_PATH}' folder.")
if not os.path.exists(CONST.RESIZED_FOLDER_PATH): 
    os.mkdir(CONST.RESIZED_FOLDER_PATH); print(f"[♦️] Created '/{CONST.RESIZED_FOLDER_PATH}' folder.")

NEW_PIXEL_SIZE = int(CONST.NEW_MAX_SIZE * CONST.DPI / 2.54)

###########################################################################################################################
#####################################################     PROGRAM     #####################################################
###########################################################################################################################

images = [element for element in os.listdir(CONST.ORIGINAL_FOLDER_PATH) if element.lower().endswith(SUPPORTED_FORMATS)]

if not images: exit(print(f"[χ] Could not find any image in '{CONST.ORIGINAL_FOLDER_PATH}' folder: "\
    "Check if the image formats are '.png', '.jpg', '.jpeg' or '.webp'.\n"))

counter = 0
for image in images:
    try: img = Image.open(f'./Original/{image}')
    except: print(f"[‼] Could not open '{image}'. Check if it is damaged."); continue

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

    if not CONST.PDF_OUTPUT:
        try: img_resized.save(f'{CONST.RESIZED_FOLDER_PATH}/{image}')
        except: print(f"[‼] Could not resize {image}"); continue
    else:
        # ↓↓ Creates a blank image with the size of the resized one
        pdf = Image.new("RGB", img_resized.size, (255, 255, 255))
        # ↓↓ If image has transparent background, else will raise the except
        try: pdf.paste(img_resized, (0, 0), img_resized)
        except: pdf.paste(img_resized, (0, 0)); continue
        # ↓↓ Saves as '.pdf' keeping the resolution
        try: pdf.save(f"{CONST.RESIZED_FOLDER_PATH}/{'.'.join(image.split('.')[:-1])}.pdf", "PDF", resolution = CONST.DPI)
        except: print(f"[‼] Could not resize {image}"); continue

    print(f"[♦️] Image resized: '{image}'")
    counter += 1

print(f"\n[√] Successfully resized {counter}/{len(images)} images!\n")