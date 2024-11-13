import zipfile
import os
import gzip

def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                absolute_path = os.path.join(root, file)
                relative_path = os.path.relpath(absolute_path, folder_path)
                zipf.write(absolute_path, relative_path)

# Example usage
# zip_folder(r"C:\Users\ASUS\Downloads\Telegram Desktop\mini-s6\mini-s6\temp1", "output.zip")



def compress_file(input_file_path, output_file_path):
    """
    Compresses a file using gzip.

    Args:
        input_file_path (str): The path to the input file.
        output_file_path (str): The path to save the compressed file.

    Returns:
        None
    """
    try:
        with open(input_file_path, 'rb') as f_in:
            with gzip.open(output_file_path, 'wb') as f_out:
                f_out.writelines(f_in)
        return True 
    except Exception as e:
        print(f"Error: {e}")
        return False