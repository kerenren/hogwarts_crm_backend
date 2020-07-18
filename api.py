from flask import Flask, json, abort, request, render_template
from user.student import Student
from data.data_layer import DataLayer
from validators.validators import Validators

app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

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
    creation_time = request.args.get('added_on')
    students_per_day = data_layer.get_students_per_day(creation_time)
    # date existence validation
    if len(students_per_day) == 0:
        abort(404, f"No students created on {creation_time}")
    return app.response_class(response=json.dumps(students_per_day),
                              status=200,
                              mimetype="application/json")


# get count of desired skills (how many of the students desire a specific skill)
@app.route("/students/desired_magic_skill/<string:desired_skill>")
def count_desired_skill(desired_skill):
    cnt = data_layer.count_skill("desired_magic_skills", desired_skill)
    return app.response_class(response=json.dumps({desired_skill: cnt}),
                              status=200,
                              mimetype="application/json")


# get count for how many students have each type of skill
@app.route("/students/existing_magic_skill/<string:existing_skill>")
def count_existing_skill(existing_skill):
    cnt = data_layer.count_skill("existing_magic_skills", existing_skill)
    return app.response_class(response=json.dumps({existing_skill: cnt}),
                              status=200,
                              mimetype="application/json")


# add a new student (request which will be invoked by admin)  - the route will receive a json with the student fields.
@app.route("/admin/add_student", methods=["POST"])
def add_student():
    student_dict = request.json
    # todo: validate student fields and existence
    new_student = Student.from_json(student_dict)
    authorization = request.headers.get("Authorization").split(":")
    auth_email = authorization[0]
    auth_password = authorization[1]

    with open("data/admin.json", "r") as r_f:
        admins_dict = json.load(r_f)
        if auth_email not in admins_dict.keys() or admins_dict[auth_email]['password'] != auth_password:
            abort(404, "Only Admin can create new student account")
        # add new student to data_layer students dict and students.json
        data_layer.add_student(new_student)
        data_layer.persist_students()

        return app.response_class(response=json.dumps(new_student.__dict__),
                                  status=200,
                                  mimetype="application/json")


# login a student(email + password) - the route will receive a json with the data.
@app.route("/admin/log_in", methods=["POST"])
def log_in():
    # ? how to transfer user credential to json?
    student_credential = request.json

    # validate student credential
    validator = Validators(student_credential)
    validation = validator.valid_user_credential(students_dict)
    if not validation:
        abort(404, "wrong user email or password")

    return app.response_class(response=json.dumps({"message": "user log in successfully!"}),
                              status=200,
                              mimetype="application/json")


# edit student - the route will receive a json with the student fields
@app.route("/admin/edit_student", methods=["PUT"])
def edit_student():
    updated_student = request.json
    # todo: validate students fields
    student_email = updated_student["email"]
    data_layer.edit_student(updated_student, student_email)

    data_layer.persist_students()
    return app.response_class(response=json.dumps({"message": "The student's capabilities has been updated"}))


# question, after load all student from json to student_dictionary in datalayer, and call get_student from datalayer, the student instance changed from Student class to dict. How should we deal with this in real database practice?

# Create DELETE (with an empty implementation at this point) route for delete a student
@app.route("/admin/delete", methods=["DELETE"])
def delete_student():
    student = request.json
    secrete_password = request.headers.get("secrete_password")
    if secrete_password != "88888":
        abort(404, "wrong secrete_password!")
    data_layer.remove_student(student)

    data_layer.persist_students()
    return app.response_class(response=json.dumps({"message": "user has been deleted!"}),
                              status=200,
                              mimetype="application/json")


if __name__ == "__main__":
    app.run()
