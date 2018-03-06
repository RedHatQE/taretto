API Reference for Sentaku
=========================

.. py:currentmodule:: sentaku


.. _implementation-context:

ImplementationContext
------------------------

.. autoclass:: ImplementationContext
  :members:



.. _application-element:

Application Elements
--------------------

Application elements are subclasses of :py:class:`sentaku.Element`.
They describe single Elements of Applications

Elements on a abstract perspective Refer to Collections, Entries and sets of actions.

Depending on implementation they can be listings,
forms, rest collections/data entries, or file contents.


.. autoclass:: Element
  :members:

.. _contextual-method:

Contextual Methods
------------------

.. autoclass:: ContextualMethod()
  :members:


Contextual Properties
---------------------

.. autoclass:: ContextualProperty()
  :members: