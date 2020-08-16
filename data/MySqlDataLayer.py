import mysql.connector
from decouple import config
from data.BaseDataLayer import BaseDataLayer


class MySqlDataLayer(BaseDataLayer):
    def __connect(self):
        self.__mydb = mysql.connector.connect(
            host="localhost",
            user=config('MYSQL_USER'),
            passwd=config('PASSWORD'),
            database='Hogwarts'
        )
        self.cursor = self.__mydb.cursor()

        self.__mydb.autocommit = True

    def shut_down(self):
        self.__mydb = mysql.connector.close()

    def __init__(self):
        super().__init__()
        self.__connect()

    def add_student(self, student_dict):
        try:
            sql = "INSERT INTO students (id,first_name, last_name, email, password, creation_time, last_updated_time) VALUES (default, %s, %s, %s, %s, curdate() ,CURRENT_TIMESTAMP)"
            data_student = (student_dict['first_name'],student_dict['last_name'],student_dict['email'],student_dict['password'])
            self.cursor.execute(sql,data_student)
            print(self.cursor.rowcount, "record inserted.")
            return self.cursor.rowcount
        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))

        finally:
            self.cursor.close()




