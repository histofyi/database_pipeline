import os
import toml

from steps.create_sqlite_db import create_sqlite_db
from steps.load_latest_data import load_latest_data

def main():
    print('Hello from the database pipeline!\n')

    print ('Reading config file\n')
    try:
        with open('/config/config.toml') as f:
            config = toml.load(f)
            print ('Config file read successfully\n')
            print (config)
    except:
        print ('Error reading config file\n')

    tables = ['motifs','alleles','relationships','structures']
    output_folder = '/outputs'

    print ('Loading latest data\n')
    load_latest_data(tables=tables)

    print ('\nCreating SQLite database\n')
    create_sqlite_db(tables=tables, output_folder=output_folder)

    print ('Listing files in versions/1.0.0\n')
    ls_command = f"ls -l {output_folder}/versions/1.0.0/*"

    os.system(ls_command)

    print ("Done!")

if __name__ == "__main__":
    main()