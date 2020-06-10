#########################
Working with Github Classroom
#########################


1. Why Github Classroom
=================
A software development project is all about continuous improvement:

An opportunity is identified.
Some initial code is written to address that opportunity.
Feedback is provided for that code.
The code is modified to create that feedback.
A final version of the code is released.
Steps 3-4 will be repeated multiple times until the development team (which could even be a single developer) deems it is ready for release.

In this course, you will not only learn about Python but also about the development process that most Python projects go through. Github Classroom allows for the steps indicated above to be completed in an academic environment.

2. Initial setup
=================
If you don't have a Github account or if you would prefer to use a separate one for this course, make sure you setup a new account on Github (Links to an external site.). Always keep in mind that your account name will be part of the private repositories that will be created for each of your assignments and it will be visible to both your instructors and your classmates.
Setup Git on the computer your will use for developing your code for this course. If you use Windows, you will need to setup Git for Windows (Links to an external site.) if you haven't done so already. 
Select a folder / directory within that development system for keeping your work. This is the folder where all your assignment repositories will reside.
Open Git Bash (if using Git for Windows) or a terminal (Linux and Mac OS), go to the folder selected in step 3 and run:

``git init``

This will setup your folder / directory to house Git repositories.

3. Accepting an assignment
=================
Each assignment page will contain a section named Accepting your assignment, click on the corresponding link, which will take you to Github Classroom to accept the corresponding assignment.

Some things to consider:

You will need to accept each assignment separately.
Accepting an assignment will trigger the creation of a private repository for you to work on your assignment. This repository is only assigned to you. Any work you do there will not affect the work of your classmates.
The name of the new repository will include your Github user name at the end.
Once your repository has been created, go to its link and clone it on your development system, under the folder you selected for this purpose (here (Links to an external site.) is Github's official guide on how to clone a repository).

4. Before you start working on your assignment
=================
Once your repository is setup, it's good to get familiar with your repository view. You should see a tab there called "Pull Requests", they indicate code changes that are desired to be pulled into a main repository; by default you should see one already there called "Feedback". Go ahead and click on it, and take a look at Files Changed tab - as of now it should show "No changes to show". As you start committing your code you will see your changes there.

5. Committing your code
=================
A "commit" is snapshot of your code (and any other files included in your project for that matter). You are encouraged to make frequent commits, as this will make it easier for you to restore your code to an earlier state if things go wrong.

To create a new commit:

Type the following to add all files and subdirectories in the folder to your commit (note the command includes a dot, make sure you  include it as well):
``git add``.

Commit your code by typing the following:
``git commit -m "Commit message"``

Note that Commit message should be replaced with something descriptive of what that commit includes ("added new functionality", "fixed floating point error", "ready for review", etc.), that will later help you remember what that particular commit was about.

6. Pushing your code
=================
"Pushing" refers to the process of synchronizing the commits you have made on your development system into your Github repository. This is an important process, since it is needed before you can submit your code for review. Also, it will allow you to have a copy of your code that you can later use to restore it if your local development system failed.

You can push your code immediately after every commit or do it once a day (in which case, several commits will be included in a single push). To do it, simply type:

git push
The first time you push your code to a repository, Github will ask you to select the remote repository (i.e., your Github repository). Just copy the suggested push command (you will only need to do this once per assignment).

7. Asking coding questions
=================
While working on your code, you might run into a situation in which you would like one of the instructors to look at it and provide some feedback before actually reviewing and grading it. You can go back to "Feedback" pull request and write a comment about your question or issue, you need to make sure you tag your instructor as part of your comment (your instructors username is @natasha-aleksandrova).

For example: "@natasha-aleksandrova I need some help on line 20"

We will get notified via tag, and will be able to review your questions.

8. Submitting your assignment
=================
Once your assignment is ready for review, copy the link of your Feedback pull request and submit it in the submission form. Here is an example of a submission link (yours will look a little different but will end with /pull/1)

https://github.com/UWPCE-Py210-SelfPaced-2021/lesson-02-fizzbuzz-exercise-uw-test-student-natasha/pull/1

As per UW's requirements, you also need to submit a zip file with your code on EdX. Note that only the code included in your pull request will be reviewed.

9. Resubmitting your assignment
=================
On occasion, your instructor will provide feedback on elements in your assignment that need to be modified in order to get the full grade for the assignment. In those cases, follow the process in Asking coding questions. Let us know that you would like another review for grade adjustment and make sure to tag your instructor. 

Happy coding!
