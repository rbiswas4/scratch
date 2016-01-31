
# SQLITE

- Open a file: Here we will use the ipython history file. This is found in `.ipython/profile_default` and the file is called `history.sqlite`  This is done by
```
$sqlite3
$.open filename

Example:
$sqlite3
sqlite> .open history.sqlite
```

- Find Tables in the file: If the file has been opened using `.open`
```
sqlite> .tables
Example
sqlite> .tables
history         output_history  sessions
```
- Find the columns: This is done by querying sqlite_master which displays all tables and their columns along with type. It also gives you the 
```
Example:
sqlite> SELECT * FROM sqlite_master;
table|sessions|sessions|2|CREATE TABLE sessions (session integer
                        primary key autoincrement, start timestamp,
                        end timestamp, num_cmds integer, remark text)
table|sqlite_sequence|sqlite_sequence|3|CREATE TABLE sqlite_sequence(name,seq)
table|history|history|4|CREATE TABLE history
                (session integer, line integer, source text, source_raw text,
                PRIMARY KEY (session, line))
index|sqlite_autoindex_history_1|history|5|
table|output_history|output_history|6|CREATE TABLE output_history
                        (session integer, line integer, output text,
                        PRIMARY KEY (session, line))
index|sqlite_autoindex_output_history_1|output_history|7|
```
- Obtain the records from the column which contain a string like import
```
sqlite> SELECT * FROM history WHERE source LIKE '%import%' LIMIT 10;
2|1|import numpy as np|import numpy as np
2|13|import matplotlib.pyplot as plt|import matplotlib.pyplot as plt
3|1|import sys|import sys
4|1|import sncosmo|import sncosmo
5|1|import sncosmo
#Check version and source
print "version is ", sncosmo.__version__
print "PATH to file is ",sncosmo.__file__
import timeit|import sncosmo
#Check version and source
print "version is ", sncosmo.__version__
print "PATH to file is ",sncosmo.__file__
import timeit
7|1|import root as ROOT|import root as ROOT
10|1|import ROOT|import ROOT
10|2|import ROOT as root|import ROOT as root
11|1|import ROOT as root|import ROOT as root
13|1|import ROOT|import ROOT
```
