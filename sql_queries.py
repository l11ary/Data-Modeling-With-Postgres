# DROP TABLES

songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES

songplay_table_create = ("""create table if not exists songplays  
                            (songplay_id SERIAL NOT NULL,
                             start_time bigint NOT NULL REFERENCES time, 
                             user_id integer  NOT NULL REFERENCES users, 
                             level text, 
                             song_id text  REFERENCES songs, 
                             artist_id text   REFERENCES artists, 
                             session_id integer , 
                             location text, 
                             user_agent text,
                             PRIMARY KEY (songplay_id))
""")

user_table_create = ("""create table if not exists users
                        (user_id integer NOT NULL,
                         first_name text, 
                         last_name text, 
                         gender text, 
                         level text,
                         PRIMARY KEY (user_id) )
""")

song_table_create = ("""create table if not exists songs 
                        (song_id text NOT NULL, 
                         title text, 
                         artist_id text, 
                         year numeric, 
                         duration numeric,
                         PRIMARY KEY (song_id))
""")

artist_table_create = ("""create table if not exists artists 
                          (artist_id text NOT NULL, 
                           name text, 
                           location text, 
                           latitude text, 
                           longitude text,
                           PRIMARY KEY (artist_id))
""")

time_table_create = ("""create table if not exists time 
                        (start_time bigint NOT NULL, 
                         hour integer, 
                         day integer, 
                         week integer, 
                         month integer, 
                         year integer, 
                         weekday integer,
                         PRIMARY KEY (start_time))
""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays 
                        (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                         values  (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s) 
                         on conflict (songplay_id)
                         do nothing
""")

user_table_insert = ("""insert into users 
                        (user_id, first_name, last_name, gender, level)
                         values  (%s, %s, %s, %s, %s)
                         on conflict (user_id)
                         do update
                         set level = excluded.level
""")

song_table_insert = ("""insert into songs 
                        (song_id, title, artist_id, year, duration)
                        values  (%s, %s, %s, %s, %s)
  
""")

artist_table_insert = ("""insert into artists 
                         (artist_id, name, location, latitude, longitude) 
                          values  (%s, %s, %s, %s, %s)
                          on conflict (artist_id)
                          do nothing
""")


time_table_insert = ("""insert into time 
                        (start_time, hour, day, week, month, year, weekday)
                        values  (%s, %s, %s, %s, %s, %s, %s)
                        on conflict (start_time)
                        do nothing
""")

# FIND SONGS

song_select = ("""select songs.song_id, songs.artist_id 
                  from songs join artists 
                  on songs.artist_id = artists.artist_id
                  where songs.title=%s and artists.name=%s and duration=%s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [ user_table_drop, song_table_drop, artist_table_drop, time_table_drop, songplay_table_drop]