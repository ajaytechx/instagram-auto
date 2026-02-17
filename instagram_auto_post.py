import pyautogui
import pyperclip
import time
import os
import shutil
from datetime import datetime

# Import config
from config import (
    COORDINATES,
    POSTS,
    IMAGES_FOLDER,
    CAPTIONS_FOLDER,
    SCREENSHOTS_FOLDER,
    POSTED_FOLDER,
    GAP_BETWEEN_POSTS,
    WAIT_DESKTOP,
    WAIT_CHROME_OPEN,
    WAIT_PAGE_LOAD,
    WAIT_MENU_OPEN,
    WAIT_POPUP_OPEN,
    WAIT_FILE_DIALOG,
    WAIT_IMAGE_LOAD,
    WAIT_NORMAL,
    WAIT_LOCATION_SEARCH,
    WAIT_UPLOAD,
    WAIT_BEFORE_START,
    FAILSAFE_ENABLED,
    PAUSE_BETWEEN_ACTIONS,
    INSTAGRAM_URL,
)

# ============================================
# PYAUTOGUI SETUP
# ============================================

pyautogui.FAILSAFE = FAILSAFE_ENABLED
pyautogui.PAUSE = PAUSE_BETWEEN_ACTIONS

# ============================================
# HELPER FUNCTIONS
# ============================================

def log(message, level="INFO"):
    """Print log message with timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    icons = {
        "INFO": "ℹ️ ",
        "OK": "✅",
        "ERROR": "❌",
        "WAIT": "⏳",
        "CLICK": "🖱️ ",
        "DOUBLE": "🖱️🖱️",
        "TYPE": "⌨️ ",
        "KEY": "🔑",
    }
    
    icon = icons.get(level, "•")
    print(f"[{timestamp}] {icon} {message}")


def wait(seconds, message=""):
    """Wait with countdown display"""
    if message:
        log(f"{message} ({seconds}s)", "WAIT")
    
    for i in range(seconds, 0, -1):
        print(f"         ⏳ {i} seconds remaining...  ", end="\r")
        time.sleep(1)
    
    print(" " * 50, end="\r")


def single_click(element_name):
    """Single click on element"""
    if element_name not in COORDINATES:
        log(f"Unknown: {element_name}", "ERROR")
        return False
    
    x, y = COORDINATES[element_name]
    
    if x == 0 and y == 0:
        log(f"Coordinate not set: {element_name}", "ERROR")
        return False
    
    log(f"Click: {element_name} ({x}, {y})", "CLICK")
    pyautogui.click(x, y)
    time.sleep(0.5)
    return True


def double_click(element_name):
    """Double click on element"""
    if element_name not in COORDINATES:
        log(f"Unknown: {element_name}", "ERROR")
        return False
    
    x, y = COORDINATES[element_name]
    
    if x == 0 and y == 0:
        log(f"Coordinate not set: {element_name}", "ERROR")
        return False
    log(f"Double-click: {element_name} ({x}, {y})", "DOUBLE")
    pyautogui.doubleClick(x, y)
    time.sleep(0.5)
    return True


def type_text(text, interval=0.03):
    """Type text using keyboard (English only)"""
    log(f"Typing: {text[:40]}{'...' if len(text) > 40 else ''}", "TYPE")
    pyautogui.typewrite(text, interval=interval)
    time.sleep(0.3)


def paste_text(text):
    """Paste text using clipboard (supports Tamil/Unicode)"""
    log(f"Pasting: ({len(text)} characters)", "TYPE")
    pyperclip.copy(text)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)


def press_key(key):
    """Press a single key"""
    log(f"Key: {key}", "KEY")
    pyautogui.press(key)
    time.sleep(0.3)


def hotkey(*keys):
    """Press key combination"""
    log(f"Hotkey: {' + '.join(keys)}", "KEY")
    pyautogui.hotkey(*keys)
    time.sleep(0.3)


def take_screenshot(name):
    """Take and save screenshot"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOTS_FOLDER, filename)
    
    try:
        pyautogui.screenshot(filepath)
        log(f"Screenshot: {filename}", "OK")
        return True
    except Exception as e:
        log(f"Screenshot failed: {e}", "ERROR")
        return False


def read_caption(filename):
    """Read caption from file"""
    filepath = os.path.join(CAPTIONS_FOLDER, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        log(f"Caption loaded: {filename}", "OK")
        return content
    except Exception as e:
        log(f"Caption failed: {e}", "ERROR")
        return ""


def move_to_posted(filename):
    """Move image to posted folder"""
    source = os.path.join(IMAGES_FOLDER, filename)
    dest = os.path.join(POSTED_FOLDER, filename)
    
    try:
        if os.path.exists(source):
            shutil.move(source, dest)
            log(f"Moved: {filename}", "OK")
            return True
    except Exception as e:
        log(f"Move failed: {e}", "ERROR")
    
    return False


def file_exists(folder, filename):
    """Check if file exists"""
    return os.path.exists(os.path.join(folder, filename))


# ============================================
# MAIN POSTING FUNCTION
# ============================================

def post_to_instagram(post_data, post_number, start_from_desktop=True):
    """
    Complete posting process for one post
    """
    
    image_file = post_data['image']
    caption_file = post_data['caption']
    location = post_data.get('location', '')
    
    # Header
    print("")
    print("╔" + "═" * 50 + "╗")
    print(f"║  POST {post_number}: {image_file}")
    print("╚" + "═" * 50 + "╝")
    print("")
    
    try:
        
        if start_from_desktop:
            # ═══════════════════════════════════════════════════
            # STEP 1: SHOW DESKTOP
            # ═══════════════════════════════════════════════════
            
            log("STEP 1: Showing Desktop...", "INFO")
            hotkey('win', 'd')
            wait(WAIT_DESKTOP, "Desktop")
            
            # ═══════════════════════════════════════════════════
            # STEP 2: DOUBLE-CLICK CHROME
            # ═══════════════════════════════════════════════════
            
            log("STEP 2: Double-clicking Chrome...", "INFO")
            double_click('chrome_icon')
            wait(WAIT_CHROME_OPEN, "Chrome opening")
            
            # ═══════════════════════════════════════════════════
            # STEP 3: CLICK ADDRESS BAR
            # ═══════════════════════════════════════════════════
            
            log("STEP 3: Clicking address bar...", "INFO")
            single_click('address_bar')
            wait(1, "")
            
            # ═══════════════════════════════════════════════════
            # STEP 4: TYPE INSTAGRAM URL
            # ═══════════════════════════════════════════════════
            
            log("STEP 4: Typing Instagram URL...", "INFO")
            
            # Select all first (in case there's existing text)
            hotkey('ctrl', 'a')
            time.sleep(0.2)
            
            # Type URL
            type_text(INSTAGRAM_URL)
            
            # ═══════════════════════════════════════════════════
            # STEP 5: PRESS ENTER
            # ═══════════════════════════════════════════════════
            
            log("STEP 5: Pressing Enter...", "INFO")
            press_key('enter')
            wait(WAIT_PAGE_LOAD, "Instagram loading")
        
        else:
            # If not from desktop, just open URL
            log("STEP 1-5: Opening Instagram...", "INFO")
            import webbrowser
            webbrowser.open(INSTAGRAM_URL)
            wait(WAIT_PAGE_LOAD, "Instagram loading")
        
        # ═══════════════════════════════════════════════════
        # STEP 6: SKIP FULL SCREEN (removed F11)
        # ═══════════════════════════════════════════════════
        
        log("STEP 6: Skipping full screen...", "INFO")
        time.sleep(1)
        
        # ═══════════════════════════════════════════════════
        # STEP 7: CLICK CREATE (+)
        # ═══════════════════════════════════════════════════
        
        log("STEP 7: Clicking Create (+)...", "INFO")
        single_click('create_button')
        wait(WAIT_MENU_OPEN, "Menu opening")
        
        # ═══════════════════════════════════════════════════
        # STEP 8: CLICK POST
        # ═══════════════════════════════════════════════════
        
        log("STEP 8: Clicking Post...", "INFO")
        single_click('post_option')
        wait(WAIT_POPUP_OPEN, "Popup")
        
        # ═══════════════════════════════════════════════════
        # STEP 9: CLICK SELECT FROM COMPUTER
        # ═══════════════════════════════════════════════════
        
        log("STEP 9: Clicking 'Select from computer'...", "INFO")
        single_click('select_computer')
        wait(WAIT_FILE_DIALOG, "File dialog")
        
        # ═══════════════════════════════════════════════════
        # STEP 10: TYPE FILE PATH + ENTER
        # ═══════════════════════════════════════════════════
        
        log("STEP 10: Selecting image file...", "INFO")
        image_path = os.path.join(IMAGES_FOLDER, image_file)
        
        # Type file path
        time.sleep(0.5)
        type_text(image_path, interval=0.02)
        time.sleep(0.5)
        
        # Press Enter
        press_key('enter')
        wait(WAIT_IMAGE_LOAD, "Image loading")
        
        # ═══════════════════════════════════════════════════
        # STEP 11: CLICK NEXT (CROP)
        # ═══════════════════════════════════════════════════
        
        log("STEP 11: Clicking Next (crop)...", "INFO")
        single_click('next_button_crop')
        wait(WAIT_NORMAL, "Filter screen")
        
        # ═══════════════════════════════════════════════════
        # STEP 12: CLICK NEXT (FILTER)
        # ═══════════════════════════════════════════════════
        
        log("STEP 12: Clicking Next (filter)...", "INFO")
        single_click('next_button_filter')
        wait(WAIT_NORMAL, "Caption screen")
        
        # ═══════════════════════════════════════════════════
        # STEP 13: CLICK CAPTION AREA
        # ═══════════════════════════════════════════════════
        
        log("STEP 13: Clicking caption area...", "INFO")
        single_click('caption_area')
        wait(1, "")
        
        # ═══════════════════════════════════════════════════
        # STEP 14: PASTE CAPTION
        # ═══════════════════════════════════════════════════
        
        log("STEP 14: Pasting caption...", "INFO")
        caption = read_caption(caption_file)
        
        if caption:
            paste_text(caption)
        
        wait(WAIT_NORMAL, "")
        
        # STEP 15-18: ADD LOCATION (if provided)
        if location:
            log("STEP 15: Clicking Add location...", "INFO")
            single_click('add_location')
            wait(WAIT_NORMAL, "Location popup")
            
            log("STEP 16: Clicking location search...", "INFO")
            single_click('location_search')
            wait(1, "")
            
            # Step 17: Type location using CLIPBOARD (works better!)
            log(f"STEP 17: Typing location: {location}...", "INFO")
            pyperclip.copy(location)           # Copy to clipboard
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'v')      # Paste
            time.sleep(0.5)
            wait(WAIT_LOCATION_SEARCH, "Searching")
            
            # Step 18: Click first result
            log("STEP 18: Clicking first result...", "INFO")
            single_click('location_first_result')
            wait(WAIT_NORMAL, "")
        
        else:
            log("STEP 15-18: Skipping location...", "INFO")
        
        # ═══════════════════════════════════════════════════
        # STEP 19: CLICK SHARE
        # ═══════════════════════════════════════════════════
        
        log("STEP 19: Clicking Share...", "INFO")
        single_click('share_button')
        wait(WAIT_UPLOAD, "Uploading")
        
        # ═══════════════════════════════════════════════════
        # STEP 20: TAKE SCREENSHOT
        # ═══════════════════════════════════════════════════
        
        log("STEP 20: Taking screenshot...", "INFO")
        take_screenshot(f"post_{post_number}_complete")
        
        # ═══════════════════════════════════════════════════
        # STEP 21: CLOSE TAB
        # ═══════════════════════════════════════════════════
        
        log("STEP 21: Closing tab...", "INFO")
        hotkey('ctrl', 'w')
        wait(WAIT_NORMAL, "")
        
        # ═══════════════════════════════════════════════════
        # STEP 22: SKIP (no full screen to exit)
        # ═══════════════════════════════════════════════════
        
        log("STEP 22: Skipping...", "INFO")
        
        # ═══════════════════════════════════════════════════
        # STEP 23: MOVE TO POSTED FOLDER
        # ═══════════════════════════════════════════════════
        
        log("STEP 23: Moving to posted folder...", "INFO")
        move_to_posted(image_file)
        
        # ═══════════════════════════════════════════════════
        # SUCCESS!
        # ═══════════════════════════════════════════════════
        
        print("")
        print("╔" + "═" * 50 + "╗")
        print(f"║  ✅ POST {post_number} COMPLETE!")
        print("╚" + "═" * 50 + "╝")
        print("")
        
        return True
    
    except Exception as e:
        log(f"ERROR: {str(e)}", "ERROR")
        take_screenshot(f"error_post_{post_number}")
        return False


