.. _html_renderer_tutorial:

#######################################
Tutorial for the Html Render Assignment
#######################################

If you are finding that you don't really know where to start with the html render assignment, this tutorial will walk you through the process.

However, you generally learn more if you figure things out for yourself. So I highly suggest that you give each step a try on your own first, before reading that step in this tutorial. Then, if you are really stuck -- follow the process here.

.. _render_tutorial_1:

Step 1:
-------

Step one is a biggie -- that's 'cause you need a fair bit all working before you can actually have anything to test, really. But let's take it bit by bit.

First, we are doing test driven development, and we already have a test or two. So let's run those, and see what we get.

You should now be in a terminal with the current working directory set to where you downloaded ``html_render.py`` and ``test_html_render.py``. If you run pytest, it will find the ``test_html_render.py`` file and run the tests in it:

.. code-block:: bash

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 3 items

    test_html_render.py ..F                                                  [100%]

    =================================== FAILURES ===================================
    _____________________________ test_render_element ______________________________

        def test_render_element():
            """
            Tests whether the Element can render two pieces of text
            So it is also testing that the append method works correctly.

            It is not testing whether indentation or line feeds are correct.
            """
            e = Element("this is some text")
            e.append("and this is some more text")

            # This uses the render_results utility above
            file_contents = render_result(e).strip()

            # making sure the content got in there.
    >       assert("this is some text") in file_contents
    E       AssertionError: assert 'this is some text' in 'just something as a place holder...'

    test_html_render.py:72: AssertionError
    ====================== 1 failed, 2 passed in 0.06 seconds ======================

Hey! that's pretty cool -- two tests are already passing! Let's take a quick look at those:

.. code-block:: python

    def test_init():
        """
        This only tests that it can be initialized with and without
        some content -- but it's a start
        """
        e = Element()

        e = Element("this is some text")

So that one simply tested that an ``Element`` class exists, and that you can pass in a string when you initialize it -- not a bad start, but it doesn't show that you can *do* anything with it.


.. code-block:: python

    def test_append():
        """
        This tests that you can append text

        It doesn't test if it works --
        that will be covered by the render test later
        """
        e = Element("this is some text")
        e.append("some more text")

And this one shows that you can call the ``append()`` method with some text -- nice, but again, it doesn't test if that appended text was used correctly. But it does show you got the API right.

But this one failed:

.. code-block:: python

    def test_render_element():
        """
        Tests whether the Element can render two pieces of text
        So it is also testing that the append method works correctly.

        It is not testing whether indentation or line feeds are correct.
        """
        e = Element("this is some text")
        e.append("and this is some more text")

        # This uses the render_results utility above
        file_contents = render_result(e).strip()

        # making sure the content got in there.
        assert("this is some text") in file_contents
        assert("and this is some more text") in file_contents

        # make sure it's in the right order
        assert file_contents.index("this is") < file_contents.index("and this")

        # making sure the opening and closing tags are right.
        assert file_contents.startswith("<html>")
        assert file_contents.endswith("</html>")

OK -- this one really does something real -- it tries to render an html element -- which did NOT pass -- so it's time to put some real functionality in the ``Element`` class.

This is the code:

.. code-block:: python

    class Element:

        def __init__(self, content=None):
            pass

        def append(self, new_content):
            pass

        def render(self, out_file):
            out_file.write("just something as a place holder...")

Looking there, we can see why the tests did what they did -- we have the three key methods, but they don't actually do anything. But the ``render`` method is the only one that actually provides some results to test.

So back to the assignment:

    The ``Element`` class should have a class attribute for the tag name ("html" first).

Each html element has a different "tag", specifying what kind of element it is. so our class needs one of those. Why a class attribute? Because each *instance* of each type (or class) of element will share the same tag.  And we don't want to store the tag in the render method, because then we couldn't reuse that render method for a different type of element.

So we need to add a tiny bit of code:

.. code-block:: python

    class Element:

        tag = "html"

        def __init__(self, content=None):
            pass

That's not much -- will the test pass now? Probably not, because we aren't doing anything with the tag. But you can run it to see if you'd like. It's always good to run tests frequently to make sure you haven't inadvertently broken anything.

Back to the task at hand:

  The class should have an ``append`` method that can add another string to the content.

  ...

  So your class will need a way to store the content in a way that you can keep adding more to it.

OK, so we need a way to store the content: both what gets passed in to the ``__init__`` and what gets added with the ``append`` method.  We need a data structure that can hold an ordered list of things, and can be added to in the future -- sounds like a list to me. So let's create a list in __init__ and store it in ``self`` for use by the other methods:

.. code-block:: python

    def __init__(self, content=None):
        self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

OK -- let's run the tests and see if anything changed::

    >       assert("this is some text") in file_contents
    E       AssertionError: assert 'this is some text' in 'just something as a place holder...'

    test_html_render.py:72: AssertionError

Nope -- still failed at the first assert in test_render. This makes sense because we haven't done anything with the render method yet!

.. rubric:: 1c.

From the assignment:

  It should have a ``render(file_out)`` method that renders the tag and the strings in the content.

We have the render method, but it's rendering arbitrary text to the file, not an html tag or contents. So let's add that.

First let's add the contents, adding a newline in between to keep it readable.  Remember that there can be multiple pieces of content, so we need to loop though the list:

.. code-block:: python

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write(content)
            out_file.write("\n")

And run the tests::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 3 items

    test_html_render.py ..F                                                  [100%]

    =================================== FAILURES ===================================
    _____________________________ test_render_element ______________________________

        def test_render_element():
            """
            Tests whether the Element can render two pieces of text
            So it is also testing that the append method works correctly.

            It is not testing whether indentation or line feeds are correct.
            """
            e = Element("this is some text")
            e.append("and this is some more text")

            # This uses the render_results utility above
            file_contents = render_result(e).strip()

            # making sure the content got in there.
            assert("this is some text") in file_contents
            assert("and this is some more text") in file_contents

            # make sure it's in the right order
            assert file_contents.index("this is") < file_contents.index("and this")

            # making sure the opening and closing tags are right.
    >       assert file_contents.startswith("<html>")
    E       AssertionError: assert False
    E        +  where False = <built-in method startswith of str object at 0x10e23fcf0>('<html>')
    E        +    where <built-in method startswith of str object at 0x10e23fcf0> = 'this is some text\nand this is some more text'.startswith

    test_html_render.py:79: AssertionError
    ====================== 1 failed, 2 passed in 0.05 seconds ======================

Failed in test_render again. But look carefully. It didn't fail on the first assert! It failed on this line::

  assert file_contents.startswith("<html>")

