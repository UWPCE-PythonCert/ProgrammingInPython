#!/usr/bin/env python3

"""A class-based system for rendering html."""


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "  "

    def __init__(self, content=None, **kwargs):
        self.contents = []
        if content is not None:
            self.contents.append(content)
        self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        if self.attributes:  # only if there are any attributes
            open_tag = ["<{}".format(self.tag)]
            atts = [f'{key}="{value}"' for key, value in self.attributes.items()]
            tag = f"<{self.tag} {' '.join(atts)}>"
        else:
            tag = f"<{self.tag}>"
        return tag

    def _close_tag(self):
        return f"</{self.tag}>"

    def render(self, out_file, cur_ind=""):
        # loop through the list of contents:
        out_file.write(cur_ind)
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent)
                out_file.write(content)
                out_file.write("\n")
        out_file.write(cur_ind)
        out_file.write(self._close_tag())
        out_file.write("\n")


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Head(Element):
    tag = 'head'


class OneLineTag(Element):

    def append(self, content):
        if self.contents:
            raise TypeError("OneLineTag elements can not have content added")
        else:
            super().append(content)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())
        out_file.write("\n")


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_ind=""):
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(cur_ind)
        out_file.write(tag)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class Hr(SelfClosingTag):

    tag = "hr"


class Br(SelfClosingTag):

    tag = "br"


class A(OneLineTag):

    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class H(OneLineTag):
    """
    section head
    """
    tag = "H"

    def __init__(self, level, *args, **kwargs):
        self.tag = "h" + str(int(level))
        super().__init__(*args, **kwargs)


class Ul(Element):
    """
    unordered list
    """
    tag = "ul"


class Li(Element):
    """
    list element
    """
    tag = "li"


class Meta(SelfClosingTag):
    """
    metadata tag
    """
    tag = "meta"
