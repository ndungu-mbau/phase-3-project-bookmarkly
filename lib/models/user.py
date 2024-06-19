from db import conn, cursor


class User:

    def __init__(self, id, email, username):
        self.id = id
        self.email = email
        self.username = username

    def __repr__(self):
        return f"<User: {self.email} {self.username}>"

    # class method responsible for creating the database table
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            email TEXT NOT NULL,
            username NOT NULL
            )
        """

        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS user;
        """

        cursor.execute(sql)
        conn.commit()

    # when saving data into a database table, we need an instance of the class- hence an instance method
    # we use bounded params to avoid directly passing malicious characters and gettig sql injections
    def save(self):
        # we dont need to pass in the id in the query because it is auto incrementing.
        sql = """
            INSERT INTO user (
            email, username
            ) VALUES (?, ?)
        """

        cursor.execute(
            sql,
            (self.email, self.username),
        )
        conn.commit()
        # update the object to contain the auto generated id from the db
        # this id will be required on other queries like update and delete
        self.id = cursor.lastrowid
        # print(f"The last row id: {cursor.lastrowid}")

    # create a class method that automatically creates the instance and saves it in the db
    # class method because the object doesnt yet exist when we call this method
    @classmethod
    def create(cls, email, username):
        # create a category instance
        user = cls(cursor.lastrowid, email, username)

        # save the instance
        user.save()

        # return the instantiated object
        return user

    # method to update an existing record that corresponds to the object instance
    def update(self):
        sql = """
            UPDATE user SET email = ?, username = ?
            WHERE id = ?
        """

        cursor.execute(
            sql,
            (
                self.email,
                self.username,
                self.id,
            ),
        )

        conn.commit()

    def delete(self):
        sql = """
            DELETE FROM user
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()

    @classmethod
    def find_all(cls):
        sql = """
            SELECT * FROM user
        """

        cursor.execute(sql)
        results = cursor.fetchall()

        return [cls(*result) for result in results]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM user
            WHERE id = ?
        """

        cursor.execute(sql, (id,))
        result = cursor.fetchone()

        return cls(*result)

    @classmethod
    def find_by_email(cls, email):
        try:
            sql = """
                SELECT * FROM user
                WHERE email = ?
            """

            cursor.execute(sql, (email,))
            result = cursor.fetchone()

            return cls(*result)
        except Exception:
            print(f"User does not exist with email: {email}")