This makes sense because we haven't rendered anything like that yet. So let's add that now. Recall that we want the results to look something like this:

.. code-block:: html

    <html>
    Some content.
    Some more content.
    </html>

In this case, the "html" part is stored in a class attribute. So how would you make that tag? Looks like a good place for string formatting::

  "<{}>".format(self.tag)

and::

  "</{}>".format(self.tag)

So the method looks something like this:

.. code-block:: python

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            out_file.write(content)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))

Now run the tests again::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 3 items

    test_html_render.py ...                                                  [100%]

    =========================== 3 passed in 0.02 seconds ===========================

Whoo Hoo!  All tests pass! But wait, there's more. Comprehensive testing is difficult. We tested that you could initialize the element with one piece of content, and then add another, and we checked that the opening and closing tag are there correctly. But is it actually rendering correctly? We may not have tested for everything. So we should take a look at the results, and see how it's doing. My trick for this is to print what I want to see in the test::

    print(file_contents)

and add a forced test failure at the end of the test, so we'll see that print::

    assert False

And let's run it::

    =================================== FAILURES ===================================
    _____________________________ test_render_element ______________________________

        def test_render_element():
            """
            Tests whether the Element can render two pieces of text
            So it is also testing that the append method works correctly.

            It is not testing whether indentation or line feeds are correct.
            """
            e = Element("this is some text")
            e.append("and this is some more text")

            # This uses the render_results utility above
            file_contents = render_result(e).strip()
            print(file_contents)
            # making sure the content got in there.
            assert("this is some text") in file_contents
            assert("and this is some more text") in file_contents

            # make sure it's in the right order
            assert file_contents.index("this is") < file_contents.index("and this")

            # making sure the opening and closing tags are right.
            assert file_contents.startswith("<html>")
            assert file_contents.endswith("</html>")
    >       assert False
    E       assert False

    test_html_render.py:82: AssertionError
    ----------------------------- Captured stdout call -----------------------------
    <html>
    this is some text
    </html>
    <html>
    and this is some more text
    </html>

It failed on the ``assert False``. It's a good sign that it didn't fail before that.  We can now look at the results we printed, and whoops! we actually got *two* html elements, rather than one with two pieces of content. Why is that? Before you look at the code again, let's make sure the test catches that and fails. How about this?

.. code-block:: python

    assert file_contents.count("<html>") == 1
    assert file_contents.count("</html>") == 1

And it does indeed fail on this line::

    >       assert file_contents.count("<html>") == 1
    E       AssertionError: assert 2 == 1
    E        +  where 2 = <built-in method count of str object at 0x103967030>('<html>')
    E        +    where <built-in method count of str object at 0x103967030> = '<html>\nthis is some text\n</html>\n<html>\nand this is some more text\n</html>'.count

    test_html_render.py:83: AssertionError

Now that we know we can test for the issue, we can try to fix it, and we'll know it's fixed when the tests pass.

So looking at the code -- why did I get two ``<html>`` tags?

.. code-block:: python

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            out_file.write(content)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))

Hmm -- when are those tags getting rendered? *Inside* the loops through the contents! Oops! We want to write the tag *before* the loop, and the closing tag *after* loop. (Did you notice that the first time? I hope so.) So a little restructuring is in order.

.. code-block:: python

    def render(self, out_file):
        # loop through the list of contents:
        out_file.write("<{}>\n".format(self.tag))
        for content in self.contents:
            out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))

That's it -- let's see if the tests pass now::


    >       assert False
    E       assert False

    test_html_render.py:86: AssertionError
    ----------------------------- Captured stdout call -----------------------------
    <html>
    this is some text
    and this is some more text
    </html>

Mine failed on the ``assert False``. So the actual test passed -- good. And the rendered html tag looks right, too. So we can go ahead and remove that ``assert False``, and move on!

We have tested to see that we could initialize with one piece of content, and then add another, but what if you initialized it with nothing, and then added some content?  Try uncommenting the next test: ``test_render_element2`` and see what you get.

This is what I got with my code::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 4 items

    test_html_render.py ...F                                                 [100%]

    =================================== FAILURES ===================================
    _____________________________ test_render_element2 _____________________________

        def test_render_element2():
            """
            Tests whether the Element can render two pieces of text
            So it is also testing that the append method works correctly.

            It is not testing whether indentation or line feeds are correct.
            """
            e = Element()
            e.append("this is some text")
            e.append("and this is some more text")

            # This uses the render_results utility above
    >       file_contents = render_result(e).strip()

    test_html_render.py:95:
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    test_html_render.py:30: in render_result
        element.render(outfile)
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    self = <html_render.Element object at 0x10c4d5c88>
    out_file = <_io.StringIO object at 0x10c4881f8>

        def render(self, out_file):
            # loop through the list of contents:
            for content in self.contents:
                out_file.write("<{}>\n".format(self.tag))
    >           out_file.write(content)
    E           TypeError: string argument expected, got 'NoneType'

    html_render.py:23: TypeError
    ====================== 1 failed, 3 passed in 0.08 seconds ======================

Darn! Something is wrong here. And this time it errored out before it even got results to test.  So look and see exactly what the error is. (pytest does a really nice job of showing you the errors)::

                  out_file.write("<{}>\n".format(self.tag))
    >           out_file.write(content)
    E           TypeError: string argument expected, got 'NoneType'

It failed when we tried to write to the file. We're trying to write a piece of content, and we got a ``NoneType``.  How in the world did a ``NoneType`` (which is the type of None) get in there?

Where does the ``self.contents`` list get created? In the ``__init__``. Let's do a little print debugging here. Add a print to the ``__init__``:

.. code-block:: python

    def __init__(self, content=None):
        self.contents = [content]
        print("contents is:", self.contents)

And run the tests again::

    >           out_file.write(content)
    E           TypeError: string argument expected, got 'NoneType'

    html_render.py:24: TypeError
    ----------------------------- Captured stdout call -----------------------------
    contents is: [None]
    ====================== 1 failed, 3 passed in 0.06 seconds ======================


Same failure -- but pytest does a nice job of showing you what was printed (stdout) when a test fails. So in this case, at the end of the ``__init__`` method, the contents list looks like ``[None]`` -- a list with a single None object in it. No wonder it failed later when we tried to write that ``None`` to a file!

But why? Well, looking at the ``__init__``, it looks like content gets set to None by default:

.. code-block:: python

    def __init__(self, content=None):

