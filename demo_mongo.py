import pymongo
import pandas as pd
import os
import pathlib
from datetime import datetime
from bson import ObjectId


def read_json_file() -> list[str]:
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
    return list(set_hosts)

def update_document_into_mongo_db(index, document_id: ObjectId, data: dict):
    return index.find_one_and_update(
        {"_id": ObjectId(document_id)},
        {"$set": data},
        upsert=False
    )

def write_document_into_mongo_db(index, data: dict):
    return index.insert_one(data)

def main():
    DOMAIN = "localhost"
    PORT = 27017
    USERNAME = "root"
    PASSWORD = "alexandre"
    MONGO_DETAILS = f"mongodb://{DOMAIN}:{PORT}"

    client = pymongo.MongoClient(
        MONGO_DETAILS,
        username=USERNAME,
        password=PASSWORD
    )
    db = client["formation"]

    run_dict = {
        "creation_date": datetime.now(),
        "made_by": "Alexandre RASPAUD",
        "tested_hosts": []
    }
    result = write_document_into_mongo_db(
        db["runs"],
        run_dict
    )
    if getattr(result, "inserted_id"):
        run_id = result.inserted_id
    else:
        raise Exception("Run could not be created into Mongo database.")

    ids = []
    for host in read_json_file():
        result = write_document_into_mongo_db(
            db["formations"],
            {
                "host": host,
                "result": "success",
                "datetime": datetime.now(),
                "run": run_id
            }
        )
        if getattr(result, "inserted_id"):
            ids.append(result.inserted_id)

    run_dict["tested_hosts"] = ids
    result = update_document_into_mongo_db(
        db["runs"],
        run_id,
        run_dict
    )

if __name__ == "__main__":
    main()