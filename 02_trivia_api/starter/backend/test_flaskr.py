import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        

        self.database_name = "trivia_test"
        self.database_path = 'postgresql://postgres:root@localhost:5432/{}'.format(self.database_name)
        
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    test for each test for successful operation and for expected errors.
    """

    # Testing getting all categories
    def test_get_categories(self):
        res = self.client().get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["categories"])

    # Testing getting all questions paginated
    def test_get_questions(self):
        res = self.client().get("/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["totalQuestions"])
        self.assertTrue(len(data["questions"]))
        self.assertTrue(data["categories"])

    # Testing case for 404 error - for requesting an invalid page
    def test_404_requesting_beyond_valid_page(self):
        res = self.client().get("/questions?page=500")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    # Testing deleting a question by id
    def test_delete_question(self):
        res = self.client().delete("/questions/17")
        data = json.loads(res.data)

        question = Question.query.get(28)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(question, None)

    # Testing case for 422 error - deleting a non existed question
    def test_422_not_exist_question(self):
        res = self.client().delete("/questions/40000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    # Testing posting a new question
    def test_post_question(self):
        res = self.client().post("/questions", json={"question":"Hello", "answer":"Checking", "category":4, "difficulty":3})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    # Testing case for 422 error - posting an invalid question
    def test_422_invalid_question(self):
        res = self.client().post("/questions", json={"question":"", "answer":"", "category":"", "difficulty":""})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    # Testing searching a question
    def test_search_question(self):
        res = self.client().post("/questions", json={"searchTerm": "title"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])

    # Testing getting questions of a specific category
    def test_get_category_questions(self):
        res = self.client().get("/categories/4/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])

    # Testing case for 422 error - getting non existed category
    def test_422_invalid_category(self):
        res = self.client().get("/categories/10000/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    # Testing posting quizzes
    def test_post_quizzes(self):
        res = self.client().post("/quizzes", json={"previous_questions": [1, 2], "quiz_category": "History"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["question"])

    # Testing case for 422 error - invalid quiz
    def test_422_invalid_quiz(self):
        res = self.client().post("/quizzes", json={"previous_questions": 22, "quiz_category": 2})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()