import requests
import zipfile
import io

def gdrive_download(url:str, folder:str) -> bool:
    """
    Downloads a ZIP file from a Google Drive URL and extracts its contents into a specified folder.

    Args:
        url (str): The URL of the ZIP file to download.
        folder (str): The path to the folder where the contents of the ZIP file will be extracted.

    Returns:
        bool: True if the ZIP file was extracted successfully, False otherwise.

    Raises:
        Exception: If there is an error during the download or extraction process.

    Note:
        This function skips SSL certificate validations by setting verify=False in the requests.get method.

    Example:
        gdrive_download("https://drive.google.com/file/d/1234567890abcdefg/view?usp=sharing", "/path/to/extract/folder")
    """
    response = requests.get(url, verify=False)  # verify=False is used to skip SSL certificate validations
    zip_data = response.content
    try:
        # Open zip file
        with zipfile.ZipFile(io.BytesIO(zip_data), 'r') as zip_ref:
            # Extract ZIP content into files folder
            zip_ref.extractall(folder)
        print('ZIP file extracted successfully!')
        return True
    except Exception as e:
        print(e)
        return False  # Return False if extraction fails