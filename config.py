# ============================================
# INSTAGRAM AUTO POST - CONFIGURATION
# ============================================

import os

# ============================================
# FOLDER PATHS
# ============================================

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
IMAGES_FOLDER = os.path.join(BASE_FOLDER, "images")
CAPTIONS_FOLDER = os.path.join(BASE_FOLDER, "captions")
HASHTAGS_FOLDER = os.path.join(BASE_FOLDER, "hashtags")
SCREENSHOTS_FOLDER = os.path.join(BASE_FOLDER, "screenshots")
POSTED_FOLDER = os.path.join(BASE_FOLDER, "posted")

# ============================================
# COORDINATES
# ============================================

COORDINATES = {
    'chrome_icon': (183, 633),
    'address_bar': (164, 62),
    'create_button': (72, 633),
    'post_option': (57, 682),
    'select_computer': (947, 646),
    'next_button_crop': (1287, 193),
    'next_button_filter': (1456, 197),
    'caption_area': (1180, 289),
    'add_location': (1187, 512),
    'location_search': (1152, 545),
    'location_first_result': (1230, 588),
    'share_button': (1448, 200),
}

# ============================================
# POSTS TO PUBLISH
# ============================================

POSTS = [
    {
        "image": "post_01.jpg",
        "caption": "caption_01.txt",
        "location": "Thoothukudi",
    },
    {
        "image": "post_02.jpg",
        "caption": "caption_02.txt",
        "location": "Thoothukudi",
    },
    {
        "image": "post_03.jpg",
        "caption": "caption_03.txt",
        "location": "Thoothukudi",
    },
]

# ============================================
# TIMING SETTINGS (in seconds)
# ============================================

GAP_BETWEEN_POSTS = 2

WAIT_DESKTOP = 2
WAIT_CHROME_OPEN = 5
WAIT_PAGE_LOAD = 8
WAIT_MENU_OPEN = 2
WAIT_POPUP_OPEN = 3
WAIT_FILE_DIALOG = 3
WAIT_IMAGE_LOAD = 5
WAIT_NORMAL = 2
WAIT_LOCATION_SEARCH = 4
WAIT_UPLOAD = 20
WAIT_BEFORE_START = 10

# ============================================
# SAFETY SETTINGS
# ============================================

FAILSAFE_ENABLED = True
PAUSE_BETWEEN_ACTIONS = 0.3

# ============================================
# URL
# ============================================

INSTAGRAM_URL = "https://www.instagram.com/"