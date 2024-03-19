import datetime as dt
from polygon_wrapper import PolygonEndpoint, PolygonFileWrapper, PolygonMarket


def test_get_list_objects():
    """ This test will download the files and save them in a tmp directory"""
    wrapper = PolygonFileWrapper()
    list_objects = wrapper.get_list_objects(PolygonMarket.OPTIONS, PolygonEndpoint.TRADES, 2024, 2)
    assert len(list_objects) > 10


def test_download_and_save_options():
    wrapper = PolygonFileWrapper()
    wrapper.download_and_save_options(
        PolygonEndpoint.TRADES,
        dt.date(2024, 2, 1),
        dt.date(2024, 2, 4),
        dir="options"
    )


def test_download_options_trades_for_date_range():
    """ This test will download the history between the two dates in memory"""
    wrapper = PolygonFileWrapper()
    df = wrapper.download_options(
        PolygonEndpoint.TRADES, dt.date(2024, 1, 30), dt.date(2024, 1, 31)
    )
    assert len(df) > 1_000_000


def test_download_options_minute_bars_for_date_range():
    wrapper = PolygonFileWrapper()
    df = wrapper.download_options(
        PolygonEndpoint.MINUTES,
        dt.date(2024, 1, 30),
        dt.date(2024, 1, 31)
    )
    assert len(df) > 1_000_000


def test_download_options_daily_bars_for_date_range():
    wrapper = PolygonFileWrapper()
    df = wrapper.download_options(
        PolygonEndpoint.DAY,
        dt.date(2024, 1, 30),
        dt.date(2024, 1, 31)
    )
    assert len(df) > 1_000


def test_download_stock_trades():
    wrapper = PolygonFileWrapper()
    df = wrapper.download_stocks(
        PolygonEndpoint.TRADES,
        dt.date(2024, 1, 30),
        dt.date(2024, 1, 31)
    )
    assert len(df) > 100_000


def test_download_stock_minute_bars():
    wrapper = PolygonFileWrapper()
    df = wrapper.download_stocks(
        PolygonEndpoint.MINUTES,
        dt.date(2024, 1, 30),
        dt.date(2024, 1, 31)
    )
    assert len(df) > 100_000


def test_download_stock_daily_bars():
    wrapper = PolygonFileWrapper()
    df = wrapper.download_stocks(
        PolygonEndpoint.DAY,
        dt.date(2024, 1, 30),
        dt.date(2024, 1, 31)
    )
    assert len(df) > 10_000
