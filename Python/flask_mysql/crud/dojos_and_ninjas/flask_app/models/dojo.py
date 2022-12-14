from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_dojo_and_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        for ninja_row in results:
            ninja_data = {
                "id": ninja_row['ninjas.id'],
                "first_name": ninja_row['first_name'],
                "last_name": ninja_row['last_name'],
                "age": ninja_row['age'],
                "created_at": ninja_row['created_at'],
                "updated_at": ninja_row['updated_at']
            }
            dojo.ninjas.append( ninja.Ninja(ninja_data))
        return dojo
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name = %(name)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

