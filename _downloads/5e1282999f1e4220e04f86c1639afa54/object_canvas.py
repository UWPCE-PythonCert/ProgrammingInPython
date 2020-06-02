#!/usr/bin/env python

"""
object canvas: an example of multiple inheritance and mix-ins

This is a simplified version of FloatCanvas -- an extension to the
wxPython desktop GUI library

FloatCanvas is a system for handling zoomable and scalable graphics in
a object-persistant way. That is, graphic objects like circles and
rectangles and what not can be created ahead of time, and then the Canvas
can render them accoding to the current zoom level and pan position, etc.

This lets the user think about their graphics object should look like,
and not have to worry about exactly how to draw them -- or their pixel
coordinates, or anything else.

If you want to see all this in all its full complexity, the FloatCanvas
code in part of the wxPython project, and can be seen here:

https://github.com/wxWidgets/Phoenix/tree/master/wx/lib/floatcanvas

This code: object_canvas is a simplified version. It doesn't allow scaling
or zooming, and only renders in pixel coordinates. But it does allow
object-persistance, and is a nice demo of the use of mixins.

This version requires the Python Imaging Library to do the rendering.

You can get it by installing the "pillow" package from PyPi:

python -m pip install pillow

Its docs are here:

https://pillow.readthedocs.io/en/4.3.x/index.html

"""
from math import ceil

from PIL import Image, ImageDraw


class ObjectCanvas():
    """
    An object-oriented canvas for drawing things
    """

    def __init__(self,
                 size=(500, 500),
                 background=(255, 255, 255, 0)
                 ):
        self.size = size
        self.draw_objects = []
        self.background = background

    def add_object(self, draw_object, position="top"):
        #fixme: maybe overload the inplace addition operator?
        """
        Add a new object to the canvas.

        :param: draw_object -- DrawObject to add

        :param position="top": Position to add the object. "top" puts
                               the object on top of teh other objects.
                               "bottom" puts them on the bottom of the stack.
                               A integer puts it in that place in the order
                               -- 0 is the bottom.
        """
        if position == "top":
            self.draw_objects.append(draw_object)
        elif position == "bottom":
            self.draw_objects.insert(0, draw_object)
        else:
            self.draw_objects.insert(position, draw_object)

    def render(self, filename):
        """
        render the drawing to a file with the given name
        """
        image = Image.new('RGBA', self.size, color=self.background)
        drawer = ImageDraw.Draw(image)

        for do in self.draw_objects:
            do.draw(drawer)
        image.save(filename)


class DrawObject:
    """
    base class for all draw objects
    """

    def __init__(self, *args, **kwargs):
        print("in DrawObject __init__", kwargs)
        # do nothing, but to make super happy
        super().__init__(*args, **kwargs)


class LineObject:
    """
    mixin for classes with a line
    """

    def __init__(self,
                 line_color='black',
                 line_width=1,
                 **kwargs,
                 ):
        print("in LineObject __init__", kwargs)
        super().__init__(**kwargs)
        self.line_color = line_color
        self.line_width = line_width


class FillObject:
    """
    mixin for classes with a fill
    """

    def __init__(self,
                 fill_color=None,
                 **kwargs
                 ):
        print("in FillObject __init__", kwargs)
        self.fill_color = fill_color


class PolyLine(DrawObject, LineObject):
    def __init__(self,
                 vertices,
                 **kwargs
                 ):
        self.vertices = vertices
        print("in PolyLine init", kwargs)
        super().__init__(**kwargs)

    def draw(self, drawer):
        """
        draw the object

        :param drawer: PIL.ImageDraw object to draw to
        """
        drawer.line(self.vertices, fill=self.line_color, width=self.line_width)


class Circle(DrawObject, LineObject, FillObject):
    def __init__(self, center, diameter, **kwargs):
        self.center = center
        self.diameter = diameter
        super().__init__(**kwargs)

    def draw(self, drawer):
        """
        Draw the object
        :param drawer: PIL.ImageDraw object to draw to
        """
        r = self.diameter // 2
        c = self.center
        # PIL doesn't support different line widths for ellipses,
        # so we fake it.
        lw2 = self.line_width / 2
        bounds = ((c[0] - r, c[1] - r), (c[0] + r, c[1] + r))
        drawer.ellipse(bounds, fill=self.fill_color, outline=None)
        for i in range(int(ceil(lw2)), int(-lw2), -1):
            r = self.diameter // 2 + i
            bounds = ((c[0] - r, c[1] - r), (c[0] + r, c[1] + r))
            drawer.ellipse(bounds, fill=None, outline=self.line_color)






