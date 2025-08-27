import connectorx as cx
import pyarrow as pa
import polars as pl
import sqlalchemy as sa
from extract_play.polars_playground import read_csv
from extract_play.connectorx_playground import read_db_to_arrow

def test_read_db_to_arrow(postgres_connection_url, csv_file):
    # GIVEN
    engine = sa.create_engine(postgres_connection_url)
    with engine.begin() as conn:
        read_csv(csv_file).write_database(table_name="test_table", connection=conn)

    # WHEN
    table = read_db_to_arrow(postgres_connection_url, "SELECT * FROM test_table")

    # THEN
    assert table.num_rows == 5
    assert table.num_columns == 7
    assert table.column_names == ["boolean_col", "string_col", "date_col", "timestamp_col", "int_col", "decimal_col", "json_col"]
    assert table.schema == pa.schema([
        pa.field("boolean_col", pa.bool_()),
        pa.field("string_col", pa.string()),
        pa.field("date_col", pa.date32()),
        pa.field("timestamp_col", pa.timestamp('us', tz='+00:00')),
        pa.field("int_col", pa.int64()),
        pa.field("decimal_col", pa.float64()),
        pa.field("json_col", pa.string()),
    ])
