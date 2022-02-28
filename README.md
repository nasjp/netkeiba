[![ci](https://github.com/nasjp/netkeiba/actions/workflows/ci.yml/badge.svg)](https://github.com/nasjp/netkeiba/actions/workflows/ci.yml)

# netkeiba

- [競馬データベース - netkeiba.com](https://db.netkeiba.com/race/201006020101/)からレース結果をスクレイピングする Python スクリプトです。
- <https://db.netkeiba.com/race/{race_id}/>の`race_id`ごとにレース結果をスクレイピングし、保存します。
- 結果の保存スクリプトは[main.py](main.py)です。
- 保存した結果野サンプルは[race_result.csv](data/race_result.csv)です。216 件分のスクリプトで取得したデータを保存しています。
- それぞれのレース結果を取得する関数は[race_result.py](netkeiba/race_result.py)です。
- それぞれのレース結果を取得する関数のテストは[test_race_result.py](tests/test_netkeiba/test_race_result.py)です。

## setup

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## run

```sh
source .venv/bin/activate
python main.py
```

## dependencies

- Python 3.10.2
- pandas
- requests
- BeautifulSoup
