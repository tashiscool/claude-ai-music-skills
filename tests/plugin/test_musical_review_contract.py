"""Guard the shipped instruction contract, not an LLM's artistic judgment.

These checks prevent specific contradictory routes/rules from returning.
Scenario outcomes still require an agent review and an identified performance
when a listening claim is made; string checks cannot certify either.
"""

from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
pytestmark = pytest.mark.plugin


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_engineer_prepares_before_execution_checkpoint():
    text = read("skills/suno-engineer/SKILL.md")
    assert "## Execution Boundary" in text
    boundary = text.split("## Execution Boundary", 1)[1].split("\n## ", 1)[0]
    assert "prompt-only" in boundary
    assert "/bitwize-music:pre-generation-check" in boundary
    assert "remaining" in boundary and "budget" in boundary
    assert "retry" in boundary and "authorization" in boundary


def test_instrumental_has_an_arrangement_review_route():
    reviewer = read("skills/lyric-reviewer/SKILL.md")
    checkpoint = read("skills/pre-generation-check/SKILL.md")
    assert "## Instrumental Arrangement Review" in reviewer
    assert "Instrumental Arrangement Review" in checkpoint
    assert "SKIP — Instrumental track (no lyrics to review)" not in reviewer


def test_reviewer_discovery_covers_instrumentals_without_vocal_prerequisites(all_skill_frontmatter):
    metadata = all_skill_frontmatter["lyric-reviewer"]
    assert "arrangement" in metadata["description"].lower()
    assert not {"lyric-writer", "pronunciation-specialist"}.intersection(metadata.get("prerequisites", []))


@pytest.mark.parametrize("skill", ["suno-engineer", "pre-generation-check"])
def test_instrumental_capable_metadata_does_not_require_vocal_work(all_skill_frontmatter, skill):
    metadata = all_skill_frontmatter[skill]
    assert not {"lyric-writer", "pronunciation-specialist"}.intersection(metadata.get("prerequisites", []))


@pytest.mark.parametrize("skill", ["resume", "next-step"])
def test_album_helpers_route_all_three_track_mixes(skill):
    text = read(f"skills/{skill}/SKILL.md")
    for kind in ("Vocal-only", "Instrumental-only", "Mixed"):
        assert kind in text
    assert "Instrumental Arrangement Review" in text
    assert "execution authorization" in text
    assert "(lyric-writer, pronunciation-specialist, lyric-reviewer)" not in text


@pytest.mark.parametrize(
    ("path", "obsolete"),
    [
        ("skills/lyric-writer/SKILL.md", "Syllable counts consistent within verses"),
        ("skills/lyric-writer/SKILL.md", "Don't rhyme the same word twice"),
        ("skills/lyric-writer/SKILL.md", "Repeat title at song's beginning AND end"),
        ("skills/lyric-writer/SKILL.md", "**Bookend rule**"),
        ("skills/lyric-writer/craft-reference.md", "Don't ask — cut it down"),
        ("skills/lyric-writer/craft-reference.md", "Never exceed 8"),
        ("skills/lyric-writer/examples.md", '"Start" appears in both — chorus loses impact.'),
        ("skills/lyric-writer/examples.md", '"Warehouse" and "walls" appear in both.'),
        ("skills/lyric-reviewer/checklist-reference.md", "Any section exceeding its genre max must be flagged for trimming"),
        ("skills/lyric-reviewer/SKILL.md", "skip instrumental tracks"),
        ("skills/lyric-reviewer/SKILL.md", "instrumental-only checks marked N/A"),
        ("skills/lyric-reviewer/SKILL.md", "Only if RESEARCH.md exists"),
        ("skills/lyric-writer/SKILL.md", "**Respect hard limits**"),
        ("skills/lyric-refiner/SKILL.md", "**Respect hard limits**"),
        ("skills/lyric-writer/SKILL.md", "Stressed syllables on strong beats"),
        ("skills/lyric-writer/examples.md", "Six packed lines at 75 BPM — Suno will rush or compress."),
        ("skills/lyric-writer/examples.md", '"Love" rhymes with itself.'),
        ("reference/SKILL_INDEX.md", "Instrumental tracks skip: lyric-writer, pronunciation-specialist, lyric-reviewer."),
        ("reference/SKILL_INDEX.md", "auto-skips Gates 2"),
        ("skills/next-step/SKILL.md", "instrumental tracks auto-skip lyrics gates"),
        ("skills/resume/SKILL.md", "instrumental tracks auto-skip lyrics gates"),
    ],
)
def test_removed_blanket_rules_stay_removed(path, obsolete):
    assert obsolete not in read(path)


def test_documentary_review_distinguishes_evidence_modes():
    text = read("skills/lyric-writer/documentary-standards.md")
    for heading in ("Factual Narration", "Sourced Quotation", "Attributed Inference", "Disclosed Fiction"):
        assert f"### {heading}" in text
    assert "not legal clearance" in text
    assert "third-person narrator voice only" not in text
    assert "Legally Safe" not in text


def test_checkpoint_requires_current_inputs_not_a_stale_report():
    text = read("skills/pre-generation-check/SKILL.md")
    for term in ("Lyrics Box", "Style Box", "Generation Settings", "reference audio", "stale"):
        assert term in text
    assert "input fingerprint" in text
    assert "authorization" in text


def test_verbal_scansion_is_shown_not_inferred_from_time_signature():
    text = read("skills/lyric-writer/prosody-review.md")
    assert "## Show the Verbal Pattern" in text
    for term in ("foot", "accent", "every distinct lyric line", "mixed", "4/4"):
        assert term in text


@pytest.mark.parametrize("path", [
    "skills/lyric-reviewer/SKILL.md", "skills/suno-engineer/SKILL.md",
    "skills/resume/SKILL.md", "skills/next-step/SKILL.md", "CLAUDE.md",
])
def test_post_take_routes_reference_the_shared_review(path):
    assert "prosody-review.md#after-generation" in read(path)


def test_resume_resolves_inputs_before_persisting_phase():
    text = read("skills/resume/SKILL.md")
    assert "phase=detected_phase" not in text
    assert text.index('get_album_full(album_slug, include_sections="lyrics,style")') < text.index("phase=resolved_phase")
    assert "status-only estimate" in text


def test_scenarios_cover_the_reviewed_failure_modes():
    text = read("skills/lyric-writer/review-scenarios.md")
    for case in ("M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11"):
        assert f"### {case}:" in text
