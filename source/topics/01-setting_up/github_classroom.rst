.. _gitHub_classroom:

#############################
Working with gitHub Classroom
#############################

The Python Certificate program uses `gitHub Classroom <https://classroom.github.com/>`_ to manage the submission and review of your coding assignments.


Why gitHub Classroom?
=====================

A software development project is all about continuous improvement:

1. An opportunity is identified.

2. Some initial code is written to address that opportunity.

3. Feedback is provided for that code.

4. The code is modified to create that feedback.

5. A final version of the code is released.

Steps 3-4 will be repeated multiple times until the development team (which could even be a single developer) deems it is ready for release.

In this course, you will not only learn about Python but also about the development process that most Python projects (and virtually any other programming language) go through. gitHub Classroom allows for the steps indicated above to be completed in an academic environment.

In short: you will be using real professional tools and workflow when doing the work for this program. Be patient -- it is a lot to learn, but the goal is for you to learn useful skills, not to complete the coursework as easily as possible.


Initial Setup
=============

You will need an account on gitHub to participate in this course.
If you don't already have a gitHub account, or if you would prefer to create a new one for this course, make sure you setup a new account on `gitHub <https://github.com/>`_. Always keep in mind that your account name will be part of the private repositories that will be created for each of your assignments and it will be visible to both your instructors and your classmates. Make sure you let your instructors know what your gitHub handle is -- it's not always obvious!

You will need to have git setup on the computer you will use for developing your code for this course.
You can find instructions for setting up git (and the rest of your development environment) here:

:ref:`setup_details`

Once you have all the tools set up, you will need to create a folder (directory) within your development system for keeping your work.
This is the folder where all your assignment repositories will reside. It will be helpful to keep them all together in one place.
This folder (directory) should be somewhere in your "user" or "home" directory.


Accepting an Assignment
-----------------------

On each assignment page in your LMS (Canvas or Edx), there should be a link to the assignment on gitHub classroom. Click on this link, and it should take you to gitHub classroom, and allow you to "Accept this Assignment".


Possible Confusions:
....................

The first time you accept an assignment, gitHub will "invite" you to join the class organization. You will need to click the link to accept the invitation. Once you have done that the first time, you shouldn't need to do it again. However, gitHub seems to get confused, and may continue to tell you about the invitation. You can ignore it if the invitation is working.


When accepting the assignment, gitHub will take a little while to set it up. after waiting a minute or two, you can refresh the browser window, and you should get a link to your assignment repo. If you get an error you can do what it suggests, and go back and try to accept the assignment again. It usually works after a try or two.


Some Things to Consider
.......................

* You will need to accept each assignment separately.

* Accepting an assignment will trigger the creation of a new gitHub repository for you to work on your assignment. That repository will be in your gitHub account. By default it is "private", so that only you and the instructors will be able to see it.

* This repository is only assigned to you.

* Any work you do there will not affect the work of your classmates.

* The name of the new repository will include your gitHub user name at the end.

Once your repository has been created, go to its link (provided by gitHub) and clone it on your development system, under the folder you selected for this purpose.

Here: `Cloning a repo <https://docs.github.com/en/gitHub/creating-cloning-and-archiving-repositories/cloning-a-repository>`_
is gitHub's official guide on how to clone a repository.

.. _gitHub_classroom_workflow:

gitHub Classroom Assignment Workflow
====================================

The following is the workflow you will need to follow for each individual assignment.


1) Accept the Assignment
------------------------

The first step is to click on the link for the assignment in your LMS -- that will take you to gitHub classroom, where you can accept the assignment.

When you accept, gitHub will create a new repository for the assignment in your gitHub account.


2) Clone the Repo
-----------------

Once the repository has been created on gitHub, you need to make a copy, or "clone" of it on your local workstation, where you will be writing your code.


a) Click on the "Code" button in gitHub:

.. image:: images/gitHubclassroom/code_button.png
..   :width: 600

b) Copy the "https: " url that shows up -- you can click the little clipboard icon to copy -- or highlight and copy the url

.. image:: images/gitHubclassroom/clone_url.png
..   :width: 600

c) Go to your command line in the terminal application (Terminal, git bash, CMD prompt, etc). Make sure you are "in" the directory that you have set up for this class. ``ls``, ``dir`` and ``pwd`` can be helpful to make sure.

d) Clone the repo

::

   git clone https://github.com/UWPCE-Py310-Fall2020/the_assignment_url.git

(you should be able to type ``git clone`` and then paste the url you copied from gitHub)

