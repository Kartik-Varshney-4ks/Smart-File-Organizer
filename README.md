# 📂 Smart File Organizer

A Python-based command-line file management application that automatically organizes files into categories, detects duplicate files using SHA-256 hashing, previews file operations, provides statistics and search, maintains activity logs, and supports undo functionality.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## ✨ Features

- 📂 **Automatic File Organization**
- 📋 **Preview Organization** before moving files
- 🔁 **Duplicate File Detection** using SHA-256 hashing
- 🗑️ **Duplicate Management** with confirmation before deletion
- 📊 **File Statistics**
- 🔎 **File Search**
- 📝 **Activity Logging**
- ↩️ **Undo Last Organization**
- 🛡️ **Error Handling**
- 📁 **Folder Validation**
- 💻 **Interactive Command-Line Interface**

---

## 📸 Screenshots

### 🖥️ Main Menu

![Main Menu](screenshots/main-menu.png)

### 📋 Organization Preview

![Organization Preview](screenshots/preview.png)

### 📊 File Statistics

![File Statistics](screenshots/statistics.png)

### ↩️ Undo Organization

![Undo Organization](screenshots/undo.png)

---

## 🛠️ Technologies Used

- **Python 3**
- `os` — file and directory operations
- `shutil` — file movement
- `hashlib` — SHA-256 hashing
- File handling
- Directory traversal
- Exception handling
- Logging
- Command-line interface

---

## 📁 Project Structure

```text
Smart-File-Organizer/
│
├── core/
│   ├── __init__.py
│   ├── organizer.py
│   ├── duplicate.py
│   ├── statistics.py
│   ├── search.py
│   ├── preview.py
│   └── logger.py
│
├── screenshots/
│   ├── main-menu.png
│   ├── preview.png
│   ├── statistics.png
│   └── undo.png
│
├── main.py
├── README.md
├── LICENSE
└── .gitignore
---

## Copyright

© 2026 Kartik Varshney. All rights reserved.

This project and its source code are the property of Kartik Varshney.
Unauthorized copying, modification, distribution, or use of this code is not permitted without prior written permission.