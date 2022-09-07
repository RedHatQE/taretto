from sentaku import ImplementationContext as _SentakuImplementationContext
from sentaku import ContextualMethod, ContextualProperty, Element, Collection

__all__ = ["ContextualMethod", "ContextualProperty", "Element", "Collection"]


# subclass to have a custom dectate registration point
class ImplementationContext(_SentakuImplementationContext):
    pass
