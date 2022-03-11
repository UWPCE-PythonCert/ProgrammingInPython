#!/usr/bin/env python3

"""
test code for the object_canvas

Note: Testing image generation is hard.  So for now, this mostly just
      tests that the rendering function runs.
      And during development, you can look at the resulting files.

      One could store "properly" rendered results for future tests to
      check against.
"""

# import os
import pathlib
import object_canvas as oc

SAVE_ALL=True  # save all the temp files?


def render_to_file(canvas, filename="test_image.png", save=False):
    """
    utility to render a canvas to a file

    :param filename: name of file to render to it will be put in a test_images dir.

    :param remove=True: whether to remove the file after rendering.
    """
    path = pathlib.Path("test_images")
    path.mkdir(exist_ok=True)
    path /= filename
    canvas.render(str(path))
    assert path.is_file()
    if not (SAVE_ALL or save):
        path.unlink()


def test_init():
    canvas = oc.ObjectCanvas()

    assert canvas

def test_backgound():
    canvas = oc.ObjectCanvas(background='blue')
    render_to_file(canvas, "blue_background.png")

def test_polyline():
    """
    can we draw a polyline?
    """
    canvas = oc.ObjectCanvas()
    points = ((10, 10),  # this should be a triangle
              (10, 400),
              (400, 10),
              (10, 10),
              )

    pl = oc.PolyLine(points)
    canvas.add_object(pl)
    render_to_file(canvas, "polyline.png")


def test_circle():
    canvas = oc.ObjectCanvas()
    center = (100, 100)
    diameter = 75
    for line_width in range(1, 5):
        c = oc.Circle(center,
                      diameter,
                      line_color="red",
                      fill_color="blue",
                      line_width=line_width,
                      )
        canvas.add_object(c)
        center = (center[0] + 50, center[0] + 50)
    render_to_file(canvas, "circle.png")

