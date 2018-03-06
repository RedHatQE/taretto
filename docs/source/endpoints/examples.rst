Examples
=============


.. _mini-example:

Mini example
**************

The mini example demonstrates Sentaku usage
by searching a package on pypi and opening the first result in a browser

.. automodule:: mini_example
  :members:



Todo example
**************


The todo example demonstrates Sentaku usage in a more complex manner.
A Example Todo list manager that has Multiple interfaces and
api differences between them.


Api Reference
--------------

.. toctree::

  example_reference


Structure Description
---------------------

The Todo list example has 3 entrypoints

:py:class:`todo_example.api.TodoApp`
  The Basic implementation as "internal api"
:py:class:`todo_example.ux.TodoUX`
  A pseudo-ux sharing the api with :py:class:`todo_example.api.TodoApp`
:py:class:`todo_example.pseudorpc.PseudoRpc`
  A pseudo RPC exposing the bahaviour using a different api
