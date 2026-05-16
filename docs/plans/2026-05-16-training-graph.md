# Training Graph Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add an experiment graph showing the relation between training episodes, average score, and best score to the LaTeX coursework.

**Architecture:** Reuse measured experiment data, generate a static chart image in the LaTeX images directory, and update chapter 4 text/table/figure so the document explains the methodology and conclusions consistently.

**Tech Stack:** Python, LaTeX, static image asset

---

### Task 1: Update experiment methodology

**Files:**
- Modify: `latex-coursework/sections/chapter4.tex`

**Step 1:** Replace the old short methodology text with the validated experiment setup.

**Step 2:** Update the experiment table so it matches the actual runs: 5 training runs per point, 100 evaluation games, and the selected episode counts.

### Task 2: Add the training graph

**Files:**
- Modify: `latex-coursework/main.tex`
- Modify: `latex-coursework/sections/chapter4.tex`

**Step 1:** Add `pgfplots` to the LaTeX preamble.

**Step 2:** Replace the old raster chart include with an inline plot that shows the dependence of average score and best score on the number of training episodes.

### Task 3: Align the written conclusions

**Files:**
- Modify: `latex-coursework/sections/chapter4.tex`

**Step 1:** Update the interpretation paragraph so it reflects the observed plateau after the main growth phase.

**Step 2:** Keep the explanation concise and coursework-friendly.
