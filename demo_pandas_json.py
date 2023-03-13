import pandas as pd
import os
import pathlib


def main():
    PATH_TO_JSON = os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        "statics",
        "ntt.json"
    )
    if not os.path.exists(PATH_TO_JSON):
        raise Exception(f"Could not find file ntt.json under {PATH_TO_JSON}")

    df = pd.read_json(PATH_TO_JSON)
    df_hits = df["hits"]["hits"]
    # print(df_hits)
    hosts = []
    for hit in df_hits:
        hosts.append(hit["_source"]["host"]["name"])
    set_hosts = set(hosts)
    


if __name__ == '__main__':
    main()