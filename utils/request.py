import requests
import pandas as pd


class Client:
    def __init__(
        self,
        cacheResponse: dict[str, requests.Response] = {},
        cacheDataFrames: dict[str, list[pd.DataFrame]] = {},
    ) -> None:
        self.__cacheResponse = cacheResponse
        self.__cacheDataFrames = cacheDataFrames

    def get_response(self, url: str) -> requests.Response:
        resp = self.__cacheResponse.get(url)
        if resp is None:
            resp = requests.get(url)
            self.__cacheResponse[url] = resp
        return resp

    def get_dataframes(self, url: str) -> list[pd.DataFrame]:
        dataframes = self.__cacheDataFrames.get(url)
        if dataframes is None:
            dataframes = pd.read_html(url)
            self.__cacheDataFrames[url] = dataframes
        return dataframes
