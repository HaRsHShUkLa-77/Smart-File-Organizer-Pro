# 📂 Smart File Organizer Pro

A Python project that automatically organizes files into categorized folders based on their file extensions.

## ✨ Features

- 📁 Automatically categorizes files
- 🖼️ Organizes Images
- 🎥 Organizes Videos
- 🎵 Organizes Music
- 📄 Organizes Documents
- 🐍 Organizes Python files
- 📦 Creates category folders automatically
- 🔄 Handles duplicate filenames automatically
- 📝 Logs all successful file movements
- ⚠️ Handles common exceptions gracefully
- 📊 Displays a summary after completion

---

## 🛠️ Technologies Used

- Python 3
- os
- shutil
- logging

---

## 📂 Supported File Types

| Category | Extensions |
|----------|------------|
| Images | .jpg, .jpeg, .png |
| Videos | .mp4, .mkv |
| Music | .mp3 |
| Documents | .pdf, .docx, .txt |
| Python | .py |
| Others | Any unsupported extension |

---

## 🚀 How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/smart-file-organizer-pro.git
```

2. Go to the project folder

```bash
cd smart-file-organizer-pro
```

3. Run the program

```bash
python main.py
```

4. Enter the folder path when prompted.

---

## 📸 Example Output

```text
========== Smart File Organizer Pro ==========

Folder Found

Files Found:

photo.jpg -----> Images
movie.mp4 -----> Videos
notes.pdf -----> Documents

Success: Moved 'photo.jpg'
Success: Moved 'movie.mp4'
Success: Moved 'notes.pdf'

========== Summary ==========
Total Files          : 3
Moved Successfully   : 3
Failed               : 0
============================
```

---

## 📁 Project Structure

```
Smart-File-Organizer-Pro/
│
├── main.py
├── organizer.log
├── README.md
```

---

## 🎯 Future Improvements

- Progress Bar
- GUI Version (Tkinter / CustomTkinter)
- Undo Operation
- Configuration File
- Command Line Arguments
- More Supported File Types

---

## 👨‍💻 Author

**Harsh Shukla**

GitHub: https://github.com/your-username

---

## ⭐ If you like this project, consider giving it a star!
