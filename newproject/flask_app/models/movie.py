from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

class Movie:

    db = "movie_schema"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.rating = data['rating']
        self.release_date = data['release_date']
        self.author_id = data['author_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO movies (title, rating, description, release_date, author_id, created_at, updated_at) VALUES (%(title)s, %(rating)s, %(description)s, %(release_date)s, %(author_id)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM movies;"
        results = connectToMySQL(cls.db).query_db(query)
        if not results:
            return []
        movies = []
        for movie in results:
            movies.append(cls(movie))
        return movies

    @classmethod
    def get_movie_with_author(cls, data):
        query = "SELECT * FROM movies JOIN users ON users.id = movies.author_id WHERE movies.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if not result:
            return False
        movie_instance = cls(result[0])
        user_data = {
            "id": result[0]['users.id'],
            "first_name": result[0]['first_name'],
            "last_name": result[0]['last_name'],
            "email": result[0]['email'],
            "password": result[0]['password'],
            "created_at": result[0]['users.created_at'],
            "updated_at": result[0]['users.updated_at']
        }
        user_instance = user.User(user_data)
        movie_instance.user = user_instance
        return movie_instance

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM movies WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE movies SET title = %(title)s, rating = %(rating)s, release_date = %(release_date)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM movies WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_movie(movie):
        is_valid = True
        if len(movie['title']) < 1:
            is_valid = False
            flash('Please enter a title')
        if len(movie['rating']) < 1:
            is_valid = False
            flash('Please enter a rating')

        return is_valid
        