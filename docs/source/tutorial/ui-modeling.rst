Tutorial Part 1: UI Modeling
============================

Creating a view of your page:

.. code-block:: python

   class MyPage(View):
       breadcrumb = Breadcrumb()
       first_name = TextInput("first_name")
       save = Button("Save")
