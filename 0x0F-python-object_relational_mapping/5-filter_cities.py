#!/usr/bin/python3

"""Module for accessing hbtn_0e_0_usa db"""
import MySQLdb
import sys


def dbConnect(host, user, password, database, port):
    """Connects to db
        Args:
            host (str): The 'db host'
            user (str): The 'db user'
            password (str): The 'db user password'
            database (str): The 'db name'
            port (str): The 'db port' to connect to
        Returns: The db connection object
    """

    return MySQLdb.connect(host, user, password, db=database, port=port)


def main():
    """Entry point of the application"""
    args = sys.argv[1:]
    db_host = 'localhost'
    db_user = args[0]
    db_password = args[1]
    database = args[2]
    db_port = 3306
    search_state = args[3]
    query = """
    SELECT cities.name FROM cities
    JOIN states
    ON states.id = cities.state_id
    WHERE states.name LIKE %s
    ORDER BY cities.id ASC;
    """
    db_connection = dbConnect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=database,
        port=db_port)
    db_cursor = db_connection.cursor()
    db_cursor.execute(query, ('%' + search_state + '%',))
    rows = db_cursor.fetchall()
    for index, row in enumerate(rows):
        if index != len(rows) - 1:
            print(row[0], end=', ')
        else:
            print(row[0])


if __name__ == "__main__":
    main()
