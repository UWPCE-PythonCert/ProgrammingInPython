.. _git_workflow:

git Workflow
============

Git is a very flexible system that can be used in a lot of different ways to manage code development. This page describes the workflow we are using for this class -- about as simple a workflow as you can have with git.

We start with an overview of the usual process. This overview may be all you need for future work, once you have created your home directory within the students directory.

The instructions following the overview are very explicit for those new to git and the command line.

The usual process
-----------------

This is the usual series of steps you will want to go through when you do a new project / assignment.

First make sure you are on the command line "in" your copy of the class repo.

Remember that ``git status`` is your friend -- when in doubt, run that command to see what's going on in your repo.

1. Make sure you are on the correct branch -- though if you never branch, you'll only need to do this once:

   ``$ git checkout master``

2. Get any changes from class repository -- good to do this whenever you start on something new

   ``$ git pull upstream master``

3. If there are changes merged in from upstream, you want to push them to your repository on GitHub.

   ``$ git push``

4. Make sure you are in your student directory, do some work -- create new files, edit then, etc. Verify you are happy with changes. Check the status of your repo:

   ``$ git status``

    Make sure you add any new files:

   ``$ git add the_name_of_new_file``

   you may want to do something like ``git add *.py`` if there are multiple files to add.

5. Commit the all the changes -- make sure to add a good commit message.

   ``$ git commit -m 'my message here'``

6. Push your changes to your remote github account.

   ``$ git push``

7. If your are ready to submit your work, make a pull request on the gitHub website.

Note that when you are working, you may want to do steps 2-6 far more often than step 7. (Don't go too crazy here, we don't want you to wait until the end of the quarter to get to step 7. ;-))

Now put that to work to get you set up for class:

Required Initial Setup
-----------------------

The first step in getting ready for the class is to create an individual directory for yourself inside the class repository, initiated with a README file. This step is necessary to ensure you have everything setup correctly and understand the process for future assignment submissions. Your instructor can review the workflow and give you early feedback before you start working on your first assignment submission.

When you start a new class project or exercise, you should create a folder within this folder for that particular project (ex. lesson1). You should only ever add things inside your OWN directory -- don't add or change anything anywhere else.

Note that when you start doing projects on your own (outside of classwork), you will want to create a whole new repository for each project.

Create Your Own Working Directory
.................................

The first step is to ``cd`` to the students directory:

``$ cd students``

Then create a directory for yourself. You can use your first name, your gitHub handle (username), or any nickname you like -- just make sure your instructor knows who you are so you can get credit for your work.

``$ mkdir marie_curie``

Switch into that dir:

``$ cd marie_curie``

Adding a new file
.................

Note that git does not track directories -- you do not have to add a new dir to git -- when you add a new file in that dir, git will track where it is.

Now you can do your coding. For this example, that is simply adding a readme file. You can do that with your text editor, or directly on the command line::

    cat > README.rst
    Python code for UWPCE-PythonCert class, written by Marie Curie
    ctrl+D

Now tell git to track that new file:

``git add README.rst``

Once you are done coding, always a good idea to look at what you have done.

``$ git status``

Carefully observe new files or files that you have changed to ensure no other files are being committed outside of your student directory.

Committing your changes
.......................

Commit the changes with a summary of what you have done:

``$ git commit -a -m 'added a readme file'``

Push your changes to your repo on gitHub:

``$ git push origin master``

"origin" is the default name given by git referring to the server you cloned (in this case your github repository)

"master" is the branch that you are currently pushing to that server.

Since these are the default, you can usually simply do:

``git push``

Make a PR
.........

In high level overview, pull request provides a view to see the difference between a source branch (your fork) and a target branch (the main class repo), this view is used for code reviews and to provide feedback to the author. Keep in mind that this view is not static, meaning any subsequent commits to the source branch will show in this diff view.

Now go onto GitHub, and make your first pull request (PR)!

Here is some gitHub help for that:

https://help.github.com/articles/creating-a-pull-request-from-a-fork/

You've pushed your own changes to that fork, and then issued pull requests to have that work merged back to the main class repo in (UWPCE-PythonCert-ClassRepos). An instructor will look at your code, make comments and approve your pull request if your work is satisfactory.

Do that now with just the README file, so we can get the class repo all set up, and so that both you and your instructors know you have your gitHub repo all set up correctly.

Starting a new Exercise
-----------------------

Once you have created your directory, and are starting a new project, the process will look very much the same. This example is for marie_curie working on her mailroom exercise:

Make sure you are "in" your copy of the class repo on your machine:

``$ cd students/marie_curie``

Regardless of what you are working on, first make sure you don't have anything in your repository that you forgot to commit:

``$ git status``

Note that when git status tells you that 'Your branch is up-to-date with 'origin/master',  that does NOT mean that you are up-to-date with stuff that has been pushed to the github repository, only, confusingly, with what your local machine currently knows about.

So, your next step is to make sure you have any changes that other people have made recently to the *remote* repository.

``$ git pull upstream master``

"upstream" is the name we gave to the repository as it sits in the UWPCE github site. If you get an error message, check with the :ref:`git` documentation to make sure you set up the upstream shortcut correctly.

"master" is the branch that you are currently pulling from that server, for the purpose of this class, we will always use master.

If there are changes upstream that you did not have, it is a good idea to go ahead and push these changes to your github account right away so they don't confuse things:

``$ git push``

Now you can begin your work:

create a dir to do the Exercise in:

``$ mkdir mailroom``

(remember to make sure you are creating this new dir in *your own working directory*)

Create your new python file(s) in that new directory. Then add it to git before you start writing any real code -- just to make sure you don't forget:

``$ git add mailroom.py``

Then as you work, each time you get to a good saving point, make a commit:

``git commit -a -m "added the donation listing feature"``

And when you are done, push it to gitHub:

``$ git push``

If you are ready for an instructor to review it, go to your repo on the gitHub website and make a pull request.

Final Thoughts
--------------

We are using gitHub to submit and review your work because it provides a nice interface for code review. But more importantly, because the git revision control system, and the gitHub collaborative code development platform are industry standard tools for developing code.

Learning git is a great skill -- we are only requiring the very basics for this class, but do take the opportunity to explore git a bit more -- making branches, reverting to older versions, etc.

Also -- by doing it this way, you are getting an automatic back up of your work. Each time you "push", a copy of your work is getting backed up on gitHub. And you can also use it to coordinate your work among multiple computers -- you can have as many clones of your repo on gitHub as you like -- say one on a computer at work, and one at home. If you push a change from one computer, then running:

``$ git pull``

on the other will bring that change down.  This makes it really easy to do your classwork (or any work) in multiple places.





