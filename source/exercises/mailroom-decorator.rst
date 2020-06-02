.. _exercise_mailroom_decorator:


Mailroom -- Decoratoring it
===========================

We want to know who is making changes to our database, so make a decorator that will ask for a user's name, before making any changes to our donor list. If you want to get really fancy, figure out how to cache the answer, so you don't have to ask more than once per session.

The Goal
--------

Think about which methods will affect the database. Will sending a letter add a user? (Should it? Maybe this is a good time for refactoring.) These are the methods that should get decorated. The decorator should get the user's name. Eventually, we will want to store this permanently, but that is for a different day. However, you might want to figure out how to store it temporarily, so you don't repeatedly ask the same user for their name. This could be done on a timeout basis, or you could assume that the user only changes when the interface is instantiated. 





