###########################################################################################################################
#  Who doesn't like colors? Just a script to print with colors in the terminal to make it more visual.                    #
###########################################################################################################################

###########################################################################################################################
####################################################     CONSTANTS     ####################################################
###########################################################################################################################

SPECIAL = {
    "Default"       : '0',
    "Bold"          : '1',
    "Italics"       : '3',
    "Underlined"    : '4',
    "Strikethrough" : '9'
}

COLORS = {
    "Black"     : '30',
    "Red"       : '31',
    "Green"     : '32',
    "Yellow"    : '33',
    "Blue"      : '34',
    "Magenta"   : '35',
    "Cyan"      : '36',
    "White"     : '37',

    "DarkGray"      : '90',
    "LightRed"      : '91',
    "LightGreen"    : '92',
    "LightYellow"   : '93',
    "LightBlue"     : '94',
    "LightMagenta"  : '95',
    "LightCyan"     : '96',
}

BACKGROUND = {
    "Black"     : '40',
    "Red"       : '41',
    "Green"     : '42',
    "Yellow"    : '43',
    "Blue"      : '44',
    "Magenta"   : '45',
    "Cyan"      : '46',
    "White"     : '47',
}

INFO = f'\033[{COLORS["Magenta"]}m[♦️] \033[0;m'
CORRECT = f'\033[{COLORS["Magenta"]}m[√] \033[0;m'
WARN = f'\033[{COLORS["Magenta"]}m[‼] \033[0;m'
ERROR = f'\033[{COLORS["Magenta"]}m[χ] \033[0;m'

###########################################################################################################################
######################################################     INFO     #######################################################
###########################################################################################################################

IMAGE_RESIZED = \
    f'{INFO}\033[{SPECIAL["Bold"]};{COLORS["Blue"]}m{"Image Resized: "}\033[0;m'+\
    f'\033[{COLORS["Blue"]};{SPECIAL["Italics"]}m{"{image_name}"}\033[0;m'

###########################################################################################################################
#####################################################     CORRECT     #####################################################
###########################################################################################################################

ALL_IMAGES_RESIZED = \
    f'\n{CORRECT}\033[{SPECIAL["Bold"]};{COLORS["Green"]}m{"Successfully resized "}\033[0;m'+\
    f'\033[{COLORS["Green"]};{SPECIAL["Italics"]}m{"{images} "}\033[0;m'+\
    f'\033[{COLORS["Green"]};{SPECIAL["Bold"]}m{"image(s)!"}\033[0;m'

###########################################################################################################################
#####################################################     WARNING     #####################################################
###########################################################################################################################



###########################################################################################################################
######################################################     ERROR     ######################################################
###########################################################################################################################

NO_IMAGES_FOUND = \
    f"""{ERROR}\033[{SPECIAL["Bold"]};{COLORS["Red"]}m{"Could not find any image in '{folder}' folder: "}\033[0;m"""+\
    f"""\033[{COLORS["Red"]};{SPECIAL["Italics"]}m{"Check if the image formats are '.png', '.jpg' or '.jpeg'..."}\033[0;m"""

WRONG_FORMAT = \
    f'{ERROR}\033[{SPECIAL["Bold"]};{COLORS["Red"]}m{"Constant(s) "}\033[0;m'+\
    f'\033[{COLORS["Red"]};{SPECIAL["Italics"]}m{"{constant} "}\033[0;m'+\
    f'\033[{COLORS["Red"]};{SPECIAL["Bold"]}m{"must be "}\033[0;m'+\
    f'\033[{COLORS["Red"]};{SPECIAL["Italics"]}m{"{type}"}\033[0;m'

###########################################################################################################################
#####################################################     PROGRAM     #####################################################
###########################################################################################################################

if __name__ == '__main__':
    print(INFO, CORRECT, WARNING, ERROR)