About Sentaku
==============

Sentaku_ is a python library that allows objects to dynamically choose their implementation.
Sentaku_ is the Japanese word for choice.

With Sentaku_ it is possible to describe the Elements of the Applocations you interact with
and the actions/attributes they have.
Sentaku_ takes care of chosing the impliementation of the Actions/Attributes.


Installing
----------

::

	pip install sentaku



Use cases
-----------

A common use for such a system is Testing Various layers of an application with the same code,
as well as using different Layers of an Application for Setup/Teardown and for concise acceptance-tests.


A typical use case is Testing your modern html5 application.
Such an application usually consists of different layers.

1. the internal backend api
2. a rest api
3. a rich fronend
4. apis that directly interact with other services the application uses

When doing test setup/teardown it is
desirable to run against the fast backend api or rest API,
while when running the actual acceptance/system tests
it is more desirable to run against the rich user interface or the rest API

.. _Sentaku: http:://pypi.python.org/pypi/sentaku
