from mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO surveys (name, location, language, comments, created_at, updated_at) VALUES ( %(name)s, %(location)s, %(language)s, %(comments)s, NOW(), NOW() );"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @classmethod
    def get_recent(cls):
        query = "SELECT * FROM surveys WHERE id = (SELECT max(id) FROM surveys);"
        result = connectToMySQL('dojo_survey_schema').query_db(query)
        return cls(result[0])

    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(survey['location']) < 3:
            flash("Location must be at least 3 characters.")
            is_valid = False
        if len(survey['language']) < 1:
            flash("Please Select a Language.")
            is_valid = False
        if len(survey['comments']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid