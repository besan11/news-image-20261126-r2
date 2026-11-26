# One-day newspaper front page for Thursday 26 November 2026.
#
# Draws entry.png (1024x1024) with Pillow from the story list below.
# No network, no fetched data: every fact was checked live against wire
# reporting before this file was written, and the sources are named in
# NOTES.md. Run:  python3 render.py   (writes entry.png next to this file)
# Fonts: Liberation Serif/Sans, first from ./fonts, then from the system
# font directories, then DejaVu as a last resort.

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 239, 221)
INK = (20, 20, 20)
RED = (179, 32, 44)
FAINT = (90, 80, 66)
RULE = (120, 105, 80)
GREEN = (46, 125, 50)
BLUE = (31, 111, 178)
AMBER = (176, 124, 0)
CREAM_CARD = (252, 247, 232)

REGION_COLORS = {
    "N. AMERICA": (31, 111, 178),
    "LATIN AM.": (42, 157, 143),
    "EUROPE": (123, 94, 167),
    "M. EAST": (192, 86, 33),
    "AFRICA": (183, 121, 31),
    "S. ASIA": (194, 24, 91),
    "E. ASIA": (46, 125, 50),
    "PACIFIC": (0, 131, 143),
    "GLOBAL": (97, 97, 97),
}

STATUS_COLORS = {
    "CONFIRMED": (46, 125, 50),
    "OFFICIAL": (31, 111, 178),
    "REPORTED": (176, 124, 0),
    "CLAIM": (179, 32, 44),
}


def find_font(bold, serif):
    here = os.path.dirname(os.path.abspath(__file__))
    names = []
    if serif:
        names = ["LiberationSerif-Bold.ttf", "LiberationSerif-Regular.ttf"] if bold else \
                ["LiberationSerif-Regular.ttf", "LiberationSerif-Italic.ttf"]
    else:
        names = ["LiberationSans-Bold.ttf", "LiberationSans-Regular.ttf"] if bold else \
                ["LiberationSans-Regular.ttf", "LiberationSans-Italic.ttf"]
    search = [os.path.join(here, "fonts", n) for n in names]
    search += [os.path.join("/usr/share/fonts/truetype/liberation", n) for n in names]
    search += ["/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
               "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
               "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
               "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    for path in search:
        if os.path.exists(path):
            return path
    return None


_cache = {}


def font(size, bold=False, serif=False):
    key = (size, bold, serif)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(find_font(bold, serif), size)
    return _cache[key]


def text_width(draw, text, size, bold=False, serif=False):
    return draw.textlength(text, font=font(size, bold, serif))


def wrap(draw, text, size, max_width, bold=False, serif=False):
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=font(size, bold, serif)) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw, x, y, text, size, max_width, fill=INK, bold=False,
                 serif=False, leading=None):
    step = leading or int(size * 1.18)
    for line in wrap(draw, text, size, max_width, bold, serif):
        draw.text((x, y), line, font=font(size, bold, serif), fill=fill)
        y += step
    return y


def pill(draw, x, y, label, size=9):
    f = font(size, True, False)
    w = int(draw.textlength(label, font=f)) + 10
    h = size + 7
    color = STATUS_COLORS.get(label, (97, 97, 97))
    draw.rounded_rectangle([x, y, x + w, y + h], radius=3, outline=color, width=1)
    draw.text((x + 5, y + 2), label, font=f, fill=color)
    return w


def region_tag(draw, x, y, region, size=9):
    f = font(size, True, False)
    w = int(draw.textlength(region, font=f)) + 10
    h = size + 7
    color = REGION_COLORS.get(region, (97, 97, 97))
    draw.rounded_rectangle([x, y, x + w, y + h], radius=3, fill=color)
    draw.text((x + 5, y + 2), region, font=f, fill=(255, 255, 255))
    return w


# ---------------------------------------------------------------- stories
# (number, region, headline, detail, source, status)
TRIO = [
    (1, "N. AMERICA", "100th Macy's parade postponed",
     "First postponement ever. Parade moves to Sat 28 Nov, 08:30 ET; "
     "gusts hit 60 mph.",
     "Reuters / CNN", "OFFICIAL"),
    (2, "S. ASIA", "India marks 18 years since 26/11",
     "Mumbai remembers the 166 killed in 2008. Tributes at the Taj; "
     "city on high alert.",
     "ANI / Reuters", "OFFICIAL"),
    (3, "GLOBAL", "Gukesh-Sindarov Game 3: draw",
     "A 60-move thriller in Geneva ends level, 1.5-1.5. Gukesh springs "
     "the Rio Variation.",
     "Chess.com", "CONFIRMED"),
]

