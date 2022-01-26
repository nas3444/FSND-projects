# Backend - Full Stack Trivia API 

### Installing Dependencies for the Backend

1. **Python 3.7** - it is recommended to install the following version of python to run the project without errors [python3.7.9](https://www.python.org/downloads/release/python-379/)

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

## API Endpoints

METHOD Url
Request parameters
Response body

### GET '/categories'
* Returns a dictionary of categories
* Request parameters: None
* Response body:
```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "success": true
}
```

### GET '/questions'
* Returns a list of questions with each question include question, answer, category and difficulty
* Request parameters: None
* Response body:
```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "currentCategory": null,
    "questions": [
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        }
    ],
    "success": true,
    "totalQuestions": 22
}
```

### DELETE '/questions/<int:question_id>'
* Delete a specific question by a given ID 
* Request parameters: question_id
* Response body:
```
{
    "success": true
}
```

### POST '/questions'
* Create a new question in the database
* Request parameters: a question object containing question, answer, category and difficulty
* Response body:
```
{
    "success": true
}
```

### POST '/questions'
* Search the database for a question by a search term
* Request parameters: searchTerm
* Response body: when searchTerm = "title"
```
{
    "questions": [
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }
    ],
    "success": true
}
```

### GET '/categories/<int:category_id>/questions'
* Returns a list of questions for a specific category by a given category id
* Request parameters: category_id
* Response body: when category_id = 2
```
{
    "questions": [
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        {
            "answer": "One",
            "category": 2,
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
            "answer": "Jackson Pollock",
            "category": 2,
            "difficulty": 2,
            "id": 19,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        },
        {
            "answer": "Test answer",
            "category": 2,
            "difficulty": 2,
            "id": 24,
            "question": "Test question"
        },
        {
            "answer": "Test answer",
            "category": 2,
            "difficulty": 2,
            "id": 25,
            "question": "Test question"
        },
        {
            "answer": "This is an answer",
            "category": 2,
            "difficulty": 2,
            "id": 31,
            "question": "This is a question"
        }
    ],
    "success": true
}
```

### POST '/quizzes'
* Takes a previous list of questions and a current category and returns a randomize question based on the category with a condition that the question shouldn't be one of the previous questions
* Request parameters: previous_questions, quiz_category
* Response body:
```
{
    "question":
        {
            "answer": "This is an answer",
            "category": 2,
            "difficulty": 2,
            "id": 31,
            "question": "This is a question"
     },
    "success": true
}



## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
