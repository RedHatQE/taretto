quickly combining things
========================

the getting started guide is based on the :ref:`mini-example`


1. importing all the things we need in the example

  .. literalinclude:: ../examples/mini_example.py
    :lines: 10-20

2. implementations the core objects of backends you want to be able to use
   and preparing them.

  .. literalinclude:: ../examples/mini_example.py
    :pyobject: Browser, FastSearch  

3. declaring a context type for your application

  .. literalinclude:: ../examples/mini_example.py
    :pyobject: SearchContext

4. Declaring a element class and a few contextual methods

  .. literalinclude:: ../examples/mini_example.py
    :lines: 40-47

5. registration of the implementations for each backend

  .. literalinclude:: ../examples/mini_example.py
    :lines: 49-74

6. bringing it all together

  .. literalinclude:: ../examples/mini_example.py
    :lines: 76-
