import os
import aspose.words as aw 

def docx_to_txt(folder_path):

    """
    Converts .docx files in the specified folder to plain text files.

    Args:
        folder_path (str): The path to the folder containing the .docx files.

    Returns:
        None: The function prints the conversion status for each file.
    """


    # Generate a list of all .docx files present in the folder
    docx_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.docx')]

    # Converting each .docx file to .txt using the aspose library
    for docx_file in docx_files:
        docx_file_path = os.path.join(folder_path, docx_file)
        txt_file_path = os.path.splitext(docx_file_path)[0] + '.txt'

        try:
            doc = aw.Document(docx_file_path)
            doc.save(txt_file_path)
            print(f"Converted {docx_file} to {os.path.basename(txt_file_path)}")
            
        except Exception as e:
            print(f"Error converting {docx_file}: {e}")

