
class TodoUX(object):
    """
    example root UX fore todo lists
    """
    def __init__(self, app):
        self.app = app

    def get_by(self, name):
        """get a todo list ux by name

        :rtype: TodoListUX
        """
        item = self.app.get_by(name)
        return TodoListUX(ux=self, controlled_list=item)

    def create_item(self, name):
        """create a new named todo list

        :rtype: TodoListUX
        """
        item = self.app.create_item(name)

        return TodoListUX(ux=self, controlled_list=item)


class TodoListUX(object):
    """
    example ux for single todo lists
    .. attribute:: ux

        reference to the root ux

    .. attribute:: controlled_list

        reference of the todo list implementation

    """

    def __init__(self, ux, controlled_list):
        self.ux = ux
        self.controlled_list = controlled_list

    def get_by(self, name):
        """
        find a todo list element by name
        """
        item = self.controlled_list.get_by(name)
        if item:
            return TodoElementUX(parent=self, controlled_element=item)

    def create_item(self, name):
        """
        create a new todo list item
        """
        elem = self.controlled_list.create_item(name)
        if elem:
            return TodoElementUX(parent=self, controlled_element=elem)

    def clear_completed(self):
        """
        remove all completed elements
        """
        self.controlled_list.clear_completed()


class TodoElementUX(object):
    """
    ux controller element for a todo list element

    .. attribute:: parent

        the controling TodoListUX

    .. attribute:: controlled_element

        the controlled TodoElement

    """
    def __init__(self, parent, controlled_element):
        self.parent = parent
        self.controlled_element = controlled_element

    @property
    def completed(self):
        """
        completion state of the controlled element
        """
        return self.controlled_element.completed

    @completed.setter
    def completed(self, value):
        self.controlled_element.completed = value
