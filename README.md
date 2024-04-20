# Database Pipeline
A pipeline to combine csv files into a database for datasette (and eventually update datasette and zenodo)

Currently working

- loading tables from GitHub
- creating a database
- writing the database to the GC bucket

Not yet working

- loading config from GC bucket
- using config from GC bucket
- using secrets provided in environment variables

Backlog

- update dataset
- update Zenodo
- write next version number to file in config folder
- write a file with the hash of the different csv files to compare versions
- only update the version and the GC bucket file if the hashes have changed
- write a log to GC log bucket