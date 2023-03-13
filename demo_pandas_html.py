import pandas as pd
import os
import pathlib


def open_html_file_with_pandas(filename: str):
    PATH_TO_HTML = os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        "statics",
        filename
    )
    if not os.path.exists(PATH_TO_HTML):
        raise Exception(f"Could not find file ntt.json under {PATH_TO_HTML}")
    df = pd.read_html(PATH_TO_HTML)
    return df


def main():
    for df in open_html_file_with_pandas("prognosis.html"):
        if "Node" in df.columns and "Status" in df.columns and "Customer" in df.columns:
            items = pd.Series(df.Status.values, index=df.Customer).to_dict()
            for item in items.items():
                if item[1] != "Connected":
                    print(f"{item[0]} n'est pas connecte !")

if __name__ == "__main__":
    main()
