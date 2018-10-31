import importscan

from pkg_resources import iter_entry_points
from taretto.modeling import EntityCollections
from taretto.context import ImplementationContext

from {{cookiecutter.application_name}}.base.application.implementations.web_ui import ViaWebUI


class Application(object):

    def __init__(self, hostname, path="", scheme="https", username="", password=""):
        self.application = self
        self.username = username
        self.password = password
        self.hostname = hostname
        self.path = path
        self.scheme = scheme
        self.web_ui = ViaWebUI(owner=self)
        self.context = ImplementationContext.from_instances([self.web_ui])
        self.collections = EntityCollections.for_application(self, self.load_collections())

    @property
    def address(self):
        return "{}://{}/{}".format(self.scheme, self.hostname, self.path)

    def list_destinations(self):
        """This function returns a list of all valid destinations for a particular object
        """
        return {
            impl.name: impl.navigator.list_destinations(self)
            for impl in self.application.context.implementations.values()
            if impl.navigator
        }

    @staticmethod
    def load_collections():
        return {ep.name: ep.resolve() for ep in iter_entry_points("{{cookiecutter.application_name}}.application_collections")}


from {{cookiecutter.application_name}} import base  # noqa

importscan.scan(base)
