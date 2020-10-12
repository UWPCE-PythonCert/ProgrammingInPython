.. _git:

############
Intro to Git
############

What is Git?
------------

A "version control system"

Why Version Control?
--------------------

.. figure:: http://phdcomics.com/comics/archive/phd101212s.gif

   "Piled Higher and Deeper" by Jorge Cham: www.phdcomics.com

A history of everything everyone does to 'your' code

A graph of "states" in which the code has existed

That last one is a bit tricky, and is not necessary to understand right out of the gate. When you are ready, you can look at this supplement to gain a better understanding:

:ref:`git_overview`

There are other versioning systems, such as Mercurial and Subversion (and commercial offerings), but Git is the most popular.

It is incredibly important to learn and understand version control to work as a developer today, so we have incorporated Git into our work flow for submitting students' work in this class.


Setting up Git
--------------

You should have git installed on your machine and accessible from the command line. If you don't have git working on the command line, revisit the appropriate instructions for your platform here: :ref:`installing_python`.

Once git is installed and working, there is a little bit of setup for git that you should only have to do once:

Letting git know your identity
..............................

.. code-block:: bash

   $ git config --global user.name "Marie Curie"
   $ git config --global user.email "marie@radioactive.com"

(using your email and name, of course)

Editor
......

* git needs an editor occasionally
* default is VI, which is not very intuitive to non-Unix Geeks
* Nano is simple, easy solution for Macs and Linux
* Nano no longer available for windows, use Sublime Text or Notepad++ or Atom

For windows users: :ref:`install_nano_win`

Once you have chosen/installed an editor, configure git to use it:

(full notes here: `GitHub help on Editors <https://help.github.com/articles/associating-text-editors-with-git/>`_)

**nano:**

``$ git config --global core.editor "nano -w"``

**Sublime Text (mac):**

``$ git config --global core.editor "subl -n -w"``

**Sublime Text(win):**

``$ git config --global core.editor "'c:/program files/sublime text 2/sublime_text.exe' -w"``

**Notepad++ (Win):**

``$ git config --global core.editor "'c:/program files (x86)/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"``

**Atom:**

``git config --global core.editor "atom --wait"``

Repositories
------------

A repository is just a collection of files that 'belong together'.

Since ``git`` is a *distributed* versioning system, there is no **primary**
repository that serves as the one to rule them all. This simply means that all repositories on each users machine should look the same.

However, to keep things sane, there is generally one "central" repository chosen that users check with for changes. For us this is the one hosted on GitHub in the UWPCE-PythonCert-ClassRepos organization.


.. Working with Remotes
.. --------------------

.. With git, you work with *local* repositories and the *remotes* that they are connected to.

.. Git uses shortcuts to address *remotes*. When you *clone* a repository from its remote location to your local machine, you get an *origin* shortcut for free:

.. .. code-block:: bash

..   $ git remote -v
..   origin  https://github.com/UWPCE-PythonCert-ClassRepos/ExampleRepo.git (fetch)
..   origin  https://github.com/UWPCE-PythonCert-ClassRepos/ExampleRepo.git (push)

.. This shows that the local repo on my machine *originated* from one in
.. the UWPCE-PythonCert-ClassRepos GitHub account (it shows up twice, because there is a shortcut for both ``fetch`` from and ``push`` to this remote).

GitHub forks
------------

You can work on any project you wish to that has a public repository on GitHub. However, since you won't have permission to edit most projects directly, there is such a thing as *forking* a project.

When you *fork* a repository, you make a copy of that repository in your own (GitHub) account.

When you have made changes that you believe the rest of the community will want to adopt, you make a *pull request* to the original project. The maintainer(s) of that project than have the option of accepting your changes, in which case your changes will become part of that project.

For this class, we are using gitHub classroom -- whihc does the creating and forkin go repos for you, so you proably dont need to use this feature now. 

With one exception: your instructor may use a gitHub repository to manage note3s, examples, and solutions for the class -- if so, it may be helpful to make a fork of that repo, particularly if you want to make suggestions etc.

Another possiblity is if you notice an error, or can suggest a claification in these very pages. They are managed on gitUb as well, in this repo:

https://github.com/UWPCE-PythonCert/ProgrammingInPython

So you may want to fork that repo in order to make suggestions.


Structure of multiple git repos
-------------------------------

Each repository will have a directory called ``.git`` that is normally
not seen. This directory is how git keeps track of everything. Leave it alone. :)

Please do not set up a git repository inside another git repository, this can lead to heartache.

Absolutely, do NOT set up a git repository in your home root directory.
This will put everything in your home directory up on GitHub, and you do not want that.

Setting up new repositories can be confusing because when you clone a git repository it creates the directory that will be the repository, but when you are creating a new repository, you need to first be **IN** the directory in which you want the repository to be rooted. Please ask if this does not make sense.

It’s also important to note that you do not run the ``$ git init`` command at any point in the process of cloning and configuring your local copy of a remote repo. The ``init`` git command is used to initialize a git repository on your local machine and is not necessary in our case because the cloned repository has already been initialized.

Additional Resources:

git tutorial:
https://try.github.io/levels/1/challenges/1

basic git commands:
https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html

