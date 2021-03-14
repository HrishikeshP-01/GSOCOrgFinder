import pandas as pd
# version - 1.2.3

from pathlib import Path, os

path = Path(Path.cwd(), 'Data')
# csv files are named as 'year-orgs.csv'

starting_yr = 2018
ending_yr = 2021


def search_by_year(year):
    filename = str(year)+'-orgs.csv'
    if os.path.exists(Path(path, filename)):
        print("File exist")
        df = pd.read_csv(Path(path, filename), index_col=0, header=0)

        return(df.to_json(orient='records'))
    else:
        return("404")


def search_by_tech(tech):
    files = loop_thru_files()
    techwise_df = pd.DataFrame()

    for file in files:
        df = pd.read_csv(file, index_col=0, header=0)
        row_df = pd.DataFrame()
        row_df = df[df['Technologies'].str.contains(tech, regex=False)]
        techwise_df = techwise_df.append(row_df)

    return(techwise_df.to_json(orient='records'))
    # function to return the jsonArray


def loop_thru_files():
    existing_files = []

    for year in range(starting_yr, ending_yr+1):
        filename = str(year)+'-orgs.csv'
        file_path = Path(path, filename)

        if os.path.exists(file_path):
            existing_files.append(Path(path, filename))

    return existing_files

# output - returns a JSONArray