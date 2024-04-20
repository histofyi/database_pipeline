import os

from steps.create_sqlite_db import create_sqlite_db


def main():
    print("Hello World!")

    create_sqlite_db()

    ls_command = 'ls -l versions/1.0.0/*'

    os.system(ls_command)

    print ("Done!")

if __name__ == "__main__":
    main()