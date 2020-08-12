.. _exercise_trigrams:

====================================
Trigrams -- Simple Text Manipulation
====================================

.. rubric:: Kata Fourteen: Tom Swift Under the Milk Wood

Adapted from Dave Thomas's work:

http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/


Trigrams
=========

Trigrams can be used to mutate text into new, surreal, forms. But what
heuristics do we apply to get a reasonable result?

The Problem
------------

As a boy, one of my treats was go to the shops on a Saturday and spend part
of my allowance on books; for a nine-year old, I had quite a collection of books from the
Tom Swift and Hardy Boys series. Wouldn’t it be great to be able to create
more and more of these classic books, to be able to generate a new Tom
Swift adventure on demand?


OK, perhaps not. But that won’t stop us trying. I coded up a quick
program to generate some swashbuckling scientific adventure on demand. It
came up with:

    ... it was in the wind that was what he thought was his companion. I
    think would be a good one and accordingly the ship their situation
    improved. Slowly so slowly that it beat the band! You’d think no one
    was a low voice. "Don’t take any of the elements and the
    inventors of the little Frenchman in the enclosed car or cabin completely
    fitted up in front of the gas in the house and wringing her hands.
    "I’m sure they’ll fall!"

    She looked up at them. He dug a mass of black vapor which it had
    refused to accept any. As for Mr. Swift as if it goes too high I’ll
    warn you and you can and swallow frequently. That will make the airship was
    shooting upward again and just before the raid wouldn’t have been
    instrumental in capturing the scoundrels right out of jail."


Stylistically, it’s Victor Appleton (pseudonymous author of the Tom Swift series) meets Dylan Thomas (Welsh poet). Technically,
it’s all done with trigrams.

Trigram analysis is very simple. Look at each set of three adjacent words
in a document. Use the first two words of the set as a key, and remember
the fact that the third word followed that key. Once you’ve finished,
you know the list of individual words that can follow each two word
sequence in the document. For example, given the input::

  I wish I may I wish I might

You might generate::

    "I wish" => ["I", "I"]
    "wish I" => ["may", "might"]
    "may I"  => ["wish"]
    "I may"  => ["I"]


This says that the words "I wish" are twice followed by the word
"I", the words "wish I" are followed once by "may" and once by "might"
and so on.

To generate new text from this analysis, choose an arbitrary word pair as a
starting point. Use this pair of words to look up a random next word (using the table
above) and append this new word to the text so far. This now gives you three words with a
new word pair (second and third words) at the end of the three-word text. Look up a potential next word
based on this pair. This generates another pair to add to the list, and so on. In the previous example,
we could start with "I may". The only possible next word is
"I", so now we have::

  I may I

The last two words are "may I," so the next word is
"wish". We then look up "I wish," and find our choice
is constrained to another "I"::

   I may I wish I


Now we look up "wish I," and find we have a choice. Let’s
choose "may"::

   I may I wish I may

Now we’re back where we started from, with "I may."
Following the same sequence, but choosing "might" this time, we
get::

   I may I wish I may I wish I might

At this point we stop, as no sequence starts "I might."


Given a short input text, the algorithm isn’t too interesting. Feed
it a book, however, and you give it more options, so the resulting output
can be surprising.

For this exercise, try implementing a trigram algorithm that generates a couple
of hundred words of text using a book-sized file as input.
`Project Gutenberg <http://www.gutenberg.org/>`_ is a good source of online
books (*Tom Swift and His Airship* is `here <http://sailor.gutenberg.org/etext02/03tom10.txt>`_.)

Be warned that these files have DOS line endings (carriage return followed by
newline).


Here is a copy of short-story collection *The Adventures of Sherlock Holmes*:

:download:`sherlock.txt  <./sherlock.txt>`.

And a shorter copy for testing (a paragraph from one of the stories, "A Scandal in Bohemia"):

:download:`sherlock_small.txt  <./sherlock_small.txt>`.


Objectives
-----------

Katas are about trying something many times. In this one, what
we’re experimenting with is not just the code, but the heuristics of
processing the text. What do we do with punctuation? Paragraphs? Do we have
to implement backtracking if we chose a next word that turns out to be a
dead end?

I’ll fire the signal and the fun will commence...

Developing Your Solution
========================

This assignment has two parts: the key one is the trigrams exercise itself, but you also need to do some text processing to get a full book in shape for processing.

I suggest you write the trigrams part first; it's more interesting :-)