Then we put that ``None`` in the ``self.contents`` list.  What do we want when content is ``None``?
An empty list, so that we can add to it later, not a list with a ``None`` object in it.  So you need some code that checks for ``None`` (hint: use ``is None`` or ``is not None`` to check for ``None``), and only adds content to the list if it is *not* ``None``.

I'll leave it as an exercise for the reader to figure out how to do that, but make sure all tests are passing before you move on! And once the tests pass, you may want to remove that ``print()`` line.

.. _render_tutorial_2_A:

Step 2:
-------

OK, we have nice little class here; it has a class attribute to store information about the tag, information that's the same for all instances.

And we are storing a list of contents in "self" -- information that each instance needs its own copy of.

And we are using that data to render an element.

So we're ready to move on.

Part A
......

.. rubric:: Instructions:


"Create a couple subclasses of ``Element``, for each of ``<html>``, ``<body>``, and ``<p>`` tags. All you should have to do is override the ``tag`` class attribute (you may need to add a ``tag`` class attribute to the ``Element`` class first, if you haven't already)."

So this is very straightforward. We have a class that represents an element, and the only difference between basic elements is that they have a different tag. For example::

    <body>
    Some content.
    Some more content.
    </body>

and::

    <p>
    Some content.
    Some more content.
    </p>


The ``<body>`` tag is for the entire contents of an html page, and the ``<p>`` tag is for a paragraph.  But you can see that the form of the tags is identical, so we don't have to change much to make classes for these tags. In fact, all we need to change is the ``tag`` class attribute.

Before we do that -- let's do some test-driven development. Uncomment the next few tests in ``test_html_render.py``: ``test_html``, ``test_body``, and ``test_p``, and run the tests::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 7 items

    test_html_render.py ....FFF                                              [100%]

    =================================== FAILURES ===================================
    __________________________________ test_html ___________________________________

        def test_html():
    >       e = Html("this is some text")
    E       NameError: name 'Html' is not defined

    test_html_render.py:117: NameError
    __________________________________ test_body ___________________________________

        def test_body():
    >       e = Body("this is some text")
    E       NameError: name 'Body' is not defined

    test_html_render.py:129: NameError
    ____________________________________ test_p ____________________________________

        def test_p():
    >       e = P("this is some text")
    E       NameError: name 'P' is not defined

    test_html_render.py:142: NameError
    ====================== 3 failed, 4 passed in 0.08 seconds ======================

So we have three failures. Of course we do, because we haven't written any new code yet!
Yes, this is pedantic, and there is no real reason to run tests you know are going to fail. But there is a reason to *write* tests that you know are going to fail, and you have to run them to know that you have written them correctly.

Now we can write the code for those three new element types. Try to do that yourself first, before you read on.

OK, did you do something as simple as this?

.. code-block:: python

    class Body(Element):
        tag = 'body'

(and similarly for ``Html`` and ``P``)

That's it!  But what does that mean?  This line:

.. code-block:: python

    class Body(Element):

means: make a new subclass of the ``Element`` tag called ``Body``.

and this line:

.. code-block:: python

        tag = 'body'

means:  set the ``tag`` class attribute to ``'body'``. Since this class attribute was set on the ``Element`` class already, this is called "overriding" the tag attribute.

The end result is that we now have a class that is exactly the same as the ``Element`` class, except with a different tag. Where is that attribute used? It is used in the ``render()`` method.

Let's  run the tests and see if this worked::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 7 items

    test_html_render.py .......                                              [100%]

    =========================== 7 passed in 0.02 seconds ===========================

Success! We now have three different tags.

.. note::
  Why the ``Html`` element? Doesn't the ``Element`` class already use the "html" tag?
  Indeed it does, but the goal of the ``Element`` class is to be a base class for the other tags, rather than being a particular element.
  Sometimes this is called an "abstract base class": a class that can't do anything by itself, but exists only to provide an interface (and partial functionality) for subclasses.
  But we wanted to be able to test that partial functionality, so we had to give it a tag to use in the initial tests.
  If you want to be pure about it, you could use something like ``abstract_tag`` in the ``Element`` class to make it clear that it isn't supposed to be used alone.  And later on in the assignment, we'll be adding extra functionality to the ``Html`` element.

Making a subclass where the only thing you change is a single class attribute may seem a bit silly -- and indeed it is.
If that were going to be the *only* difference between all elements, There would be other ways to accomplish that task that would make more sense -- perhaps passing the tag in to the initializer, for instance.
But have patience, as we proceed with the exercise, some element types will have more customization.

Another thing to keep in mind. The fact that writing a new subclass is ALL we need to do to get a new type of element demonstrates the power of subclassing. With the tiny change of adding a subclass with a single class attribute, we get a new element that we can add content to, and render to a file, etc., with virtually no repeated code.

.. _render_tutorial_2_B:

Part B:
.......

Now it gets more interesting, and challenging!

The goal is to be able to render nested elements, like so:

.. code-block:: html

    <html>
    <body>
    <p>
    a very small paragraph
    </p>
    <p>
    Another small paragraph.
    This one with multiple lines.
    </p>
    </body>
    </html>

This means that we need to be able to append not just text to an element, but also other elements.  The appending is easy -- the tricky bit is when you want to render those enclosed elements.

Let's take this bit by bit -- first with a test or two.
Uncomment ``test_subelement`` in the test file, and run the tests::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 8 items

    test_html_render.py .......F                                             [100%]

    =================================== FAILURES ===================================
    _______________________________ test_sub_element _______________________________

        def test_sub_element():
            """
            tests that you can add another element and still render properly
            """
            page = Html()
            page.append("some plain text.")
            page.append(P("A simple paragraph of text"))
            page.append("Some more plain text.")

    >       file_contents = render_result(page)

    test_html_render.py:163:
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    test_html_render.py:30: in render_result
        element.render(outfile)
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    self = <html_render.Html object at 0x1032f8438>
    out_file = <_io.StringIO object at 0x10325b5e8>

        def render(self, out_file):
            # loop through the list of contents:
            for content in self.contents:
                out_file.write("<{}>\n".format(self.tag))
    >           out_file.write(content)
    E           TypeError: string argument expected, got 'P'

    html_render.py:26: TypeError
    ====================== 1 failed, 7 passed in 0.11 seconds ======================

Again, the new test failed; no surprise because we haven't written any new code yet. But do read the report carefully; it did not fail on an assert, but rather with a ``TypeError``.  The code itself raised an exception before it could produce results to test.

So now it's time to write the code. Look at where the exception was raised: line 26 in my code, inside the ``render()`` method. The line number will likely be different in your code, but it probably failed on the render method. Looking closer at the error::

    >           out_file.write(content)
    E           TypeError: string argument expected, got 'P'

It occurred in the file ``write`` method, complaining that it expected to be writing a string to the file, but it got a ``'P'``. ``'P'`` is the name of the paragraph element class.
So we need a way to write an element to a file. How might we do that? Inside the element's render method, we need to render an element...

Well, elements already know how to render themselves. This is what is meant by a recursive approach. In the ``render`` method, we want to make use of the ``render`` method itself.

Looking at the signature of the render method:

.. code-block:: python

      def render(self, out_file):

it becomes clear -- we render an element by passing the output file to the element's render method. Here is what mine looks like now:

.. code-block:: python

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            out_file.write(content)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))

So let's update our render by replacing that ``out_file.write()`` call with a call to the content's ``render`` method:

.. code-block:: python

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            # out_file.write(content)
            content.render(out_file)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))

And let's see what happens when we run the tests::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 8 items

    test_html_render.py ..FFFFFF                                             [100%]

    =================================== FAILURES ===================================

    ... lots of failures here

    _______________________________ test_sub_element _______________________________

        def test_sub_element():
            """
            tests that you can add another element and still render properly
            """
            page = Html()
            page.append("some plain text.")
            page.append(P("A simple paragraph of text"))
            page.append("Some more plain text.")

    >       file_contents = render_result(page)

    test_html_render.py:163:
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    test_html_render.py:30: in render_result
        element.render(outfile)
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    self = <html_render.Html object at 0x10b10dfd0>
    out_file = <_io.StringIO object at 0x10b123828>

        def render(self, out_file):
            # loop through the list of contents:
            for content in self.contents:
                out_file.write("<{}>\n".format(self.tag))
                # out_file.write(content)
    >           content.render(out_file)
    E           AttributeError: 'str' object has no attribute 'render'

    html_render.py:27: AttributeError
    ====================== 6 failed, 2 passed in 0.12 seconds ======================

Whoaa! Six failures! We really broke something! But that is a *good* thing. It's the whole point of unit tests. When you are making a change to address one issue, you know right away that you broke previously working code.

So let's see if we can fix these tests, while still allowing us to add the feature we intended to add.

Again -- look carefully at the error, and the solution might pop out at you::

    >           content.render(out_file)
    E           AttributeError: 'str' object has no attribute 'render'

Now we are trying to call a piece of content's ``render`` method, but we got a simple string, which does not *have* a ``render`` method.
This is the challenge of this part of the exercise. It's easy to render a string, and it's easy to render an element, but the content list could have either one. So how do we switch between the two methods?

There are a number of approaches you can take. This is a good time to read the notes about this here: :ref:`notes_on_handling_duck_typing`.
You may want to try one of the more complex methods, but for now, we're going to use the one that suggests itself from the error.

We need to know whether we want to call a ``render()`` method, or simply write the content to the file. How would we know which to do? Again, look at the error:
We tried to call the render() method of a piece of content, but got an ``AttributeError``. So the way to know whether we can call a render method is to try to call it -- if it works, great! If not, we can catch the exception, and do something else. In this case, the something else is to try to write the content directly to the file:

.. code-block:: python

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))

And run the tests again::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 8 items

    test_html_render.py ........                                             [100%]

    =========================== 8 passed in 0.03 seconds ===========================

Yeah! all eight tests pass!  I hope you found that at least a little bit satisfying.  And pretty cool, really, that the solution requires only two extra lines of code. This is an application of the EAFP method: it's Easier to Ask Forgiveness than Permission. You simply try to do one thing, and if that raises the exception you expect, than do something else.

It's also taking advantage of Python's "Duck Typing". Notice that we don't know if that piece of content is actually an ``Element`` object. All we know is that it has a ``render()`` method that we can pass a file-like object to.
This is quite deliberate. If some future user (that might be you) wants to write their own element type, they can write it any way they like, as long as it defines a ``render()`` method that can take a file-like object to write to.

So what are the downsides to this method? Well, there are two:

1. When we successfully call the ``render`` method, we have no idea if it's actually done the right thing -- it could do anything. If someone puts some completely unrelated object in the content list that happens to have a ``render`` method, this is not going to work. But what are the odds of that?

2. This is the bigger one: if the object *HAS* a render method, but that render method has something wrong with it, then it could conceivably raise an ``AttributeError`` itself, but it would not be the Attribute Error we are expecting. The trick here is that this is very hard to debug.

However, we are saved by tests. If the render method works in all the other tests, It's not going to raise an ``AttributeError`` only in this case. Another reason to have a good test suite.


.. _render_tutorial_3:

Step 3:
-------

Now we are getting a little more interesting.

"Create a ``<head>`` element -- a simple subclass."

This is easy; you know how to do that, yes?

But the training wheels are off -- you are going to need to write your own tests now.  So before you create the ``Head`` element class, write a test for it. You should be able to copy and paste one of the previous tests, and just change the name of the class and the tag value. Remember to give your test a new name, or it will simply replace the previous test.

I like to run the tests as soon as I make a new one. If nothing else, I can make sure I have one more test.

OK, that should have been straightforward.  Now this part:

  Create a ``OneLineTag`` subclass of ``Element``:

  * It should override the render method, to render everything on one line -- for the simple tags, like::

      <title> PythonClass - Session 6 example </title>

Some html elements don't tend to have a lot of content, such as the document title. So it makes sense to render them all on one line.  This is going to require a new render method.  Since there are multiple types of elements that should be rendered on one line, we want to create a base class for all one-line elements. It should subclass from ``Element``, and override the render method with a new one, which will be pretty much the same as the main ``Element`` method, but without the newlines.

Before we do that though -- let's write a test for that!  Because the ``ONeLineTag`` class is a base class for actual elements that should be rendered on one line, we really don't need to write a test directly for it. We can write one for its first subclass: ``Title``. The title elements should be rendered something like this::

    <title> PythonClass - title example </title>

Which should be generated by code like this::

    Title("PythonClass - title example")

Take a look at one of the other tests to get ideas, and maybe start with a copy and paste, and then change the names:

.. code-block:: python

    def test_title():
        e = Title("this is some text")
        e.append("and this is some more text")

        file_contents = render_result(e).strip()

        assert("this is some text") in file_contents
        assert("and this is some more text") in file_contents
        print(file_contents)
        assert file_contents.startswith("<title>")
        assert file_contents.endswith("</title>")

That's not going to pass, as there is no ``Title`` class. But before we get that far -- what else do we need to change about this test?
For starters, this test is appending additional content.
That's not very likely for a title, is it? So let's get rid of that line.

