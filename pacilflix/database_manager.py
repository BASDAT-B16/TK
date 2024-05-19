import psycopg2
import psycopg2.extras
import environ

# Load environment variables
env = environ.Env()
environ.Env.read_env('.env')

class DatabaseManager:
    connection = None

    @staticmethod
    def connect():
        DatabaseManager.connection = psycopg2.connect(
            user=env('DB_USER'),
            password=env('DB_PASS'),
            host=env('DB_HOST'),
            port=env('DB_PORT'),
            dbname=env('DB_NAME')
        )

    @staticmethod
    def get_connection():
        if DatabaseManager.connection is None or DatabaseManager.connection.closed:
            DatabaseManager.connect()
        return DatabaseManager.connection

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

    @staticmethod
    def rollback():
        conn = DatabaseManager.get_connection()
        conn.rollback()

    @staticmethod
    def close():
        if DatabaseManager.connection and not DatabaseManager.connection.closed:
            print("Closing database connection")
            DatabaseManager.connection.close()
            DatabaseManager.connection = None

    def __enter__(self):
        DatabaseManager.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
        else:
            self.commit()
        self.close()
