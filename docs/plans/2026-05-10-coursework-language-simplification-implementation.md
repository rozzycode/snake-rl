# Coursework Language Simplification Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Rewrite the coursework in a simpler, clearer academic style without changing the technical meaning, structure, or factual content.

**Architecture:** Work from the current Overleaf sync directory, rewrite each section file in place, then mirror the same text into the standalone local LaTeX copy. Keep formatting, equations, tables, images, and bibliography references intact while simplifying only the prose around them.

**Tech Stack:** LaTeX, Overleaf CLI (`olcli`)

---

### Task 1: Refresh the editable Overleaf mirror

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/.olcli.json`
- Reference: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/*.tex`

**Step 1: Pull the current project**

Run: `olcli pull "Курсовая работа 3 курс" /Users/sadrozzy/BSU/coursework/overleaf-sync --force`
Expected: project files are refreshed locally.

**Step 2: Verify all section files are present**

Run: `ls /Users/sadrozzy/BSU/coursework/overleaf-sync/sections`
Expected: introduction, four chapter files, and conclusion.

### Task 2: Simplify the framing sections

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/intro.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/conclusion.tex`

**Step 1: Rewrite the introduction**

Keep the same goals and tasks, but make the prose shorter and easier to read aloud.

**Step 2: Rewrite the conclusion**

Keep the metrics and ML conclusions, but reduce abstract wording and make the logic more direct.

### Task 3: Simplify the analytical chapters

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter1.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter2.tex`

**Step 1: Rewrite theory and approach comparison**

Use simpler explanations while preserving RL terminology and comparison logic.

**Step 2: Rewrite design rationale**

Explain state features, actions, rewards, and architecture in plainer language.

### Task 4: Simplify implementation and experiment chapters

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter3.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter4.tex`

**Step 1: Rewrite implementation explanations**

Keep module descriptions and screenshots, but use shorter, more direct sentences.

**Step 2: Rewrite experiment interpretation**

Keep metrics and limitations, but explain them more simply and clearly.

### Task 5: Mirror and verify

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/latex-coursework/sections/*.tex`

**Step 1: Mirror the rewritten section files**

Copy the final text from `overleaf-sync` into `latex-coursework`.

**Step 2: Push to Overleaf**

Run: `olcli push /Users/sadrozzy/BSU/coursework/overleaf-sync`
Expected: updated files upload successfully.

**Step 3: Compile in Overleaf**

Run: `olcli compile "Курсовая работа 3 курс"`
Expected: successful compile and fresh PDF URL.
