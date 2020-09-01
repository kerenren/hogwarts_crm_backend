##### Prerequisites
install all requirements
configure .env file:

`MYSQL_USER=<username> 
PASSWORD=<sqlpassword>
DB=<Mysql/MongoDB>`


###### Get started with mongodb (for MacOS)
To run MongoDB (i.e. the mongod process) as a macOS service, issue the following:
`brew services start mongodb-community@4.4`

To stop a mongod running as a macOS service, use the following command as needed:
`brew services stop mongodb-community@4.4`

###### Connect and Use MongoDB
To begin using MongoDB, connect a mongo shell to the running instance. From a new terminal, issue the following:
 `mongo`
 
###### Get started with mysql (for MacOS)
to add aliases to your shell's resource file to make it easier to access commonly used programs such as mysql and mysqladmin from the command line
`alias mysql=/usr/local/mysql/bin/mysql`
`alias mysqladmin=/usr/local/mysql/bin/mysqladmin`
`alias mysqlshow=/usr/local/mysql/bin/mysqlshow`

###### Connect sql server:
`mysql -u root -p`
And enter the password

### to start the server
run api.py from pycharm

###### PyMongo
[Mongodb Python plugin- PyMongo totorial][https://pymongo.readthedocs.io/en/stable/tutorial.html]
Installing with pip:
 `python -m pip install pymongo`
>> Before we start, make sure that you have the PyMongo distribution installed. In the Python shell, the following should run without raising an exception:
`import pymongo`
>> This tutorial also assumes that a MongoDB instance is running on the default host and port. Assuming you have downloaded and installed MongoDB, you can start it like so:
 `mongod`

## Hogwarts CRM


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


### Flask Milestone1:


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

### Flask Milestone2:
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

#### MongoDB Milestone1:


Refactor the existing implementation:
At this point we stop using the file system in order to persist data.
We will persist the Hogwarts related data to the mongoDB database.


Create a class called MongoDataLayer.
This class (instance) can only be accessed from within the previously created data layer.


Create all the mongo collections required in order to persist and fetch the CRM data.
The mongoDB database should be called: hogwarts

Within the MongoDataLayer class create all the required functions for adding / updating / fetching/ deleting  data in/ from  mongoDB.
These functions will be called by corresponding functions that were previously defined within the Data layer class.


Data fetched from the DB should be converted to a class instance whenever possible.
E.g. loading a student from DB: after fetching the data from the student collection, the fetched student dictionary data should be converted to a class instance. 


At this point we will stop using the  @app.before_first_request
in order to load previously saved data into the dictionary of the data layer.
whenever we need data we will fetch it directly from the database and serve it to the client.
Whenever we need to persist data we will save it directly to the database.
At this point we will stop using any dictionary objects within the data layer class. 


Within the data layer class create a new function that will take the student data which is stored within the students.json file (in the file system) and persist all the students in the mongoDB database using the MongoDataLayer class.
After migrating all the student.json data, you may delete the student.json file from the file system and git repository.


Make sure not to return the password field value to the client (React).

#### MongoDB Milestone2:


Within the previously created MongoDataLayer class,
create the functions for fetching data for the dashboard:
* Counting how many students have each existing skill.
* Counting how many students have each desired skill.
* Counting how many students were added per day

The functions will use mongoDB aggregation queries in order to fetch the data.


Create a backup file of the hogwarts database.
Either using mongodump or mongoexport commands.
The backup files should be stored in a folder named: db_backup.
* https://docs.mongodb.com/manual/tutorial/backup-and-restore-tools/
*https://www.tutorialspoint.com/mongodb/mongodb_create_backup.htm#:~:text=To%20create%20backup%20of%20database,backup%20of%20your%20remote%20server.


Implement a Flask shutdown “hook” that will invoke a function within the data layer class, that in turn will  call a mongoDataLayer function to close the pymongo client.


Ninja: Within the previously created MongoDataLayer class,
create the functions for fetching data for the following requirements:
* get the 5 most recently updated students.
* get the 5 least recently created students.
* get students with the same last name and different first name.
* get students which do not have any existing skill with level 5.

Within api.py create corresponding routes for the newly created functions. 


## Hogwarts CRM- SQL

Let’s revise the Hogwarts CRM project to use SQL Database.

Using the following entities: 

Students
Admin Users
Magic Skills
Existing Magic Skills
Desired Magic Skills

### Day 1

Create an Entities Relationship Diagram (ERD) of all entities of the Hogwarts CRM and the relationships between them.
Consider when to use one to one relationships,
when to use one to many relationships,
And when to use many to many relationships.

You can choose whichever tool you prefer for the drawing. 


Create a new Mysql schema (database) called Hogwarts . 

Create the database tables representing the different entities from the ERD. 
Don’t forget to include foreign keys when required.


Create a new GIT branch called: mysql_integration
Make sure you commit your code to this branch.


Create a class called MysqlDataLayer which will use the python mysql connector in order to communicate with the Mysql Database.


Create the required functions in order to populate data into the database tables.


Create the functions to delete specific rows in a specified table in the database.


Create the functions to delete all rows in a specified table in the database.

### Flask Milestone3:
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


###  Flask Milestone4:
Remove the empty implementations from the flask routes in api.py
And using the functions previously created in the dataLayer class
implement all the required functionalities for all of the flask routes.
(At this point we are connecting between api.py flask app routes and the DataLayer functions).


All routes will return jsons (either single or lists of jsons).

Ninja:
After a new student process has ended successfully, send email to the student’s email account, with the credentials.


[https://pymongo.readthedocs.io/en/stable/tutorial.html]: https://pymongo.readthedocs.io/en/stable/tutorial.hztml