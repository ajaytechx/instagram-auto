<div align="center">

# 📸 Instagram Auto Post

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-10%2F11-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-Automation-FF6B6B?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.3-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-GEM.AI-blueviolet?style=for-the-badge)

### 🤖 Automate Your Instagram Posting Workflow

*A powerful desktop automation tool that posts images to Instagram with captions and location tags automatically*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Configuration](#%EF%B8%8F-configuration) • [Documentation](#-documentation) • [FAQ](#-faq)

---

<img src="https://img.shields.io/badge/Tamil_Caption-Supported-green?style=flat-square" />
<img src="https://img.shields.io/badge/Unicode-Supported-green?style=flat-square" />
<img src="https://img.shields.io/badge/Location_Tag-Supported-green?style=flat-square" />

</div>

---

## 🎯 Overview

**Instagram Auto Post** is a Python-based desktop automation tool that automatically posts images to Instagram with captions and location tags. Built using PyAutoGUI, it simulates human interaction with Instagram Web to streamline your social media workflow.

### 🎪 Who is this for?

| User Type | Use Case |
|-----------|----------|
| 📱 Social Media Managers | Schedule and automate daily posts |
| 🏢 Digital Marketing Agencies | Handle multiple client accounts efficiently |
| 🛒 E-commerce Businesses | Post product images consistently |
| 📷 Content Creators | Focus on content, automate posting |
| 🌐 Recruitment Agencies | Share job postings automatically |

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🖥️ **Full Desktop Automation** | Launches Chrome, navigates to Instagram, and posts automatically |
| 🖼️ **Image Upload** | Supports JPG/PNG images (1080x1080 recommended) |
| 📝 **Multi-language Captions** | Full support for **Tamil**, English & Unicode text |
| 📍 **Location Tagging** | Auto-adds location to your posts |
| ⏰ **Scheduled Posting** | Configurable delays between posts (default: 2 min) |
| 📸 **Screenshot Proof** | Saves proof of every successful post |
| 📁 **Smart File Management** | Automatically moves posted images to archive |
| 🛑 **Fail-Safe Protection** | Move mouse to corner to instantly stop automation |
| ✅ **Pre-flight Check** | Validates all files and settings before starting |

---

## 📋 System Requirements

| Component | Requirement |
|-----------|-------------|
| **Operating System** | Windows 10 / 11 |
| **Python** | 3.8 or higher |
| **RAM** | 4 GB minimum |
| **Display** | 1920x1080 recommended |
| **Browser** | Google Chrome (latest) |
| **Internet** | Stable connection |

---

## 🚀 Installation

### Method 1: One-Click Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/ajaytechx/instagram-auto.git
cd instagram-auto

# Run setup script
setup.bat
```

### Method 2: Manual Setup

```bash
# Clone the repository
git clone https://github.com/ajaytechx/instagram-auto.git
cd instagram-auto

# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt
```

### 📦 Dependencies

```
pyautogui
pillow
pyperclip
opencv-python
```

---

## 📁 Project Structure

```
instagram-auto/
│
├── 📄 config.py                 # Configuration settings
├── 📄 instagram_auto_post.py    # Main automation script
├── 📄 find_coordinates.py       # Coordinate finder tool
├── 📄 xy_finder.py              # Live coordinate viewer
├── 📄 requirements.txt          # Python dependencies
│
├── 🔧 setup.bat                 # One-click setup
├── 🔧 run.bat                   # One-click run
├── 🔧 run_coordinates.bat       # Run coordinate finder
│
├── 📁 images/                   # Images to post
│   ├── post_01.jpg
│   ├── post_02.jpg
│   └── post_03.jpg
│
├── 📁 captions/                 # Caption text files (UTF-8)
│   ├── caption_01.txt
│   ├── caption_02.txt
│   └── caption_03.txt
│
├── 📁 screenshots/              # Proof screenshots (auto-saved)
└── 📁 posted/                   # Completed images (auto-moved)
```

---

## ⚙️ Configuration

### Step 1: Find Your Screen Coordinates

Since coordinates depend on your screen resolution, you must find them first:

```bash
python xy_finder.py
```

Move your mouse to each Instagram element and note the X, Y values.

### Step 2: Update config.py

| Element | Description |
|---------|-------------|
| `chrome_icon` | Chrome icon on desktop |
| `address_bar` | URL bar in Chrome |
| `create_button` | + icon in Instagram sidebar |
| `post_option` | "Post" option in create menu |
| `select_computer` | Blue "Select from computer" button |
| `next_button_crop` | Next button on crop screen |
| `next_button_filter` | Next button on filter screen |
| `caption_area` | Caption text input box |
| `add_location` | "Add location" link |
| `location_search` | Location search input |
| `share_button` | Blue "Share" button |

### Step 3: Timing Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `GAP_BETWEEN_POSTS` | 2 min | Wait time between posts |
| `WAIT_PAGE_LOAD` | 8 sec | Instagram page load time |
| `WAIT_UPLOAD` | 20 sec | Image upload time |
| `WAIT_CHROME_OPEN` | 5 sec | Chrome startup time |

---

## 🎮 Usage

### Preparing Content

1. **Add Images** → Place in `images/` folder
   - Format: JPG or PNG
   - Size: 1080 x 1080 pixels (recommended)
   - Naming: `post_01.jpg`, `post_02.jpg`, etc.

2. **Add Captions** → Place in `captions/` folder
   - Format: TXT files with **UTF-8 encoding**
   - Naming: `caption_01.txt`, `caption_02.txt`, etc.
   - Supports: Tamil, English, Emojis, Hashtags

### Running the Automation

**Option 1: Double-click** `run.bat`

**Option 2: Command Line**
```bash
.\venv\Scripts\Activate
python instagram_auto_post.py
```

### ✅ Pre-Run Checklist

- [ ] Chrome is installed and set as default browser
- [ ] Logged into Instagram in Chrome
- [ ] Images placed in `images/` folder
- [ ] Captions placed in `captions/` folder  
- [ ] Coordinates updated in `config.py`
- [ ] All other windows closed

### 🛑 Emergency Stop

> **Move mouse to any corner of the screen** → Automation stops instantly!

---

## 🔄 Automation Flow

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Desktop   │───▶│   Chrome    │───▶│  Instagram  │───▶│ Create Post │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                                                │
┌─────────────┐    ┌─────────────┐    ┌─────────────┐           │
│   Archive   │◀───│ Screenshot  │◀───│    Share    │◀──────────┘
└─────────────┘    └─────────────┘    └─────────────┘
```

### Detailed Steps

| # | Action | Wait Time |
|---|--------|-----------|
| 1 | Show Desktop (Win + D) | 2s |
| 2 | Open Chrome | 5s |
| 3 | Navigate to Instagram | 8s |
| 4 | Click Create (+) | 2s |
| 5 | Select "Post" | 3s |
| 6 | Upload Image | 5s |
| 7 | Click Next (Crop) | 2s |
| 8 | Click Next (Filter) | 2s |
| 9 | Add Caption | 2s |
| 10 | Add Location | 4s |
| 11 | Click Share | 20s |
| 12 | Save Screenshot | - |
| 13 | Move to Posted | - |

---

## 📊 Best Practices

### ✅ Posting Guidelines

| Recommendation | Reason |
|----------------|--------|
| 2-3 minute gap between posts | Avoid Instagram spam detection |
| Maximum 3-5 posts per session | Stay under Instagram rate limits |
| Vary your posting times | Appear more natural |
| Don't run 24/7 | Prevent account flags |
| Mix with manual engagement | Reply to comments manually |

### 📷 Image Guidelines

| Specification | Recommendation |
|---------------|----------------|
| Format | JPG or PNG |
| Dimensions | 1080 x 1080 pixels |
| File size | Under 8 MB |
| Aspect ratio | 1:1 (square) |

---

## 🛠️ Troubleshooting

| Error | Solution |
|-------|----------|
| `python is not recognized` | Reinstall Python with "Add to PATH" checked |
| `No module named pyautogui` | Run: `pip install pyautogui` |
| `No module named config` | Run script from project folder |
| `Fail-safe triggered` | Keep mouse away from screen corners |
| `Clicks at wrong position` | Re-run `xy_finder.py` and update coordinates |
| `Caption not pasting` | Ensure caption file is saved as UTF-8 |
| `Tamil text not showing` | Check file encoding is UTF-8 |

---

## 📚 Documentation

### Key Files

| File | Purpose |
|------|---------|
| `config.py` | All settings - coordinates, timing, posts list |
| `instagram_auto_post.py` | Main automation logic |
| `xy_finder.py` | Live coordinate display tool |
| `find_coordinates.py` | Guided coordinate finder |

### Core Functions

| Function | Description |
|----------|-------------|
| `post_to_instagram()` | Main posting workflow |
| `single_click(element)` | Click at named coordinate |
| `paste_text(text)` | Paste Unicode/Tamil text |
| `take_screenshot(name)` | Save proof screenshot |
| `pre_flight_check()` | Validate before starting |

---

## ❓ FAQ

<details>
<summary><b>Does this work with Instagram mobile app?</b></summary>
<br>
No, this works only with Instagram Web (instagram.com) in Chrome browser.
</details>

<details>
<summary><b>Will Instagram ban my account?</b></summary>
<br>
Using automation carries some risk. Follow the best practices section to minimize risk. Use 2-3 minute gaps and limit posts per session.
</details>

<details>
<summary><b>Can I post Reels or Stories?</b></summary>
<br>
Currently supports only regular image posts. Reels/Stories support may be added in future versions.
</details>

<details>
<summary><b>Does it work on Mac/Linux?</b></summary>
<br>
Designed for Windows 10/11. Mac/Linux would require modifications to keyboard shortcuts and file paths.
</details>

<details>
<summary><b>Why do coordinates keep changing?</b></summary>
<br>
Coordinates depend on screen resolution, browser window size, and zoom level. Re-run xy_finder.py if your display setup changes.
</details>

<details>
<summary><b>How do I post Tamil captions?</b></summary>
<br>
Save your caption files with UTF-8 encoding. The tool uses clipboard paste (Ctrl+V) which supports all Unicode characters including Tamil.
</details>

<details>
<summary><b>How do I add more posts?</b></summary>
<br>
1. Add images to `images/` folder (post_04.jpg, etc.)
2. Add captions to `captions/` folder (caption_04.txt, etc.)
3. Update the POSTS list in config.py
</details>

---

## 🔒 Safety Features

| Feature | Description |
|---------|-------------|
| **Fail-Safe** | Move mouse to any corner to stop instantly |
| **Pre-Flight Check** | Validates all files exist before starting |
| **Screenshot Proof** | Saves evidence of every successful post |
| **Auto-Archive** | Moves posted images to prevent duplicates |

---

## 📄 License

Licensed by **GEM.AI** | Version 1.3 | January 2026

---

## 👨‍💻 Author

<div align="center">

**AJAY N**

*Full Stack Developer | AI/ML Enthusiast*

*Pavishna Tech, Thoothukudi*

[![GitHub](https://img.shields.io/badge/GitHub-ajaytechx-181717?style=for-the-badge&logo=github)](https://github.com/ajaytechx)
[![Instagram](https://img.shields.io/badge/Instagram-ajay.techx-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/ajay.techx)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:angryajay23515@gmail.com)

</div>

---

<div align="center">

### ⭐ Star this repo if you find it useful!

**Made with ❤️ in Tamil Nadu, India**

</div>
