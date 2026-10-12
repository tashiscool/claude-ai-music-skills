# 14-Point Checklist Reference

Detailed criteria for each lyric review checkpoint.

---

## 1. Rhyme Check

**What to scan:**
- Line endings across all verses/choruses
- Repeated end words
- Self-rhymes (love/love)
- Overused patterns (heart/apart, fire/desire, night/light, moon/June)

**Severity:**
- **Warning**: Repeated endings used as padding without a musical or dramatic purpose; an intentional refrain is not a defect
- **Info**: Predictable/lazy rhyme

**Output format:**
```
### Rhyme Check
- [⚠] V1:L2-L4: The repeated ending adds padding; compare a revision with the retained version
- [✓] Chorus: The repeated address is the deliberate hook; preserve it
- [⚠] V2:L1-L3: Predictable "fire/desire"
- [✓] Chorus: No issues
```

---

## 2. Prosody Check

**What to scan:**
- Multi-syllable words
- Natural stress alignment with beat positions
- Section function, musical accent and phrase contrast; follow [prosody-review.md](../lyric-writer/prosody-review.md) for every sung section
- Inverted word order forced for rhyme

**How to check:**
- Speak the lyric aloud
- Would you naturally emphasize those syllables?
- Preserve ordinary to-NIGHT and a-BOUT rather than accidentally emphasizing TO-night or A-bout
- Check the musical setting as well as speech: pickups, syncopation, held notes, releases and breath space
- Report a proposed setting as proposed; only an identified performed take supports a listening verdict

**Severity:**
- **Warning**: Clear stress misalignment
- **Info**: Subtle/debatable prosody issue

**Output format:**
```
### Prosody Check
- [✗] V1:L3: "reservoir" stress on wrong beat
- [⚠] Bridge:L2: Inverted word order "the truth he knew"
- [✓] Chorus: Natural flow
```

---

## 3. Pronunciation Check