This will create a new directory for the repository, named by the assignment and your gitHub handle -- this is where you will put all the work for that assignment.


3) Create a develop branch for your work
----------------------------------------

Create and check out a new branch for your work.

a) Change the working directory to the repo just created by the clone:

::

  cd the_name_of_the_assignment_repo

b) Make a new branch:

::

  git checkout -b develop

After that command, git will be "in" the develop branch -- anything you change will only be reflected in that branch.

.. note:: A git "branch" is an independent "version" of your code where you can write and change code, create and delete files, etc, and it will be kept separate from the main code. When you are happy with this version, it can be merged into the main branch. For the purposed of this course, it will not be merged into the main branch until it has been reviewed, and both you and your instructors think its done.

If you get an error from this command that says::

    fatal: A branch named 'develop' already exists

That means two things:

 1) You have already created a develop branch. IN which case you chould already be using it, or you can "check it out" again: `git checkout develop`

or

 2) That branch was created already by gitHub classroom. Which you'd think would be nice, but it turns out that the way it's created doesn't allow the next steps: the Pull Request. THe solution in this case is to use a different name for your working branch, e.g.

::

    git checkout -b develop2

Then be sure to use the "develop2" branch when you make your PR to accept the assignment (see step 7). It doesn't really matter what you call this branch, as long as it's a new one you create.

c) Check the git status

::

  $ git status
  On branch develop
  nothing to commit, working tree clean

That lets you know that you are on the develop branch, and that you haven't made any changes to your files (the "working tree" is the dir and files on your machine)

4) Start the Assignment
-----------------------

a) Add some files. Create a new file or files for the assignment with your text editor. Once they are there, it's a good idea to add them before you do much work on them, but you can add them at any time.

::

  git add a_new_file.py

You can also add all the files in the directory with::

  git add .

But be careful -- only do that if you really want everything added to git.

b) Commit your work. When you have gotten to a good "pause point" in your work: the first feature works, you need help from the instructors, etc, you can "commit" the current state of your project. It's a good idea to check the status first.

::

    $ git status
    On branch develop
    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
        new file:   a_simple_script.py
        new file:   another_file.py
        new file:   install_test.py

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
        modified:   install_test.py

note that in this case, I edited the ``install_test.py`` file after adding it. When you edit a file, git will not track those changes unless you tell it to, which you can do by running ``git add`` again. So ``git add`` tells git that you want it to keep track of that file -- called "staging for commit"::

    $ git add install_test.py 

    $ git status
    On branch develop
    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
        new file:   a_simple_script.py
        new file:   another_file.py
        new file:   install_test.py

(there is no harm done running ``git add`` any number of times on the same file)

Note that after adding the file (again!) it is now ready to be committed::

    git commit -m "adding the initial files"

``-m`` means "message" -- you always need to provide a commit message.

There is a trick to save a step -- you can ask git to commit all changes you've made since the last commit::

    $ git commit -a -m "initial files added"

    [develop 4985f9d] initial files added
     3 files changed, 17 insertions(+)
     create mode 100644 a_simple_script.py
     create mode 100644 another_file.py
     create mode 100644 install_test.py

The ``-a`` means "all". Note that you still need to use ``git add`` to ask git to track a new file that it is not already managing.

5) Push your work to gitHub
---------------------------

All this adding and committing has only affected the repository on your own machine -- gitHub has not been changed.
In order to get your changes up to gitHub you need to "push" them. It's always a good idea to check the status before you push -- to make sure you're ready.

::

    $ git status
    On branch develop
    nothing to commit, working tree clean

Note that I am on the "develop" branch, which is what's wanted, and nothing new to commit -- all my changes have been committed -- it's time to push.

::

    $ git push
    fatal: The current branch develop has no upstream branch.
    To push the current branch and set the remote as upstream, use

        git push --set-upstream origin develop

Hmm -- "fatal" -- I don't like the look of that! But it's pretty simple, really. git is telling you that it doesn't know where to push the code to -- your gitHub version of the repo doesn't have a develop branch. But it tells you want to do to create that branch on gitHub (origin), so do that:

::

    $ git push --set-upstream origin develop
    Enumerating objects: 4, done.
    Counting objects: 100% (4/4), done.
    Delta compression using up to 4 threads
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (3/3), 639 bytes | 319.00 KiB/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    remote: 
    remote: Create a pull request for 'develop' on gitHub by visiting:
    remote:      https://github.com/UWPCE-Py310-Fall2020/initial-setup-PythonCHB/pull/new/develop
    remote: 
    To https://github.com/UWPCE-Py310-Fall2020/initial-setup-PythonCHB.git
     * [new branch]      develop -> develop
    Branch 'develop' set up to track remote branch 'develop' from 'origin'.

