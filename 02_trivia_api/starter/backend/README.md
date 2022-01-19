# Backend - Full Stack Trivia API 

### Installing Dependencies for the Backend

1. **Python 3.7** - it is recommended to install the following version of python to run the project without errors [python3.7.9](https://www.python.org/downloads/release/python-379/)

    if you have a higer version like 3.9 or higher do the following 
    1. uninstall 3.9
    2. install python 3.7.9 don't forget to check the add to path while installing
    3. after you install make sure that when typeing python -v  in the termainal it gives you python3.7.9
    4. if the above gives you 3.9 restart the shell and make sure you uninstalled 3.9
    4. reinstall all the requirements again
    then run the app as stated in the document

2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
1. **database creation**  inside psql write the following command to run the database
```postgres
> create database trivia;
```
2. **you can simply copy the contents of trivia.psql and paste them in the psql shell on windows**
or 
* on linux
```bash
psql trivia < trivia.psql
```
* on windows (powershell)
```powershell
> $ENV:PGPASSWORD="<password>"
> cat trivia.psql | psql -U postgres trivia 
```

### Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:
* linux bash
```bash
> export FLASK_APP=flaskr
> export FLASK_DEBUG=1
> flask run --reload
```

* windows powershell
```bash
> $ENV:FLASK_APP="flaskr"
> flask run --reload
```


* windows cmd
```bash
> set FLASK_APP=flaskr
> flask run --reload
```
The `--reload` flag will detect file changes and restart the server automatically.

## ToDo Tasks
These are the files you'd want to edit in the backend:

1. *./backend/flaskr/`__init__.py`*
2. *./backend/test_flaskr.py*


One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 


2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 


3. Create an endpoint to handle GET requests for all available categories. 


4. Create an endpoint to DELETE question using a question ID. 


5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 


6. Create a POST endpoint to get questions based on category. 


7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 


8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 


9. Create error handlers for all expected errors including 400, 404, 422 and 500. 



## Review Comment to the Students
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/api/v1.0/categories'
GET ...
POST ...
DELETE ...

GET '/api/v1.0/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