# ============================================
# PRE-FLIGHT CHECK
# ============================================

def pre_flight_check():
    """Check everything before starting"""
    
    print("")
    print("╔" + "═" * 50 + "╗")
    print("║  PRE-FLIGHT CHECK")
    print("╚" + "═" * 50 + "╝")
    print("")
    
    all_ok = True
    
    # Check folders exist
    folders = [
        ("Images", IMAGES_FOLDER),
        ("Captions", CAPTIONS_FOLDER),
        ("Screenshots", SCREENSHOTS_FOLDER),
        ("Posted", POSTED_FOLDER),
    ]
    
    for name, path in folders:
        if os.path.exists(path):
            log(f"Folder OK: {name}", "OK")
        else:
            log(f"Folder MISSING: {name}", "ERROR")
            os.makedirs(path, exist_ok=True)
            log(f"Created: {name}", "OK")
    
    print("")
    
    # Check files for each post
    for i, post in enumerate(POSTS, 1):
        img_ok = file_exists(IMAGES_FOLDER, post['image'])
        cap_ok = file_exists(CAPTIONS_FOLDER, post['caption'])
        
        if img_ok and cap_ok:
            log(f"Post {i}: {post['image']} ✓", "OK")
        else:
            if not img_ok:
                log(f"Post {i}: Image MISSING - {post['image']}", "ERROR")
                all_ok = False
            if not cap_ok:
                log(f"Post {i}: Caption MISSING - {post['caption']}", "ERROR")
                all_ok = False
    
    print("")
    
    # Check essential coordinates
    essential = [
        'create_button',
        'post_option', 
        'select_computer',
        'next_button_crop',
        'next_button_filter',
        'caption_area',
        'share_button',
    ]
    
    for coord in essential:
        if coord in COORDINATES:
            x, y = COORDINATES[coord]
            if x > 0 or y > 0:
                log(f"Coord OK: {coord} = ({x}, {y})", "OK")
            else:
                log(f"Coord NOT SET: {coord}", "ERROR")
                all_ok = False
        else:
            log(f"Coord MISSING: {coord}", "ERROR")
            all_ok = False
    
    return all_ok


