import pandas as pd
import json
# version - 1.2.3

from pathlib import Path, os




def search_by_year(year):
    path = Path(Path.cwd(), 'Data')
    # csv files are named as 'year-orgs.csv'
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
    path = Path(Path.cwd(), 'Data')
    # csv files are named as 'year-orgs.csv'

    starting_yr = 2018
    ending_yr = 2021
    for year in range(starting_yr, ending_yr+1):
        filename = str(year)+'-orgs.csv'
        file_path = Path(path, filename)

        if os.path.exists(file_path):
            existing_files.append(Path(path, filename))

    return existing_files


def master_fn():
    

    
    choice = input("By Tech - (1) \nby year - (2)\n")

    if choice == '1':
        tech_list = input("Enter the tech array: ")
        tech_list = tech_list.split(" ")
        tech_json = ''

        for tech in tech_list:
            tech_json+=(search_by_tech(tech.lower()))

        fin_str =  (tech_json.replace("][", ","))
        return(json.loads(fin_str))


    elif choice == '2':
        year = input("Enter the year: ")
        return (search_by_year(year))


#master_fn()
print(master_fn())


# output - returns a JSONArray
