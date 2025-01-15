# Photo Organizer Kit

Photo Organizer Kit is a collection of Python tools designed to help you organize, verify, and manage your photo and file collections.

## Features
- **File Integrity Checker**: Compare files between two folders using MD5 hash.
- **Future Tools**: Additional tools for photo and file organization (stay tuned).

## Table of Contents
- [Getting Started](#getting-started)
- [Photo Archive Checker](#photo-archive-checker)
- [License](#license)

## Getting Started
   ```bash
   git clone https://github.com/ChunChih3310/Photo-Organizer-Kit.git
   cd Photo-Organizer-Kit
   pip install -r requirements.txt
   ```


## Photo Archive Checker
The Photo Archive Checker is a Python script designed to ensure that all files from a source folder have been correctly archived to a destination folder. This is particularly useful for verifying that no files were accidentally missed or corrupted during the archiving process.

### How It Works
1. Scan Folders: The script scans both the source and destination folders for files with supported extensions.
2. Compute MD5 Hashes: Calculates MD5 hashes for files in the destination folder and stores them in a set.
3. Compare Files: Matches the MD5 hashes of files in the source folder with those in the destination folder.
4. Identify Missing/Corrupted Files: Lists files from the source folder that are either missing or corrupted in the destination folder.

### Usage
```bash
python photo_archive_checker.py --source <source_folder> --destination <destination_folder>
```




## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


