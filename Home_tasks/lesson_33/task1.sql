-- Create a table of your choice inside the sample SQLite database,
-- rename it, and add a new column. Insert a couple rows inside your table.
-- Also, perform UPDATE and DELETE statements on inserted rows.


import sqlite3 as sq

-- creating a new table
with sq.connect("less33.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS les3 (
                name TEXT,
                old INTEGER,
                score INTEGER DEFAULT 0,
                games INTEGER
                )""")
-- rename table
ALTER TABLE les3 RENAME TO les33

-- adding a column
ALTER TABLE les33 ADD sex TEXT

-- inserting a few rows
INSERT INTO les33 VALUES ('Anton', 37, 1000, 1), ('Lesya', 33, 2000, 2), ('Alex', 38, 1500, 2), ('Jane', 40, 3000, 3)

-- UPDATE
UPDATE les33 SET score = 1500 WHERE rowid = 1

-- DELETE
DELETE FROM les33 WHERE rowid IN (1, 4)