import mysql.connector
from mysql.connector import Error
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Label


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

    def read_query_not_based_on_value(self, query):
        cursor = self.__connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

    def read_query(self, query, value):
        cursor = self.__connection.cursor()
        result = None
        try:
            cursor.execute(query, value)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")
    def retrieve_all_course_based_on_userid(self, username):
        query = "SELECT course_name, course_id from course_info where user_id = %s"
        result = self.read_query(query, (username,))
        return result

    def retrieve_course_content_based_on_course_id(self, course_id):
        query = "Select * From course_page WHERE course_id = %s"
        result = self.read_query(query, (course_id,))
        return result

    def retrieve_quiz_content_based_on_course_id(self, course_id):
        query = "Select * From quiz WHERE course_id = %s"
        result = self.read_query(query, (course_id,))
        return result

    def retrieve_all_course(self):
        query = "SELECT course_name, course_id from course_info"
        result = self.read_query_not_based_on_value(query)
        return result

class User:

    def __init__(self, username=None, password=None, email=None, gender=None, role=None):
        self.user_id = None
        self.__username = username
        self.__password = password
        self.__email = email
        self.__gender = gender
        self.__role = role
        self.db = Database()
        self.connection = self.db.connect_db()
        self.user_info = None



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

    def get_user_info(self):
        return self.user_info
    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

    def create_user_info_table(self):
        query = ("""create table user_info (
                 user_id INT PRIMARY KEY AUTO_INCREMENT,
                 username VARCHAR(20) NOT NULL,
                 password VARCHAR(20) NOT NULL,
                 email VARCHAR(40) NOT NULL,
                 gender VARCHAR(10) NOT NULL,
                 role VARCHAR(10) NOT NULL
                 );
                 """)
        self.execute_query(query)

    def create_user_account(self):
        query = "INSERT INTO user_info (username, password, email, gender, role) VALUES (%s, %s, %s, %s, %s)"
        print(self.__username)
        print(self.__role)
        values = (self.__username, self.__password, self.__email, self.__gender, self.__role)
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()

    def search_by_username(self):
        query = "SELECT * FROM user_info WHERE username = %s"
        result = self.read_query(query, (self.__username,))
        return result

    def search_by_username2(self, username):
        query = "SELECT * FROM user_info WHERE username = %s"
        result = self.read_query(query, (username,))
        print("result = ", result)
        return result

    def login_confirmation(self):
        # Construct the query with placeholders
        query = "SELECT * FROM user_info WHERE username = %s AND password = %s AND role = %s"
        result = self.read_query(query, (self.__username, self.__password, self.__role))
        print(result)
        self.user_info = result
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
    def __init__(self, course_name = None, course_create_date = None, user_info = None):
        self.course_name = course_name
        self.course_create_date = course_create_date
        self.db = Database()
        self.connection = self.db.connect_db()
        self.user_info = user_info
        self.user_details = user_info[0]
        self.user_id = self.user_details[0]
        print(self.user_info)


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
                 user_id INT,
                 FOREIGN KEY (user_id) REFERENCES user_info(user_id)
                 );
                 """)
        self.execute_query(query)

    def create_course_info(self):
        query = "INSERT INTO course_info (course_name, course_create_date, user_id) VALUES (%s, %s, %s)"
        values = (self.course_name, self.course_create_date, self.user_id)
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

    def read_query_not_based_on_value(self, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

    def search_by_course_name(self):
        query = "SELECT * FROM course_info WHERE course_name = %s"
        result = self.read_query(query, (self.course_name,))
        return result[0]

    def search_by_course_name2(self):
        query = "SELECT * FROM course_info WHERE course_name = %s"
        result = self.read_query(query, (self.course_name,))
        return result

    def clear_table(self):
        query = "Drop TABLE user_info"
        self.execute_query(query)



class Course_page:
    def __init__(self, course_page_number = None, course_title = None, course_author = None, course_abstract = None, tabview1_subtopic_entry = None, tabview1_data_entry1 = None,
                 tabview1_data_entry2 = None, tabview1_data_entry3 = None, tabview1_textbox = None, tabview2_subtopic_entry = None, tabview2_data_entry1 = None,
                 tabview2_data_entry2 = None, tabview2_data_entry3 = None, tabview2_textbox = None, tabview3_subtopic_entry = None, tabview3_data_entry1 = None,
                 tabview3_data_entry2 = None, tabview3_data_entry3 = None, tabview3_textbox = None, img_1 = None,  img_2 = None, img_3 = None,  img_4 = None,
                 img_5 = None, img_6 = None, img_7 = None, img_8 = None, img_9 = None, course_info = None):
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
        self.img_1 = img_1
        self.img_2 = img_2
        self.img_3 = img_3
        self.img_4 = img_4
        self.img_5 = img_5
        self.img_6 = img_6
        self.img_7 = img_7
        self.img_8 = img_8
        self.img_9 = img_9
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
                 img_1 VARCHAR(100) NOT NULL,
                 img_2 VARCHAR(100) NOT NULL,
                 img_3 VARCHAR(100) NOT NULL,
                 img_4 VARCHAR(100) NOT NULL,
                 img_5 VARCHAR(100) NOT NULL,
                 img_6 VARCHAR(100) NOT NULL,
                 img_7 VARCHAR(100) NOT NULL,
                 img_8 VARCHAR(100) NOT NULL,
                 img_9 VARCHAR(100) NOT NULL,
                 course_id INT,
                 FOREIGN KEY (course_id) REFERENCES course_info(course_id)
                 );
                 """)
        self.execute_query(query)

    def read_query(self, query, value):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query, value)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")



    def retrieve_img_1(self):
        query = "SELECT img_1 FROM course_page WHERE course_title = %s"
        result = self.read_query(query, ("Jay",))
        return result[0]

    def create_course_page_info(self):
        query = """INSERT INTO course_page (course_page_number, course_title, course_author, course_abstract, tabview1_subtopic_entry, tabview1_data_entry1, tabview1_data_entry2, tabview1_data_entry3, tabview1_textbox, 
                   tabview2_subtopic_entry, tabview2_data_entry1, tabview2_data_entry2, tabview2_data_entry3, tabview2_textbox, 
                   tabview3_subtopic_entry, tabview3_data_entry1, tabview3_data_entry2, tabview3_data_entry3, tabview3_textbox, img_1, img_2, img_3, img_4, img_5, img_6, img_7, img_8, img_9, course_id) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (self.course_page_number, self.course_title, self.course_author, self.course_abstract,
                  self.tabview1_subtopic_entry, self.tabview1_data_entry1, self.tabview1_data_entry2, self.tabview1_data_entry3, self.tabview1_textbox,
                  self.tabview2_subtopic_entry, self.tabview2_data_entry1, self.tabview2_data_entry2, self.tabview2_data_entry3, self.tabview2_textbox,
                  self.tabview3_subtopic_entry, self.tabview3_data_entry1, self.tabview3_data_entry2, self.tabview3_data_entry3, self.tabview3_textbox,
                  self.img_1, self.img_2, self.img_3, self.img_4, self.img_5, self.img_6, self.img_7, self.img_8, self.img_9,
                  self.course_id)
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()

class Quiz:
    def __init__(self, input_type = None, quiz_number = None, quiz_question = None, short_answer_ans = None, radio_choice_1 = None, radio_choice_2 = None, radio_choice_3 = None, radio_choice_4 = None, radio_answer = None, course_info = None):
        self.db = Database()
        self.connection = self.db.connect_db()
        self.input_type = input_type
        self.quiz_page_number = quiz_number
        self.quiz_question = quiz_question
        self.short_answer_ans = short_answer_ans
        self.radio_choice_1 = radio_choice_1
        self.radio_choice_2 = radio_choice_2
        self.radio_choice_3 = radio_choice_3
        self.radio_choice_4 = radio_choice_4
        self.radio_answer = radio_answer
        self.course_info = course_info
        self.course_id = course_info[0]

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

    def create_quiz_table(self):
        query = ("""create table quiz  (
                 quiz_id INT PRIMARY KEY AUTO_INCREMENT,
                 input_type varchar(20) NOT NULL,
                 quiz_page_number INT NOT NULL,
                 quiz_question TEXT NOT NULL,
                 short_answer_ans TEXT NULL,
                 radio_choice_1 TEXT NULL,
                 radio_choice_2 TEXT NULL,
                 radio_choice_3 TEXT NULL,
                 radio_choice_4 TEXT NULL,
                 radio_answer TEXT NULL,
                 course_id INT,
                 FOREIGN KEY (course_id) REFERENCES course_info(course_id)
                 );
                 """)
        self.execute_query(query)

    def create_quiz_info(self):
        query = "INSERT INTO quiz (input_type, quiz_page_number, quiz_question, short_answer_ans, radio_choice_1, radio_choice_2, radio_choice_3, radio_choice_4, radio_answer, course_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (self.input_type, self.quiz_page_number, self.quiz_question, self.short_answer_ans, self.radio_choice_1, self.radio_choice_2, self.radio_choice_3, self.radio_choice_4, self.radio_answer, self.course_id)
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

    # def search_by_course_name(self):
    #     query = "SELECT * FROM course_info WHERE course_name = %s"
    #     result = self.read_query(query, (self.course_name,))
    #     return result[0]
    # def clear_table(self):
    #     query = "DROP TABLE course_info"
    #     self.execute_query(query)


# course = Course_page()
#
# quiz = Quiz()
# quiz.create_quiz_table()