.. code-block:: python

    def test_title():
        e = Title("This is a Title")

        file_contents = render_result(e).strip()

        assert("This is a Title") in file_contents
        print(file_contents)
        assert file_contents.startswith("<title>")
        assert file_contents.endswith("</title>")

So that's a bit cleaner.  But let's look at those asserts -- what are we testing for?  Looks like we're testing for the correct start and end tags, and that the content is there. That's a pretty good start, but it isn't checking for newlines at all.  In fact, all the previous tests would pass even if our render method did not have any newlines in it at all. Which is probably OK -- html does not require newlines.  You could go back and update the tests to check for the proper newlines, though later on, when we get to indenting, we'll be doing that anyway.

But for this element, we want to make sure that we don't have any newlines. So let's add an assert for that:

.. code-block:: python

    assert "\n" not in file_contents

You can run the tests now if you like -- it will fail due to there being no Title element. So let's make one now. Remember that we want to start with a ``OneLineTag`` element, and then subclass ``Title`` from that.

.. code-block:: python

    class OneLineTag(Element):
        pass


    class Title(OneLineTag):
        tag = "title"

The ``pass`` means "do nothing." But it is required to satisfy Python. There needs to be *something* in the class definition.  So in this case, we have a ``OneLineTag`` class that is exactly the same as the ``Element`` class,  and a ``Title`` class that is the same except for the tag. Time to test again::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 10 items

    test_html_render.py .........F                                           [100%]

    =================================== FAILURES ===================================
    __________________________________ test_title __________________________________

        def test_title():
            e = Title("This is a Title")

            file_contents = render_result(e).strip()

            assert("This is a Title") in file_contents
            print(file_contents)
            assert file_contents.startswith("<title>")
            assert file_contents.endswith("</title>")
    >       assert "\n" not in file_contents
    E       AssertionError: assert '\n' not in '<title>\nThis is a Title\</title>'
    E         '\n' is contained here:
    E           <title>
    E         ? -------
    E           This is a Title
    E           </title>

    test_html_render.py:203: AssertionError
    ----------------------------- Captured stdout call -----------------------------
    <title>
    This is a Title
    </title>
    ====================== 1 failed, 9 passed in 0.12 seconds ======================

The title test failed on this assertion::

    >       assert "\n" not in file_contents

Which is what we expected because we haven't written a new render method yet.  But look at the end of the output, where is says ``-- Captured stdout call --``.  That shows you how the title element is being rendered -- with the newlines. That's there because there is a print in the test:

.. code-block:: python

  print(file_contents)

.. note::

  pytest is pretty slick with this. It "Captures" the output from print calls, etc., and then only shows them to you if a test fails.
  So you can sprinkle print calls into your tests, and it won't clutter the output -- you'll only see it when a test fails, which is when you need it.

This is a good exercise to go through. If a new test fails, it lets you know that the test itself is working, testing what it is supposed to test.

So how do we get this test to pass? We need a new render method for ``OneLineTag``.  For now, you can copy the render method from ``Element`` to ``OneLineTag``, and remove the newlines:

.. code-block:: python

    class OneLineTag(Element):

        def render(self, out_file):
            # loop through the list of contents:
            for content in self.contents:
                out_file.write("<{}>".format(self.tag))
                try:
                    content.render(out_file)
                except AttributeError:
                    out_file.write(content)
                out_file.write("</{}>\n".format(self.tag))

Notice that I left the newline in at the end of the closing tag -- we do want a newline there, so the next element won't get rendered on the same line.  And the tests::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 10 items

    test_html_render.py ..........                                           [100%]

    ========================== 10 passed in 0.03 seconds ===========================

We done good. But wait! there *is* a newline at the end, and yet the assert: ``assert "\n" not in file_contents`` passed!  Why is that?

Take a look at the code in the tests that renders the element:

.. code-block:: python

    file_contents = render_result(e).strip()

It's calling ``.strip()`` on the rendered string.  That will remove all whitespace from both ends -- removing that last newline.

However, there is still some extra code in that ``render()`` method.  It's still looping through the contents and checking for an ``Element`` type. But for this, we hope that there will only be one piece of content, and it should not be an element. So we can make the render method simpler:

.. code-block:: python

    class OneLineTag(Element):
        def render(self, out_file):
            out_file.write("<{}>".format(self.tag))
            out_file.write(self.contents[0])
            out_file.write("</{}>\n".format(self.tag))

If you are nervous about people appending content that will then be ignored, you can override the append method, too:

.. code-block:: python

    def append(self, content):
        raise NotImplementedError

``NotImplementedError`` means just what it says -- this method is not implemented.  My tests still pass, but how do I test to make sure that I can't append to a OneLineTag? Let's try that:

.. code-block:: python

    def test_one_line_tag_append():
        """
        You should not be able to append content to a OneLineTag
        """
        e = OneLineTag("the initial content")
        e.append("some more content")

        file_contents = render_result(e).strip()
        print(file_contents)

And run the tests::

    test_html_render.py:199:
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    self = <html_render.OneLineTag object at 0x1020bb198>
    content = 'some more content'

        def append(self, content):
    >       raise NotImplementedError
    E       NotImplementedError

    html_render.py:57: NotImplementedError
    ===================== 1 failed, 10 passed in 0.09 seconds ======================

Hmm. It raised a ``NotImplementedError``, which is what we want, but it is logging as a test failure.  An exception raised in a test is going to cause a failure -- but what we want is for the test to pass only *if* that exception is raised.
Fortunately, pytest has a utility to do just that. Make sure there is an ``import pytest`` in your test file, and then add this code:

.. code-block:: python

    def test_one_line_tag_append():
        """
        You should not be able to append content to a OneLineTag
        """
        e = OneLineTag("the initial content")
        with pytest.raises(NotImplementedError):
            e.append("some more content")

That ``with`` is a "context manager" (kind of like the file ``open()`` one). More on that later in the course, but what this means is that the test will pass if and only if the code inside that ``with`` block raised a ``NotImplementedError``.  If it raises something else, or it doesn't raise an exception at all, then the test will fail.

OK, I've got 11 tests passing now. How about you? Time for the next step.

.. _render_tutorial_4:

Step 4.
-------

From the exercise instructions:

"Extend the ``Element`` class to accept a set of attributes as keywords to the constructor, e.g. ``run_html_render.py``"

If you don't know what attributes of an element are, read up a bit more on html on the web, and/or take another look at :ref:`html_primer`. But in short, attributes are a way to "customize" an element -- give it some extra information. The syntax looks like this::

    <p style="text-align: center" id="intro">

