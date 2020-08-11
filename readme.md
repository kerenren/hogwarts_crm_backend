##### Prerequisites
###### Get started with mongodb (for MacOS)
To run MongoDB (i.e. the mongod process) as a macOS service, issue the following:
`brew services start mongodb-community@4.4`

To stop a mongod running as a macOS service, use the following command as needed:
`brew services stop mongodb-community@4.4`

###### Connect and Use MongoDB
To begin using MongoDB, connect a mongo shell to the running instance. From a new terminal, issue the following:
 `mongo`

###### PyMongo
[Mongodb Python plugin- PyMongo totorial][https://pymongo.readthedocs.io/en/stable/tutorial.html]
Installing with pip:
 `python -m pip install pymongo`
>> Before we start, make sure that you have the PyMongo distribution installed. In the Python shell, the following should run without raising an exception:
`import pymongo`
>> This tutorial also assumes that a MongoDB instance is running on the default host and port. Assuming you have downloaded and installed MongoDB, you can start it like so:
 `mongod`

##### Hogwarts CRM


You are instructed to build the CRM for the “Hogwarts School of Magic”


Task (NOT TO BE IMPLEMENTED AT THIS TIME)
You shall build a system that has the following screens:
Students list - showing a big table with each row being a student 
Student page - showing a single student entry
Edit capabilities
Add new student page - for adding new students
Add dashboard to show all students - showing stats about students
How many students were added per day

Pie chart that counts how many students have each skills


Pie chart that counts of how many students have each desired skills


Delete a student using a predefined secret password.




 Create a signup page for a student


 Create a login page for a student
Using POST request sending JSON).


 Make it pretty




Each student has the following fields:
ID
First name
Last name
Email
Password
Creation time
Last update time
Existing magic skills
From a predefined list (Strings)
Each one has a level 1-5
Desired magic skills
From a predefined list (Strings)
Each one has a level 1-5



Skill will have the following fields:
name

















Flask Milestone1:


Create a new Project.


Create a Flask project in a new file named api.py.


Create GET routes (with an empty implementation at this point) for:
* get student by email - email will be a path param
* get all students
* get added students per day of the year - day will be a query param
E.g. 2016_01_03
* get count of desired skills (how many of the students desire a specific skill)

* get count for how many students have each type of skill


Create POST/PUT (with an empty implementation at this point) routes for:
* add a new student (request which will be invoked by admin)  - the route will receive a json with the student fields.
* login a student(email + password) - the route will receive a json with the data.
* edit student - the route will receive a json with the student fields.


Create DELETE (with an empty implementation at this point) route for delete a student



















Flask Milestone2:
Create a class for a student.


Override the builtin str function to return a json string of all the properties of a student.


Create a function called fromJson() which will create a student class instance from json string.
Think carefully about what type of function it should be.
You can also invoke the class constructor instead.


Create class for a skill.



Override the builtin str function to return a json string of all the properties of a skill.


think carefully about the connections between the 2 classes.


Create a class for an admin user.


Create validations for add new student
* validate that all required fields have values
* validate that all required fields values are of the right type


Create validations for editing an existing student
* validate that all required fields have values
* validate that all required fields values are of the right type
* validate that the user actually exists


Create validations for login a student
* validate that all required fields have values
* validate that all required fields values are of the right type


Create validations for get student by email
* validate that email was provided
* validate the type of the email property (hint: string)


Create validations for get added students per day
* validate that date property was provided



* validate that the date provided is of type string


Failed validation will return false.


Ninja: Failed validation will raise an exception of type ValidationError




































Flask Milestone3:
Create a class called DataLayer.
The class will have a dictionary containing the students class instances.
each instance will be stored using its email property as the key within the dictionary.


Implement the functions for setting and getting a specific student from the dictionary by its email.


Implement a function for receiving all students within the dictionary.


Implement a function for receiving all students within the dictionary as json strings.
The function will call the previous function and afterwards convert the returned data to be a list of json strings.


Implement a function for removing a student from the students dictionary.


Implement a function for persisting all the students' class instances in the dictionary into a json file called students.json.
The file will be saved within a directory called data (to be created in the top directory of the project.


Implement a function for loading the data from students.json, converting it to students class instances and populating the instances into the students dictionary object of the DataLayer class.


in file api.py add a function with decorator @app.before_first_request
The function will create a new dataLayer instance to be used by the flask app.
Which will invoke the previously created function in order to populate the DataLayer’s students dictionary.


Add a validation for the create new student function that validates that there are no email duplications (no student with the email already exists within the system)
prior to adding a new student to the dictionary.






Flask Milestone4:
Remove the empty implementations from the flask routes in api.py
And using the functions previously created in the dataLayer class
implement all the required functionalities for all of the flask routes.
(At this point we are connecting between api.py flask app routes and the DataLayer functions).


All routes will return jsons (either single or lists of jsons).

Ninja:
After a new student process has ended successfully, send email to the student’s email account, with the credentials.


[https://pymongo.readthedocs.io/en/stable/tutorial.html]: https://pymongo.readthedocs.io/en/stable/tutorial.hztml