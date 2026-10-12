---
name: next-step
description: Analyzes album state and recommends the optimal next action. Use when the user asks "what should I do next?" or "what's left to do?"
argument-hint: "[album-name]"
model: haiku
prerequisites:
  - resume
allowed-tools:
  - Read
  - Glob
  - Grep
  - bitwize-music-mcp
---

## Your Task

**Input**: $ARGUMENTS (optional album name)

Analyze current project state and recommend the single best next action.

---

# Next Step Advisor

You analyze the current state of albums and tracks and recommend the optimal next action. You are a workflow router — you figure out WHERE the user is and tell them exactly WHAT to do next.

---

## Logic

### If No Album Specified

1. Call `get_session()` — check `last_album` from session context
2. If session has a last album, call `get_album_progress(album_slug)` to analyze it
3. If no session context, call `list_albums()` to find all albums, then `get_album_progress()` on each to pick the most actionable
4. If no albums exist, recommend creating one

### If Album Specified

1. Call `find_album(name)` — fuzzy match by name, slug, or partial
2. Call `get_album_progress(album_slug)` — get status, phase, track counts
3. Recommend next action based on detected phase

---

## Decision Tree

Analyze album and track statuses to determine the optimal next action.

**Instrumental detection**: Check each track's instrumental fields and report disagreements. Instrumentals skip vocal writing/pronunciation, not musical review: prepare Style Box and structural tags with `/bitwize-music:suno-engineer`, then obtain the lyric-reviewer's **Instrumental Arrangement Review**.

Inspect actual inputs with `get_album_full(album_slug, include_sections="lyrics,style")`
when status alone is ambiguous. A recommendation is not execution authorization:
every first take or retry must pass the current checkpoint and the engineer's
Execution Boundary, including the remaining user-authorized budget. Pending
sources block generation, not an explicitly requested provisional craft review.

```
Album Status = "Concept"
  → "Define the album concept. Run the 7 Planning Phases with /bitwize-music:album-conceptualizer"

Album Status = "Research Complete"
  → Any tracks Sources Pending?
    YES → "Sources need verification. Review SOURCES.md and verify each source."
    NO  → First "Not Started" track instrumental?
      YES → "Create Style Box for instrumental track [name]. Use /bitwize-music:suno-engineer"
      NO  → "Ready to write! Pick a track and use /bitwize-music:lyric-writer"

Album has tracks with status "Not Started"
  → First not-started track instrumental?
    YES → "Create Style Box for instrumental track [name]. Use /bitwize-music:suno-engineer directly"
    NO  → "Write lyrics for track [first not-started track]. Use /bitwize-music:lyric-writer"

Album has "In Progress" tracks with incomplete actual inputs
  → Vocal: finish the lyric with /bitwize-music:lyric-writer
  → Instrumental: finish style/structure with /bitwize-music:suno-engineer in prompt-only mode

Album has tracks with status "Sources Pending"
  → "Obtain human source verification for [name] through /bitwize-music:verify-sources; do not infer approval from an agent review."

All tracks have lyrics (or Style Box for instrumentals), none generated
  → Vocal-only: pronunciation-specialist, then lyric-reviewer
  → Instrumental-only: lyric-reviewer's Instrumental Arrangement Review
  → Mixed: pronunciation on vocal tracks, then the appropriate reviewer route for every track
  → All cases: /bitwize-music:pre-generation-check for current inputs, source clearance and execution authorization

Some tracks generated, some not
  → Any Generated tracks without ✓ in Generation Log Rating?
    YES → "Track [name] needs review. Listen and approve (mark ✓ in Generation Log) or regenerate.
           Style issue → /bitwize-music:suno-engineer to revise Style Box, then regenerate
           Lyrics issue → /bitwize-music:lyric-writer to fix lyrics, then regenerate
           Another-take proposal → Check current review and remaining authorization before any retry"
    NO  → "Generate track [first un-generated track] on Suno. Use /bitwize-music:suno-engineer"

All tracks generated, none Final
  → "All tracks generated! Review each track:
     Mark keepers with ✓ in Generation Log, regenerate rejected ones.
     Once all approved, batch-approve:
     Use update_track_field(album_slug, track_slug, 'status', 'Final') for each.
     Once all Final, album advances to Complete."

All tracks generated, some Final
  → Any Generated (non-Final) without ✓?
    YES → "Review track [name] — approve (✓) or regenerate"
    NO  → "All reviewed! Batch-approve remaining: update_track_field(album_slug, track_slug, 'status', 'Final') for each.
           Then import audio with /bitwize-music:import-audio, then master with /bitwize-music:mastering-engineer"

All tracks Final
  → "All tracks approved! Import audio with /bitwize-music:import-audio, then master with /bitwize-music:mastering-engineer"

Album Status = "Complete"
  → "Album is complete! Release with /bitwize-music:release-director"

Album Status = "Released"
  → "This album is released! Consider promotional content with /bitwize-music:promo-director"
  → Also suggest: "Start a new album? Check your ideas with /bitwize-music:album-ideas list"
```

---

## Output Format

```
NEXT STEP
=========

Album: [name] ([genre]) — [status]
Progress: [X/Y tracks complete]

RECOMMENDED ACTION:
  [Clear, specific instruction with skill name]

WHY:
  [One sentence explaining why this is the right next step]

AFTER THAT:
  [Brief mention of what comes after this step]
```

### When Analyzing Multiple Albums

If no album specified and multiple exist:

```
NEXT STEP
=========

You have X albums. Here's the most actionable:

PRIORITY 1: [album-name] ([genre])
  Status: [status] | Progress: [X/Y tracks]
  → [Recommended action]

Also in progress:
  - [album-2] — [brief status]
  - [album-3] — [brief status]

Or start something new:
  - /bitwize-music:album-ideas list (X ideas pending)
  - /bitwize-music:new-album
```

---

## Priority Rules

When multiple albums are in progress, prioritize:

1. **Closest to completion** — An album with 7/8 tracks done beats one with 2/10
2. **Unblocked work** — Source verification can block generation while provisional writing/refinement remains possible; choose within the user's requested scope
3. **Last worked on** — Favor the album from the last session (continuity)
4. **Higher track count** — Bigger album = more investment to protect

---

## Remember

1. **One clear recommendation** — Don't list 5 options. Pick the best one.
2. **Include the skill name** — "/bitwize-music:lyric-writer" not "write lyrics"
3. **Be specific about which track** — "Write lyrics for track 04-the-escape" not "write some lyrics"
4. **Explain why briefly** — Users trust recommendations they understand
5. **Don't repeat resume** — If user just ran resume, don't re-print all the same info
