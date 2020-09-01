import mysql.connector
from decouple import config
from data.BaseDataLayer import BaseDataLayer


class MySqlDataLayer(BaseDataLayer):
    def __connect(self):
        try:
            self.__mydb = mysql.connector.connect(
                host="localhost",
                user=config('MYSQL_USER'),
                passwd=config('PASSWORD'),
                database='Hogwarts'
            )
            self.cursor = self.__mydb.cursor()

            self.__mydb.autocommit = False
        except Exception as e:
            print(e)

    def shut_down(self):
        self.__mydb = mysql.connector.close()

    def __init__(self):
        super().__init__()
        self.__connect()

    def add_student(self, student_dict):
        desired_skills = student_dict["desired_magic_skills"]
        skill_values = []
        existing_skills = student_dict['existing_magic_skills']
        try:
            self.__mydb.start_transaction()
            sql_wizard = "INSERT INTO wizards (id,first_name, last_name, email, creation_time, last_updated_time) VALUES (default, %s, %s, %s, curdate() ,CURRENT_TIMESTAMP)"
            data_wizard = (student_dict['first_name'], student_dict['last_name'], student_dict['email'])
            sql_student = "INSERT INTO students (id, wizard_id) VALUES (default, LAST_INSERT_ID())"

            sql_skill = "INSERT INTO skills (id, name,skill_type,level, student_id) VALUES (default, %s, %s, %s, %s)"

            self.cursor.execute(sql_wizard, data_wizard)
            self.cursor.execute(sql_student)
            student_id = self.cursor.lastrowid

            def get_skills(skills, type):
                for skill in skills:
                    skill_values.append((skill['name'], type, str(skill['level']), student_id))
                return skill_values

            desired_skill_values = get_skills(desired_skills, 'desired')
            skills_values = get_skills(existing_skills, 'existing')


            for skill_value in skills_values:
                self.cursor.execute(sql_skill, skill_value)

            print(self.cursor.rowcount, "record inserted.")
            self.__mydb.commit()
            return self.cursor.rowcount

        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
            self.__mydb.rollback()

        finally:
            self.cursor.close()

    def get_all_students(self):
        students_list = []
        try:
            self.__mydb.start_transaction()
            sql_all_students = "SELECT first_name,last_name,email,creation_time,last_updated_time, students.id from students inner join wizards on wizards.id = students.wizard_id"
            self.cursor.execute(sql_all_students)
            ans = self.cursor.fetchall()

            for item in ans:
                student = {'first_name': item[0], 'last_name': item[1], 'email': item[2],
                           'creation_time': item[3],
                           'last_updated_time': item[4], 'desired_magic_skills': [],
                           'existing_magic_skills': []}

                sql_get_skills_by_student_id = "SELECT name , skill_type, level from skills WHERE student_id = %s"
                self.cursor.execute(sql_get_skills_by_student_id, (item[-1],))
                skills = self.cursor.fetchall()
                print(skills)

                for skill in skills:
                    if skill[1] == 'desired':
                        student['desired_magic_skills'].append({"name": skill[0], "level": skill[2]})
                    if skill[1] == 'existing':
                        student['existing_magic_skills'].append({"name": skill[0], "level": skill[2]})

                students_list.append(student)
            return students_list

        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
            self.__mydb.rollback()

        finally:
            self.cursor.close()

    def remove_student(self, student_dict):
        try:
            self.__mydb.start_transaction()
            sql_delete = 'DELETE from wizards WHERE email = %s'
            self.cursor.execute(sql_delete,(student_dict['email'],))

            print(self.cursor.rowcount, "record deleted.")
            self.__mydb.commit()
            output = {'Status': 'Successfully Deleted' if self.cursor.rowcount > 0 else "Student not found."}
            return output

        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
            self.__mydb.rollback()

        finally:
            self.cursor.close()
