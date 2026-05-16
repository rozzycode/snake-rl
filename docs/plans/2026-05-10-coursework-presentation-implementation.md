# Coursework Presentation Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a polished 11-slide defense presentation for the coursework and export it as an editable PPTX deck.

**Architecture:** Use the Presentations skill workflow with an artifact-tool workspace under `outputs/<thread-id>/presentations/coursework-defense`. Create a compact claim spine, a deck design system, slide modules for each slide, preview renders, and a final `.pptx` export built from the real coursework assets and metrics.

**Tech Stack:** artifact-tool presentation composition, Node.js runtime, local coursework assets, Presentations skill build scripts

---

### Task 1: Prepare the presentation workspace

**Files:**
- Create: `/Users/sadrozzy/BSU/coursework/outputs/019e11dd-2a95-7582-837d-38903acdbf38/presentations/coursework-defense/**`
- Reference: `/Users/sadrozzy/BSU/coursework/latex-coursework/sections/*.tex`
- Reference: `/Users/sadrozzy/BSU/coursework/artifacts/coursework/assets/*`

**Step 1: Create workspace directories**

Create `slides`, `preview`, `layout`, `assets`, `qa`, and `output`.

**Step 2: Record source notes**

List the coursework sections, screenshots, diagram, and chart used in the deck.

### Task 2: Lock story and design system

**Files:**
- Create: `claim-spine.txt`
- Create: `design-system.txt`
- Create: `contact-sheet-plan.txt`
- Create: `profile-plan.txt`

**Step 1: Write the claim spine**

Map each slide to one claim and one proof object.

**Step 2: Lock the visual system**

Define typography, palette, layout families, spacing, and slide grammar.

### Task 3: Implement slide modules

**Files:**
- Create: `slides/helpers.mjs`
- Create: `slides/slide-01.mjs` through `slides/slide-11.mjs`

**Step 1: Build helper utilities**

Add shared slide styles, colors, typography, and asset paths.

**Step 2: Build each slide**

Compose each slide as editable presentation content with images and text hierarchy.

### Task 4: Render and export the deck

**Files:**
- Create: `preview/*`
- Create: `layout/*`
- Create: `output/coursework-defense-presentation.pptx`

**Step 1: Run the deck builder**

Use the skill build script to export PPTX, preview PNGs, and layout JSON.

**Step 2: Review rendered output**

Check the contact sheet and adjust weak slides if needed.

### Task 5: Deliverables

**Files:**
- Final: `output/coursework-defense-presentation.pptx`

**Step 1: Confirm final export**

Return the PPTX path to the user and note the slide count and included proof objects.