Test Driven Development
-----------------------

You've recently learned about unit testing and Test Driven Development (TDD). That's put that to work on this exercise. Remember that the key to TDD is that you first decide on what you need a piece of your code to do, then you write a test to check that it does that, and only then do you write the actual code itself.

Because you're new to this, we're going to give you some tests to get you started. You'll find them in: :download:`test_trigrams.py <./test_trigrams.py>`, which should be with this assignment.

Running the Tests
.................

To run the tests, use the ``pytest`` test runner: set your working directory the dir with the test file, and run the ``pytest`` command:

.. code-block:: bash

  $ pytest
  ======================= test session starts =======================
  platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
  rootdir: /Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/exercises/trigrams
  collected 0 items / 1 error

  ============================= ERRORS ==============================
  ________________ ERROR collecting test_trigrams.py ________________
  ImportError while importing test module '/Users/chris.barker/Personal/UWPCE/Python210CourseMaterials/source/exercises/trigrams/test_trigrams.py'.
  Hint: make sure your test modules/packages have valid Python names.
  Traceback:
  test_trigrams.py:17: in <module>
      import trigrams
  E   ModuleNotFoundError: No module named 'trigrams'
  ===================== short test summary info =====================
  ERROR test_trigrams.py
  !!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!
  ======================== 1 error in 0.13s =========================

You should have gotten something like that error: it is indicating that the "trigrams" module does not exist -- which makes sense, as you haven't written in yet. So the first step is the create your code file: name it ``trigrams.py`` and put it in the same directory as the ``test_trigrams.py`` file. It can be empty for now. Now try running pytest again, and it should get farther: you'll have a lot of test failures, but the test should actually run. You should get something like:

.. code-block:: bash

  ...
  >       tris = trigrams.build_trigram(IWISH)
  E       AttributeError: module 'trigrams' has no attribute 'build_trigram'

  test_trigrams.py:29: AttributeError
  ====================== short test summary info =======================
  FAILED test_trigrams.py::test_trigrams_keys - AttributeError: modul...
  ========================= 1 failed in 0.15s ==========================

You get an Attribute error, as you haven' defined anything in your ``trigrams.py`` file. But now it's time to actually work on the code!

trigrams
--------

Key to the trigrams problem is the selection of the data structure to use to hold the "trigrams" themselves. What do we need here?

The text
........

First, you'll want a bit of text to try your code out on. Why not try the example here::

  I wish I may I wish I might

You need that in a python data structure somehow, so how about:

.. code-block:: python

    words = "I wish I may I wish I might".split()

This produces an (ordered) list of words::

  ['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might']

Now you've got some words to play with. Once you think you've got it working, try a bit longer piece of text. But this will do for now, and it's small and simple enough that you can immediately see if your code is working.

You will find that example in the test file, so we can write tests against it:

.. code-block:: python

  IWISH = ["I", "wish", "I", "may", "I", "wish", "I", "might"]


The trigrams structure
----------------------

Now we need to think a bit about what we want the trigrams structure to be.

From above, we know that we need to build up something like this::

    "I wish" => "I", "I"
    "wish I" => "may", "might"
    "may I"  => "wish"
    "I may"  => "I"

Hmmm, in a way, that's almost pseudo code. You have a bunch of word pairs, and for each word pair, there are one or more words that follow it.

Those following words look a lot like they could be in a list, yes? Perfect, the list structure keeps order, and you can keep adding (appending) new words to it.

Each of those lists of words needs to be mapped to a particular pair. Each pair is unique; it only shows up once (when that same pair is encountered again in the text, you add the follower to the list of following words).

That sounds a lot like a dictionary. The keys (word pairs) are unique, and map to a list of following words. (Note that, technically, in python the dictionary is only one implementation of a
`Mapping <https://docs.python.org/3/glossary.html#term-mapping>`_.)

Now you have a choice of data structures for the word pairs, or keys in the dict: a string or a tuple.

**String**: The keys are a pair of words and can be represented as a string of two words with a space like so:

.. code-block:: python

    trigrams = {"I wish": ["I", "I"],
                "wish I": ["may", "might"],
                "may I": ["wish"],
                "I may": ["I"],
                }