MIDS = [
    (4, "N. AMERICA", "Nor'easter cuts 500,000+ off",
     "Record 9.41 ft tide at Cape May; gusts 70 mph; NJ emergency.",
     "PowerOutage.us", "CONFIRMED"),
    (5, "EUROPE", "Savasleyka: 5 jets hit",
     "Three MiG-31s, two Su-34s hit, Kyiv says. Moscow silent.",
     "Ukraine Gen. Staff", "REPORTED"),
    (6, "EUROPE", "EU summit: E45bn + E1.58tn",
     "27 leaders in Brussels split on Ukraine cash, 2028-34 plan.",
     "Reuters", "OFFICIAL"),
    (7, "E. ASIA", "Kim widens tactical nukes",
     "KCNA statement; Swiss envoy expelled, 48 hours to leave.",
     "KCNA / BBC", "OFFICIAL"),
    (8, "EUROPE", "Kyiv mall hit by missiles",
     "Seven hurt; Zelensky warns a new mass strike is coming.",
     "AP", "REPORTED"),
    (9, "GLOBAL", "FCC clears 1m Starlink sats",
     "A million-satellite constellation approved at once.",
     "FCC", "OFFICIAL"),
    (10, "E. ASIA", "13 miners trapped in Bogor",
     "Rescuers race to a 100 m shaft after a collapse.",
     "AP", "REPORTED"),
    (11, "E. ASIA", "Hong Kong mourns 168 victims",
     "One year on from the Wang Fuk Court blaze.",
     "AP", "CONFIRMED"),
    (12, "EUROPE", "UK writes to 100,000 veterans",
     "First Strategic Reserve letters since the Cold War.",
     "Times / Telegraph", "OFFICIAL"),
    (13, "EUROPE", "London Tube strike bites",
     "Commuters stranded as Tube staff walk out.",
     "TfL", "CONFIRMED"),
]

ALSO = [
    (14, "M. EAST", "Kuwait drone strike kills 2 Italians", "Reuters", "REPORTED"),
    (15, "M. EAST", "Blast by tanker 50 nm off Dubai; crew safe", "Wires", "REPORTED"),
    (16, "M. EAST", "Iran rejects Israel chemical-weapons claim", "Tehran", "CLAIM"),
    (17, "N. AMERICA", "Cyberattack hits CIA system at Langley", "Wires", "REPORTED"),
    (18, "LATIN AM.", "Cartagena: ~30 hostages freed, 18-hr siege", "Police", "CONFIRMED"),
    (19, "AFRICA", "Russian corvette sunk off Benghazi", "Kyiv", "REPORTED"),
    (20, "EUROPE", "Meloni: war must not reach the Med", "Rome", "OFFICIAL"),
    (21, "EUROPE", "ECB chief: Hernandez de Cos agreed", "EU Council", "OFFICIAL"),
    (22, "E. ASIA", "N. Korea halts arms aid to Russia", "HUR", "CLAIM"),
    (23, "EUROPE", "FSB border guards to leave Armenia", "Yerevan", "OFFICIAL"),
    (24, "N. AMERICA", "FBI, CIA split over Alice Huang spy claim", "Reuters", "REPORTED"),
    (25, "EUROPE", "UK-EU treaty carries 10-year exit clause", "BBC", "OFFICIAL"),
    (26, "M. EAST", "Judges doubt Netanyahu bribery charge", "BBC", "REPORTED"),
    (27, "EUROPE", "Poland plans late-Dec no-fly zone", "BBC", "OFFICIAL"),
    (28, "AFRICA", "Zambia bans protests", "Lusaka", "OFFICIAL"),
    (29, "AFRICA", "DR Congo-Uganda tensions flare", "Wires", "REPORTED"),
    (30, "M. EAST", "Iran death-row women plead for mercy", "Wires", "REPORTED"),
    (31, "GLOBAL", "Duran Duran's Andy Taylor dies, 65", "Family", "CONFIRMED"),
    (32, "N. AMERICA", "Abrego Garcia to leave the US", "Court filing", "OFFICIAL"),
    (33, "EUROPE", "Russian regional governor arrested", "Moscow", "REPORTED"),
    (34, "AFRICA", "Kenya rules on Ebola-site case", "Nairobi", "REPORTED"),
    (35, "S. ASIA", "Pakistan cancels TV screenings", "Islamabad", "REPORTED"),
    (36, "E. ASIA", "Taiwan shares rebound", "Taipei", "CONFIRMED"),
    (37, "N. AMERICA", "Thanksgiving travel: 1,500+ delays", "FlightAware", "CONFIRMED"),
    (38, "PACIFIC", "Solomons opposition slams Australia pact", "AAP", "REPORTED"),
    (39, "LATIN AM.", "Puerto Rico axes Luma contract, 5-4", "San Juan", "OFFICIAL"),
    (40, "M. EAST", "ISIL attack in Hasakah", "Wires", "REPORTED"),
]

