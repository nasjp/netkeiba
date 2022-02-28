from bs4 import BeautifulSoup
import utils.request as request
import pandas as pd
import re
import requests

__NET_KEIBA_ROOT = "https://db.netkeiba.com"


def get_race_result(race_id: str, client: request.Client) -> pd.DataFrame:
    result = __get_race_result(race_id, client)

    result["race_id"] = race_id
    result["horse_id"] = __select_horse_ids(race_id, client)
    result["jockey_id"] = __select_jockey_ids(race_id, client)
    result["trainer_id"] = __select_trainer_ids(race_id, client)
    result["owner_id"] = __select_owner_ids(race_id, client)

    return result


def __get_race_result(race_id: str, client: request.Client) -> pd.DataFrame:
    page = __get_race_page(race_id, client)

    return client.get_dataframes(page.text)[0]


def __select_horse_ids(race_id: str, client: request.Client) -> pd.Series:
    return __select_ids(race_id, client, "horse")


def __select_jockey_ids(race_id: str, client: request.Client) -> pd.Series:
    return __select_ids(race_id, client, "jockey")


def __select_trainer_ids(race_id: str, client: request.Client) -> pd.Series:
    return __select_ids(race_id, client, "trainer")


def __select_owner_ids(race_id: str, client: request.Client) -> pd.Series:
    return __select_ids(race_id, client, "owner")


def __select_ids(race_id: str, client: request.Client, target: str) -> pd.Series:
    page = __get_race_page(race_id, client)

    soup = BeautifulSoup(page.text, "html.parser")

    a_tags = soup.find("table", attrs={"summary": "レース結果"}).find_all(
        "a", attrs={"href": re.compile(f"^/{target}")}
    )

    return pd.Series([re.findall(r"\d+", v["href"])[0] for v in a_tags])


def __get_race_page(race_id: str, client: request.Client) -> requests.Response:
    page = client.get_response(__race_page_url(race_id))
    page.encoding = "EUC-JP"

    return page


def __race_page_url(race_id: str) -> str:
    return f"{__NET_KEIBA_ROOT}/race/{race_id}"


