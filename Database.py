import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.__host_name = "localhost"
        self.__user_name = "root"
        self.__password = "127425"
        self.__db_name = "self_learning_platform_db"
        self.__connection = self.connect_db()
        self.__create_db_query = "Create database self_learning_platform_db;"


    def connect_db(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host = self.__host_name,
                user = self.__user_name,
                passwd = self.__password,
                database = self.__db_name
            )
            print("Database Connection Established>>>")
        except Error as err:
            print(f"Error: {err}")
        return connection

    def create_database(self):
        cursor = self.__connection.cursor()
        try:
            cursor.execute(self.__create_db_query)
            self.__connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
    def delete_database(self, database_name):
        cursor = self.__connection.cursor()
        try:
            cursor.execute(f"DROP DATABASE {database_name}")
            self.__connection.commit()
            print(f"Database '{database_name}' deleted successfully.")
        except Error as err:
            print(f"Error: '{err}'")

class Instructor:

    def __init__(self, username=None, password=None, email=None, gender=None, role=None):
        self.__instructor_id = None
        self.__username = username
        self.__password = password
        self.__email = email
        self.__gender = gender
        self.__role = role
        self.db = Database()
        self.connection = self.db.connect_db()

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self, password):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_role(self):
        return self.__role

    def set_role(self, value):
        self.__role = value
    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

    def create_intructor_info_table(self):
        query = ("""create table instructor_info (
                 instructor_id INT PRIMARY KEY AUTO_INCREMENT,
                 username VARCHAR(20) NOT NULL,
                 password VARCHAR(20) NOT NULL,
                 email VARCHAR(40) NOT NULL,
                 gender VARCHAR(10) NOT NULL,
                 role VARCHAR(10) NOT NULL
                 );
                 """)
        self.execute_query(query)

    def create_instructor_account(self):
        query = "INSERT INTO instructor_info (username, password, email, gender, role) VALUES (%s, %s, %s, %s, %s)"
        print(self.__username)
        print(self.__role)
        values = (self.__username, self.__password, self.__email, self.__gender, self.__role)
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()

    def search_by_username(self):
        query = "SELECT * FROM instructor_info WHERE username = %s"
        result = self.read_query(query, (self.__username,))
        return result

    def login_confirmation(self):
        # Construct the query with placeholders
        query = "SELECT * FROM instructor_info WHERE username = %s AND password = %s"
        result = self.read_query(query, (self.__username, self.__password))
        return result


    def read_query(self, query, value):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query, value)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")



# ins = Instructor()
# ins.create_intructor_info_table()

# db.create_database()