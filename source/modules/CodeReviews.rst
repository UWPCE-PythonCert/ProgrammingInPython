:orphan:

.. _code_review:

############
Code Reviews
############


Why code review
===============
As professional developers, we need to always be learning and improving.

Code review is one of the best tools for this.

Code review is like having a personal tutor.

Code review helps more people to become familiar with the code.

Code review squishes bugs.


Getting code ready for review
-----------------------------

- Write tests - if there are tests, much easier to make changes on the fly during review
- First draft is messy, refactor before code review
- To get the most out of it, correct all that you can before review
- Expect advice and corrections, and learn from them!
- For this class, messy is okay. :-)

Size of code
------------

- Code to review should be between 200 and 400 lines of code
- Code can, and often will, be part of a bigger project
- Code should be modular, so can examine one smallish piece during review:
   - and be able to explain how it fits in the bigger project
   - and be able to explain what the smallish piece is doing in a few sentences


When/Why to review code
-----------------------

- Think your code is ready for production
- Have code working, but seems there is probably a better way
- Totally Stuck
- Having difficulty making it modular, can help you break large chunks into smaller chunks


What to look for
----------------

- readability
- 'pythonic'
- tests
- short functions/methods
- anything not clear
- logic issues


Types of code review
--------------------

- in person
- in-line comments
- using tools https://en.wikipedia.org/wiki/List_of_tools_for_code_review


When refactoring or doing code reviews in person
------------------------------------------------

Write comments explaining what the code is doing (if unclear) and/or questions about the code

Then, if time permits you can jointly:

- work on making the code clearer
- run tests after changes
- goal is to make it clear enough to get rid of the comment(s) that were added

Or do this yourself afterwards, as you would for written code reviews


How this will work in class
---------------------------

- Code can be pretty rough, no judging. :)

- Person having code reviewed will send out link to code (a couple of days out, preferably)

- At the beginning of the code review, reviewee will:

   - give a quick overview of the bigger picture

   - give a quick overview of the specific code we will look at

- We will go over code together. Everyone is encouraged to make comments and ask questions.

Feel free to ask your classmates in slack or on the mailing list about code you are writing. 
This is why you have access to everyone's code, to share and learn from each other.
