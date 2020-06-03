.. _install_nano_win:

Making your text Editor work with git on Windows
================================================

By default, git will dump you into the "vim" editor when you make a commit.

"vim" is a venerable old Unix tool that no one but Unix geeks can make any sense of.

So you are likely to want to use something else.

git can be configured to use any editor you like.

Here are some options:

Notepad:
--------

https://github.com/github/GitPad/

Sublime Text:
-------------

http://stackoverflow.com/questions/32282847/opening-sublime-text-from-windows-git-bash

Notepad++
---------

https://danlimerick.wordpress.com/2011/06/12/git-for-windows-tip-setting-an-editor/

Nano
----

This was a nice way to go -- but unfortunately, there no longer seems to be a Windows binary available for nano.

For all Windows installations, download the WinNT/9x binary from here:

http://www.nano-editor.org/download.php

Unzip the file and move the files into the git bin directory: C:\Program Files\Git\bin

That's it! You should now be able to use nano from git bash:

.. code-block:: bash

    $ nano test.txt

Command shortcuts are helpfully written in the editor!