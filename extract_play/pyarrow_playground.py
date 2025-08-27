import pyarrow as pa
import pyarrow.csv as csv
from pathlib import Path

def read_csv(path: Path) -> pa.Table:
    table = csv.read_csv(path)
    return table
