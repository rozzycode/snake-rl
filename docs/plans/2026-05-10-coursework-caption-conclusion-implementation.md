# Coursework Caption And Conclusion Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Update the LaTeX coursework so captions use the required Russian format and the conclusion contains concrete numeric outcomes plus future discussion topics.

**Architecture:** Work from the freshly pulled Overleaf sync directory to avoid drift, make global caption-formatting changes in the preamble, then revise only the conclusion text and sync the same edits back to the local source copy for consistency. Finish by pushing to Overleaf and recompiling there.

**Tech Stack:** LaTeX, Overleaf CLI (`olcli`), local file sync

---

### Task 1: Refresh synced Overleaf workspace

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/.olcli.json`
- Reference: `/Users/sadrozzy/BSU/coursework/docs/plans/2026-05-10-coursework-caption-conclusion-design.md`

**Step 1: Pull the project before editing**
Run: `olcli pull "Курсовая работа 3 курс" /Users/sadrozzy/BSU/coursework/overleaf-sync --force`
Expected: synced project files downloaded successfully.

**Step 2: Verify the target files exist**
Run: `ls /Users/sadrozzy/BSU/coursework/overleaf-sync`
Expected: `main.tex`, `sections/`, `images/`, `references.bib`, `latexmkrc`.

### Task 2: Apply global caption formatting

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/main.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/latex-coursework/main.tex`

**Step 1: Replace default caption labels**
Set the Russian names explicitly so figures use `Рисунок` and tables use `Таблица`.

**Step 2: Replace caption separator**
Configure caption formatting so the rendered form becomes `Рисунок N. Текст` and `Таблица N. Текст`.

**Step 3: Keep changes mirrored locally**
Apply the same preamble edit to the standalone local LaTeX copy.

### Task 3: Expand the conclusion with measured results

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/conclusion.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/latex-coursework/sections/conclusion.tex`
- Reference: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/chapter3.tex`

**Step 1: Insert concrete metrics**
Mention the measured averages for 100, 300, and 500 episodes, the best result around 16.333, and 18 passing tests.

**Step 2: Add future discussion topics**
Close with a short paragraph about what else can be discussed: reward tuning, state representation, epsilon decay, scaling to larger boards, and comparison with DQN.

### Task 4: Push and verify in Overleaf

**Files:**
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/main.tex`
- Modify: `/Users/sadrozzy/BSU/coursework/overleaf-sync/sections/conclusion.tex`

**Step 1: Push the synced directory**
Run: `olcli push /Users/sadrozzy/BSU/coursework/overleaf-sync`
Expected: changed files uploaded.

**Step 2: Compile in Overleaf**
Run: `olcli compile "Курсовая работа 3 курс"`
Expected: successful compile with a fresh PDF URL.

**Step 3: Sanity-check outputs**
Confirm there is no remaining `Figure` or `Table` wording in the source and report the updated result back to the user.
