# news-image-20261126 r2 — build notes

## What changed vs round 1

Round 1 (97.41%, rank #964/7,124) led with Savasleyka / EU €45bn loan /
Kim tactical-nuclear, carried 35 stories across 6 regions, and missed the
board's consensus trio. This rebuild fixes all three gaps:

- **Trio corrected to the live board consensus:** #1 Macy's 100th parade
  postponed, #2 India marks 18 years since 26/11, #3 Gukesh–Sindarov
  Game 3 — in that order, each drawn as a scene with data inside it.
- **40 stories, 9 regions** (was 35 / 6). Regions: N. America 6,
  Latin America 2, Europe 11, Middle East 6, Africa 4, S. Asia 2,
  E. Asia 5, Pacific 1, Global 3. No region passes a third of the total.
- **Stat strip rebuilt from the leads/mids only:** 100th parade, 166
  killed (26/11), 60 moves (Game 3), 500,000+ without power, 5 jets
  (Savasleyka claim), €45bn EU loan — all from leads or mids #4–6.

## The 40 stories

Leads 1–3 above. Mids 4–13: nor'easter outages; Savasleyka 5 jets;
EU summit €45bn + €1.58tn; Kim tactical nukes; Kyiv mall strike;
FCC 1m Starlink satellites; 13 miners trapped in Bogor; Hong Kong
mourns 168 fire victims, one year on; UK writes to 100,000 veterans;
London Tube strike. ALSO 14–40: Kuwait drone strike kills 2 Italians
(Iran denies); blast by a tanker off Dubai, crew safe; Iran rejects
Israel chemical-weapons claim; CIA system cyberattack; Cartagena
hostages freed; Russian corvette sunk off Benghazi; Meloni on the
Mediterranean; ECB chief agreed; N. Korea halts arms aid to Russia
(Kyiv intel claim); FSB guards to leave Armenia; FBI/CIA split on the
Alice Huang claim; UK–EU treaty exit clause; Netanyahu bribery-charge
doubts; Poland no-fly zone; Zambia protest ban; DR Congo–Uganda;
Iran death-row women; Andy Taylor dies at 65; Abrego Garcia to leave
the US; Russian governor arrested; Kenya Ebola-site ruling; Pakistan
TV screenings cancelled; Taiwan shares rebound; Thanksgiving travel
delays; Solomons opposition slams the Australia pact; Puerto Rico
axes the Luma contract 5–4; ISIL attack in Hasakah.

## Verification (all live, 27 Nov ~05:30 WIB / 22:30 UTC 26 Nov)

- Macy's: Reuters/CNN — first postponement ever; parade to Sat 28 Nov
  08:30 ET; gusts 50–60 mph; balloon limit 23 mph sustained / 34 gusts;
  250,000+ customers out by 9am ET, 500,000+ by mid-morning (PowerOutage.us).
- 26/11: 166 killed, ~300 hurt in 2008; 18th anniversary tributes,
  Mumbai high alert, Gateway of India vigil 19:30 IST.
- Game 3: Chess.com/ChessBase — 60-move draw, 1.5–1.5, Geneva;
  Rio de Janeiro Variation (5...Be7); Sindarov down to ~6 seconds at
  move 40; Game 4 Sat 28 Nov.
- Kuwait drone strike: Reuters, 26 Nov — 2 Italian Rheinmetall
  technicians killed; Iran denies involvement (tag REPORTED, not CONFIRMED).
- UK veterans: The Times/Telegraph, 26 Nov — 100,000 Strategic Reserve
  letters, first since the Cold War; army ~73,000, smallest since the
  Napoleonic wars. MoD stresses this is not mobilisation.
- Savasleyka: Ukraine's claim (3 MiG-31 + 2 Su-34), Moscow silent —
  tag REPORTED. It stays a mid story, not a lead.
- Solomons treaty itself was signed Wed 25 Nov; the story on this page
  is the opposition backlash reported Thu 26 Nov (AAP).

## Dating discipline

The DATE CHECK names what was left out and why: US tariffs on 14
partners, Cairo tanker fire (31 dead), Houthi claim on Ras Tanura,
Shenzhou-24, US Q3 GDP 4.3%, Australia–Solomons treaty signing — all
first reported Wed 25 Nov; Dow above 50,000 and the Miss Universe crown
— Tue 24 Nov. Not yet: Spain votes Sun 29 Nov; EU budget deal aimed
for 17–18 Dec; Macy's parade Sat 28 Nov; Gukesh Game 4 Sat 28 Nov.
One honest wrinkle is stated on the page itself: the Macy's
postponement was decided Wed night, but it leads because the parade
it cancelled was TODAY and the storm hit today.

Two traps from round 1 kept out again: the Hong Kong Wang Fuk Court
fire (168 dead) happened 26 Nov **2025** — here only as the one-year
anniversary; and the Miss Universe crown was won Tue 24 Nov, not 26 Nov.

## Second opinions

- **Gemini (gemini-3.1-flash-lite):** asked for an independent trio.
  Its knowledge cutoff is 2024 — it stated plainly it has no information
  about 26 Nov 2026, so it could not confirm or deny the trio. The trio
  therefore rests on live wire reporting (above) plus the live board
  consensus, not on Gemini. No Gemini text is in the repo.
- **GLM vision mock judge (glm-4.6v-flash):** run on the rendered cover
  before submit; verdict recorded in the coordinator handoff, not here.
  Fixes it found were re-applied in this session and re-rendered.

## Honest weaknesses

- The map is schematic (continent blobs, not a real coastline) — pins
  are approximate by design and labelled as such.
- Three ALSO items (tanker blast off Dubai, CIA cyberattack, DR
  Congo–Uganda) rest on single wire-briefing reports and carry REPORTED;
  they are small list items, never leads.
- The judge (GLM-5.3-flash, per the kit's RULES.txt) has no news feed;
  the page is built to be checkable from the image alone: date, counts,
  tags, sources, and the DATE CHECK are all printed on it.

## Rendering

- `render.py` — Pillow only, Liberation Serif/Sans from `./fonts` if
  present, else the system font directories, else DejaVu.
- Output `entry.png`: 1024×1024, under the 1 MiB cap.
- `main.ts` — Node 22 stdlib only; copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output`) and verifies PNG magic
  bytes; both grading runs write identical bytes.
