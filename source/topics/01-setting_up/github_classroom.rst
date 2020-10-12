.. _github_classroom:

#############################
Working with GitHub Classroom
#############################

The Python Certificate program uses `GitHub Classroom <https://classroom.github.com/>`_ to manage the submission and review of your coding assignments.


Why GitHub Classroom?
=====================

A software development project is all about continuous improvement:

1. An opportunity is identified.

2. Some initial code is written to address that opportunity.

3. Feedback is provided for that code.

4. The code is modified to create that feedback.

5. A final version of the code is released.

Steps 3-4 will be repeated multiple times until the development team (which could even be a single developer) deems it is ready for release.

In this course, you will not only learn about Python but also about the development process that most Python projects go through. GitHub Classroom allows for the steps indicated above to be completed in an academic environment.

Initial setup
=============

You will need an account on GitHub to participate in this course.
If you don't have already have a GitHub account or if you would prefer to create a new one for this course, make sure you setup a new account on `GitHub <https://github.com/>`_. Always keep in mind that your account name will be part of the private repositories that will be created for each of your assignments and it will be visible to both your instructors and your classmates.

You will need to have git setup on the computer you will use for developing your code for this course.
You can find instructions for setting up git (and the rest of your development environment) here:

:ref:`installing_python`

Once you have all the tools set up, you will need to create a folder (directory) within your development system for keeping your work.
This is the folder where all your assignment repositories will reside. It will be helpful to keep them all together in one place.


Accepting an assignment
=======================

Each assignment page will contain a section named "Accepting your Assignment". Click on the corresponding link, which will take you to GitHub Classroom to accept the corresponding assignment.


Some things to consider:
------------------------

* You will need to accept each assignment separately.

* Accepting an assignment will trigger the creation of a private repository for you to work on your assignment.

* This repository is only assigned to you.

* Any work you do there will not affect the work of your classmates.

* The name of the new repository will include your GitHub user name at the end.

Once your repository has been created, go to its link and clone it on your development system, under the folder you selected for this purpose.

Here: `Cloning a repo <https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository>`_
is GitHub's official guide on how to clone a repository.


Before You Start Working on your Assignment
===========================================

Once your repository is setup, it's good to get familiar with your repository view.
You should see a tab there called "Pull Requests": they indicate code changes that are desired to be pulled into a main repository.
By default you should see one already there called "Feedback". Go ahead and click on it, and take a look at "Files Changed" tab - as of now it should show "No changes to show". As you start committing your code you will see your changes there.


Committing your code
====================

A "commit" is snapshot of your code (and any other files included in your project).
You are encouraged to make frequent commits, as this will make it easier for you to restore your code to an earlier state if things go wrong.


Creating a New Commit:
----------------------

Type the following to add all files and subdirectories in the folder to your commit (note the command includes a dot, make sure you  include it as well: the dot means "the current working directory")::

  git add .

NOTE: this can be a bit dangerous, as it will add everything! It's usually a bit safer to specifically add the file(s) you want to add::

  git add some_code.py

After adding the file(s), you can commit your code by typing the following::

  git commit -m "Commit message"

Note that the commit message should be replaced with something descriptive of what that commit includes ("added new functionality", "fixed floating point error", "ready for review", etc.) that will later help you remember what that particular commit was about.

After every change to the file, you will need to "commit" the changes.

You can always know what state git is in by using the "git status" command::

  git status

It's a good idea to do that before committing, so you know what will happen.


Pushing Your Code
=================

"Pushing" refers to the process of synchronizing the commits you have made on your development system with your GitHub repository.
This is an important process, since it is needed before you can submit your code for review.
Also, it makes a copy of your code in your GitHub account that you can later use to restore it if your local development system fails.

You can push your code immediately after every commit or do it once a day (in which case, several commits will be included in a single push). To do it, simply type::

  git push

The first time you push your code to a repository, GitHub will ask you to select the remote repository (i.e., your GitHub repository). Just copy the suggested push command (you will only need to do this once per assignment).

git will also ask you for your gitHUb username and password the first time -- it should remember them after that -- until you try on a new machine.

Asking Coding Questions
=======================

While working on your code, you might run into a situation in which you would like one of the instructors to look at it and provide some feedback before actually reviewing and grading it.
In order to do that, go to "Feedback" pull request and write a comment about your question or issue. You should make sure to tag your instructor in your comment, to assure that they are notified of your comment. This is done by writing `@the_instructors_github_handle`, e.g. `@natasha-aleksandrova`.

For example::

  @natasha-aleksandrova: I need some help on line 20

When you submit a comment with a tag, the instructor will be notified by GitHub and will be able to review your question.


Submitting your assignment
==========================

Once your assignment is ready for review, copy the link of your Feedback pull request and submit it in the submission form. Here is an example of a submission link (yours will look a little different but will end with `/pull/1`)::

  https://github.com/UWPCE-Py210-SelfPaced-2021/lesson-02-fizzbuzz-exercise-uw-test-student-natasha/pull/1

As per UW's requirements, you also need to submit a zip file with your code on EdX or Canvas. Note that only the code included in your pull request will be reviewed.


Resubmitting your Assignment
============================

On occasion, your instructor will provide feedback on elements in your assignment that need to be modified in order to get the full grade for the assignment. In those cases, follow the process outlined in the Asking Coding Questions section above. Let us know that you would like another review for grade adjustment and make sure to tag your instructor.

Happy coding!
