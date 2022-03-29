"""
Unit tests for :py:mod:`trajcalc.ballparks`.
"""


from trajcalc import ballparks


def test_current_ballparks():
    """
    Unit tests for :py:func:`trajcalc.ballparks.current_ballparks`.
    """
    _index = list(range(30))
    _columns = [
        "Stadium", "Stadium_URL", "Team", "Team_URL", "City",
        "City_URL", "Capacity", "LF", "LC", "CF",
        "RC", "RF", "BS"
    ]
    df = ballparks.current_ballparks()

    assert len(df.index) == 30, df.index
    assert len(df.columns) == 13, df.columns

    assert list(df.index) == _index
    assert list(df.columns) == _columns
