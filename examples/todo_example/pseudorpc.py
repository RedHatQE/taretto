"""
a hideous rpc interface used to demonstrate partial implementation
"""
import attr
from . import spec


@attr.s
class PseudoRpc(object):
    """a hideous implementation"""

    _backend = attr.ib(repr=False)

    def make_collection(self, collection):
        """creates a todo list"""
        self._backend.create_item(collection)

    def make_item(self, collection, name):
        """creates a todo list element"""
        self._backend.get_by(collection).create_item(name)

    def has_item(self, collection, name):
        """checks for the existence of a todo list element"""
        return self._backend.get_by(collection).get_by(name) is not None

    def complete_item(self, collection, name):
        """marks a todo list element as completed"""
        self._backend.get_by(collection).get_by(name).completed = True

    def clear_completed(self, collection):
        """clears the completed elements of a todo list"""
        self._backend.get_by(collection).clear_completed()


@spec.TodoAPI.external_for(spec.TodoItem.completed.setter, spec.ViaRPC)
def todo_item_set_item_completion(item, value):
    if value:
        item.impl.complete_item(item.parent.name, item.name)
    else:
        raise NotImplementedError('rpc cant undo completion')


@spec.TodoAPI.external_for(spec.TodoCollection.create_item, spec.ViaRPC)
def create_todo_item(coll, name):
    coll.impl.make_item(coll.name, name)
    return spec.TodoItem(coll, name=name)


@spec.TodoAPI.external_for(spec.TodoCollection.get_by, spec.ViaRPC)
def get_by(self, name):
    if self.impl.has_item(self.name, name):
        return spec.TodoItem(self, name=name)


@spec.TodoAPI.external_for(spec.TodoCollection.clear_completed, spec.ViaRPC)
def clear_completed(coll):
    coll.impl.clear_completed(coll.name)


@spec.TodoAPI.external_for(spec.TodoAPI.create_collection, spec.ViaRPC)
def create_collection(api, name):
    api.impl.make_collection(name)
    return spec.TodoCollection(api, name=name)
