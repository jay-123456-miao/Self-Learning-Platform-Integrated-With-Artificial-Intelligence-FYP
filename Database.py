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
        self.instructor_info = None

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

    def get_instructor_info(self):
        return self.instructor_info
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
        print(result)
        self.instructor_info = result
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

class Course:
    def __init__(self, course_name = None, course_create_date = None, instructor_info = None):
        self.course_name = course_name
        self.course_create_date = course_create_date
        self.db = Database()
        self.connection = self.db.connect_db()
        self.instructor_info = instructor_info
        self.instructor_id = instructor_info[0]
        print(self.instructor_info)


    def set_course_name(self, course_name):
        self.course_name = course_name

    def get_course_name(self):
        return self.course_name

    def set_course_create_date(self, course_date):
        self.course_create_date = course_date

    def get_course_create_date(self):
        return self.course_create_date

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

    def create_course_info_table(self):
        query = ("""create table course_info (
                 course_id INT PRIMARY KEY AUTO_INCREMENT,
                 course_name VARCHAR(100) NOT NULL,
                 course_create_date DATE NOT NULL,
                 instructor_id INT,
                 FOREIGN KEY (instructor_id) REFERENCES instructor_info(instructor_id)
                 );
                 """)
        self.execute_query(query)

    def create_course_info(self):
        query = "INSERT INTO course_info (course_name, course_create_date, instructor_id) VALUES (%s, %s, %s)"
        values = (self.course_name, self.course_create_date, self.instructor_id)
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()

    def read_query(self, query, value):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query, value)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

    def search_by_course_name(self):
        query = "SELECT * FROM course_info WHERE course_name = %s"
        result = self.read_query(query, (self.course_name,))
        return result[0]
    def clear_table(self):
        query = "DROP TABLE course_info"
        self.execute_query(query)


