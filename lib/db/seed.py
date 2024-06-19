from models import Bookmark, Category, User

usr = User.create("test@mail.com", "test")
cat = Category.create("test", "test")
bookmark = Bookmark.create("test", "test", usr.id, cat.id)
