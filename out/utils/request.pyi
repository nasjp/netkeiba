import pandas as pd
import requests

class Client:
    def __init__(self, cacheResponse: dict[str, requests.Response] = ..., cacheDataFrames: dict[str, list[pd.DataFrame]] = ...) -> None: ...
    def get_response(self, url: str) -> requests.Response: ...
    def get_dataframes(self, url: str) -> list[pd.DataFrame]: ...
