import os
import sys
import subprocess
import shutil
from pathlib import Path

def customInstallerUnnamed(pkg_name):
    subprocess.run([sys.executable, "-m", "pip", "install", pkg_name], check=True)

if sys.version_info >= (3, 13):
    print("Error: Python 3.13 is not supported by PyInstaller. Please use Python 3.12 or lower.")
    sys.exit(1)

customInstallerUnnamed("pyinstaller")
customInstallerUnnamed("pywin32")

import win32com.client  # Safe to import after pywin32 install

def create_stub_py_file(index, folder):
    filename = folder / f"stub_{index}.py"
    with open(filename, "w") as f:
        f.write("import sys\nsys.exit(0)\n")
    return filename

def compile_exe(py_file, dist_folder):
    exe_name = py_file.stem
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--name", exe_name,
        "--distpath", str(dist_folder),
        "--workpath", str(dist_folder / "build"),
        "--specpath", str(dist_folder / "spec"),
        str(py_file)
    ], check=True)

def create_shortcut(target_path, shortcut_path, icon_path=None):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(str(shortcut_path))
    shortcut.TargetPath = str(target_path.resolve())
    shortcut.WorkingDirectory = str(target_path.parent.resolve())
    if icon_path and icon_path.exists():
        shortcut.IconLocation = str(icon_path.resolve())
    shortcut.Save()

def main(n):
    script_dir = Path(__file__).parent.resolve()
    icon_file = script_dir / "separator.ico"

    base = (script_dir / "result").resolve()
    exe_folder = base
    shortcut_folder = base / "shortcuts"
    build_folder = exe_folder / "build"
    spec_folder = exe_folder / "spec"

    if base.exists():
        shutil.rmtree(base)
    exe_folder.mkdir(parents=True)
    shortcut_folder.mkdir(parents=True)

    for i in range(n):
        stub_py = create_stub_py_file(i, exe_folder)
        compile_exe(stub_py, exe_folder)
        exe_name = f"{stub_py.stem}.exe"
        exe_path = exe_folder / exe_name
        shortcut_path = shortcut_folder / f"{stub_py.stem}.lnk"
        create_shortcut(exe_path, shortcut_path, icon_path=icon_file)

    for item in exe_folder.glob("stub_*.py"):
        item.unlink()
    if build_folder.exists():
        shutil.rmtree(build_folder)
    if spec_folder.exists():
        shutil.rmtree(spec_folder)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_exes.py <number_of_exes>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: parameter must be an integer.")
        sys.exit(1)

    main(n)
