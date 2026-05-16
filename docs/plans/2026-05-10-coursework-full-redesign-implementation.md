# Coursework Full Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Rebuild the coursework document into a four-chapter, defense-ready LaTeX report with improved heading typography, TOC styling, stronger chapter logic, and richer explanatory content.

**Architecture:** Treat `/Users/sadrozzy/BSU/coursework/overleaf-sync` as the editable Overleaf mirror, then mirror the same content changes back into `/Users/sadrozzy/BSU/coursework/latex-coursework` for local consistency. Most work is concentrated in `main.tex` plus the section files, with one new chapter file added and chapter boundaries rebalanced instead of rewriting the whole report from scratch.

**Tech Stack:** LaTeX, Overleaf CLI (`olcli`), existing local screenshots and diagrams

---

### Task 1: Refresh the Overleaf mirror and inventory current structure

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/.olcli.json`
- Reference: `/Users/sadrozzy/BSU/coursework/overleaf-sync/main.tex`
- Reference: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/*.tex`

**Step 1: Pull the current project**

Run: `olcli pull "Курсовая работа 3 курс" /Users/sadrozzy/BSU/coursework/overleaf-sync --force`
Expected: the synced copy refreshes successfully.

**Step 2: Verify chapter and asset files**

Run: `ls /Users/sadrozzy/BSU/coursework/overleaf-sync /Users/sadrozzy/BSU/coursework/overleaf-sync/sections`
Expected: `main.tex`, `images/`, `references.bib`, existing section files.

### Task 2: Rework top-level typography and TOC behavior

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/main.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/latex-coursework/main.tex`

**Step 1: Reduce vertical spacing before chapter-like headings**

Adjust chapter spacing so `ВВЕДЕНИЕ` and chapter openings start closer to the top body area.

**Step 2: Make major heading labels uppercase, bold, and large**

Configure chapter formatting so the rendered chapter label and title are visually stronger and uppercase.

**Step 3: Style main TOC entries**

Make only chapter-level TOC entries uppercase and bold while leaving subsection entries normal.

### Task 3: Restructure the report into four chapters

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/main.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter1.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter2.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter3.tex`
- Create: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter4.tex`
- Mirror same changes to `/Users/sadrozzy/BSU/coursework/latex-coursework/sections/`

**Step 1: Reframe chapter titles**

Rename chapters to the approved academic structure.

**Step 2: Reassign section content**

Move theory, design, implementation, and experiments into clearer chapter boundaries.

**Step 3: Update `main.tex` includes**

Insert the new fourth chapter and keep introduction/conclusion flow intact.

### Task 4: Strengthen the explanatory content for defense readiness

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter1.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter2.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter3.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter4.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/conclusion.tex`

**Step 1: Add explicit comparison and justification text**

Answer why Q-learning was chosen over rule-based logic and DQN.

**Step 2: Strengthen design rationale**

Explain the 11-feature state vector, relative actions, and reward shaping more explicitly.

**Step 3: Strengthen experiment framing**

Clarify metrics, experimental setup, limitations, and implications of the observed scores.

### Task 5: Preserve and place visuals intentionally

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter2.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter3.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter4.tex`

**Step 1: Keep the architecture figure near system-design discussion**

Place it in the design chapter.

**Step 2: Keep screenshots in the implementation chapter**

Use them to explain user-visible modes of the application.

**Step 3: Keep training chart in the experiment chapter**

Use it as the visual anchor for the reported metrics.

### Task 6: Push and verify

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/main.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/*.tex`

**Step 1: Push the synced project**

Run: `olcli push /Users/sadrozzy/BSU/coursework/overleaf-sync`
Expected: updated files upload successfully.

**Step 2: Compile in Overleaf**

Run: `olcli compile "Курсовая работа 3 курс"`
Expected: successful compile and fresh PDF URL.

**Step 3: Spot-check the result**

Confirm:
- main headings are uppercase and bold
- top spacing is reduced
- TOC main entries are uppercase and bold
- the document contains four chapters
- visuals remain in the expected places.
