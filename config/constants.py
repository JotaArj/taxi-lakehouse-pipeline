from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
DATA_LANDING_PATH = ROOT_DIR / "data" / "landing"
DATA_METADATA_PATH = ROOT_DIR / "data" / "metadata"
DATA_INGESTION_MANIFEST_PATH = DATA_METADATA_PATH / "ingestion_manifest.parquet"
DATA_BRONZE_PATH = ROOT_DIR / "data" / "bronze"
DATA_SILVER_PATH = ROOT_DIR / "data" / "silver"
DATA_GOLD_PATH = ROOT_DIR / "data" / "gold"
DATA_QUARENTINE_PATH = ROOT_DIR / "data" / "quarentine"
TAXI_VENDOR_ENUM = "TaxiVendor"
RATE_CODE_ENUM = "RateCode"
PAYMENT_TYPE_ENUM = "PaymentType"