from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import movie
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:

    db = "movie_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if not result:
            return False
        else:
            return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            is_valid = False
            flash('First name is too short, must be at least 3 characters')
        if len(user['last_name']) < 3:
            is_valid = False
            flash('Last name is too short, must be at least 3 characters')
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash('bad email')
        if user['password'] != user['confirm']:
            is_valid = False
            flash('passwords must match')

        return is_valid