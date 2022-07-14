from distutils.log import error
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash, session

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    db = "email_erd"
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(cls.db).query_db(query)
        emails = []
        for row in results:
            one_email = cls(row)
            emails.append(one_email)
        return emails

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM emails WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_email(data):
        # query = "SELECT * FROM emails WHEN email = %(email)s;"
        # results = connectToMySQL(Email.db).query_db(query, data)

        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Eamil is not valid!", "error")
        # if len(results) >= 1:
        #     is_valid = False
        #     flash("Eamil has been taken", "error")
        else:
            flash(f"The email you entered {data['email']} is a VALID email address! Thank you!")
        return is_valid