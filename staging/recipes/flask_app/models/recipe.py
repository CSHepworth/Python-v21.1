from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    
    db = "recipes_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under30 = data['under30']
        self.author_id = data['author_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under30, author_id, created_at, updated_at) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under30)s, %(author_id)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_by_name(cls, data):
        query = "SELECT * FROM recipes WHERE name = %(name)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_by_author(cls, data):
        query = "SELECT * FROM recipes WHERE author_id = %(author_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])