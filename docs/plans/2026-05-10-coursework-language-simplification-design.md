# 2026-05-10 Coursework Language Simplification Design

## Goal
Simplify the language of the entire coursework so it reads more naturally and is easier to explain during defense, while preserving academic tone, technical correctness, and project-specific substance.

## Approved design
1. Keep the current four-chapter structure and formatting.
2. Rewrite the text in a simpler academic style:
   - shorter sentences
   - fewer bureaucratic turns of phrase
   - direct wording instead of inflated formal constructions
   - preserve key ML terms only where they matter.
3. Do not downgrade the paper into conversational prose.
4. Preserve the real project facts, metrics, screenshots, diagrams, tables, and conclusions.
5. Synchronize changes through the Overleaf mirror first, then mirror back to the local LaTeX source copy.

## Style rules
- Replace heavy phrases like “представляет собой”, “обусловлено”, “с практической точки зрения” with plainer equivalents where possible.
- Prefer one clear idea per sentence.
- Keep Q-learning, DQN, reward shaping, exploration/exploitation, and epsilon where they add value, but explain them in simpler language.
- Make introduction, analysis chapters, and conclusion easier to retell aloud.

## Verification
- Pull before editing.
- Rewrite all section files, not just the conclusion.
- Push after editing.
- Recompile in Overleaf.
