import os
import shutil

# 1. Configuration Dictionary
TRACKED_EXTENSIONS = {
    '.py': 'Development/Python',
    '.java': 'Development/Java',
    '.class': 'Development/Java/Compiled',
    '.pdf': 'Documents/PDFs',
    '.docx': 'Documents/Word',
    '.zip': 'Archives',
    '.txt': 'Plain text',
    '.tpg': 'Photo/jpg',
    '.jpeg': 'Photo/jpeg',
    '.png': 'Photo/png'
}

# 2. File Routing Function
def get_destination_folder(filename):
    file_name, ext = os.path.splitext(filename)
    ext = ext.lower()
    return TRACKED_EXTENSIONS.get(ext, 'Other')

# 3. Collision Resolution Function
def resolve_collision(destination_folder, filename):
    name, ext = os.path.splitext(filename)
    count = 1
    
    # Unified variable name to fix the previous NameError
    destination_path = os.path.join(destination_folder, filename)

    # If the file already exists, loop until a unique name is generated
    while os.path.exists(destination_path):
        new_filename = f"{name}_{count}{ext}"
        destination_path = os.path.join(destination_folder, new_filename)
        count += 1
        
    return destination_path

# 4. Main Sorting Engine
def organize_folder(target_directory):
    if not os.path.exists(target_directory):
        print(f"Error: The directory {target_directory} does not exist.")
        return

    for filename in os.listdir(target_directory):
        source_path = os.path.join(target_directory, filename)

        # Skip directories and hidden files (e.g. .DS_Store)
        if os.path.isdir(source_path) or filename.startswith('.'):
            continue
            
        # Clean Integration: Use your helper function to get the target path
        subfolder_name = get_destination_folder(filename)
        destination_folder = os.path.join(target_directory, subfolder_name)
        
        # Build the dynamic directory paths safely
        os.makedirs(destination_folder, exist_ok=True)
        final_destination_path = resolve_collision(destination_folder, filename)
        
        # Execute storage relocation safely
        try:
            shutil.move(source_path, final_destination_path)
            print(f"Successfully allocated: {filename} -> {subfolder_name}/")
        except PermissionError:
            print(f"Skipped: {filename} (File is currently locked or downloading).")
        except Exception as e:
            print(f"Failed to move {filename}. Error: {e}")


# 5. Live Execution Block
if __name__ == "__main__":
    # os.path.expanduser("~") automatically resolves to /Users/yourusername on macOS
    downloads_path = os.path.expanduser("~/Downloads")
    
    print("====================================")
    print(" RUNNING SMART FILE ALLOCATION SYSTEM")
    print("====================================")
    organize_folder(downloads_path)

