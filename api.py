from flask import Flask, json, abort, request, render_template
from user.student import Student
from data.data_layer import DataLayer

app = Flask(__name__)
data_layer = DataLayer()
students_dict = data_layer.load_all_students()
skills_dict = {}


@app.before_first_request
def before_first_request_func():
    new_data_layer = DataLayer()
    new_students_dict = data_layer.load_all_students()
    return new_students_dict


# question: why variables inside before_first_request_func can not access outer scope variable even with the same name?


# The homepage is what will be shown to the user when they visit the / URL
@app.route("/")
def index():
    # return render_template("index.html")
    return "Welcome to visit Hogwarts CRM system!"


# the dashboard page (/dashboard) will be shown to the user once they’ve logged into their account
# @app.route("/dashboard")
# def dashboard():
#     return render_template("dashboard.html")

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
def get_student(student_email):
    if students_dict == {}:
        abort(404, "students_dict is empty")

    # student email existence has been validated inside data_layer.get_student method
    student = data_layer.get_student(student_email)
    return app.response_class(response=json.dumps(student),
                              status=200,
                              mimetype="application/json")


#  get added students per day of the year - day will be a query param E.g. 2016_01_03 -> dashboard page
@app.route("/students/add_students")
def get_students_per_day():
    # query parameter ?added_on=2016_01_03
    creation_time = request.args.get('creation_time')
    students_per_day = data_layer.get_students_per_day(creation_time)
    # date existence validation
    if len(students_per_day) == 0:
        abort(404, f"No students created on {creation_time}")
    return app.response_class(response=json.dumps(students_per_day),
                              status=200,
                              mimetype="application/json")


# get count of desired skills (how many of the students desire a specific skill)
@app.route("/students/<string:desired_skill>")
def count_desired_skill(desired_skill):
    pass


# get count for how many students have each type of skill
@app.route("/students/<string:existing_skill>")
def count_existing_skill(existing_skill):
    pass


# add a new student (request which will be invoked by admin)  - the route will receive a json with the student fields.
@app.route("/admin/add_student", methods=["POST"])
def add_student():
    data = request.json
    # todo: validate student fields
    # it should return a json string send to Student class from_json() to create student instance
    pass


# login a student(email + password) - the route will receive a json with the data.
@app.route("/admin/log_in", methods=["POST"])
def log_in():
    # ? how to transfer user credential to json?
    student_credential = request.json
    # todo: validate student credential
    # logic

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
@app.route("/admin/delete", methods=["POST"])
def delete_student():
    pass


if __name__ == "__main__":
    app.run()
