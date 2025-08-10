import os


def get_files_info(working_directory, directory="."):
    try:
        result = ""
        full_path = os.path.join(working_directory, directory)
        abs_path = os.path.abspath(full_path)

        if not os.path.isdir(abs_path):
            result += f"\tError: '{directory}' is not a directory"
            return result
        
        if not abs_path.startswith(os.path.abspath(working_directory)):
            result += f"\tError: Cannot list '{directory}' as it is outside the permitted working directory"
            return result
        
        for i, file in enumerate(sorted(os.listdir(abs_path))):
            file_path = os.path.join(abs_path, file)
            file_info = f"\n - {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}"
            result += file_info
        
        return result

    except Exception as e:
        return f"Error: {e}"
