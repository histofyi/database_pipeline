from typing import Dict

import requests
import hashlib


def load_latest_data(**kwargs) -> Dict:
    table_hashes = {}
    tables = kwargs['tables']
    for table in tables:
        print (f"Loading {table}")
        url = f"https://raw.githubusercontent.com/histofyi/datatables/main/csv/{table}.csv"
        response = requests.get(url)
        with open(f"tmp/{table}.csv", 'wb') as f:
            f.write(response.content)
        print (f"{table} table is ready to combine...\n")
        table_hashes[table] = hashlib.md5(response.content).hexdigest()

    return table_hashes

    
    



