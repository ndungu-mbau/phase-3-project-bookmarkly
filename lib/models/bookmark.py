from db import conn, cursor


class Bookmark:

    def __init__(self, title, url, user, category):
        self.id = id
        self.title = title
        self.url = url
        self.user = user
        self.category = category

    def __repr__(self):
        return f"<Bookmark: {self.title} {self.url}>"

    # class method responsible for creating the database table
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE bookmark (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            user INTEGER NOT NULL,
            category INTEGER NOT NULL
            )
        """

        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS bookmark;
        """

        cursor.execute(sql)
        conn.commit()

    # when saving data into a database table, we need an instance of the class- hence an instance method
    # we use bounded params to avoid directly passing malicious characters and gettig sql injections
    def save(self):
        # we dont need to pass in the id in the query because it is auto incrementing.
        sql = """
            INSERT INTO bookmark (
            title, url, user, category
            ) VALUES (?, ?, ?, ?)
        """

        cursor.execute(
            sql,
            (self.title, self.url, self.user, self.category),
        )
        conn.commit()
        # update the object to contain the auto generated id from the db
        # this id will be required on other queries like update and delete
        self.id = cursor.lastrowid
        # print(f"The last row id: {cursor.lastrowid}")

    # create a class method that automatically creates the instance and saves it in the db
    # class method because the object doesnt yet exist when we call this method
    @classmethod
    def create(cls, title, url, user_id, category_id):
        # create a category instance
        category = cls(title, url, user_id, category_id)

        # save the instance
        category.save()

        # return the instantiated object
        return category

    # method to update an existing record that corresponds to the object instance
    def update(self):
        sql = """
            UPDATE bookmark SET title = ?, url = ?, user = ?, category = ?
            WHERE id = ?
        """

        cursor.execute(
            sql,
            (
                self.title,
                self.url,
                self.user,
                self.category,
                self.id,
            ),
        )

        conn.commit()

    def delete(self):
        sql = """
            DELETE FROM bookmark
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()

    @classmethod
    def fetch_by_id(cls, id):
        sql = """
            SELECT * FROM bookmark
            WHERE id = ?
        """

        cursor.execute(sql, (id,))
        result = cursor.fetchone()

        return cls(*result)

    @classmethod
    def fetch_all(cls):
        sql = """
            SELECT * FROM bookmark
        """

        cursor.execute(sql)
        results = cursor.fetchall()

        return [cls(*result) for result in results]

    @classmethod
    def fetch_by_user(cls, user):
        sql = """
            SELECT * FROM bookmark
            WHERE user = ?
        """

        cursor.execute(sql, (user,))
        results = cursor.fetchall()

        return [cls(*result) for result in results]

    @classmethod
    def fetch_by_category(cls, category):
        sql = """
            SELECT * FROM bookmark
            WHERE category = ?
        """

        cursor.execute(sql, (category,))
        results = cursor.fetchall()

        return [cls(*result) for result in results]
