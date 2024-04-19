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

    version = '1.0.0'
    output_folder = f"versions/{version}"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    tables = ['motifs','alleles','relationships','structures']
    input_filenames = []
    for table in tables:
        input_filenames.append(f"tmp/{table}.csv")

    output_filename = "versions/1.0.0/histo.db"        


    
    create_db_from_csvs(input_filenames, output_filename)
    print(f"Created sqlite db at {output_filename}")




if __name__ == "__main__":
    create_sqlite_db()