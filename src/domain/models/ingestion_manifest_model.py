from pathlib import Path
from datetime import date
from src.domain.enum.enums import IngestionStatus
from pydantic import BaseModel



class IngestionManifestModel(BaseModel):
    run_id: str
    source_file_name: str
    source_file_path: Path
    file_size: int
    dataset_type: str
    period_year: int
    period_month: int
    started_at: date
    finished_at: date
    ingestion_status: IngestionStatus
    rows_read: int
    rows_written: int