:orphan:

.. _submitting_to_gitHub:

##############################
Submitting your work to gitHub
##############################

In this program, we are using the gitHub source code management system to manage each student's code, as well as examples and solutions.

gitHub is designed as a system to develop collaborative software projects. As such, it is a great tool to learn for your future programming endeavors.

It also has great interface for code review, so provides a system with which the instructors can review and provide feedback on your code.

Starting a New Exercise
=======================

Most Exercise will begin with creating a new python file.

1) Start by creating a folder for the current lesson ("lesson02" or "lesson03", or....)

2) Create your python file and save it into the lesson folder you just created.

3) Once the file exists, it can be added to your local git "repo" to be managed::

      git add the_file.py

4) If the exercise requires more than one file, create them and add each to the manged by git in the same way.

5) As you work, when you have something working that you might want to go back to, commit the changes to your repo. You have two options now -- you can commit everything that you have changed (-a means "all") ::

      git commit -a

   or you can commit only those files that you want to. To do that, you need to "stage" the files you want to commit::

      git add one_file.py another_file.py

   (Yes, it is confusing -- "add" means: "add this file to the ones git is managing" if it's a new file, but "add this file to the ones I want to commit (staged)" if git is already managing the file. In fact, for a new file, you need to do "git add the_file.py" twice!)

   Now you can do::

      git commit

   and the files that are "staged for commit" will be committed to your repo.

   **reminder** -- you can (and frequently should) run::

      git status

   To see what is going on -- it will tell you which files are staged for commit, which files have been modified, and which are not being managed by git at all.

6) Recall that all this git adding and committing is only effecting your local repo -- the one on your local machine. Once you have everything at a point where you want to share it with others (i.e. the instructors, classmates, or yourself on another machine!), you want to "push" it to your gitHub account::

     git push

   Should do it.

   If you are working from multiple machines, and pushing to gitHub, you will need to do::

     git pull

   To get everything that is up on gitHub down to your local machine.

7) Once you have completed the assignment, and are ready to "turn it in" (that is, have the instructors review your work), you need to:

  a) make sure the latest version is in your gitHub account::

       git push

  b) Go to *your* repo in gitHub in a browser.

  c) Submit a "Pull Request" to the class repo:

     (more detail here)

     Make sure to add a note to the PR letting the instructors know which code is ready for review, or of you have any specific questions.

When you submit you PR on gitHub, the instructors will automatically get an email letting them know that you have submitted something.














