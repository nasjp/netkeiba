import utils.request as request
import requests
import pandas as pd


def test_request_get_response_use_cache():
    url = "http://example.com"
    cacheResponse = requests.Response()
    c = request.Client(cacheResponse={url: cacheResponse})
    resp = c.get_response(url)
    assert resp == cacheResponse


def test_request_get_response_without_cache():
    url = "http://example.com"
    c = request.Client()
    resp = c.get_response(url)
    assert resp != requests.Response()


def test_request_get_dataframes_use_cache():
    url = "https://developer.mozilla.org/ja/docs/Web/HTML/Element/table"
    cacheDataFrames = list[pd.DataFrame]
    c = request.Client(cacheDataFrames={url: cacheDataFrames})
    resp = c.get_dataframes(url)
    assert resp == cacheDataFrames


def test_request_get_without_cache():
    url = "https://developer.mozilla.org/ja/docs/Web/HTML/Element/table"
    c = request.Client()
    resp = c.get_dataframes(url)
    assert resp != list[pd.DataFrame]()
