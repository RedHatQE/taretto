import attr
import sentaku
from .ux import TodoUX

ViaAPI = sentaku.ImplementationName('API')
ViaUX = sentaku.ImplementationName('UX')
ViaRPC = sentaku.ImplementationName('RPC')


class TodoAPI(sentaku.ImplementationContext):
    """example description for a simple todo application"""

    @classmethod
    def from_api(cls, api):
        """
        create an application description for the todo app,
        that based on the api can use either tha api or the ux for interaction
        """
        ux = TodoUX(api)
        from .pseudorpc import PseudoRpc
        rpc = PseudoRpc(api)

        return cls({ViaAPI: api, ViaUX: ux, ViaRPC: rpc})

    create_collection = sentaku.ContextualMethod()


@attr.s
class TodoItem(sentaku.Element):
    """describing a todo list element"""
    name = attr.ib()
    completed = sentaku.ContextualProperty()


@TodoAPI.external_for(TodoAPI.create_collection, ViaAPI)
@TodoAPI.external_for(TodoAPI.create_collection, ViaUX)
def create_todo_collection(self, name):
    self.impl.create_item(name)
    return TodoCollection(self, name=name)


@attr.s
class TodoCollection(sentaku.Collection):
    """domain object describing a todo list"""
    name = attr.ib()
    create_item = sentaku.ContextualMethod()
    get_by = sentaku.ContextualMethod()
    clear_completed = sentaku.ContextualMethod()


@TodoAPI.external_for(TodoItem.completed.setter, ViaAPI)
@TodoAPI.external_for(TodoItem.completed.setter, ViaUX)
def completed(self, value):
    col = self.impl.get_by(self.parent.name)
    elem = col.get_by(self.name)
    elem.completed = value


@TodoAPI.external_for(TodoCollection.create_item, ViaAPI)
@TodoAPI.external_for(TodoCollection.create_item, ViaUX)
def create_item(self, name):
    collection = self.impl.get_by(self.name)
    elem = collection.create_item(name=name)
    assert elem
    return TodoItem(self, name=name)


@TodoAPI.external_for(TodoCollection.get_by, ViaAPI)
@TodoAPI.external_for(TodoCollection.get_by, ViaUX)
def get_by(self, name):
    collection = self.impl.get_by(self.name)
    elem = collection.get_by(name)
    if elem is not None:
        return TodoItem(self, name=name)


@TodoAPI.external_for(TodoCollection.clear_completed, ViaUX)
@TodoAPI.external_for(TodoCollection.clear_completed, ViaAPI)
def clear_completed(self):
    collection = self.impl.get_by(self.name)
    collection.clear_completed()