Inside the opening tag, there is the tag name, then a space, then the attributes separated by spaces. Each attribute is a ``name="value"`` pair, with the name in plain text, and the value in quotes.

Note that these name:value pairs look a lot like python keyword arguments, which lends itself to an initialization signature. For the above example, we would create the element like so:

.. code-block:: python

  el = P("A paragraph of text", style="text-align: center", id="intro")

Which should result in the following html::

    <p style="text-align: center" id="intro">
    a paragraph of text
    </p>


Now that we know how to initialize an element with attributes, and how it should get rendered, we can write a test that will check if the attributes are rendered correctly. Something like:

.. code-block:: python

    def test_attributes():
        e = P("A paragraph of text", style="text-align: center", id="intro")

        file_contents = render_result(e).strip()
        print(file_contents)  # so we can see it if the test fails

        # note: The previous tests should make sure that the tags are getting
        #       properly rendered, so we don't need to test that here.
        #       so using only a "P" tag is fine
        assert "A paragraph of text" in file_contents
        # but make sure the embedded element's tags get rendered!
        # first test the end tag is there -- same as always:
        assert file_contents.endswith("</p>")

        # but now the opening tag is far more complex
        # but it starts the same:
        assert file_contents.startswith("<p")

Note that this doesn't (yet) test that the attributes are actually rendered, but it does test that you can pass them in to constructor. What happens when we run this test? ::

    =================================== FAILURES ===================================
    _______________________________ test_attributes ________________________________

        def test_attributes():
    >       e = P("A paragraph of text", style="text-align: center", id="intro")
    E       TypeError: __init__() got an unexpected keyword argument 'style'

    test_html_render.py:217: TypeError
    ===================== 1 failed, 11 passed in 0.19 seconds ======================

Yes, the new test failed -- isn't TDD a bit hard on the ego? So many failures! But why? Well, we passed in the ``style`` and ``id`` attributes as keyword arguments, but the ``__init__`` doesn't expect those arguments. Hence the failure.

So should be add those two as keyword parameters? Well, no we shouldn't because those are two arbitrary attribute names; we need to support virtually any attribute name. So how do you write a method that will accept ANY keyword argument? Time for our old friend ``**kwargs``. ``**kwargs**`` will allow any keyword argument to be used, and will store them in the ``kwargs`` dict. So time to update the ``Element.__init__`` like so:

.. code-block:: python

    def __init__(self, content=None, **kwargs):

But then, make sure to *do* something with the ``kwargs`` dict -- you need to store those somewhere. Remember that they are a collection of attribute names and values -- and you will need them again when it's time to render the opening tag. How do you store something so that it can be used in another method? I'll leave that as an exercise for the reader.

And let's try to run the tests again::

    ========================== 12 passed in 0.07 seconds ===========================

They passed! Great, but did we test whether the attributes get rendered in the tag correctly? No -- not yet, let's make sure to add that.  It may be helpful to add and ``assert False`` in there, so we can see what our tag looks like while we work on it::

    ...
           assert False
    E       assert False

    test_html_render.py:243: AssertionError
    ----------------------------- Captured stdout call -----------------------------
    <p>
    A paragraph of text
    </p>
    ===================== 1 failed, 11 passed in 0.11 seconds ======================

OK, so we have a regular old <p> element -- no attributes at all -- no surprise here.  Let's first add a couple tests for the attributes:

.. code-block:: python

    # order of the tags is not important in html, so we need to
    # make sure not to test for that
    # but each attribute should be there:
    assert 'style="text-align: center"' in file_contents
    assert 'id="intro"' in file_contents

We know the tests will fail -- so let's go straight to the code. We need to update our ``render()`` method to put the attributes in the opening tag. Let's remind ourselves what this needs to look like::

    <p style="text-align: center" id="intro">

So we need to render the ``<``, then the ``p``, then a bunch of attribute name=value pairs. Let's start with breaking up the rendering of the opening tag, and make sure the existing tests still pass.

.. code-block:: python

    def render(self, out_file):
        # loop through the list of contents:
        open_tag = ["<{}".format(self.tag)]
        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        ...

OK, the rest of the tests are still passing for me; I haven't broken anything else. Now to add code to render the attributes. You'll need to write some sort of loop to loop through each attribute, probably looping through the keys and the values:

.. code-block:: python

    for key, value in self.attributes:

Then you can render them in html form inside that loop.

Once you've done that, run the tests again. When I do that, mine passes the asserts checking the attributes, but fails on the ``assert False``, so I can see how it's rendering::

    >       assert False
    E       assert False

    test_html_render.py:247: AssertionError
    ----------------------------- Captured stdout call -----------------------------
    <pid="intro" style="text-align: center">
    A paragraph of text
    </p>
    ===================== 1 failed, 11 passed in 0.11 seconds ======================

Hmmm -- the attributes are rendered correctly, but there is no space between the "p" (that tag name) and the first attribute. So let's update our tests to make sure that we check for that:

.. code-block:: python

        assert file_contents.startswith("<p ") # make sure there's space after the p

Note that I added a space after the ``p`` in the test. Now my test is failing on that line, so I need to fix it -- I've added an extra space in there, and now my test passes, and I like how it's rendered::

    <p style="text-align: center" id="intro">
    A paragraph of text
    </p>

However, my code for rendering the opening tag is a bit klunky -- how about yours? Perhaps you'd like to refactor it? Before you do that, you might want to make your tests a bit more robust. This is really tricky. It's very hard to test for everytihng that might go wrong, without nailing down the expected results too much. For example, in this case, we haven't tested that there is a space between the two attributes. In fact, this would pass our test::

    <p style="text-align: center"id="intro">
    A paragraph of text
    </p>

See how there is no space before "id"? But the order of the attributes is arbitrary, so we don't want to assume that the style will come before id. You could get really fancy with parsing the results, but I think we could get away with assuring there are the right number of spaces in the opening tag.

.. code-block:: python

    assert file_contents[:file_contents.index(">")].count(" ") == 3

This now fails with my broken code, but passes when I fix it with that space between the attributes. What else might you want to check to make sure it's all good?

Here's my final test for attribute rendering:

