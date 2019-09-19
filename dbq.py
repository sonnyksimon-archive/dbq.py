#!/usr/bin/env python
from __future__ import print_function
from utils import storage, publishjson
import sqlalchemy as sa
import sys
import json

def showHelp(progname):
    print("Usage: %s [CONNECTION STRING] [SQL QUERY]" % (" ".join(progname)))

def run(connection_string, sql_query):
    db = sa.create_engine(connection_string)
    conn = db.connect()
    rows = conn.execute(sql_query).fetchall()
    data = [storage(zip(row.keys(), row)) for row in rows]
    print(publishjson(data))

def main(): 
    if len(sys.argv) != 3: 
        showHelp(sys.argv[0:1])
        sys.exit(1)
    else:
        try:
            run(sys.argv[1], sys.argv[2])
            sys.exit(0)
        except Exception as e:
            print(str(e))
            sys.exit(1)


if __name__ == '__main__':
    main()
