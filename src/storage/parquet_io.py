from pyspark.sql.utils import AnalysisException
from pathlib import Path
from pyspark.sql import SparkSession


class ParquetIO:

    @staticmethod
    def read_parquet(spark: SparkSession, path: Path):
        try:
            return spark.read.parquet(str(path))
        
        except AnalysisException as e:
            print(f"[ERROR] Path does not exist or is invalid: {path}")
            raise

        except Exception as e:
            print(f"[ERROR] Unexpected error reading parquet: {e}")
            raise

    @staticmethod
    def write_parquet(df, path: Path, file_name: str, mode: str = "overwrite"):
        try:
            full_path = path / file_name
            df.write.mode(mode).parquet(str(full_path))

        except Exception as e:
            print(f"[ERROR] Error writing parquet to {path}: {e}")
            raise

    @staticmethod
    def parquet_exists(spark: SparkSession, path: Path) -> bool:
        try:
            hadoop_conf = spark._jsc.hadoopConfiguration()
            fs = spark._jvm.org.apache.hadoop.fs.FileSystem.get(hadoop_conf)
            return fs.exists(spark._jvm.org.apache.hadoop.fs.Path(str(path)))
        
        except Exception as e:
            print(f"[WARNING] Could not check path {path}: {e}")
            return False