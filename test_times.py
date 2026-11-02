from times import compute_overlap_time, time_range

import pytest


def test_time_range_backwards():
    with pytest.raises(ValueError, match="end_time must be greater than start_time"):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")

def test_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected


def test_case2():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 09:30:00", "2010-01-12 09:59:00")
    expected = []
    assert compute_overlap_time(large, short) == expected

def test_case3():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 11:00:00", 3)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:40:00"), ("2010-01-12 10:40:00", "2010-01-12 10:50:00"),
                ("2010-01-12 10:50:00","2010-01-12 11:00:00")]
    assert compute_overlap_time(large, short) == expected


def test_case4():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")
    expected = []
    assert compute_overlap_time(large, short) == expected