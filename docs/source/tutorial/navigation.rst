Tutorial Part 2: Navigation
===========================

Set up navigation:

.. code-block:: python

   navigator = Navigate()

   class MyEntity(object):
       def __init__(self, name):
           self.name = name

   @navigator.register(MyEntity, 'All')
   class AllEntities(NavigateStep):
       def am_i_here(self):
           return is_this_step_active()

       def step(self):
           browser.go('/all-entities')
