import pytest
from pathlib import Path
import testcontainers.postgres

@pytest.fixture
def data_dir():
    return Path(__file__).parent / "data"

@pytest.fixture
def csv_file(data_dir):
    return data_dir / "generic_rfc4180.csv"

@pytest.fixture
def postgres_connection_url():
    with testcontainers.postgres.PostgresContainer(driver=None) as postgres:
        yield postgres.get_connection_url()