.. code-block:: python

    def test_attributes():
        e = P("A paragraph of text", style="text-align: center", id="intro")

        file_contents = render_result(e).strip()
        print(file_contents)  # so we can see it if the test fails

        # note: The previous tests should make sure that the tags are getting
        #       properly rendered, so we don't need to test that here.
        #       so using only a "P" tag is fine
        assert "A paragraph of text" in file_contents
        # but make sure the embedded element's tags get rendered!
        # first test the end tag is there -- same as always:
        assert file_contents.endswith("</p>")

        # but now the opening tag is far more complex
        # but it starts the same:
        assert file_contents.startswith("<p ") # make sure there's space after the p

        # order of the tags is not important in html, so we need to
        # make sure not to test for that
        # but each attribute should be there:
        assert 'style="text-align: center"' in file_contents
        assert 'id="intro"' in file_contents

        # # just to be sure -- there should be a closing bracket to the opening tag
        assert file_contents[:-1].index(">") > file_contents.index('id="intro"')
        assert file_contents[:file_contents.index(">")].count(" ") == 3

With this test in place, you can safely refactor your attribute rendering if you like. I know I did.

Step 5:
-------

Create a ``SelfClosingTag`` subclass of Element, to render tags like::

    <hr />

and::

    <br />

(horizontal rule and line break)

Including with attributes::

    <hr width="400" />

So let's start with two tests:

.. code-block:: python

    def test_hr():
        """a simple horizontal rule with no attributes"""
        hr = Hr()
        file_contents = render_result(hr)
        print(file_contents)
        assert file_contents == '<hr />\n'


    def test_hr_attr():
        """a horizontal rule with an attribute"""
        hr = Hr(width=400)
        file_contents = render_result(hr)
        print(file_contents)
        assert file_contents == '<hr width="400" />\n'

Which, of course, will fail initially.

We'll want multiple self closing tags -- so we'll start with a base class, and then derive the Hr tag from that:

.. code-block:: python

    class SelfClosingTag(Element):
        pass


    class Hr(SelfClosingTag):
        tag = "hr"

Test still fails -- but gets further.
You'll need to override the ``render()`` method:

.. code-block:: python

    class SelfClosingTag(Element):

        def render(self, outfile):
            # put rendering code here.

What needs to be there? Well, self closing tags can have attributes, same as other elements.
So we need a lot of the same code here as with the other ``render()`` methods.  You could copy and paste the ``Element.render()`` method, and edit it a bit.  But that's a "Bad Idea" -- remember DRY (Don't Repeat Yourself)?
You really don't want two copies of that attribute rendering code you worked so hard on.
How do we avoid that? We take advantage of the power of subclassing. If you put the code to render the opening (and closing) tags in it's own method, then we can call that method from multiple render methods, something like:

.. code-block:: python

    def render(self, out_file):
        # loop through the list of contents:
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        out_file.write(self._close_tag())
        out_file.write("\n")

So instead of making the tag in the render method itself, we call the ``_open_tag`` and ``_close_tag`` methods. Note that I gave those names with a single underscore at the beginning. This is a Python convention for indicating a "private" method -- one that is expected to be used internally, rather than by client code.

Are all the existing tests still passing?

Now that you've got the tag-building code in its own method, we can give the self closing tag a render method something like this:

.. code-block:: python

    def render(self, outfile):
        tag = self._open_tag()[:-1] + " />\n"
        outfile.write(tag)

And do your tests pass? Once they do add a couple more for the "br" element:

.. code-block:: python

    def test_br():
        br = Br()
        file_contents = render_result(br)
        print(file_contents)
        assert file_contents == "<br />\n"


    def test_content_in_br():
        with pytest.raises(TypeError):
            br = Br("some content")


    def test_append_content_in_br():
        with pytest.raises(TypeError):
            br = Br()
            br.append("some content")

Getting that first test to pass should be straightforward -- but what about the other two? Self closing tags are now supposed to contain any content. So you want your ``SelfClosingTag`` class to raise an exception if you try to create one with some content. But you also want it to raise an exception if you try to append content. So do we need to override both the ``__init__()`` and ``append()`` methods? Maybe not.

The ``__init__`` needs to do some other initializing, so not as easy to override as ``append``.  Let's start with the ``append`` method. We need it to do nothing other than raise a ``TypeError``:

.. code-block:: python

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

And run your tests. I still get a single failure::

    =================================== FAILURES ===================================
    ______________________________ test_content_in_br ______________________________

        def test_content_in_br():
            with pytest.raises(TypeError):
    >           br = Br("some content")
    E           Failed: DID NOT RAISE <class 'TypeError'>

    test_html_render.py:297: Failed
    ===================== 1 failed, 17 passed in 0.08 seconds ======================

So ``append`` did the right thing. But we still have a failure when we try to initialize it with content. So we want to override the ``__init__``, check if there was any content passed in, and if there is, raise an error. And if not, then call the usual ``__init__``.

.. code-block:: python

    class SelfClosingTag(Element):

        def __init__(self, content=None, **kwargs):
            if content is not None:
                raise TypeError("SelfClosingTag can not contain any content")
            super().__init__(content=content, **kwargs)

What's that ``super()`` call? That's a way to call a method on the "super class'" -- that is, the class that this class is derived from. In this case, that's exactly the same as if we had written:

.. code-block:: python

        def __init__(self, content=None, **kwargs):
            if content is not None:
                raise TypeError("SelfClosingTag can not contain any content")
            Element.__init__(self, content=content, **kwargs)

But ``super`` provides some extra features if you are doing multiple inheritance. And it makes your intentions clear.

I've now got 18 tests passing. How about you? And I can also uncomment step 5 in ``run_html_render.py``, and get something reasonable::

    $ python run_html_render.py
    <html>
    <head>
    <title>PythonClass = Revision 1087:</title>
    </head>
    <body>
    <p style="text-align: center; font-style: oblique;">
    Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text
    </p>
    <hr />
    </body>
    </html>

If you get anything very different than this, write some tests to catch the error, and then fix them :-)


Step 6:
-------

Create an ``A`` class for an anchor (link) element. Its constructor should look like::

    A(self, link, content)

where ``link`` is the link, and ``content`` is what you see. It can be called like so::

    A("http://google.com", "link to google")

and it should render like::

    <a href="http://google.com">link to google</a>

Notice that while the a ("anchor") tag is kind of special, the link is simply an "href" (hyperlink reference) attribute. So we should be able to use most of our existing code, but simply add the link as another attribute.

You know that drill now. Create a test first: one that makes the above call, and then checks that you get the results expected. Notice that this is a single line tag, so it should subclass from OneLineTag. If I start with that, I get::

    =================================== FAILURES ===================================
    _________________________________ test_anchor __________________________________

        def test_anchor():
    >       a = A("http://google.com", "link to google")
    E       TypeError: __init__() takes from 1 to 2 positional arguments but 3 were given

    test_html_render.py:307: TypeError

