from models import Bookmark


class BookmarkController:
    @classmethod
    def create(cls, email, category) -> Bookmark:
        bookmark = Bookmark.create(email, category)
        current_bookmark = bookmark
        return current_bookmark

    @classmethod
    def update(cls, id, bookmarkname, email) -> Bookmark:
        bookmark = Bookmark.find_by_id(id)
        bookmark.email = email
        bookmark.bookmarkname = bookmarkname
        bookmark.update()
        return bookmark

    @classmethod
    def find_by_email(cls, email) -> Bookmark:
        bookmark = Bookmark.find_by_email(email)
        current_bookmark = bookmark
        return current_bookmark

    @classmethod
    def find_by_id(cls, id) -> Bookmark:
        bookmark = Bookmark.find_by_id(id)
        current_bookmark = bookmark
        return current_bookmark

    @classmethod
    def find_all(cls) -> list:
        bookmarks = Bookmark.find_all()
        return bookmarks
