"""Rasterize an OFL serif onto a coarse pixel grid and rebuild as a real TTF/WOFF2.
Every glyph = union of pixel-square contours (horizontal runs merged per row)."""
import sys
import freetype
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen

SRC = sys.argv[1]
PPEM = int(sys.argv[2])          # pixel grid per em — coarser = chunkier
OUT = sys.argv[3]
FAMILY = sys.argv[4]

UPM = 1024
U = UPM / PPEM                   # font units per pixel

CHARS = [chr(c) for c in range(32, 127)] + list("’‘“”—–·₹…é")

face = freetype.Face(SRC)
face.set_pixel_sizes(0, PPEM)

def glyph_pixels(ch):
    face.load_char(ch, freetype.FT_LOAD_RENDER | freetype.FT_LOAD_TARGET_MONO | freetype.FT_LOAD_MONOCHROME)
    g = face.glyph
    bmp = g.bitmap
    rows, width, pitch = bmp.rows, bmp.width, bmp.pitch
    buf = bmp.buffer
    px = []
    for r in range(rows):
        row_runs = []
        c = 0
        while c < width:
            byte = buf[r * pitch + (c >> 3)]
            on = (byte >> (7 - (c & 7))) & 1
            if on:
                start = c
                while c < width:
                    byte = buf[r * pitch + (c >> 3)]
                    if not ((byte >> (7 - (c & 7))) & 1):
                        break
                    c += 1
                row_runs.append((start, c))   # [start, c) filled
            else:
                c += 1
        if row_runs:
            px.append((r, row_runs))
    adv = g.advance.x >> 6
    return px, g.bitmap_left, g.bitmap_top, adv

glyph_order = [".notdef"]
cmap = {}
glyphs = {}
metrics = {}

# .notdef: empty box
pen = TTGlyphPen(None)
glyphs[".notdef"] = pen.glyph()
metrics[".notdef"] = (int(UPM * 0.5), 0)

for ch in CHARS:
    if face.get_char_index(ord(ch)) == 0:
        print("skip (missing in source):", repr(ch))
        continue
    gname = "uni%04X" % ord(ch)
    runs, left, top, adv = glyph_pixels(ch)
    pen = TTGlyphPen(None)
    for r, row_runs in runs:
        y_top = (top - r) * U
        y_bot = y_top - U
        for start, end in row_runs:
            x0 = (left + start) * U
            x1 = (left + end) * U
            pen.moveTo((round(x0), round(y_bot)))
            pen.lineTo((round(x1), round(y_bot)))
            pen.lineTo((round(x1), round(y_top)))
            pen.lineTo((round(x0), round(y_top)))
            pen.closePath()
    glyphs[gname] = pen.glyph()
    metrics[gname] = (round(adv * U), round(left * U))
    glyph_order.append(gname)
    cmap[ord(ch)] = gname

asc = round((face.size.ascender >> 6) * U)
desc = round((face.size.descender >> 6) * U)

fb = FontBuilder(UPM, isTTF=True)
fb.setupGlyphOrder(glyph_order)
fb.setupCharacterMap(cmap)
fb.setupGlyf(glyphs)
fb.setupHorizontalMetrics(metrics)
fb.setupHorizontalHeader(ascent=asc, descent=desc)
fb.setupNameTable({"familyName": FAMILY, "styleName": "Regular",
                   "fullName": FAMILY, "psName": FAMILY.replace(" ", ""),
                   "licenseDescription": "Derived from Instrument Serif (SIL Open Font License 1.1). This derived font is also licensed under the OFL 1.1."})
fb.setupOS2(sTypoAscender=asc, sTypoDescender=desc, usWinAscent=max(asc, 0), usWinDescent=abs(min(desc, 0)))
fb.setupPost()
fb.save(OUT + ".ttf")

f = fb.font
f.flavor = "woff2"
f.save(OUT + ".woff2")
print("built", OUT, "ppem", PPEM, "glyphs", len(glyph_order))
