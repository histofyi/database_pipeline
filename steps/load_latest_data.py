import requests


def load_latest_data(**kwargs) -> None:
    tables = kwargs['tables']
    for table in tables:
        print (f"Loading {table}")
        url = f"https://raw.githubusercontent.com/histofyi/datatables/main/csv/{table}.csv"
        response = requests.get(url)
        with open(f"tmp/{table}.csv", 'wb') as f:
            f.write(response.content)
        print (f"{table} table is ready to combine...\n")
    pass

