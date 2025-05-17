# CodeGen 🎁 - Multi-Platform Gift Code Generator Suite

Welcome to **CodeGen**, the ultimate, educational gift-code generator simulation tool designed for developers, testers, and UI/UX researchers. This tool creates **randomized, fake gift codes** for thousands of popular platforms like Discord, Steam, Spotify, and many more — supporting **desktop, mobile (Android), and web** deployments.

---

## 🚀 Features at a Glance

- 🎨 **Modern Multi-Platform GUI**
  - Desktop GUI (Tkinter)
  - Android GUI (Kivy)
  - Offline Web Version (React + Tailwind)

- 🔐 **Password-Protected Admin Panel**
  - Manage, add, update, or delete services
  - Multi-select delete
  - Search bar and bulk length editor
  - Save settings to a persistent local `services.json` file

- 📦 **Custom Code Generation**
  - Each service has unique customizable code length
  - Generate 1–1000 codes per request
  - Save generated results to `.txt` file

- 🧠 **Built-in Services**
  - Over **1000 preconfigured services** + support for custom entries
  - Example: Discord Nitro, Steam, Xbox, Netflix, Google Play, and more

- 🔧 **Configurable Settings**
  - Admin password configurable via environment variable: `NITRO_ADMIN_PW`
  - File-based service persistence

- 💾 **Cross-Platform Builds**
  - `.exe` via PyInstaller
  - `.apk` via Buildozer
  - Offline Web App `.html/.js` via React
  - Optional PWA support

- 🧪 **Unit-Test Ready**
  - Generator function supports testing
  - Modular codebase design for easier maintenance

---

## 💻 Desktop (Tkinter GUI)

```bash
python desktop_gui.py
```

- Fully featured admin interface
- Built-in menu bar (`Admin`, `Help`)
- Generate, view, and save codes locally
- Export-ready with `.spec` file and icon

### 💼 Build with PyInstaller

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --icon=nitro_icon.ico desktop_gui.py
```

---

## 📱 Android Version (Kivy)

- Uses Kivy framework for mobile GUI
- Touch-friendly layout and spinner interface
- Manual file saving supported
- Requires Python environment or Buildozer

### 📦 Build APK

```bash
buildozer init
buildozer -v android debug
```

> Make sure your main file is named `main.py`

---

## 🌐 Web Version (React)

- Built with React, Tailwind, and offline browser storage
- Download results as `.txt`
- Pure client-side: no server required
- Compatible with GitHub Pages, Netlify, or local use

### 🛠 Run Locally

```bash
npm install
npm run dev
```

### 📦 Build for Production

```bash
npm run build
```

---

## 🔐 Admin Features Overview

The admin panel gives you full control over service configurations:

| Feature              | Description                                         |
|----------------------|-----------------------------------------------------|
| Add/Update Service   | Add new or change length of existing services       |
| Remove Selected      | Delete any number of services                       |
| Delete All           | Wipe the entire list (confirmation required)        |
| Update Selected Len  | Change code length for multiple selected services   |
| Search Filter        | Quickly find services using the live search box     |
| Save JSON            | Automatically persists edits to `services.json`     |

**Default Password**: `starfire`  
(Override via `export NITRO_ADMIN_PW=yourpassword`)

---

## 📁 Files and Structure

```
/
├── desktop_gui.py            # Desktop version (Tkinter)
├── kivy_script.py            # Android version (Kivy)
├── web_generator.jsx         # React Web App
├── nitro_generator.spec      # PyInstaller build config
├── buildozer.spec            # Android APK config
├── nitro_icon.ico            # Application icon
├── services.json             # Local services store (auto created)
└── README.md                 # This file
```

---

## ⚠️ Legal & Ethical Disclaimer

**CodeGen is an educational simulation tool.**  
It does **not generate real codes**, nor should it be used in any manner that violates the terms of service of any platform.  
Use this only for UI/UX development, security research, or internal demos.

---

## 🤝 Credits

- 💡 Author: **Ethan Bragdon**
- ✨ Contributions, suggestions, and feedback always welcome!

---

## 📬 Questions or Support?

If you're using CodeGen in your classroom, security lab, or dev workshop — let us know! We're happy to hear how you're expanding it.

Happy generating!

---

## 🛠️ Installation Troubleshooting

### ❓ PyInstaller Build Fails
- Make sure `tkinter` is installed. On Ubuntu:
  ```bash
  sudo apt install python3-tk
  ```
- Ensure `nitro_icon.ico` is in the same directory.
- Add `--clean` flag to rebuild fresh.

### ❓ Kivy Buildozer Errors in Colab
- Switch to a single architecture in `buildozer.spec`:
  ```
  arch = arm64-v8a
  ```
- Clean your build with:
  ```bash
  buildozer android clean
  ```
- If stuck, try restarting Colab Runtime.

### ❓ React Web App Won’t Load
- Confirm Node.js and NPM are installed:
  ```bash
  node -v && npm -v
  ```
- Use local server or deploy via GitHub Pages:
  ```bash
  npm run dev
  ```

---

## ❓ Frequently Asked Questions

**Q: Are these codes real?**  
A: No. CodeGen simulates codes for educational or UI purposes only.

**Q: Where is my data stored?**  
A: Desktop saves to `services.json`. Web uses `localStorage`.

**Q: How can I change the admin password?**  
A: Set the environment variable `NITRO_ADMIN_PW`.

**Q: Can I import a custom list of services?**  
A: Yes, edit or replace the `services.json` file manually or build an import button.

**Q: Is this open source?**  
A: You are free to use, extend, and adapt CodeGen for personal or non-commercial use.

---

## 🖼️ Screenshots

### 🔧 Admin Panel
![Admin Panel Screenshot](https://via.placeholder.com/600x400?text=Admin+Panel)

### 💻 Desktop Generator UI
![Desktop UI Screenshot](https://via.placeholder.com/600x400?text=Desktop+Generator)

### 🌐 Web App Interface
![Web Generator Screenshot](https://via.placeholder.com/600x400?text=Web+App+Interface)

---

Enjoy using **CodeGen** and happy simulating!
