from flask import Flask, json, abort, request
from user.student import Student
from data.data_layer import DataLayer

app = Flask(__name__)
students_dict = {}
skills_dict = {}


# * get all students -> Students list  page
@app.route('/students')
def get_all_students():
    if students_dict == {}:
        abort(404, "students_dict is empty")
    return app.response_class(response=json.dumps(students_dict),
                              status=200,
                              mimetype="application/json")


# get student by email - email will be a path param -> Student page
@app.route("/students/<string:student_email>")
def get_student(email):
    # todo validate students dict and email
    # todo: create get_student() method in data_layer and create instance here: student = data_layer.get_student(email)
    pass


#  get added students per day of the year - day will be a query param E.g. 2016_01_03 -> dashboard page
@app.rout("/students")
def get_student_per_day():
    # query parameter ?added_on=2016_01_03
    # todo validate
    # todo: student = data_layer.get_students
    pass


# get count of desired skills (how many of the students desire a specific skill)
@app.route("students/<string:desired_skill>")
def count_desired_skill(desired_skill):
    pass


# get count for how many students have each type of skill
@app.route("students/<string:existing_skill>")
def count_existing_skill(existing_skill):
    pass


# add a new student (request which will be invoked by admin)  - the route will receive a json with the student fields.
@app.route("/admin/add_student", methods=["POST"])
def add_student():
    data = request.json
    # todo: validate student fields
    student = Student(*data)
    pass


# login a student(email + password) - the route will receive a json with the data.
@app.route("/admin/log_in", methods=["POST"])
def log_in():
    # ? how to transfer user credential to json?
    student_credential = request.json
    return app.response_class(response=json.dumps(student_credential),
                              status=200,
                              mimetype="application/json")


# edit student - the route will receive a json with the student fields
@app.route("/admin/edit_student", methods=["PUT"])
def edit_student():
    data = request.json
    # todo: validate students fields
    pass


# Create DELETE (with an empty implementation at this point) route for delete a student
@app.route("admin/delete", methods=["POST"])
def delete_student():
    pass


if __name__ == "__main__":
    app.run()
    data_layer = DataLayer()
