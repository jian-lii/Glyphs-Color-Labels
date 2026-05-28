# MenuTitle: Color Label Manager
# -*- coding: utf-8 -*-

from AppKit import NSBezierPath, NSColor, NSFont, NSImage, NSEvent, NSEventModifierFlagOption
from GlyphsApp import Glyphs
from vanilla import Button, FloatingWindow


COLORS = [
    (0, (0.95, 0.16, 0.08)),
    (1, (1.00, 0.53, 0.05)),
    (2, (0.82, 0.49, 0.14)),
    (3, (1.00, 0.84, 0.00)),
    (4, (0.66, 0.96, 0.17)),
    (5, (0.07, 0.72, 0.15)),
    (6, (0.04, 0.61, 1.00)),
    (7, (0.05, 0.25, 0.98)),
    (8, (0.43, 0.09, 0.92)),
    (9, (0.98, 0.22, 0.67)),
    (10, (0.76, 0.76, 0.76)),
    (11, (0.34, 0.34, 0.34)),
]


def optionKeyPressed():

    keys = NSEvent.modifierFlags()

    return keys & NSEventModifierFlagOption == NSEventModifierFlagOption


def setGlyphLabelColor(glyph, index):

    if index is None:
        glyph.color = None
    else:
        glyph.setColorIndex_(index)


def setLayerLabelColor(layer, index):

    if index is None:
        layer.color = None
    else:
        layer.setColorIndex_(index)


def warmUpColorSetters():

    font = Glyphs.font

    if not font or not font.selectedLayers:
        return

    layer = font.selectedLayers[0]

    if not layer:
        return

    getattr(layer, "setColorIndex_", None)

    glyph = layer.parent

    if glyph:
        getattr(glyph, "setColorIndex_", None)


def applyColor(index):

    font = Glyphs.font

    if not font:
        return

    applyToLayers = optionKeyPressed()
    selectedLayers = tuple(font.selectedLayers)

    if not selectedLayers:
        return

    font.disableUpdateInterface()

    try:

        if applyToLayers:

            for layer in selectedLayers:

                if layer:
                    setLayerLabelColor(layer, index)

            return

        done = set()

        for layer in selectedLayers:

            glyph = layer.parent if layer else None

            if not glyph:
                continue

            gid = glyph.id

            if gid in done:
                continue

            done.add(gid)

            setGlyphLabelColor(glyph, index)

    finally:

        font.enableUpdateInterface()


class Palette(object):

    def __init__(self):

        self.cache = {}
        warmUpColorSetters()

        self.w = FloatingWindow((222, 74), "")

        self.build()

        self.w.open()

    def build(self):

        left = 12
        top = 10

        size = 25
        gap = 3

        for i, (index, rgb) in enumerate(COLORS):

            x = left + (i % 6) * (size + gap)
            y = top + (i // 6) * (size + gap)

            b = Button(
                (x, y, size, size),
                "",
                callback=lambda s, n=index: applyColor(n)
            )

            ns = b.getNSButton()

            ns.setBordered_(False)
            ns.setTitle_("")
            ns.setImage_(self.swatch(rgb))

            setattr(self.w, "b%d" % i, b)

        c = Button(
            (186, 13, 16, 16),
            "×",
            callback=lambda s: applyColor(None)
        )

        ns = c.getNSButton()

        ns.setBordered_(False)
        ns.setFont_(NSFont.systemFontOfSize_(16))

        self.w.clear = c

    def swatch(self, rgb):

        key = str(rgb)

        if key in self.cache:
            return self.cache[key]

        img = NSImage.alloc().initWithSize_((25, 25))

        img.lockFocus()

        path = NSBezierPath.bezierPathWithOvalInRect_(
            ((4, 4), (16, 16))
        )

        NSColor.colorWithCalibratedRed_green_blue_alpha_(
            rgb[0],
            rgb[1],
            rgb[2],
            1
        ).set()

        path.fill()

        border = tuple(min(1, c * 0.72) for c in rgb)

        NSColor.colorWithCalibratedRed_green_blue_alpha_(
            border[0],
            border[1],
            border[2],
            0.88
        ).set()

        path.setLineWidth_(0.65)

        path.stroke()

        img.unlockFocus()

        self.cache[key] = img

        return img


try:
    __palette__.w.close()
except:
    pass

__palette__ = Palette()
