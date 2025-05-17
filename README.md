# Educational Mock Gift Code Generator

Version: Alpha 1.0.0  
Author: Ethan Bragdon  
Date: 05-16-2025

Mock gift code generator using Kivy for cross-platform and Android compatibility.

## Features
- 1000+ popular and fake services
- Batch generation and timestamped outputs
- Android-compatible Kivy UI
- Save results from Kivy text box manually
- Desktop GUI version available separately

## Build APK for Android (on Linux/macOS)

1. Install buildozer:
   sudo apt install buildozer

2. Initialize build:
   buildozer init

3. Edit buildozer.spec and run:
   buildozer -v android debug

## Desktop Build with PyInstaller

1. pip install pyinstaller
2. pyinstaller --noconfirm --onefile --windowed --icon=nitro_icon.ico desktop_gui.py (Make sure it is in the same path as all of the files)

## Prebuilt Desktop Application Instructions
1. Download Python Onto Your Local Machine
2. Open The Application
