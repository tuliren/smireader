import io

import pytest

from smireader.smireader import Address, SmiFile, Timestamp


def test_address_initialization():
    """Test Address class initialization with empty address."""
    mock_file = io.BytesIO(b'\x00')
    address = Address(mock_file, smsc=True)
    assert address.bytes == 1


def test_timestamp_initialization_with_zeros():
    """Test Timestamp class initialization with zeros."""
    mock_file = io.BytesIO(b'\x00' * 7)
    timestamp = Timestamp(mock_file)
    assert timestamp.bytes == 7


@pytest.mark.skip(reason="Requires actual SMI file")
def test_smi_file_parsing():
    """Test parsing a sample SMI file."""
    pass


if __name__ == "__main__":
    pytest.main()
