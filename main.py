import os

from steps.create_sqlite_db import create_sqlite_db
from steps.load_latest_data import load_latest_data

def main():
    print('Hello from the database pipeline!\n')

    tables = ['motifs','alleles','relationships','structures']

    print ('Loading latest data\n')
    load_latest_data(tables=tables)

    print ('\nCreating SQLite database\n')
    create_sqlite_db(tables=tables)

    print ('Listing files in versions/1.0.0\n')
    ls_command = 'ls -l versions/1.0.0/*'

    os.system(ls_command)

    print ("Done!")

if __name__ == "__main__":
    main()