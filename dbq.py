#!/usr/bin/env python
from __future__ import print_function
from utils import storage, publishjson
import sqlalchemy as sa
import sys
import json

def showHelp(progname):
    print("Usage: %s [CONNECTION STRING] [SQL QUERY]" % (" ".join(progname)))

def exitSafely(progname):
    showHelp(progname)
    sys.exit(1)

def run(connection_string, sql_query):
    db = sa.create_engine(connection_string)
    conn = db.connect()
    rows = conn.execute(sql_query).fetchall()
    data = [storage(zip(row.keys(), row)) for row in rows]
    return publishjson(data)

def main(): 
    if len(sys.argv) != 3: 
        exitSafely(sys.argv[0])
    else:
        try:
            print(run(sys.argv[1], sys.argv[2]))
            sys.exit(0)
        except Exception as e:
            exitSafely(sys.argv[0])


if __name__ == '__main__':
    main()
