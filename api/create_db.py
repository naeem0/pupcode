import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
 
if __name__ == '__main__':
    create_connection("/home/ec2-user/api/test.db")
    sql_create_table = """ CREATE TABLE IF NOT EXISTS data (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        dob text NOT NULL
                                    ); """
    conn = create_connection("/home/ec2-user/api/test.db")
    if conn is not None:
      # create projects table
        create_table(conn, sql_create_table)
    else:
        print("Error! cannot create the database connection.")