**What to scan:**
- **Proper nouns** (names, places, brands)
- **Homographs** (live, lead, read, wind, tear, bass, close, bow, wound)
- **Acronyms** (FBI, GPS, RICO → F-B-I, G-P-S, Ree-koh)
- **Tech terms** (Linux, SQL → Lin-ucks, sequel)
- **Numbers** (1993 → '93 or nineteen ninety-three)
- **Foreign names** (Jose → Ho-zay, Sinaloa → Sin-ah-lo-ah)

**Critical Check**: Compare Pronunciation Notes table against Lyrics Box
- If name in Notes table, must be phonetic in Lyrics Box
- If phonetic only in Notes but spelled normally in Lyrics Box = FAIL

**Severity:**
- **Critical**: Unphonetic proper noun in Lyrics Box (will mispronounce)
- **Critical**: Homograph without clarification
- **Warning**: Acronym not spelled out
- **Info**: Number could be written cleaner

**Output format:**
```
### Pronunciation Check
- [✗] CRITICAL: "Jose Diaz" in Lyrics Box not phonetic (Notes says "Ho-say Dee-ahz")
- [✗] CRITICAL: "live" is homograph - needs "lyve" or "liv"
- [⚠] V2:L3: "FBI" should be "F-B-I"
- [✓] Numbers: Using '93 format correctly
```

### Homograph Detection

**Always flag these words in Lyrics Box:**

| Word | Must clarify | Options |
|------|-------------|---------|
| live | Always | liv (reside) or lyve (live performance) |
| read | If past tense | red |
| lead | If metal | led |
| wind | If coil/turn | wined |
| close | If shut | clohz |
| tear | If rip | tare |
| bass | If fish | bass (rhymes with "pass") |
| wound | If coiled | wownd |
| bow | If bend | bow (rhymes with "cow") |

---

## 4. POV/Tense Check

**What to scan:**
- Pronouns per section (I/me/we vs he/she/they vs you)
- Tense consistency (past vs present)
- Unmotivated shifts

**Allowed patterns:**
- Third-person verses, first-person chorus (common)
- Past tense story, present tense reflection
- Intentional shift for emotional effect

**Severity:**
- **Warning**: Inconsistent POV within section
- **Warning**: Tense jumping without clear reason
- **Info**: Could be intentional but flag for review

**Output format:**
```
### POV/Tense Check
- [✗] V1: Shifts from "he" (L1-3) to "you" (L4)
- [⚠] Bridge: Past tense but chorus is present
- [✓] Verses: Consistent third-person
```

---

## 5. Structure Check

**What to scan:**
- Section tags present ([Verse], [Chorus], [Bridge], etc.)
- Verse/chorus contrast (different energy, specificity)
- V2 development (not twin of V1)
- Effectiveness of the chosen hook/title placement, without mandatory opening or ending positions

**V2 Twin Test:**
- Does V2 say the same thing as V1 with different words?
- Does V2 develop the story or just repeat the message?

**Severity:**
- **Warning**: Missing section tags
- **Warning**: Twin verses (V2 = V1 reworded)
- **Warning**: Buried hook (title not prominent)
- **Info**: Could use stronger contrast

**Output format:**
```
### Structure Check
- [✓] Section tags: All present
- [✗] V2 is twin of V1 - both describe "the problem" without development
- [⚠] Hook is hard to identify in this setting; compare placement or melodic emphasis without prescribing a fixed line
```

---

## 6. Flow Check

**What to scan:**
- Forced rhymes (word clearly chosen just because it rhymes)
- Inverted word order ("The truth to him was known")
- Awkward phrasing that no one would say
- Filler words/syllables
- Fit of changed words to any reused musical phrase, including intentional unequal counts

**Conversational Test:**
- Would someone actually say this?
- Does it sound like song lyrics or a thesaurus explosion?

**Severity:**
- **Warning**: Clearly forced/awkward line
- **Info**: Slightly unnatural but not jarring

**Output format:**
```
### Flow Check
- [✗] V2:L4: "Upon the desk it lay" - inverted for rhyme
- [⚠] Bridge:L2: "Verily" - no one talks like this
- [✓] Choruses: Natural conversational flow
```

---

## 7. Documentary Check (Conditional)

**When to apply**: Whenever the song makes external factual claims; a missing research file does not exempt them

**What to scan:**
- Classify factual narration, sourced quotation, attributed inference and disclosed fiction per the writer's documentary standards
- Flag invented speech, interiority or acts presented as a real person's documented history
- Review breadth and attribution of external factual claims, including negatives
- Permit clearly disclosed fictional dialogue without treating it as historical evidence

**Reference**: Check lyrics against RESEARCH.md, Source/Lyrical Approach notes and the actual supporting record

**Severity:**
- **Critical**: Fabricated evidence or a real person's invented speech presented as sourced
- **Critical**: Unsupported real-person private conduct or interiority presented as established fact
- **Warning**: Fiction/inference boundary could mislead the listener
- **Info**: Could attribute more clearly

**Output format:**
```
### Documentary Check
- [✗] CRITICAL: V2:L3 attributes an invented confession to a real subject
- [✓] Bridge: The labeled fictional singer's dialogue is not represented as testimony
- [⚠] V1:L4: Clarify where the documentary account ends and the invented scene begins
- [✓] Dates and facts match RESEARCH.md
```

---

## 8. Factual Check (Conditional)

**When to apply**: Whenever the song makes external factual claims

**What to scan:**
- Names spelled correctly
- Dates match sources
- Numbers/amounts accurate
- Events in correct order
- Key facts verified

**How to check:**
- Cross-reference lyrics against RESEARCH.md

**Severity:**
- **Critical**: Wrong date/name/major fact
- **Warning**: Minor discrepancy
- **Info**: Could be clearer

**Output format:**
```
### Factual Check
- [✗] CRITICAL: V1 says "1943" but RESEARCH.md says "1942"
- [⚠] Bridge: "seventeen convicted" - actually 17 of 22, context unclear
- [✓] Names: All match sources
```

---

## 9. Length Check

**What to scan:**
- Total word count (count all lyrics excluding section tags)
- Number of verses
- Whether user explicitly requested extra verses

**Genre targets:**

| Genre | Target Words | Max Verses |
|-------|-------------|------------|
| Pop / Dance-Pop / Synth-Pop | 150–250 | 2 |
| Punk / Pop-Punk | 150–250 | 2 |
| Rock / Alt-Rock | 200–350 | 2–3 |
| Folk / Country / Americana | 200–350 | 2–3 |
| Hip-Hop / Rap | 300–500 | 2–3 |
| Ballad (any genre) | 200–300 | 2–3 |

**Severity:**
- **Blocking**: An applicable configured input cap is exceeded
- **Warning**: Word density or duration lacks a workable musical allocation
- **Info**: Outside a genre's starting range; inspect the chosen setting before recommending a change
- **Info**: At upper end of range, could trim

**Output format:**
```
### Length Check
- [⚠] 720 words in a short pop arrangement: no phrase allocation yet supports this density
- [✓] Additional verse has a deliberate musical span and advances the story
- [ℹ] 360 words exceeds the starting range; test the selected duration and delivery
- [✓] 280 words (folk) - within 200-350 range
```

---

## 10. Section Length Check

**What to scan:**
- Count lines per section (verse, chorus, bridge, etc.)
- Compare against genre limits from lyric-writer Section Length Limits table

**Severity:**
- **Warning**: A section outside the starting range needs a documented setting or audition, not an automatic trim

**Output format:**
```
### Section Length Check
- [⚠] V2: 10 lines but only the earlier short phrase allocation is specified; test more space or propose a targeted edit
- [✓] Chorus: 4 lines (within limit)
```

---

## 11. Rhyme Scheme Check

**What to scan:**
- Verify rhyme scheme matches the genre (see lyric-writer Default Rhyme Schemes by Genre)
- Assess whether unrhymed lines and scheme changes have a deliberate function

**Severity:**
- **Warning**: An unintended break in the chosen sound pattern weakens the phrase

**Output format:**
```
### Rhyme Scheme Check
- [⚠] V1: An unexplained sound-pattern change disrupts the intended melodic return
- [✓] Bridge: An unrhymed line deliberately withholds closure
- [✓] Chorus: AABB scheme consistent
```

---

## 12. Density/Pacing Check

**What to scan:**
- Verse line count vs genre README's `Density/pacing (Suno)` default
- Cross-reference BPM/mood from Musical Direction

**Severity:**
- **Warning**: The words exceed the chosen phrase space or delivery; line count alone does not establish failure

**Output format:**
```
### Density/Pacing Check
- [⚠] V2: The same short melody is reused for a much denser return; test it or give the return a distinct setting
- [✓] V1: The documented phrasing leaves adequate releases; performed delivery remains to be tested
```

---

## 13. Verse-Chorus Echo Check

**What to scan:**
- Compare last 2 lines of every verse against first 2 lines of the following chorus
- Identify whether a shared phrase, image or rhyme gains meaning on return or merely repeats a conclusion
- Check ALL verse-to-chorus and bridge-to-chorus transitions

**Severity:**
- **Warning**: Redundant explanation without dramatic or musical development

**Output format:**
```
### Verse-Chorus Echo Check
- [⚠] V1→Chorus: Both passages explain the same conclusion without new action or musical contrast
- [✓] V2→Chorus: The same invitation returns after a refusal; preserve the changed meaning
- [✓] Bridge→Chorus: A deliberate title pickup connects the sections
```

---

## 14. Artist Name Check

**What to scan:**
- Scan lyrics AND style prompt for real artist/band names
- Cross-reference against `${CLAUDE_PLUGIN_ROOT}/reference/suno/artist-blocklist.md`

**Severity:**
- **Critical**: Any artist name in the style prompt will cause Suno to fail or produce unexpected results
- **Fix**: Replace with genre/style description from the blocklist's "Say Instead" column

**Output format:**
```
### Artist Name Check
- [✗] CRITICAL: "Nirvana" in Style Box - replace with "90s grunge, distorted guitars"
- [✓] Lyrics: No artist names found
```

---

## Severity Definitions Summary

| Level | Definition | Action Required |
|-------|------------|-----------------|
| **Critical** | Will cause Suno problems or legal risk | Must fix before generation |
| **Warning** | Quality issue, impacts song | Should fix, can proceed with caution |
| **Info** | Nitpick, optional improvement | Nice to have, not blocking |
