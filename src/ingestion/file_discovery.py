from pathlib import Path
from config.constants import DATA_LANDING_PATH, DATA_INGESTION_MANIFEST_PATH
import sqlite3

class DiscoverFile:
    def list_landing_files() -> list[Path]:
        files = [f for f in DATA_LANDING_PATH.iterdir() if f.is_file()]
        conn = sqlite3.connect(str(DATA_INGESTION_MANIFEST_PATH))

    def extract_file_info(path):
        pass
    