Hmm -- a ``TypeError`` in the ``__init__``. Well, that makes sense because we need to be able to pass the link in to it. We will need to override it, of course:

.. code-block:: python

    class A(OneLineTag):

        tag = 'a'

        def __init__(self, link, content=None, **kwargs):
            super().__init__(content, **kwargs)

Notice that I added the "link" parameter at the beginning, and that the rest of the parameters are the same as for the base ``Element`` class. This is a good approach. If you need to add an extra parameter when subclassing, put it at the front of the parameter list. We then call ``super().__init__`` with the content and any other keyword arguments. We haven't actually done anything with the link, but when I run the tests, it gets further, failing on the rendering.

So we need to do something with the link. But what? Do we need a new render method? Maybe not. After all, the link is really just the value of the "href" attribute. So we can simply create an href attribute, and the existing rendering code should work.

How are the attributes passed in? They are passed in in the ``kwargs`` dict. So we can simply add the link to the ``kwargs`` dict before calling the superclass initializer:

.. code-block:: python

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

And run the tests::

    =================================== FAILURES ===================================
    _________________________________ test_anchor __________________________________

        def test_anchor():
            a = A("http://google.com", "link to google")
            file_contents = render_result(a)
            print(file_contents)
    >       assert file_contents.startswith('<a ')
    E       AssertionError: assert False
    E        +  where False = <built-in method startswith of str object at 0x1105e28e8>('<a ')
    E        +    where <built-in method startswith of str object at 0x1105e28e8> = '<a>link to google</a>\n'.startswith

    test_html_render.py:310: AssertionError
    ----------------------------- Captured stdout call -----------------------------
    <a>link to google</a>

    ===================== 1 failed, 18 passed in 0.07 seconds =====================

Darn -- not passing! (Did yours pass?) Even though we added the ``href`` to the kwargs dict, it didn't get put in the attributes of the tag.  Why not? Think carefully about the code. Where should the attributes be added? In the ``render()`` method.
But *which* render method is being used here? Well, the ``A`` class is a subclass of ``OneLineTag``, which has defined its own ``render()`` method.
So take a look at the ``OneLineTag`` ``render()`` method. Oops, mine doesn't have anything in to render attributes -- I wrote that before we added that feature.
So it's now time to go in and edit that render method to use the ``_open_tag`` and ``_close_tag`` methods.

The tests should all pass now -- and you have a working anchor element.

Step 7:
-------

Making the list elements is pretty straightforward -- go ahead and do those -- and write some tests for them!

Header Elements
...............

You should have the tools to do this. First, write a couple tests.

Then decide what to subclass for the header elements? Which of the base classes you've developed is most like a header?

Then think about how you will update the ``__init__`` of your header subclass. It will need to take an extra parameter -- the level of the header:

.. code-block:: python

    def __init__(self, level, content=None, **kwargs):

But what to do with the level parameter? In this case, each level will have a different tag: ``h1``, ``h2``, etc. So you need to set the tag in the ``__init__``. So far, the tag has been a class attribute -- all instances of the class have the same tag.
In this case, each instance can have a different tag -- determined at initialization time. But how to override a class attribute? Think about how you access that attribute in your render methods: ``self.tag``.
When you make a reference to ``self.something``, Python first checks if "something" is an instance attribute. Then, if not, it checks for a class attribute, and, if not, then it looks in the superclasses.
So in this case, of you set an instance attribute for the tag -- that is what will be found in the other methods. So in the ``__init__``, you can set ``self.tag=the_new_tag_value``, which will be ``h1``, or ``h2``, or ...

Step 8:
-------

You have all the tools now for making a proper html element -- it should render as so::

  <!DOCTYPE html>
  <html>
  <head>
  <meta charset="UTF-8" />
  <title>Python Class Sample page</title>
  </head>
  ...

That is, put a doctype tag at the top, before the html opening tag.

(Note that that may break an earlier test. Update that test!)

Step 9:
-------

**Adding Indentation**

Be sure to read the instructions for this carefully -- this is a bit tricky. But it's also fairly straightforward once you "get it." The trick here is that a given element can be indented some arbitrary amount and there is no way to know until render time how deep it is. But when a given element is rendering itself, it needs to know how deep it's indented, and it knows that the sub-elements need to be indented one more level. So by passing a parameter to each ``render()`` method that tells that element how much to indent itself, we can build a flexible system.

Begin by uncommenting the tests in the test file for indentation:

``test_indent``, ``test_indent_contents``, ``test_multiple_indent``, and ``test_element_indent1``.


These are probably not comprehensive, but they should get you started. If you see something odd in your results, make sure to add a test for that before you fix it.

Running these new tests should result in 4 failures -- many (all?) of them like this::

  AttributeError: type object 'Element' has no attribute 'indent'

So the first step is to give you Element base class an ``indent`` attribute. This is the amount that you want one level of indentation to be -- maybe two or four spaces. You want everything the be indented the same amount, so it makes sense that you put it as a class attribute of the base class -- then *all* elements will inherit the same value. And you can change it in that one place if you want.

Once I add the ``indent`` parameter, I still get four failures -- three of them are for the results being incorrect -- which makes sense, because we haven't implemented that code yet. One of them is::

            # this so the tests will work before we tackle indentation
            if ind:
    >           element.render(outfile, ind)
    E           TypeError: render() takes 2 positional arguments but 3 were given

This is the next one to tackle; our ``render()`` methods all need to take an additional optional parameter, the current level of indentation. Remember to add that to *all* of your ``render()`` methods:

.. code-block:: python

    def render(self, out_file, cur_ind=""):

Once I do that, I still get four failures. But they are all about the rendered results being incorrect; the rendered indentation levels are not right.

Now it's time to go in one by one and add indentation code to get those tests to pass.

I got them all to pass. But when I rendered a full page (by running ``run_html_render.py``), I found some issues. The elements that overrode the ``render()`` methods where not indented properly: ``OneLineTag`` and ``SelfClosingTag``.

Write at least one test for each of those, and then go fix those ``render()`` methods!

What have you done?
-------------------

**Congrats!**

You've gotten to the end of the project. By going through this whole procedure, you've done a lot of test-driven development, and built up a class system that takes advantage of the key features of object oriented systems in Python. I hope this has given you a better understanding of:

* class attributes vs. instance attributes

* subclassing

* overriding:

  - class attributes

  - class attributes with instance attributes

  - methods

* calling a superclass' method from an overridden method.

* defining a "private" method to be used by sub-classes overridden methods to make DRY code.

* polymorphism -- having multiple classes all be used in the same way (calling the ``render`` method in this case)
