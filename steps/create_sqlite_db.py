from typing import List
import os


def create_db_from_csvs(input_filenames:List[str], output_filename:str) -> None:
    if os.path.exists(output_filename):
        os.remove(output_filename)

    if len(input_filenames) > 1:
        input_filename_str = ' '.join(input_filenames)
    else:
        input_filename_str = input_filenames[0]

    csvs_to_sqllite_command = f"csvs-to-sqlite {input_filename_str} {output_filename}"

    print (csvs_to_sqllite_command)

    os.system(csvs_to_sqllite_command)

    pass


def create_sqlite_db(**kwargs) -> None:
    tables = kwargs['tables']
    output_folder = kwargs['output_folder']
    version = kwargs['version']
    
    versions_folder = f"{output_folder}/versions"
    version_folder = f"{versions_folder}/{version}"

    if not os.path.exists(versions_folder):
        os.makedirs(versions_folder)

    if not os.path.exists(version_folder):
        os.makedirs(version_folder)

    input_filenames = []
    for table in tables:
        input_filenames.append(f"tmp/{table}.csv")

    output_filename = f"{version_folder}/histo.db"        

    create_db_from_csvs(input_filenames, output_filename)


if __name__ == "__main__":
    create_sqlite_db()  