# ============================================
# MAIN FUNCTION
# ============================================

def main():
    """Main entry point"""
    
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Header
    print("")
    print("╔" + "═" * 58 + "╗")
    print("║                                                          ║")
    print("║         INSTAGRAM AUTO POST                              ║")
    print("║         Desktop → Chrome → Instagram                     ║")
    print("║                                                          ║")
    print("╠" + "═" * 58 + "╣")
    print(f"║  Posts to publish : {len(POSTS)}")
    print(f"║  Gap between posts: {GAP_BETWEEN_POSTS} minutes")
    print(f"║  Time now         : {datetime.now().strftime('%H:%M:%S')}")
    print("║                                                          ║")
    print("╚" + "═" * 58 + "╝")
    print("")
    
    # Pre-flight check
    if not pre_flight_check():
        print("")
        log("PRE-FLIGHT CHECK FAILED!", "ERROR")
        log("Fix issues above and try again.", "ERROR")
        print("")
        input("Press ENTER to exit...")
        return
    
    print("")
    log("Pre-flight check PASSED!", "OK")
    
    # ALWAYS use Desktop mode - no question asked!
    print("")
    log("Mode: Desktop → Chrome → Instagram (All posts)", "OK")
    
    # Check desktop coordinates
    x, y = COORDINATES.get('chrome_icon', (0, 0))
    if x == 0 and y == 0:
        log("Chrome icon coordinate not set!", "ERROR")
        log("Run find_coordinates.py first", "ERROR")
        print("")
        input("Press ENTER to exit...")
        return
    
    # Safety warning
    print("")
    print("╔" + "═" * 58 + "╗")
    print("║  ⚠️  SAFETY WARNING                                       ║")
    print("║                                                          ║")
    print("║  • Move mouse to TOP-LEFT corner to STOP                 ║")
    print("║  • DON'T touch mouse/keyboard during automation          ║")
    print("║  • Close all other windows                               ║")
    print("╚" + "═" * 58 + "╝")
    print("")
    
    # Countdown
    log(f"Starting in {WAIT_BEFORE_START} seconds...", "WAIT")
    log("Move mouse to corner NOW to cancel!", "INFO")
    print("")
    
    wait(WAIT_BEFORE_START, "Prepare")
    
    # Process each post - ALL use Desktop mode!
    successful = 0
    failed = 0
    
    for i, post in enumerate(POSTS, 1):
        
        # ALL posts: Desktop → Chrome → Instagram
        if post_to_instagram(post, i, start_from_desktop=True):
            successful += 1
        else:
            failed += 1
        
        # Wait between posts
        if i < len(POSTS):
            print("")
            log(f"Waiting {GAP_BETWEEN_POSTS} minutes before next post...", "WAIT")
            wait(GAP_BETWEEN_POSTS * 60, f"Next post in")
    
    # Summary
    print("")
    print("╔" + "═" * 58 + "╗")
    print("║                                                          ║")
    print("║              AUTOMATION COMPLETE! ✅                     ║")
    print("║                                                          ║")
    print("╠" + "═" * 58 + "╣")
    print(f"║  Successful : {successful}")
    print(f"║  Failed     : {failed}")
    print(f"║  End time   : {datetime.now().strftime('%H:%M:%S')}")
    print("║                                                          ║")
    print("║  Check 'screenshots' folder for proof images             ║")
    print("║  Check 'posted' folder for completed images              ║")
    print("║                                                          ║")
    print("╚" + "═" * 58 + "╝")
    print("")
    
    input("Press ENTER to exit...")


# ============================================
# RUN
# ============================================

if __name__ == "__main__":
    main()