"""
conftest.py

This is a file that will automatically be read by pytest to
find fixtures, etc.

It's a good place to put stuff that multiple test files need.
"""
from pathlib import Path

import pytest
from mailroom.model import DonorDB
from mailroom.sample_data import sample_donor_data

test_output_path = Path(__file__).parent / "output"

# make sure the output path exists
test_output_path.mkdir(exist_ok=True)


@pytest.fixture
def sample_db():
    """a clean DonorDB for tests"""
    return DonorDB(sample_donor_data(),
                   db_file=test_output_path / "db1.json_save")


@pytest.fixture
def sample_db2():
    """so we can have two separate ones if needed"""
    return DonorDB(sample_donor_data(),
                   db_file=test_output_path / "db2.json_save")
