#!/usr/bin/env python3
from __future__ import print_function
from utils import storage, publishjson
import sqlalchemy as sa
import sys
import json
import click

def run(connection_string, sql_query):
    db = sa.create_engine(connection_string)
    conn = db.connect()
    rows = conn.execute(sql_query).fetchall()
    data = [storage(zip(row.keys(), row)) for row in rows]
    return publishjson(data)

@click.command()
@click.option('--conn', help='Connection string.')
@click.option('--file', type=click.File('rb'), help='SQL query file.')
@click.option('--sql', help='Raw query.')
def cli(conn, file, sql):
    """
    This little Python script runs SQL statements on databases from the command-line.
    
    You must pass in a valid connection string.
    
    The raw query overrides the file query.
    """
    if conn is not None and (file is not None or sql is not None):
        if sql:
            query = sql
        elif file:
            query = file.read().decode('utf-8')
        click.echo(run(conn, query))
    else:
        click.echo("You missed an argument, I can't handle invalid input. Try using --help")

if __name__ == '__main__':
    cli()
