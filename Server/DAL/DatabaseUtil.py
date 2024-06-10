import pymysql
from pymysql.cursors import DictCursor

class DatabaseUtil:
    _connection = None
    _host = "localhost"
    _port = 3306
    _user = "root"
    _password = ""
    _db = "lexi"

    @classmethod
    def get_connection(cls):
        if cls._connection is None or not cls._connection.open:
            try:
                cls._connection = pymysql.connect(
                    host=cls._host,
                    port=cls._port,
                    user=cls._user,
                    password=cls._password,
                    database=cls._db,
                    cursorclass=DictCursor
                )
                print(f"\nNew connection to database: {cls._connection}")
            except pymysql.MySQLError as e:
                print(f"Error connecting to the database: {e}")
                cls._connection = None
        return cls._connection

    @classmethod
    def close_connection(cls):
        if cls._connection and cls._connection.open:
            cls._connection.close()
            cls._connection = None