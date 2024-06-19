from models import Category


class CategoryController:
    @classmethod
    def create(cls, title, description) -> Category:
        category = Category.create(title, description)
        return category

    @classmethod
    def update(cls, id, title, description) -> Category:
        category = Category.find_by_id(id)
        category.title = title
        category.description = description
        category.update()
        return category

    @classmethod
    def delete(cls, id) -> Category:
        category = Category.find_by_id(id)
        category.delete()
        return category

    @classmethod
    def find_by_id(cls, id) -> Category:
        category = Category.find_by_id(id)
        return category

    @classmethod
    def find_by_title(cls, title) -> Category:
        category = Category.find_by_title(title)
        return category

    @classmethod
    def find_all(cls) -> list:
        categorys = Category.find_all()
        return categorys
