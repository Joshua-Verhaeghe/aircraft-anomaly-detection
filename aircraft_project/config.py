import os 

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA = os.path.join(PROJECT_ROOT, "data", "raw")
PROCESSED_DATA = os.path.join(PROJECT_ROOT, "data", "processed")
NOTEBOOKS = os.path.join(PROJECT_ROOT, "notebooks")


def get_filepath(filename: str, folder: str = "raw") -> str:

    if folder == "raw":
        base_folder = RAW_DATA
    elif folder == "processed":
        base_folder = PROCESSED_DATA
    elif folder == "notebooks":
        base_folder = NOTEBOOKS
    else:
        base_folder = os.path.join(PROJECT_ROOT, folder)

    return os.path.join(base_folder, filename)
