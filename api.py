from flask import Flask, json, abort, request
from user.student import Student
from data.data_layer import DataLayer
from validators.validators import Validators
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

data_layer = DataLayer()


# get all students -> Students list  page
@app.route('/students')
def get_all_students():
    students_list = data_layer.get_all_students()
    if not students_list or students_list == []:
        abort(404, "students collection is empty")
    return app.response_class(response=json.dumps(students_list),
                              status=200,
                              mimetype="application/json")


# get student by email - email will be a path param -> Student page
@app.route("/students/<string:student_email>")
def get_student(student_email):
    try:
        student = data_layer.get_student(student_email)
        return app.response_class(response=json.dumps(student),
                                  status=200,
                                  mimetype="application/json")
    except ValueError as error:
        abort(404, error)


#  get added students per day of the year - day will be a query param E.g. 2016_01_03 -> dashboard page
@app.route("/students/add_students")
def get_students_per_day():
    # query parameter ?added_on=2016_01_03
    creation_time = request.args.get('added_on')
    students_per_day = data_layer.get_students_per_day(creation_time)
    # date existence validation

    if len(students_per_day) == 0:
        abort(404, f"No students created on {creation_time}")
    if len(creation_time) == 0:
        abort(404, "Missing creation_time")
    if type(creation_time) != str:
        abort(404, "creation_time should be a string")

    return app.response_class(response=json.dumps(students_per_day),
                              status=200,
                              mimetype="application/json")


# get count of desired skills (how many of the students desire a specific skill)
@app.route("/students/desired_magic_skill/<string:desired_skill>")
def count_desired_skill(desired_skill):
    desired_skills_popularity = data_layer.count_desired_skill_popularity()
    for skill in desired_skills_popularity:
        if skill['_id'] == desired_skill:
            return app.response_class(response=json.dumps(skill),
                                      status=200,
                                      mimetype="application/json")


# get count for how many students have each type of skill
@app.route("/students/existing_magic_skill/<string:existing_skill>")
def count_existing_skill(existing_skill):
    existing_skills_popularity = data_layer.count_existing_skill_popularity()
    for skill in existing_skills_popularity:
        if skill['_id'] == existing_skill:
            return app.response_class(response=json.dumps(skill),
                                      status=200,
                                      mimetype="application/json")


# add a new student (request which will be invoked by admin)  - the route will receive a json with the student fields.
@app.route("/admin/add_student", methods=["POST"])
def add_student():
    student_dict = request.json
    if student_dict is None or student_dict == {}:
        return app.response_class(response=json.dumps({"Error": "Please provide connection information"}),
                                  status=400,
                                  mimetype='application/json')
    try:
        # validate student fields and existence
        validator = Validators(student_dict)
        validator.valid_user_fields_exist()
        validator.valid_user_fields_type()

        # new_student = Student.from_json(student_dict)
        authorization = request.headers.get("Authorization").split(":")
        auth_email = authorization[0]
        auth_password = authorization[1]

        with open("data/admin.json", "r") as r_f:
            admins_dict = json.load(r_f)
            if auth_email not in admins_dict.keys() or admins_dict[auth_email]['password'] != auth_password:
                abort(404, "Only Admin can create new student account")
            # add new student to data_layer students dict and students.json

        output = data_layer.add_student(student_dict)

        return app.response_class(response=json.dumps(output),
                                  status=200,
                                  mimetype="application/json")
    except ValueError as error:
        abort(404, error)


# login a student(email + password) - the route will receive a json with the data.
@app.route("/admin/log_in", methods=["POST"])
def log_in():
    admin_credential = request.json
    print(admin_credential)
    print(type(admin_credential))
    output = data_layer.log_in(admin_credential)

    if not output:
        abort(404, "wrong user email or password")

    return app.response_class(response=json.dumps({"message": "user log in successfully!"}),
                              status=200,
                              mimetype="application/json")


@app.route("/admin/signup", methods=["POST"])
def sign_up():
    admin_dict = request.json
    print(admin_dict)
    if admin_dict is None or admin_dict == {}:
        return app.response_class(response=json.dumps({"Error": "Please provide connection information"}),
                                  status=400,
                                  mimetype='application/json')
    try:
        output = data_layer.sign_up(admin_dict)

        return app.response_class(response=json.dumps(output),
                                  status=200,
                                  mimetype="application/json")
    except ValueError as error:
        abort(404, error)


# edit student - the route will receive a json with the student fields
@app.route("/admin/edit_student", methods=["PUT"])
def edit_student():
    updated_student = request.json
    try:
        # validate students fields value, types and existence
        validator = Validators(updated_student)
        validator.valid_user_fields_exist()
        validator.valid_user_fields_type()

        student_email = updated_student["email"]
        output = data_layer.edit_student(updated_student, student_email)

        if output['Status'] == "Nothing was updated.":
            abort(404, "Nothing was updated.")

        return app.response_class(response=json.dumps(output))
    except ValueError as error:
        abort(404, error)


# Create DELETE route for delete a student from database
@app.route("/admin/delete", methods=["DELETE"])
def delete_student():
    student_dict = request.json
    secrete_password = request.headers.get("secrete_password")
    if secrete_password != "88888":
        abort(404, "wrong secrete_password!")

    output = data_layer.remove_student(student_dict)
    if output['Status'] == "Student not found.":
        abort(404, "Student not found.")

    return app.response_class(response=json.dumps(output),
                              status=200,
                              mimetype="application/json")


if __name__ == "__main__":
    app.run()
