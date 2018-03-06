import attr


@attr.s
class TodoElement(object):
    """
    Element of a todo list
    """

    name = attr.ib()
    completed = attr.ib(default=False)


def get_by(self, name):
    """get element by name"""
    return next(
        (item for item in self
         if item.name == name), None)


def create_by_name(cls, collection_name):
    def create_item(self, name):
        "create a new named %r item"
        assert self.get_by(name) is None
        item = cls(name=name)
        getattr(self, collection_name).append(item)
        return item
    create_item.__doc__ %= cls
    return create_item


@attr.s
class TodoList(object):
    """a named todolist"""

    name = attr.ib()
    items = attr.ib(default=attr.Factory(list), convert=list)

    def __iter__(self):
        return iter(self.items)

    get_by = get_by
    create_item = create_by_name(TodoElement, 'items')

    def clear_completed(self):
        """
        removes completed elements
        """
        self.items = [i for i in self.items if not i.completed]


@attr.s
class TodoApp(object):
    """
    A Basic Todo List Storage

    """
    collections = attr.ib(default=attr.Factory(list), convert=list)

    def __iter__(self):
        return iter(self.collections)

    def __repr__(self):
        return '<TodoApp %r>' % (
            sorted(x.name for x in self.collections),)

    get_by = get_by
    create_item = create_by_name(TodoList, 'collections')