Good -- now the local develop branch is hooked up to a develop branch on gitHub. And it even tells you what to do next -- see the "Create a pull request for 'develop' on gitHub by visiting:" -- that's exactly what you need to do!

6) Complete the Assignment
--------------------------

Now it's time to write your code! As you work on it, make commits as you go along. Making a commit is essentially saving the state of your project -- so do it at each good "break point" -- when you have a feature working, or have fixed a bug. Do a ``git push`` every once in a while, to save your work to gitHub.

.. note:: One of the really nice things about using gitHub for this (and your own work) is that now your work is all "in the cloud" -- you can make a clone on any other machine (say one at home and one at work), do work on that machine, push it to gitHub, and then retrieve it from somewhere else. If you want to get changes from gitHub that you don't have locally, you need to "pull" them (opposite of push): ``git pull`` should do it.

7) Make a Pull Request
----------------------

When you are done with the assignment, or are at a state where you need some help, it's time to make a Pull Request (PR).
A PR is a request to "pull" the code you've just written into another branch -- usually the main branch.
In "real" development, this means that you have added a feature or fixed a bug, and want that code to be deployed.
But if you are not the primary developer, or if you work on a team, then the code may need to be reviewed before it's merged into the main branch.
For this class, we are mimicking that workflow, but it is the instructors that will review your code. When the code has been reviewed, we will "Merge" the PR into main, indicating that you have completed the assignment.

You should make the PR when you have finished the assignment, or when you are stuck and need some help. In essence, the PR is a request for review.

Go to the assignment gitHub repo in your browser. It should have a note that you have pushed a develop branch, and a button to click to create a PR:

.. image:: images/gitHubclassroom/compare_and_pr.png

Click the "compare and pull request" button to start making your PR!

After you click that -- scroll down and you can see what has changed -- it will show you the files added or removed, and the individual lines that have changed in each file. Review that, to make sure the changes are what you expect.

.. image:: images/gitHubclassroom/make_pr.png

If so -- put a message in the "leave a comment box", and click "Create Pull Request".

Note that this message is where you can start communicating with the instructors -- it should let them know why you are making the PR.
If you are all done with the assignment, say so.
If you are partially done, but have a question -- put your question in this comment box.

Once you create the PR, gitHub will show you the PR view:

.. image:: images/gitHubclassroom/pr_header.png

This is the same view that your instructors will see. 
If you click on the "conversation" tab, you can see your initial comment and any comments made after the initial PR creation.

If you click on the "files changed" tab, you will see all the changes in this PR. For this class, that should be your entire assignment.

Put a link to the PR in the LMS, to let us know that you have "turned in" the assignment.

8) Wait for review
------------------

Once you make your PR, your instructors will be notified by gitHub (and the LMS), and will review your code. They can make general comments, or comment line by line. When a review is done, you should get an email form gitHub. But you can always go and check the PR yourself and see if anything new is there.

At this point, two things might happen.

* If the work is complete and well done, your instructors will make comments, and merge the PR. This is an indication that you are done.

* If there is still more room for improvement, then your instructors will leave the PR open, and wait for you to push more changes.


14) Update your Code
--------------------

If the instructors request a change, or you just want to improve the code, you can make those changes, commit them, and push them to gitHub.
As long as the PR remains open, any new changes you push to the develop branch will show up in the PR.
Please ping your instructors if you have something new to review, by "tagging" them in a PR comment.
(you need to use their gitHub handle to tag them -- make sure you know what it is.
You can figure out what it is, because they will have been commenting on your PRs). You tag with a ``@`` symbol, like so:

::

  @PythonCHB: I've fixed that issue. Please review again. And I'm a little unclear on line 64 -- why doesn't ``name.upper()`` change the name?

15) After the merge
-------------------

When the assignment is complete and reviewed, your instructors will merge the PR. Then all that code will be in the "main" branch. If you do a ``git pull`` on your machine, and check out the main branch (``git checkout main``) you will see it there.

16) Want to improve it after it's been accepted?
------------------------------------------------

If your instructors approve your code, and merge the PR, but you still want to work on it, do that work in the develop branch, and then push and make a new PR.


.. _gitHub_classroom_workflow_summary:

