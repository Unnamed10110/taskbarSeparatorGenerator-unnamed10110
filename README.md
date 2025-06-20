# 🧱 Taskbar Separator Generator

Create invisible, unpinnable shortcuts you can use as **spacers on the Windows taskbar** — a simple trick to help visually organize your open programs.

These shortcuts are fully inert: they do nothing when clicked and serve only to act as **visual separators**.

---

# ✨ Features

- Generate any number of dummy shortcuts (e.g., `stub_0.lnk`, `stub_1.lnk`, etc.)
- Shortcuts are unpinnable (Windows won't allow pinning non-functional `.lnk` files).
- You can use these as "spacers" between taskbar icons.
- Customizable icon — use any `.ico` file to style your separators.

---

# 📸 Example Use Case

If you're like many users who keep dozens of apps pinned to the taskbar, this helps:


---

# 🛠 Requirements

- **Python 3.12 or lower**
  > PyInstaller does **not** yet support Python 3.13. Python 3.13 made internal changes that broke PyInstaller bundles apps. There is no stable release of PyInstaller that supports Python 3.13 yet.
- **PyInstaller** must be in your system PATH
  > You can install it via pip:  
  > `pip install pyinstaller`
- This script will also install `pywin32` automatically if missing.

---

# ⚙️ Usage

1. Place your `separator.ico` file in the same folder as the script (`taskbarSeparatorGen.py`)  
   *(or use the provided default — feel free to replace it)*

2. Run the script with the number of separators you want to create:

```bash
python taskbarSeparatorGen.py 5
```
---

# ⚙️ Example
![example](https://github.com/user-attachments/assets/9e833ba3-db3d-4874-8399-e5a62cbb8bef)


https://github.com/user-attachments/assets/c4a3c3aa-0f1d-4b0a-95e1-b71aee92797f



---


# 📂 Output Structure
```sql
result/
├── stub_0.exe
├── stub_1.exe
├── ...
├── shortcuts/
│   ├── stub_0.lnk
│   ├── stub_1.lnk
│   └── ...
```

---

# 🚨 Windows Defender Warning
  This script triggers Windows Defender or other antivirus tools because PyInstaller compiles a binary using a C compiler in the background.
  There is nothing malicious — the generated .exe files do absolutely nothing and simply exit with code 0.

---
# 🎨 Custom Icons
  If you want a different icon:
  Replace the separator.ico file in the script directory.
  Keep the filename as separator.ico.
  
---

# 🧼 Cleanup
  The script automatically deletes:
  Temporary .py stubs
  PyInstaller build/ and spec/ folders
  So your result/ folder will only contain what matters.
  
---
# 📃 License
  MIT License — use freely.
