.. taretto documentation master file, created by
   sphinx-quickstart on Wed May  9 13:19:16 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Taretto's documentation!
===================================

.. warning::

  **EARLY PRE-RELEASE**
  This version of Taretto is an early pre-release which is likely to change drastically until
  version 0.5.

Taretto is a collection of tooling to assist in performing functional testing of applications.
The tools are designed to be used either separately or in combination with each other. For some
tools, their integration is strong, others are more standalone. Currently Taretto offers the
following tools:

* **Navmazing** - A tool design to build up complex navigation trees from simple steps. You define
  navigation *destinations*, including a way to check if you are already at the destination already,
  a prerequisite, and a step to take once the prerequisite is reached. Navmazing will then navigate
  to a destination by chaining the prerequisites together, skipping out early if it detects it is
  already there.
* **Widgetastic** - If you have the requirement to describe and interact with web based forms and
  user interfaces, Widgetastic can simplify and maximise code reuse. The system has a powerful
  View system to enable conditional view based on the values of widgets on the page. Widgetastic
  comes with support for basic HTML elements as well as the PatternFly library. More UI frameworks
  are planned in the future.
* **Sentaku** - This tool allows you to specify multiple methods on an object with the same name and
  then let the system decide which one to run based on either a context that you specify, or a
  predefined preferential list. This allows you to support multiple implementations, ie REST, UI,
  SSH, for a single object method, and have the system pick which one to use. The beauty of this
  approach is that your test body can be the same for each implementation and the context will
  dictate which implementation of hte method will be run.

In the future, Taretto is hoping to provide tooling for

* **Browser management**
* **pytest helpers**
* **Collections and Entities Modelling**

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   guides

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