**Tuple**: But strings are not the only type that you can use as keys in a dictionary; you can use any *immutable* type. Recall that tuples are immutable (they can't be changed once they have been created). Since each pair of words is, well, a pair, it makes sense to store each pair in a tuple, keeping the individual words separate:

.. code-block:: python

    trigrams = {("I", "wish"): ["I", "I"],
                ("wish", "I"): ["may", "might"],
                ("may", "I"): ["wish"],
                ("I", "may"): ["I"],
                }

I like the version that uses tuples better, but either one will work. The test code is designed to check for word pairs in tuples. If you want to write your code using space separated strings, you can modify the tests.

Building the Trigrams dict
..........................

So you've got a list of words, and you need to build up a dict like one of the above.

It's time to create a python file and start writing some code!

Put this in your ``trigrams.py`` file

.. code-block:: python

  #!/usr/bin/env python3

  def build_trigram(words):
      """
      build up the trigrams dict from the list of words

      :param words: a list of individual words in order

      :returns: a dict with:
           keys: word pairs in tuples
           values: list of the words that follow the pain in the key
      """

      trigrams = {}

      # build up the dict here!

      return trigrams


So how do you actually build up that dict? That's kind of the point of the exercise, so I won't tell you that ... but here are some hints:

**Looping through the words**

Obviously you need to loop through all the words, so a ``for`` loop makes sense. However, this is a bit tricky. Usually in Python you loop through all the items in a list, and don't worry about the indexes:

.. code-block:: python

  for item in a_list:
     ...

But in this case, we don't need to work with one word at a time, we need to work with three at a time (a pair of words, and the single word that follows it).
So contrary to the usual practice, an index can be helpful here:

.. code-block:: python

  for i in range(len(words)-2): # why -2 ?
     pair = words[i:i + 2]
     follower = words[i + 2]

**Adding a pair to the dict:**

For each pair in the text, you need to add it to the dict. But:

- ``words[i:i + 2]`` is a list with two words in it. Can that be used as a key in a dict? (Try it.) If not, how can you make a valid key out of it?

- As you loop through the text, you will collect pairs of words. Each time, a given pair may already be in the dict.

  - If the pair is not in the dict, you want to put it in the dict, with value being a list with the follower in it::

    ("may", "I"): ["wish"]

  - If the pair already is in the dict, then you want to add the follower (the second word in the pair) to the list that's already there::

    ("wish", "I"): ["may", "might"]

Note that the description above suggests the basic logic; it's almost pseudo-code. And that logic will work.  But it turns out that this is a common enough operation that python dicts have a method that lets you do that logic in one step? Can you find it?

`Python dict Documentation <https://docs.python.org/3/library/stdtypes.html?highlight=dictionary#mapping-types-dict>`_

As you develop this code, run the tests each time you think you have made some progress::

    $ pytest test_trigrams.py

In that test file, there are two tests of the `trigrams()` function: One that tests that it gets the right word pairs as keys:

.. code-block:: python

  def test_trigrams_pairs():
      """
      test that the build_trigram function creates the right pairs of words
      """
      tris = trigrams.build_trigram(IWISH)

      pairs = tris.keys()

      # using a set here, as the dict_keys object is a set as well
      # And keys are always unique and hashable
      # and the order does not matter, so perfect for a set
      assert pairs == {("I", "wish"),
                       ("wish", "I"),
                       ("may", "I"),
                       ("I", "may"),
                       }

and one that tests if the following word lists are correct:

.. code-block:: python

  def test_trigrams_following_words():
      """
      test that the following words are correct
      """
      tris = trigrams.build_trigram(IWISH)

      # this will only print if the test fails
      # but if if does, you can see what's going on to try to fix it.
      print(tris)

      # a separate assert for each pair:
      assert tris[("I", "wish")] == ["I", "I"]
      assert tris[("wish", "I")] == ["may", "might"]
      assert tris[("may", "I")] == ["wish"]
      assert tris[("I", "may")] == ["I"]

Note that if the first test fails, almost certainly the second will too (the second test explicitly looks for all the same keys). That's OK. It's still good to keep them separate, because the first test could pass while the second one fails -- it's nice to know you've made progress!

If it seems like we have hard-coded a lot of detail in -- you are right. But this is quite deliberate. And it is why we chose such a simple set of words to start out with. If you want read a bit more about this approach, this blogger puts it nicely:
`Write Explicit Tests <https://amir.rachum.com/blog/2017/01/14/explicit-tests/>`_

If both tests pass, you should now have code that will return a dict like we noted above::

   {("I", "wish"): ["I", "I"],
    ("wish", "I"): ["may", "might"],
    ("may", "I"): ["wish"],
    ("I", "may"): ["I"]}

Try it out on a longer bit of text (your choice) before you go any further. If it doesn't work correctly, make sure to write a test that catches the problem before you fix it!


Using the Trigrams dict
.......................

This is the fun part. Once you have a mapping of word pairs to following words, you can build up some new "fake" text. Re-read the previous sections again to remind yourself of the procedure. Here are a couple of additional hints and questions to consider:

- The ``random`` module <https://docs.python.org/3/library/random.html#module-random> is your friend here:

.. code-block:: python

  import random

  # returns a number between a and b (including a and b)
  random.randint(a, b)

  # pick a random item from a sequence
  random.choice(a_list)

This is all pretty tricky to test -- after all, you are selecting random words -- you can't know what the result should be! There are two tactics you can take here. We show a bit of both in the provided tests.

Tactic one is to break you code down into pieces that you *can* test -- everything BUT the random choices.

Tactic two is to take advantage of the random "`seed <https://en.wikipedia.org/wiki/Random_seed>`_". Computers don't really make truly random numbers. What they do is compute a sequence of numbers that are statistically very much like random numbers. But if you start with the same initial value, known as the "seed", then you will get the same sequence of numbers. We can take advantage of this in our tests, as the built in ``random`` module provides a way to `set the seed <https://docs.python.org/3/library/random.html#random.seed>`_

The provided tests use a both of these tactics.

- You need to start with the first word pair; picking a random key from a dict is actually a bit tricky. But we have a test for it:

.. code-block:: python

  def test_pick_random_pair():
      test_pairs = {("one", "two"): [],
                    ("one", "three"): [],
                    ("four", "five"): [],
                    ("six", "seven"): [],
                    ("eight", "nine"): [],
                    }
      # set the seed so we'll always get the same one
      random.seed(1234)
      pair = trigrams.pick_random_pair(test_pairs)

      assert pair == ('six', 'seven')

So you'll need to define a function: ``pick_random_pair()`` that takes your trigram dict as input, and returns a random key.

Note that that particular result is using a particular algorithm -- if you use a different one, you might get a different pair -- but you should get the same one every time, so you can make the test check for that.


- As you build up your text, you probably want to build it up in a list, appending one word at a time.  You can join it together at the end with ``" ".join(the_list_of_words)``

- Remember that after adding a word to a pair to make a three-word text, the next pair is the last two words in that three-word text.

- What to do if you end up with a word pair that isn't in the original text? It's unlikely on a long text, but possible.

- How to terminate? Probably have a pre-defined length of text!



Once you have the basics working, try your code on a longer piece of input text. Then think about making it fancy. Can you make sentences with capitalized first words and punctuation? Anything else to make the text more "real"?


Processing the Input Text
-------------------------

If you get a book from Project Gutenberg (or anywhere else), it will not be "clean." That is, it will have header information, footer information, chapter headings, punctuation, what have you. So you'll need to clean it up somehow to get a simple list of words to use to build your trigrams.

The first part of the process is pretty straightforward; open the file and loop through the lines of text.

You may want to skip the header. How would you do that??
Hint: in a Project Gutenberg e-book, there is a line of text that starts with::

  *** START OF THIS PROJECT GUTENBERG EBOOK

In the loop, you can process a single line of text to break it into words:

 - calling ``.split()``

Optional steps to cleaning up the text:

 - Strip out punctuation?
   - If you do this, what about contractions, i.e. the appostrophe in "can't" vs. a single quotation mark -- which are the same character.

 - Remove capitalization?
   - If you do this, what about "I"? And proper nouns?

Any other ideas you may have.

**Hints:**

The ``string`` methods are your friend here.

There are also handy constants in the ``string`` module: ``import string``

Check out the ``str.translate()`` method; it can make multiple replacements very fast.

Do get the full trigrams code working first, then play with some of the fancier options.

Code Structure
--------------

Break your code down into a handful of separate functions. This way you can test each on its own, and it's easier to refactor one part without messing with the others.  For instance, your ``__main__`` block might look something like:

.. code-block:: python

  if __name__ == "__main__":
      # get the filename from the command line
      try:
          filename = sys.argv[1]
      except IndexError:
          print("You must pass in a filename")
          sys.exit(1)

      in_data = read_in_data(filename)
      words = make_words(in_data)
      word_pairs = build_trigram(words)
      new_text = build_text(word_pairs)

      print(new_text)