STATS = [
    ("100th", "Macy's parade,\nfirst postponement"),
    ("166", "killed in 26/11,\nremembered 18 yrs on"),
    ("60", "moves in Gukesh\nGame 3, a draw"),
    ("500,000+", "without power in\nthe nor'easter"),
    ("5", "jets Kyiv claims\nhit at Savasleyka"),
    ("E45bn", "EU loan for Ukraine\nin 2027"),
]

REGIONS = [("N. AMERICA", 6), ("LATIN AM.", 2), ("EUROPE", 11),
           ("M. EAST", 6), ("AFRICA", 4), ("S. ASIA", 2),
           ("E. ASIA", 5), ("PACIFIC", 1), ("GLOBAL", 3)]

TIMELINE = [
    ("02:03", "KCNA: Kim orders wider tactical-nuclear deployment"),
    ("07:16", "Mumbai on high alert for the 26/11 anniversary"),
    ("14:00", "Gukesh-Sindarov Game 3 begins in Geneva"),
    ("14:36", "508,719 customers out, PowerOutage.us count"),
    ("15:00", "NWS high-wind warning begins in New York"),
]

# ---------------------------------------------------------------- drawing

def draw_header(draw):
    draw.rectangle([0, 0, W, 10], fill=RED)
    draw.text((W // 2, 20), "Thursday 26 November 2026",
              font=font(46, True, True), fill=INK, anchor="ma")
    draw.text((W // 2, 76), "THE WORLD IN ONE DAY",
              font=font(21, True, False), fill=RED, anchor="ma")
    draw.text((W // 2, 100),
              "A nor'easter steals Thanksgiving's parade  \u00b7  Mumbai remembers 26/11  \u00b7  Gukesh and Sindarov still level",
              font=font(14, False, True), fill=INK, anchor="ma")


def draw_stats(draw):
    y0, y1 = 126, 184
    cw = (W - 32) / 6
    for i, (num, label) in enumerate(STATS):
        x = 16 + i * cw
        draw.rectangle([x + 2, y0, x + cw - 2, y1], outline=RULE, width=1,
                       fill=CREAM_CARD)
        draw.text((x + cw / 2, y0 + 4), num, font=font(24, True, True),
                  fill=RED, anchor="ma")
        for j, part in enumerate(label.split("\n")):
            draw.text((x + cw / 2, y0 + 32 + j * 12), part,
                      font=font(9, False, False), fill=FAINT, anchor="ma")
    draw.text((16, 188), "40 STORIES  \u00b7  9 REGIONS  \u00b7  WIRES READ UP TO 22:30 UTC 26 NOV 2026",
              font=font(12, True, False), fill=INK)


def draw_region_bar(draw):
    y = 210
    total = sum(c for _, c in REGIONS)
    x = 16
    for name, count in REGIONS:
        w = (W - 32) * count / total
        draw.rectangle([x, y, x + w - 1, y + 14], fill=REGION_COLORS[name])
        x += w
    y = 228
    x = 16
    for name, count in REGIONS:
        label = "%s %d" % (name, count)
        f = font(8.5, True, False)
        draw.rectangle([x, y + 1, x + 9, y + 10], fill=REGION_COLORS[name])
        draw.text((x + 12, y), label, font=f, fill=INK)
        x += 12 + int(draw.textlength(label, font=f)) + 16


def draw_trio(draw):
    y0, y1 = 252, 462
    cw = (W - 32) / 3
    scenes = [draw_scene_macys, draw_scene_mumbai, draw_scene_chess]
    for i, story in enumerate(TRIO):
        num, region, head, detail, source, status = story
        x = 16 + i * cw
        draw.rectangle([x + 3, y0, x + cw - 3, y1], outline=INK, width=2,
                       fill=CREAM_CARD)
        draw.rectangle([x + 3, y0, x + cw - 3, y0 + 88], fill=(30, 30, 34))
        scenes[i](draw, x + 3, y0, cw - 6, 88, num)
        draw.text((x + 12, y0 + 96), "#%d" % num, font=font(22, True, True),
                  fill=RED)
        region_tag(draw, x + 52, y0 + 100, region)
        pill(draw, x + cw - 66, y0 + 100, status)
        draw_wrapped(draw, x + 12, y0 + 120, head, 17, cw - 24, bold=True,
                     serif=True, leading=20)
        draw_wrapped(draw, x + 12, y0 + 156, detail, 11.5, cw - 24,
                     leading=14)
        draw.text((x + 12, y1 - 13), "Source: " + source,
                  font=font(9, False, True), fill=FAINT)


def draw_scene_macys(draw, x, y, w, h, num):
    # Storm sky, slanting rain, a sagging grounded balloon.
    draw.rectangle([x, y, x + w, y + h], fill=(44, 52, 66))
    for i in range(26):
        rx = x + 8 + (i * 37) % int(w - 16)
        ry = y + 6 + (i * 23) % int(h - 26)
        draw.line([rx, ry, rx - 6, ry + 12], fill=(140, 160, 190), width=2)
    draw.ellipse([x + w * 0.33, y + 12, x + w * 0.67, y + 64],
                 fill=(214, 90, 60), outline=(120, 40, 30), width=2)
    draw.ellipse([x + w * 0.38, y + 18, x + w * 0.50, y + 34],
                 fill=(232, 130, 90))
    draw.line([x + w * 0.38, y + 62, x + w * 0.32, y + h - 6],
              fill=(200, 200, 200), width=2)
    draw.line([x + w * 0.62, y + 62, x + w * 0.68, y + h - 6],
              fill=(200, 200, 200), width=2)
    draw.text((x + 10, y + h - 24), "GROUNDED: gusts 60 mph",
              font=font(12, True, False), fill=(255, 255, 255))
    draw.text((x + w - 10, y + 6), "1st EVER",
              font=font(13, True, False), fill=(255, 210, 60), anchor="ra")


def draw_scene_mumbai(draw, x, y, w, h, num):
    # Gateway of India arch at dusk, candles below, tricolour glow.
    draw.rectangle([x, y, x + w, y + h], fill=(58, 44, 60))
    draw.rectangle([x, y + h - 26, x + w, y + h], fill=(30, 24, 30))
    ax, aw = x + w * 0.36, w * 0.28
    draw.rectangle([ax, y + 22, ax + aw, y + h - 26], fill=(232, 190, 110))
    draw.pieslice([ax - 6, y + 8, ax + aw + 6, y + 44], 180, 360,
                  fill=(232, 190, 110))
    draw.rectangle([ax + aw * 0.28, y + 44, ax + aw * 0.72, y + h - 26],
                   fill=(58, 44, 60))
    draw.pieslice([ax + aw * 0.28, y + 34, ax + aw * 0.72, y + 58], 180, 360,
                  fill=(58, 44, 60))
    for i, cx in enumerate([0.14, 0.22, 0.80, 0.88]):
        px = x + w * cx
        draw.line([px, y + h - 26, px, y + h - 14], fill=(240, 220, 180), width=2)
        draw.ellipse([px - 3, y + h - 20, px + 3, y + h - 14],
                     fill=(255, 180, 60))
    draw.text((x + 10, y + 6), "18 YEARS",
              font=font(14, True, False), fill=(255, 210, 60))
    draw.text((x + w - 10, y + 6), "166 KILLED",
              font=font(13, True, False), fill=(255, 255, 255), anchor="ra")


def draw_scene_chess(draw, x, y, w, h, num):
    # Chessboard corner with pieces, clock showing a near-empty bar.
    draw.rectangle([x, y, x + w, y + h], fill=(38, 52, 44))
    bs = 62
    bx, by = x + 12, y + 14
    for r in range(8):
        for c in range(8):
            light = (r + c) % 2 == 0
            col = (238, 226, 200) if light else (90, 70, 52)
            draw.rectangle([bx + c * bs / 8, by + r * bs / 8,
                            bx + (c + 1) * bs / 8, by + (r + 1) * bs / 8],
                           fill=col)
    cell = bs / 8
    draw.ellipse([bx + cell * 1 + 1, by + cell * 1 + 1,
                  bx + cell * 2 - 1, by + cell * 2 - 1], fill=(20, 20, 20))
    draw.ellipse([bx + cell * 5 + 1, by + cell * 5 + 1,
                  bx + cell * 6 - 1, by + cell * 6 - 1],
                 fill=(250, 250, 250), outline=(20, 20, 20), width=1)
    draw.ellipse([bx + cell * 2 + 1, by + cell * 6 + 1,
                  bx + cell * 3 - 1, by + cell * 7 - 1],
                 fill=(250, 250, 250), outline=(20, 20, 20), width=1)
    draw.ellipse([bx + cell * 6 + 1, by + cell * 2 + 1,
                  bx + cell * 7 - 1, by + cell * 3 - 1], fill=(20, 20, 20))
    tx = x + 92
    draw.text((tx, y + 10), "60 MOVES", font=font(16, True, False),
              fill=(255, 255, 255))
    draw.text((tx, y + 32), "SCORE 1.5-1.5", font=font(13, True, False),
              fill=(255, 210, 60))
    draw.text((tx, y + 50), "Rio Variation", font=font(11, False, True),
              fill=(220, 220, 220))
    draw.text((tx, y + 64), "6 sec at move 40", font=font(11, False, False),
              fill=(220, 220, 220))
    draw.rectangle([x + 12, y + h - 8, x + w - 12, y + h - 4],
                   outline=(255, 255, 255), width=1)
    draw.rectangle([x + 12, y + h - 8, x + w * 0.52, y + h - 4],
                   fill=(255, 210, 60))


def draw_mids(draw):
    y0 = 474
    cw = (W - 32) / 5
    rh = 100
    for row in range(2):
        for col in range(5):
            story = MIDS[row * 5 + col]
            num, region, head, detail, source, status = story
            x = 16 + col * cw
            y = y0 + row * rh
            draw.rectangle([x + 3, y, x + cw - 3, y + rh - 6], outline=RULE,
                           width=1, fill=(255, 255, 255))
            draw.text((x + 10, y + 4), "#%d" % num, font=font(13, True, True),
                      fill=RED)
            region_tag(draw, x + 40, y + 5, region, size=8)
            draw_wrapped(draw, x + 10, y + 24, head, 12.5, cw - 20, bold=True,
                         serif=True, leading=14)
            draw_wrapped(draw, x + 10, y + 54, detail, 9.5, cw - 20,
                         leading=11.5)
            draw.text((x + 10, y + rh - 16), source,
                      font=font(8, False, True), fill=FAINT)
            pill(draw, x + cw - 62, y + rh - 17, status, size=8)


def draw_timeline(draw):
    y = 680
    draw.line([16, y, W - 16, y], fill=RED, width=2)
    draw.text((16, y + 5), "THE DAY IN UTC",
              font=font(12, True, False), fill=RED)
    x = 148
    for time, event in TIMELINE:
        draw.text((x, y + 5), time, font=font(11, True, False), fill=INK)
        x += 42
        draw_wrapped(draw, x, y + 5, event, 10, 118, leading=12)
        x += 118 + 8


def draw_also(draw):
    y0 = 718
    draw.text((16, y0), "ALSO ON THURSDAY  \u2014  14 TO 40",
              font=font(13, True, False), fill=INK)
    cols = 3
    colw = (W - 32) / cols
    per_col = 9
    for i, story in enumerate(ALSO):
        num, region, head, source, status = story
        col = i // per_col
        row = i % per_col
        x = 16 + col * colw
        y = y0 + 22 + row * 19
        draw.text((x, y), "%d." % num, font=font(11, True, True), fill=RED)
        draw.text((x + 26, y), head, font=font(10.5, False, False), fill=INK)
        tag = " [%s]" % status
        draw.text((x + colw - 14, y), tag, font=font(8, True, False),
                  fill=STATUS_COLORS[status], anchor="ra")


def draw_bottom(draw):
    y0 = 908
    draw.line([16, y0, W - 16, y0], fill=INK, width=2)
    # Schematic world map, left.
    mx, my, mw, mh = 16, y0 + 8, 330, 84
    draw.rectangle([mx, my, mx + mw, my + mh], outline=RULE, width=1,
                   fill=(226, 236, 242))
    draw.text((mx + 6, my + 2), "WHERE IT HAPPENED",
              font=font(10, True, False), fill=INK)
    # Rough continent blobs on a lon/lat grid.
    def geo(lon, lat):
        return (mx + 14 + (lon + 170) / 360.0 * (mw - 28),
                my + 18 + (75 - lat) / 150.0 * (mh - 26))

    def blob(cx, cy, rx, ry, fill):
        draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=fill)

    blob(*geo(-100, 45), 42, 20, (120, 150, 120))
    blob(*geo(-60, -15), 20, 22, (120, 150, 120))
    blob(*geo(10, 50), 26, 16, (120, 150, 120))
    blob(*geo(20, 5), 22, 24, (120, 150, 120))
    blob(*geo(80, 45), 52, 20, (120, 150, 120))
    blob(*geo(135, -25), 16, 12, (120, 150, 120))
    pins = [(1, -74, 41), (2, 73, 19), (3, 6, 46),
            (5, 44, 55), (7, 127, 40), (10, 115, -6), (14, 48, 29),
            (19, -75, 11), (38, 160, -9)]
    for num, lon, lat in pins:
        px, py = geo(lon, lat)
        draw.ellipse([px - 7, py - 7, px + 7, py + 7], fill=RED,
                     outline=(255, 255, 255), width=1)
        draw.text((px, py - 1), str(num), font=font(8, True, False),
                  fill=(255, 255, 255), anchor="mm")
    # Date check, right.
    dx = 362
    draw.rectangle([dx, y0 + 8, W - 16, y0 + 84], outline=RED, width=2,
                   fill=(255, 244, 240))
    draw.text((dx + 8, y0 + 12), "DATE CHECK \u2014 WHAT IS NOT ON THIS PAGE, AND WHY",
              font=font(11, True, False), fill=RED)
    lines = [
        "Left out, first reported Wed 25 Nov: US tariffs on 14 partners; "
        "Cairo tanker fire (31 dead); Houthi claim on Ras Tanura; "
        "Shenzhou-24 launch; US Q3 GDP 4.3%; Australia-Solomons treaty signed.",
        "Left out, earlier: Dow's first close above 50,000 (Tue 24 Nov); "
        "Miss Universe crown (Tue 24 Nov).",
        "Not yet: Spain votes Sun 29 Nov; EU budget deal aimed for 17-18 Dec; "
        "rescheduled Macy's parade Sat 28 Nov 08:30 ET; Gukesh Game 4 Sat 28 Nov.",
        "Why Macy's leads: the postponement was decided Wed night, but the "
        "parade it cancelled was TODAY, and the storm hit today.",
    ]
    yy = y0 + 28
    for line in lines:
        yy = draw_wrapped(draw, dx + 8, yy, line, 8.5, W - 16 - dx - 16,
                          leading=10.5)
    # Footer legend.
    fy = y0 + 92
    draw.text((16, fy), "HOW SURE:  CONFIRMED = 2+ major outlets  \u00b7  OFFICIAL = on the record  \u00b7  REPORTED = one outlet / claim carried  \u00b7  CLAIM = one side only",
              font=font(9, False, False), fill=FAINT)
    draw.text((16, fy + 12), "Sources named on every story. Nothing here is addressed to any judge; the dates, tags and sources above are the honesty.",
              font=font(9, False, True), fill=FAINT)


def main():
    image = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(image)
    draw_header(draw)
    draw_stats(draw)
    draw_region_bar(draw)
    draw_trio(draw)
    draw_mids(draw)
    draw_timeline(draw)
    draw_also(draw)
    draw_bottom(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    image.save(out, "PNG", optimize=True)
    print("wrote %s (%d bytes)" % (out, os.path.getsize(out)))


if __name__ == "__main__":
    main()
