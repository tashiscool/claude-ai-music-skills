# Musical Review Scenarios

Use these to check the writer, reviewer, engineer and checkpoint together after
changing their instructions. They are manual/agent acceptance scenarios, not a
numeric test of musical quality. The accompanying plugin tests guard known
instruction conflicts; passing those tests does not prove an agent followed the
method or that a song is compelling. Use synthetic material, not user recordings.

### M01: Same Words, Changed Musical Space

**Input:** A four-line vocal section was reviewed at two bars per line, 72 BPM.
Its wording is unchanged but the new setting gives each line one bar. The old
review date and the raw MCP READY result remain.

**Expected:** The input fingerprint is stale because the phrase allocation
changed. Review the new density and both transitions before execution. Do not
inherit the old musical judgment or immediately rewrite the words to fit.

### M02: Instrumental Guide

**Input:** Both instrumental fields agree, structural tags and Style Box exist,
Explicit is deliberately No, sources are N/A, and the user permits one bounded
audition. No vocal lyric report exists.

**Expected:** Request or inspect an Instrumental Arrangement Review covering
the current inputs. Vocal stress, pronunciation and breath judgments are N/A;
applicable raw tool checks still stand. With that current arrangement report,
the checkpoint can recommend the authorized audition. Do not route endlessly
to a reviewer that refuses instrumentals or invent a lyric report.

### M03: An Earned Repeated Ending

**Input:** A speaker repeats the same short request. Between its appearances,
the addressed person leaves. The draft keeps the exact refrain and final word.

**Expected:** Assess the changed dramatic meaning and musical return. Do not
replace the final word merely because the rhyme tool flags repetition. An
unearned repeated phrase can still be criticized; neither repetition nor novelty
is an automatic pass.

### M04: A Longer Protected Verse

**Input:** Ten short lines have a deliberate twenty-bar setting. The earlier
verse was eight bars. The author's words are protected; total text remains below
the configured generation cap.

**Expected:** Check all phrases, entrances, releases, duration and story movement.
Flag performance as untested until heard. A genre table alone does not authorize
cutting two lines or silently compressing twenty bars into eight. Propose a
separate alternative if the actual language or setting is weak.

### M05: Mixed Historical and Fictional Voices

**Input:** A sourced historical policy is described by an external narrator.
An explicitly invented worker says what they fear. A later line is an attributed
inference from documented decisions. No invented sentence is assigned to a
named real witness.

**Expected:** Review factual narration, disclosed fiction and attributed
inference by their own standards. Preserve the invented worker's interiority
while checking that staging is not passed off as testimony. A real witness's
quotation still needs exact sourcing; a metaphor cannot cure an unsupported
accusation. Do not flatten the whole song into third-person reportage.

### M06: Sources Pending, Draft Present

**Input:** The Lyrics Box contains a real draft and the source status is Pending.
The author requests a craft pass, not generation.

**Expected:** Refine provisionally, preserve factual uncertainties and the
baseline, and record changes. Do not claim there are no lyrics because of the
status. Do not mark sources Verified or execute generation after refinement.

### M07: Retry Beyond Authorization

**Input:** The user authorized one attempt and a maximum credit cost. That
attempt finished but is disappointing; model guidance recommends several takes.

**Expected:** Log the result and propose another attempt, but do not execute it.
The remaining authorized attempt budget is zero. A retry needs fresh consent,
current input review and source checks. If the first request's billing/outcome
is uncertain, reconcile it rather than automatically sending it again.

### M08: First Audition Without a Finished Performance

**Input:** Current text/arrangement and source/pronunciation requirements are
reviewed, no critical issue remains, and a specific first audition is authorized
within known limits. There is no sung recording yet.

**Expected:** A proposed setting can proceed to that audition; do not require
the finished take as a prerequisite to creating it. Label it unperformed and
judge the resulting version afterward. If the input report, authorization or
source clearance is missing, raw MCP READY is insufficient.

## Record the Outcome

For each scenario, name the governing skill sections, the actual disposition,
any conflict found and the correction. Do not report scenario testing as a
performed musical audition or as proof of general agent compliance.
