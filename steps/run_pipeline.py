from typing import Dict, List, Union

import os
import toml
import json
from datetime import datetime

from .load_latest_data import load_latest_data
from .create_sqlite_db import create_sqlite_db


def load_config(environment:str) -> Dict:
    """
    This function loads the configuration file and returns it as a dictionary.
    
    Args:
        environment (str): The environment to load the configuration for. Either 'local' or 'google_cloud'.
    
    Returns:
        Dict: The configuration file as a dictionary.

    """
    print ('Reading configuration...')
    config = toml.load('config.toml')

    if environment == 'google_cloud':
        config['paths'] = toml.load('gcp_paths.toml')
    else:
        config['paths'] = toml.load('local_paths.toml')
        
    
    print ('Config file loaded.\n')
    print (config)

    return config


def get_previous_version(output_folder:str, config:Dict) -> Union[Dict, str]:
    """
    This function reads the current version information from the current_version.json file and returns the table hashes and version number.

    Args:
        output_folder (str): The output folder where the current_version.json file is stored.
        config (Dict): The configuration dictionary.
    
    Returns:
        Dict: The table hashes and version number from the current_version.json file.
        str: The version number from the current_version.json file.
    """

    try:
        with open(f"{output_folder}/current_version.json", 'r') as f:
            current_version_info = json.load(f)
            current_table_hashes = current_version_info['table_hashes']
            current_version = current_version_info['version']
    except:
        print ('No current_version.json file found, starting from scratch...')
        current_table_hashes = {}
        current_version = config['INITIAL_VERSION']

    return current_table_hashes, current_version


def check_tables_for_changes(current_table_hashes:Dict, new_table_hashes:Dict, tables:List, current_version_number:str) -> Union[bool, str]:
    changed_data = False
    table_version = False
    data_version = False

    if len(current_table_hashes) != len(new_table_hashes):
        changed_data = True
        table_version = True

    for table in tables:
        if current_table_hashes.get(table) != new_table_hashes.get(table):
            changed_data = True
            if not table_version:
                data_version = True
            else:
                data_version = False
            break

    new_version_number = generate_version_number(current_version_number, table_version, data_version)

    return changed_data, new_version_number


def generate_version_number(current_version_number:str, table_version:bool, data_version:bool) -> str:
    previous_version = current_version_number.split('.')

    if table_version:
        new_version = f"{int(previous_version[0])}.{int(previous_version[1])}.0"
    elif data_version:
        new_version = f"{previous_version[0]}.{previous_version[1]}.{int(previous_version[2])+1}"
    else:
        new_version = None
    return new_version


def run_pipeline():
    print('Hello from the database pipeline!\n')

    config = load_config(os.environ.get('ENVIRONMENT', 'local'))

    output_folder = config['paths']['OUTPUT_PATH']
    tables = config['TABLES']

    if config:
        
        print ('\nLoading latest data\n')

        current_table_hashes, current_version_number = get_previous_version(output_folder, config)
        
        print ('\nChecking for changes in data...\n')
        new_table_hashes = load_latest_data(tables=tables)

        changed_data, new_version_number = check_tables_for_changes(current_table_hashes, new_table_hashes, tables, current_version_number)

        if changed_data:
            print ('Data has changed, creating SQLite database\n')

            print (f"\nCreating SQLite database for version {new_version_number}\n")

            create_sqlite_db(tables=tables, output_folder=output_folder, version=new_version_number)

            print (f"Listing files in versions/{new_version_number}\n")
            ls_command = f"ls -l {output_folder}/versions/{new_version_number}/*"
            os.system(ls_command)

            print (f"\nUpdating current_version.json\n")

            new_version_info = {'version': new_version_number, 'table_hashes': new_table_hashes, 'created_at': datetime.now().isoformat()}
            print (new_version_info)

            print (f"Writing new version information to {output_folder}/current_version.json\n")

            with open(f"{output_folder}/current_version.json", 'w') as f:
                json.dump(new_version_info, f)

        else:
            print ('Data has not changed, no need to create SQLite database\n')
        
        print ("Done!")
    
    else:

        print ('Cannot load configuration, exiting...')

