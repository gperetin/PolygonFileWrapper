import datetime as dt
from polygon_wrapper import PolygonFileWrapper

def test_get_list_objects():
    """ This test assumes that at least a full month of data will be returned """
    wrapper = PolygonFileWrapper()
    objects = wrapper.get_list_objects(verbose=True)
    assert len(objects) > 30

def test_download_from_list_objects(year,month,partition):
    """ This test will download the files and save them in a tmp directory"""
    wrapper = PolygonFileWrapper()
    df = wrapper.download_from_list_objects(year,month,partition)
    assert len(df) > 10_000    

def test_get_options_trades():
    wrapper = PolygonFileWrapper()
    df = wrapper.download_trades_parquet(dt.date(2024, 3, 8), dt.date(2024, 3, 10))
    assert len(df) > 1_000_000

if __name__ == '__main__':
    test_get_list_objects() # Pass
    test_download_from_list_objects(year=2024,month=2,partition=True) # Break because of clean_option_df when Wrapper is for STOCKS MINUTES
