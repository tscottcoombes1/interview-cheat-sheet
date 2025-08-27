import pyarrow as pa

from extract_play.pyarrow_playground import read_csv

def test_read_csv(csv_file):
    table = read_csv(csv_file)
    assert table.num_rows == 5
    assert table.num_columns == 7
    assert table.column_names == ["boolean_col", "string_col", "date_col", "timestamp_col", "int_col", "decimal_col", "json_col"]
    assert table.schema == pa.schema([
        pa.field("boolean_col", pa.bool_()),
        pa.field("string_col", pa.string()),
        pa.field("date_col", pa.date32()),
        pa.field("timestamp_col", pa.timestamp('s', tz='UTC')),
        pa.field("int_col", pa.int64()),
        pa.field("decimal_col", pa.float64()),
        pa.field("json_col", pa.string()),
    ])