Workflow Summary
================

I'm sure this seems like a lot, but it will get to be a habit, Here are the steps for each assignment:

 1) Accept the assignment from the gitHub classroom link

 2) Clone the resulting repo onto your work machine (``git clone``)

 3) Make a develop branch (``git checkout -b develop``)

 4) Do the assignment in the develop branch, committing and pushing as you go. (``git add``; ``git commit -a -m "a message"``; ``git push``)

 5) When complete or when you would like some help, make a PR on gitHub, and post a link to the PR in the LMS (Canvas or EdX)

 6) Read and respond to the comments on gitHub from your instructors

 7) Continue working, committing and pushing changes as you go.

 8) When the PR is accepted -- you are done!

Is that so bad?

Remember: this seems like a lot -- but it *does* reflect he real workflow when doing real coding. Even if you work alone, a version control system is a really good idea.


General Advice for working with git and gitHub
==============================================

Committing your code
--------------------

A "commit" is snapshot of your code (and any other files included in your project).
You are encouraged to make frequent commits, as this will make it easier for you to restore your code to an earlier state if things go wrong.


Creating a New Commit:
----------------------

Type the following to add all files and subdirectories in the folder to your commit (note the command includes a dot, make sure you  include it as well: the dot means "the current working directory")::

  git add .

.. note:: Using the "." (dot) can be a bit dangerous, as it will add everything in that directory! It's usually a bit safer to specifically add the file(s) you want to add: ``git add some_code.py``

After adding the file(s), you can commit your code by typing the following::

  git commit -m "Commit message"

Note that the commit message should be replaced with something descriptive of what that commit includes ("added new functionality", "fixed floating point error", "ready for review", etc.) that will later help you remember what that particular commit was about.

.. note:: If you omit the message, git will bring up a text editor to let you write one. If you have not configured git to use another editor, it will be "vi", an venerable old Unix editor that is a real challenge for some. To get out of vi, hit the >escape> key, the a colon and an x: ``:x``. You can configure git to use an editor you are familiar with. See: :ref:`install_nano_win` for how to do that on Windows.

After every change to the file, you will need to "commit" the changes. Keep in mind that git will not commit all the changes you have made, only the ones that are "staged for commit". You can stage them with the ``git add`` command again. So ``add`` means either "add this file" or "stage this file for committing", depending on whether it's already been added or not.

Alternatively, you can tell git to commit any changes you have made, since the last commit, with the "-a" (all) flag::

  git commit -a -m "your message"


You can always know what state git is in by using the "git status" command::

  git status

It's a good idea to do that before committing, so you know what will happen.


Pushing Your Code
-----------------

"Pushing" refers to the process of synchronizing the commits you have made on your development system with your gitHub repository.
This is an important process, since it is needed before you can submit your code for review.
Also, it makes a copy of your code in your gitHub account that you can later use to restore it if your local development system fails, or access it from another system.

You can push your code immediately after every commit or do it once a day (in which case, several commits will be included in a single push). To do it, simply type::

  git push

The first time you push your code to a repository, gitHub may ask you to select the remote repository (i.e., your gitHub repository). Just copy the suggested push command (you will only need to do this once per assignment).

git will also ask you for your gitHub username and password the first time -- it should remember them after that -- until you try on a new machine.

Asking Coding Questions
=======================

While working on your code, you might run into a situation in which you would like one of the instructors to look at it and provide some feedback before actually reviewing and grading it.
In order to do that, go to PR you've created and write a comment about your question or issue. You should make sure to tag your instructor in your comment, to assure that they are notified of your comment. This is done by writing `@the_instructors_gitHub_handle`, e.g. `@natasha-aleksandrova`.

For example::

  @natasha-aleksandrova: I need some help on line 20

When you submit a comment with a tag, the instructor will be notified by gitHub and will be able to review your question.


Submitting your assignment
--------------------------

Once your assignment is ready for review, copy the link of your Feedback pull request and submit it in the submission form. Here is an example of a submission link (yours will look a little different but will end with `/pull/1`)::

  https://github.com/UWPCE-Py210-SelfPaced-2021/lesson-02-fizzbuzz-exercise-uw-test-student-natasha/pull/1


Resubmitting your Assignment
============================

On occasion, your instructor will provide feedback on elements in your assignment that need to be modified in order to get the full grade for the assignment. In those cases, follow the process outlined in the Asking Coding Questions section above. Let us know that you would like another review for grade adjustment and make sure to tag your instructor.

Happy coding!
