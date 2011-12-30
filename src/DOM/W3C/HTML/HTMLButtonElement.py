#!/usr/bin/env python
from __future__ import with_statement

from HTMLElement import HTMLElement
from attr_property import attr_property


class HTMLButtonElement(HTMLElement):
    def __init__(self, doc, tag):
        HTMLElement.__init__(self, doc, tag)

    @property
    def form(self):
        pass

    accessKey       = attr_property("accesskey")
    disabled        = attr_property("disabled", bool)
    name            = attr_property("name")
    tabIndex        = attr_property("tabindex", long)
    type            = attr_property("type")
    value           = attr_property("value")

    def onclick(self):
        pass
