import pytest

from app import hours_saved


def test_invoice_example():
    # 10,000 invoices x 6 min = 1,000 hours; 80% automatable = 800 hours
    assert hours_saved(10000, 6, 80) == 800


def test_rejects_bad_percentage():
    with pytest.raises(ValueError):
        hours_saved(100, 5, 150)
