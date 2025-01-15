import os
import hashlib
from tqdm import tqdm

def compute_md5(file_path, chunk_size=8192):
    """
    Calculate the MD5 hash value of the specified file.
    chunk_size: The block size for reading the file, default 8192 Bytes
    """
    md5_hash = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    except Exception as e:
        print(f"[WARNING] Unable to read file {file_path}: {e}")
        return None

def main():
    source_folder = "Path to the source folder"
    dest_folder = "Path to the destination folder"

    # List of file extensions to check
    file_extensions = [
        ".jpg",
        ".arw",
        ".raw",
        ".png",
        ".jpeg",
        ".tif",
        ".tiff",
        ".heic",
        ".gif",
        ".bmp",
        ".webp",
        ".svg",
        ".mp4",
        ".mov",
    ]

    # ---------------------------------------------------------
    # Step 1: Collect photo paths from the destination folder
    # ---------------------------------------------------------
    print("Scanning the destination folder...")
    dest_files = []
    for root, dirs, files in os.walk(dest_folder):
        for filename in files:
            ext = os.path.splitext(filename)[1].lower()
            if ext in file_extensions:
                file_path = os.path.join(root, filename)
                dest_files.append(file_path)

    # ---------------------------------------------------------
    # Step 2: Calculate MD5 for all files in the destination folder and store them in a set
    # ---------------------------------------------------------
    print("Calculating MD5 for files in the destination folder...")
    dest_md5_set = set()
    for file_path in tqdm(dest_files, desc="Processing destination files", unit="file"):
        md5_value = compute_md5(file_path)
        if md5_value:
            dest_md5_set.add(md5_value)

    # ---------------------------------------------------------
    # Step 3: Collect photo paths from the source folder
    # ---------------------------------------------------------
    print("Scanning the source folder...")
    source_files = []
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            ext = os.path.splitext(filename)[1].lower()
            if ext in file_extensions:
                file_path = os.path.join(root, filename)
                source_files.append(file_path)

    # ---------------------------------------------------------
    # Step 4: Compare MD5 hashes of files in the source folder with the destination folder
    # ---------------------------------------------------------
    print("Comparing files between source and destination folders...")
    missing_or_corrupted_files = []
    for file_path in tqdm(source_files, desc="Validating source files", unit="file"):
        md5_value = compute_md5(file_path)

        # if md5_value is None or not found in dest_md5_set -> missing or corrupted
        if (md5_value is None) or (md5_value not in dest_md5_set):
            missing_or_corrupted_files.append(file_path)

    # ---------------------------------------------------------
    # Step 5: Output results
    # ---------------------------------------------------------
    if not missing_or_corrupted_files:
        print("\n[RESULT] All files in the source folder were found and are intact in the destination folder!")
    else:
        print("\n[RESULT] The following files are missing or corrupted in the destination folder:")
        for f in missing_or_corrupted_files:
            print(f)

if __name__ == "__main__":
    main()
