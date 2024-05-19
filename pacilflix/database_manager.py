import psycopg2
import psycopg2.extras
import psycopg2.pool
import environ
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)

env = environ.Env()
environ.Env.read_env('.env')

class DatabaseManager:
    _connection_pool = None

    @staticmethod
    def initialize_connection_pool(minconn=1, maxconn=10):
        if DatabaseManager._connection_pool is None:
            DatabaseManager._connection_pool = psycopg2.pool.SimpleConnectionPool(
                minconn,
                maxconn,
                user=env('DB_USER'),
                password=env('DB_PASS'),
                host=env('DB_HOST'),
                port=env('DB_PORT'),
                dbname=env('DB_NAME')
            )
            logging.info("Connection pool created")

    @staticmethod
    def get_connection():
        if DatabaseManager._connection_pool is None:
            DatabaseManager.initialize_connection_pool()
        try:
            return DatabaseManager._connection_pool.getconn()
        except Exception as e:
            logging.error(f"Error getting connection: {e}")
            raise

    @staticmethod
    def get_cursor():
        conn = DatabaseManager.get_connection()
        return conn.cursor()

    @staticmethod
    def get_dict_cursor():
        conn = DatabaseManager.get_connection()
        return conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    @staticmethod
    def commit():
        conn = DatabaseManager.get_connection()
        conn.commit()
        DatabaseManager._connection_pool.putconn(conn)

    @staticmethod
    def rollback():
        conn = DatabaseManager.get_connection()
        conn.rollback()
        DatabaseManager._connection_pool.putconn(conn)

    @staticmethod
    def close_all_connections():
        if DatabaseManager._connection_pool:
            DatabaseManager._connection_pool.closeall()
            logging.info("All database connections closed")
