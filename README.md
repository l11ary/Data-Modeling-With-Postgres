# Problem
 Sparkify has so much data collected on songs and user activity on their music app and wants to perform analysis on their users and the songs they are playing. Currently, their data is stored in json format in two set of files, `song_data` and `log_data`. They current architecture does not allow them to do the analysis effectively.
 
# Solution
 Sparkify needs a postgress database with the star schema and ETL pipeline. Since the analysis need to be optimized to query song play data, star schema should have songplay table as a fact table and other key identities (users, songs, artists, time) as dimension tables. 
 
Visual demonstrion of the final tables can be found below:
https://docs.google.com/spreadsheets/d/1v3V8NRhvv5NmlKSPx4x059n-qb6E-V3DFeCnqVI9Mdo/edit?usp=sharing
 
 
Next step is to populate these tables with their json data. Songs and artists tables are populated using `song_data`; and songplay, users, and time are populated using `log_data`. songplay table has artist_id and song_id columns to make the artist and song info readily available through simple joins. Primary keys to all tables have been identified  as well as foreign keys on the fact tables. In order to avoid null values in the tables, `not null` has been specified on appropriate columns.
 
There has been some challenges with the duplication in the data. For example, Users table had duplicated user_id, artists table had duplicated artist_id, or start_time had duplicate values in the time table. These issues were resolved by adding conflict statement to the insert queries and not allowing duplicated data to be added or modify the existing row. 



# Run
To create the tables, run `python3 create_tables.py`. This scripts makes sure to drop the tables before attempting to create ones.

To populate the tables, run `python3 etl.py`. 

Example of querying the songplay data for users in washington:
 `select * from songplays where location like '%Washington%'`
 

