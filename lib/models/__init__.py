from category import Category
from bookmark import Bookmark
from user import User

Category.drop_table()
Category.create_table()

Bookmark.drop_table()
Bookmark.create_table()

User.drop_table()
User.create_table()