class Course_page:
    def __init__(self, course_page_number = None, course_title = None, course_author = None, course_abstract = None, tabview1_subtopic_entry = None, tabview1_data_entry1 = None,
                 tabview1_data_entry2 = None, tabview1_data_entry3 = None, tabview1_textbox = None, tabview2_subtopic_entry = None, tabview2_data_entry1 = None,
                 tabview2_data_entry2 = None, tabview2_data_entry3 = None, tabview2_textbox = None, tabview3_subtopic_entry = None, tabview3_data_entry1 = None,
                 tabview3_data_entry2 = None, tabview3_data_entry3 = None, tabview3_textbox = None, course_info = None):
        self.db = Database()
        self.connection = self.db.connect_db()
        self.course_page_number = course_page_number
        self.course_title = course_title
        self.course_author = course_author
        self.course_abstract = course_abstract
        self.tabview1_subtopic_entry = tabview1_subtopic_entry
        self.tabview1_data_entry1 = tabview1_data_entry1
        self.tabview1_data_entry2 = tabview1_data_entry2
        self.tabview1_data_entry3 = tabview1_data_entry3
        self.tabview1_textbox = tabview1_textbox
        self.tabview2_subtopic_entry = tabview2_subtopic_entry
        self.tabview2_data_entry1 = tabview2_data_entry1
        self.tabview2_data_entry2 = tabview2_data_entry2
        self.tabview2_data_entry3 = tabview2_data_entry3
        self.tabview2_textbox = tabview2_textbox
        self.tabview3_subtopic_entry = tabview3_subtopic_entry
        self.tabview3_data_entry1 = tabview3_data_entry1
        self.tabview3_data_entry2 = tabview3_data_entry2
        self.tabview3_data_entry3 = tabview3_data_entry3
        self.tabview3_textbox = tabview3_textbox
        self.course_info = course_info
        self.course_id = course_info[0]

    def set_course_page_number(self, course_page_number):
        self.course_page_number =  course_page_number

    def get_course_page_number(self):
        return self.course_page_number

    def set_course_title(self, course_title):
        self.course_title = course_title

    def get_course_title(self):
        return self.course_title

    def set_course_author(self, course_author):
        self.course_author = course_author

    def get_course_author(self):
        return self.course_author
    def set_course_abstract(self, course_abstract):
        self.course_abstract = course_abstract

    def get_course_abstract(self):
        return self.course_abstract

    def set_tabview1_tuple(self, tabview1_tuple):
        self.tabview1_tuple = tabview1_tuple

    def get_tabview1_tuple(self):
        return self.tabview1_tuple

    def set_tabview2_tuple(self, tabview2_tuple):
        self.tabview2_tuple = tabview2_tuple

    def get_tabview2_tuple(self):
        return self.tabview2_tuple

    def set_tabview3_tuple(self, tabview3_tuple):
        self.tabview3_tuple = tabview3_tuple

    def get_tabview3_tuple(self):
        return self.tabview3_tuple

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

    def create_course_page_table(self):
        query = ("""create table course_page (
                 course_page_id INT PRIMARY KEY AUTO_INCREMENT,
                 course_page_number INT NOT NULL,
                 course_title VARCHAR(100) NOT NULL,
                 course_author VARCHAR(20) NOT NULL,
                 course_abstract TEXT NOT NULL,
                 tabview1_subtopic_entry VARCHAR(100) NOT NULL,
                 tabview1_data_entry1 VARCHAR(20) NOT NULL,
                 tabview1_data_entry2 VARCHAR(20) NOT NULL,
                 tabview1_data_entry3 VARCHAR(20) NOT NULL,
                 tabview1_textbox TEXT NOT NULL,
                 tabview2_subtopic_entry VARCHAR(100) NOT NULL,
                 tabview2_data_entry1 VARCHAR(20) NOT NULL,
                 tabview2_data_entry2 VARCHAR(20) NOT NULL,
                 tabview2_data_entry3 VARCHAR(20) NOT NULL,
                 tabview2_textbox TEXT NOT NULL,
                 tabview3_subtopic_entry VARCHAR(100) NOT NULL,
                 tabview3_data_entry1 VARCHAR(20) NOT NULL,
                 tabview3_data_entry2 VARCHAR(20) NOT NULL,
                 tabview3_data_entry3 VARCHAR(20) NOT NULL,
                 tabview3_textbox TEXT NOT NULL,
                 course_id INT,
                 FOREIGN KEY (course_id) REFERENCES course_info(course_id)
                 );
                 """)
        self.execute_query(query)

    def create_course_page_info(self):
        print(type(self.course_page_number))
        print(type(self.course_title))
        print(type(self.course_author))
        print(type(self.course_abstract))
        print(type(self.tabview1_subtopic_entry))
        print(type(self.tabview1_data_entry1))
        print(type(self.tabview1_data_entry2))
        print(type(self.tabview1_data_entry3))
        print(type(self.tabview1_textbox))
        print(type(self.tabview2_subtopic_entry))
        print(type(self.tabview2_data_entry1))
        print(type(self.tabview2_data_entry2))
        print(type(self.tabview2_data_entry3))
        print(type(self.tabview2_textbox))
        print(type(self.tabview3_subtopic_entry))
        print(type(self.tabview3_data_entry1))
        print(type(self.tabview3_data_entry2))
        print(type(self.tabview3_data_entry3))
        print(type(self.tabview3_textbox))
        print(self.course_id)
        query = """INSERT INTO course_page (course_page_number, course_title, course_author, course_abstract, tabview1_subtopic_entry, tabview1_data_entry1, tabview1_data_entry2, tabview1_data_entry3, tabview1_textbox, 
                   tabview2_subtopic_entry, tabview2_data_entry1, tabview2_data_entry2, tabview2_data_entry3, tabview2_textbox, 
                   tabview3_subtopic_entry, tabview3_data_entry1, tabview3_data_entry2, tabview3_data_entry3, tabview3_textbox, course_id) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (self.course_page_number, self.course_title, self.course_author, self.course_abstract,
                  self.tabview1_subtopic_entry, self.tabview1_data_entry1, self.tabview1_data_entry2, self.tabview1_data_entry3, self.tabview1_textbox,
                  self.tabview2_subtopic_entry, self.tabview2_data_entry1, self.tabview2_data_entry2, self.tabview2_data_entry3, self.tabview2_textbox,
                  self.tabview3_subtopic_entry, self.tabview3_data_entry1, self.tabview3_data_entry2, self.tabview3_data_entry3, self.tabview3_textbox,
                  self.course_id)
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()


