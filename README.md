# Database Pipeline
A pipeline to combine csv files into a database for datasette (and eventually update datasette and zenodo)

Currently working

- loading tables from GitHub
- creating a database
- writing the database to the GC bucket
- using secrets/configuration provided in environment variables
- write current version number to file in output folder
- write a file with the hash of the different csv files to compare versions
- only update the version and the GC bucket file if the hashes have changed

Not yet working
- write a log to GC log bucket

Backlog

- update datasette on Vercel
- update Zenodo
- adding a versions table with information on included data and when it was last updated


