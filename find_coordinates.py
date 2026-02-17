import pyautogui
import time
import os

def clear_screen():
    """Clear console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_coordinate(name, instruction):
    """Get coordinate for one element"""
    print("")
    print("=" * 60)
    print(f"  FIND: {name}")
    print("=" * 60)
    print("")
    print(f"  {instruction}")
    print("")
    print("  Move mouse to the element and press ENTER")
    print("")
    
    input("  >>> Press ENTER when mouse is in position...")
    
    x, y = pyautogui.position()
    print("")
    print(f"  ✅ Saved: {name} = ({x}, {y})")
    
    return (x, y)

def show_live_coordinates():
    """Show live mouse position for 20 seconds"""
    print("")
    print("  🔴 LIVE MODE - 20 seconds")
    print("  Move mouse around to see coordinates")
    print("")
    
    start = time.time()
    while time.time() - start < 20:
        x, y = pyautogui.position()
        remaining = int(20 - (time.time() - start))
        print(f"  X: {x:4d}  |  Y: {y:4d}  |  {remaining:2d}s remaining  ", end="\r")
        time.sleep(0.1)
    print("")

def main():
    """Main function"""
    
    clear_screen()
    
    # Header
    print("")
    print("╔" + "═" * 58 + "╗")
    print("║                                                          ║")
    print("║         INSTAGRAM COORDINATE FINDER                      ║")
    print("║         Step-by-Step Guide                               ║")
    print("║                                                          ║")
    print("╚" + "═" * 58 + "╝")
    print("")
    
    # Screen size
    width, height = pyautogui.size()
    print(f"  Your Screen: {width} x {height} pixels")
    print("")
    
    # Store all coordinates
    coords = {}
    
    # ══════════════════════════════════════════════════════════════
    # PART 1: DESKTOP COORDINATES (Optional)
    # ══════════════════════════════════════════════════════════════
    
    print("=" * 60)
    print("  PART 1: DESKTOP COORDINATES (Optional)")
    print("=" * 60)
    print("")
    print("  Do you want automation to start from Desktop?")
    print("  (Double-click Chrome icon)")
    print("")
    choice = input("  Type 'yes' or 'no': ").strip().lower()
    
    if choice in ['yes', 'y']:
        print("")
        print("  📌 First, show your Desktop")
        print("  📌 Press Windows + D to minimize all windows")
        print("")
        input("  Press ENTER when Desktop is visible...")
        
        # Chrome icon
        coords['chrome_icon'] = get_coordinate(
            "CHROME ICON",
            "📌 Move mouse to Chrome icon on Desktop"
        )
        
        print("")
        print("  📌 Now double-click Chrome to open it")
        print("  📌 Wait for Chrome to fully open")
        print("")
        input("  Press ENTER when Chrome is open...")
        
        # Address bar
        coords['address_bar'] = get_coordinate(
            "ADDRESS BAR",
            "📌 Move mouse to the address/URL bar at top of Chrome"
        )
    else:
        coords['chrome_icon'] = (0, 0)
        coords['address_bar'] = (0, 0)
        print("")
        print("  ✅ Skipped Desktop coordinates")
    
    # ══════════════════════════════════════════════════════════════
    # PART 2: PREPARE INSTAGRAM
    # ══════════════════════════════════════════════════════════════
    
    print("")
    print("=" * 60)
    print("  PART 2: PREPARE INSTAGRAM")
    print("=" * 60)
    print("")
    print("  📌 Open Chrome browser")
    print("  📌 Go to: https://www.instagram.com/")
    print("  📌 Login to your account")
    print("  📌 Press F11 for FULL SCREEN")
    print("")
    print("  ⚠️  IMPORTANT: Must be in FULL SCREEN (F11)")
    print("")
    input("  Press ENTER when Instagram is ready in full screen...")
    
    # ══════════════════════════════════════════════════════════════
    # PART 3: INSTAGRAM COORDINATES
    # ══════════════════════════════════════════════════════════════
    
    print("")
    print("=" * 60)
    print("  PART 3: INSTAGRAM COORDINATES")
    print("=" * 60)
    
    # 1. Create Button (+)
    coords['create_button'] = get_coordinate(
        "CREATE BUTTON (+)",
        "📌 Find the + icon (Create button)\n  📌 It's usually in the left sidebar or top menu"
    )
    
    # 2. Post Option
    print("")
    print("  📌 NOW CLICK the + button in Instagram")
    print("  📌 A menu will appear with options")
    print("")
    input("  Press ENTER after clicking + button...")
    
    coords['post_option'] = get_coordinate(
        "POST OPTION",
        "📌 Find 'Post' option in the menu\n  📌 It might show a grid icon or say 'Post'"
    )
    
    # 3. Select from Computer
    print("")
    print("  📌 NOW CLICK 'Post' option")
    print("  📌 Upload popup will appear")
    print("")
    input("  Press ENTER after clicking Post...")
    
    coords['select_computer'] = get_coordinate(
        "SELECT FROM COMPUTER",
        "📌 Find the blue 'Select from computer' button\n  📌 It's in the center of the popup"
    )
    
    # 4. Next Button (Crop)
    print("")
    print("  📌 NOW CLICK 'Select from computer'")
    print("  📌 Choose ANY image from your computer")
    print("  📌 Wait for image to load")
    print("")
    input("  Press ENTER after image is loaded...")
    
    coords['next_button_crop'] = get_coordinate(
        "NEXT BUTTON (Crop Screen)",
        "📌 Find the 'Next' button at TOP-RIGHT\n  📌 This is on the crop/resize screen"
    )
    
    # 5. Next Button (Filter)
    print("")
    print("  📌 NOW CLICK 'Next' button")
    print("  📌 Filter screen will appear")
    print("")
    input("  Press ENTER after clicking Next...")
    
    coords['next_button_filter'] = get_coordinate(
        "NEXT BUTTON (Filter Screen)",
        "📌 Find the 'Next' button at TOP-RIGHT again\n  📌 This skips the filter selection"
    )
    
    # 6. Caption Area
    print("")
    print("  📌 NOW CLICK 'Next' button again")
    print("  📌 Caption/Share screen will appear")
    print("")
    input("  Press ENTER after clicking Next...")
    
    coords['caption_area'] = get_coordinate(
        "CAPTION TEXT AREA",
        "📌 Find the text box for caption\n  📌 It says 'Write a caption...'"
    )
    
    # 7. Add Location
    coords['add_location'] = get_coordinate(
        "ADD LOCATION",
        "📌 Find 'Add location' text/link\n  📌 It's below the caption area"
    )
    
    # 8. Location Search Box
    print("")
    print("  📌 NOW CLICK 'Add location'")
    print("  📌 Location search popup will appear")
    print("")
    input("  Press ENTER after clicking Add location...")
    
    coords['location_search'] = get_coordinate(
        "LOCATION SEARCH BOX",
        "📌 Find the search box to type location\n  📌 It's where you type city name"
    )
    
    # 9. First Location Result
    print("")
    print("  📌 NOW TYPE 'Chennai' in the search box")
    print("  📌 Wait for search results to appear")
    print("")
    input("  Press ENTER after results appear...")
    
    coords['location_first_result'] = get_coordinate(
        "FIRST LOCATION RESULT",
        "📌 Find the FIRST search result\n  📌 Usually 'Chennai, India' or similar"
    )
    
    # 10. Share Button
    print("")
    print("  📌 CLICK the first result or press ESC")
    print("  📌 You should be back on caption screen")
    print("")
    input("  Press ENTER when back on caption screen...")
    
    coords['share_button'] = get_coordinate(
        "SHARE BUTTON",
        "📌 Find the blue 'Share' button at TOP-RIGHT\n  📌 This posts your image"
    )
    
    # ══════════════════════════════════════════════════════════════
    # PART 4: SAVE COORDINATES
    # ══════════════════════════════════════════════════════════════
    
    print("")
    print("")
    print("╔" + "═" * 58 + "╗")
    print("║         ALL COORDINATES FOUND! ✅                        ║")
    print("╚" + "═" * 58 + "╝")
    print("")
    print("  Copy this ENTIRE block to config.py:")
    print("")
    print("  " + "─" * 54)
    print("")
    print("COORDINATES = {")
    print(f"    # Desktop (optional)")
    print(f"    'chrome_icon': {coords['chrome_icon']},")
    print(f"    'address_bar': {coords['address_bar']},")
    print(f"    ")
    print(f"    # Instagram")
    print(f"    'create_button': {coords['create_button']},")
    print(f"    'post_option': {coords['post_option']},")
    print(f"    'select_computer': {coords['select_computer']},")
    print(f"    'next_button_crop': {coords['next_button_crop']},")
    print(f"    'next_button_filter': {coords['next_button_filter']},")
    print(f"    'caption_area': {coords['caption_area']},")
    print(f"    'add_location': {coords['add_location']},")
    print(f"    'location_search': {coords['location_search']},")
    print(f"    'location_first_result': {coords['location_first_result']},")
    print(f"    'share_button': {coords['share_button']},")
    print("}")
    print("")
    print("  " + "─" * 54)
    print("")
    
    # Save to file
    try:
        with open("my_coordinates.txt", "w", encoding="utf-8") as f:
            f.write("# ============================================\n")
            f.write("# YOUR COORDINATES - Copy to config.py\n")
            f.write("# ============================================\n\n")
            f.write("COORDINATES = {\n")
            f.write(f"    # Desktop (optional)\n")
            f.write(f"    'chrome_icon': {coords['chrome_icon']},\n")
            f.write(f"    'address_bar': {coords['address_bar']},\n")
            f.write(f"    \n")
            f.write(f"    # Instagram\n")
            f.write(f"    'create_button': {coords['create_button']},\n")
            f.write(f"    'post_option': {coords['post_option']},\n")
            f.write(f"    'select_computer': {coords['select_computer']},\n")
            f.write(f"    'next_button_crop': {coords['next_button_crop']},\n")
            f.write(f"    'next_button_filter': {coords['next_button_filter']},\n")
            f.write(f"    'caption_area': {coords['caption_area']},\n")
            f.write(f"    'add_location': {coords['add_location']},\n")
            f.write(f"    'location_search': {coords['location_search']},\n")
            f.write(f"    'location_first_result': {coords['location_first_result']},\n")
            f.write(f"    'share_button': {coords['share_button']},\n")
            f.write("}\n")
        
        print("  ✅ Also saved to: my_coordinates.txt")
        print("")
    except:
        pass
    
    print("  NEXT STEPS:")
    print("  1. Open config.py")
    print("  2. Find the COORDINATES section")
    print("  3. Replace with the coordinates above")
    print("  4. Save config.py")
    print("  5. Run run.bat to test!")
    print("")
    
    input("  Press ENTER to exit...")

# Run
if __name__ == "__main__":
    main()
