from db import conn, cursor


class Category:

    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

    def __repr__(self):
        return f"<Category: {self.title} {self.description}>"

    # class method responsible for creating the database table
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE categories (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description NOT NULL
            )
        """

        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS categories;
        """

        cursor.execute(sql)
        conn.commit()

    # when saving data into a database table, we need an instance of the class- hence an instance method
    # we use bounded params to avoid directly passing malicious characters and gettig sql injections
    def save(self):
        # we dont need to pass in the id in the query because it is auto incrementing.
        sql = """
            INSERT INTO categories (
            title, description
            ) VALUES (?, ?)
        """

        cursor.execute(
            sql,
            (self.title, self.description),
        )
        conn.commit()
        # update the object to contain the auto generated id from the db
        # this id will be required on other queries like update and delete
        self.id = cursor.lastrowid
        # print(f"The last row id: {cursor.lastrowid}")

    # create a class method that automatically creates the instance and saves it in the db
    # class method because the object doesnt yet exist when we call this method
    @classmethod
    def create(cls, title, category):
        # create a category instance
        category = cls(cursor.lastrowid, title, category)

        # save the instance
        category.save()

        # return the instantiated object
        return category

    # method to update an existing record that corresponds to the object instance
    def update(self):
        sql = """
            UPDATE categories SET title = ?, description = ?
            WHERE id = ?
        """

        cursor.execute(
            sql,
            (
                self.title,
                self.description,
                self.id,
            ),
        )

        conn.commit()

    def delete(self):
        sql = """
            DELETE FROM categorie
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()

    @classmethod
    def find_all(cls):
        sql = """
            SELECT * FROM categories
        """

        cursor.execute(sql)
        results = cursor.fetchall()

        return [cls(*result) for result in results]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM categories
            WHERE id = ?
        """

        cursor.execute(sql, (id,))
        result = cursor.fetchone()

        return cls(*result)

    @classmethod
    def find_by_title(cls, title):
        sql = """
            SELECT * FROM categories
            WHERE title = ?
        """

        cursor.execute(sql, (title,))
        result = cursor.fetchone()

        return cls(*result)
