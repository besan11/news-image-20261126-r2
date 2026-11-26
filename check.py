# Quick self-check for this entry (no network, stdlib + Pillow only).
# Verifies the finished picture and the story list before bundling:
#   python3 check.py
# Exits non-zero if anything is off.

import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import render  # noqa: E402  (importing render only defines the story data)

EXPECTED_STORIES = 40
EXPECTED_REGIONS = 9
MAX_BYTES = 1_048_576

failures = []

path = os.path.join(here, "entry.png")
if not os.path.exists(path):
    failures.append("entry.png is missing; run python3 render.py first")
else:
    with open(path, "rb") as fh:
        head = fh.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        failures.append("entry.png does not start with the PNG magic bytes")
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        failures.append("entry.png is %d bytes, over the 1 MiB cap" % size)
    from PIL import Image
    with Image.open(path) as im:
        if im.size != (1024, 1024):
            failures.append("entry.png is %s, expected 1024x1024" % (im.size,))

stories = render.TRIO + render.MIDS + render.ALSO
total = len(stories)
if total != EXPECTED_STORIES:
    failures.append("story list has %d stories, expected %d"
                    % (total, EXPECTED_STORIES))
regions = {story[1] for story in stories}
if len(regions) != EXPECTED_REGIONS:
    failures.append("story list covers %d regions, expected %d"
                    % (len(regions), EXPECTED_REGIONS))
numbers = [story[0] for story in stories]
if numbers != list(range(1, EXPECTED_STORIES + 1)):
    failures.append("story numbers are not 1..%d in order" % EXPECTED_STORIES)

if failures:
    for problem in failures:
        print("FAIL: " + problem)
    raise SystemExit(1)
print("OK: %d stories, %d regions, entry.png %d bytes"
      % (total, len(regions), os.path.getsize(path)))
