from netkeiba.race_result import get_race_result
from tqdm import tqdm
import json
import pandas as pd
import utils.request as request


def save_race_race_results():
    client = request.Client()
    race_ids = []
    with open(f"data/race_ids.json", "r") as f:
        d = json.load(f)
        race_ids = d["202202"]

    results = pd.DataFrame()

    for race_id in tqdm(race_ids):
        result = get_race_result(race_id, client)
        results = pd.concat([results, result])

    results.to_csv("data/race_result.csv", index=False)


def main():
    save_race_race_results()


if __name__ == "__main__":
    main()
