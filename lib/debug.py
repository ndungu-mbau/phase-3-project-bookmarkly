from models import Bookmark, Category, User

print("Running from debug.py")

usr = User.create("test@mail.com", "test")
cat = Category.create("test", "test")
bookmark = Bookmark.create("test", "https://test.domain", usr.id, cat.id)

usr_2 = User.create("test@mail.com", "test")
cat_2 = Category.create("test", "test")
bookmark_2 = Bookmark.create("test", "https://test.domain", usr.id, cat.id)

print(f"Bookmarks: {Bookmark.find_all()}")
print(f"Categories: {Category.find_all()}")
print(f"Users: {User.find_all()}")

# User
found_user_email = User.find_by_email(usr.email)
found_user_id = User.find_by_id(usr.id)

print(f"Found user by email: {found_user_email}")
print(f"Found user by id: {found_user_id}")

# Category
found_cat_id = Category.find_by_id(cat.id)
found_cat_title = Category.find_by_title(cat.title)

print(f"Found category by id: {found_cat_id}")
print(f"Found category by title: {found_cat_title}")

# Bookmark
found_bookmark_id = Bookmark.find_by_id(bookmark.id)
found_bookmark_by_url = Bookmark.find_by_url(bookmark.url)
found_bookmark_by_user = Bookmark.find_by_user(bookmark.user)
found_bookmark_by_category = Bookmark.find_by_category(bookmark.category)

print(f"Found bookmark by id: {found_bookmark_id}")
print(f"Found bookmark by url: {found_bookmark_by_url}")
print(f"Found bookmark by user: {found_bookmark_by_user}")
print(f"Found bookmark by category: {found_bookmark_by_category}")
