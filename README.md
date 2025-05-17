# CodeGen

Version: Alpha 1.0.3
Date: 05-17-2025

Mock gift code generator using Kivy for cross-platform and Android compatibility.

## Features
- 1000+ popular and fake services
- Batch generation and timestamped outputs
- Android-compatible Kivy UI
- Save results from Kivy text box manually
- Desktop GUI version available separately
- Admin Panel For Easy Service Creation And Editing

## Build APK for Android (on Linux/macOS)

1. Install buildozer:
   sudo apt install buildozer

2. Initialize build:
   buildozer init

3. Edit buildozer.spec and run:
   buildozer -v android debug

## Desktop Build with PyInstaller

1. pip install pyinstaller
2. pyinstaller --noconfirm --onefile --windowed --icon=nitro_icon.ico script.py
