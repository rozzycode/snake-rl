# 2026-05-10 Coursework Full Redesign Design

## Goal
Rework the coursework LaTeX document into a stronger defense-ready academic structure with improved typography, clearer chapter logic, stronger visuals, and content that proactively answers likely instructor and ML-oriented questions.

## Approved design
1. Keep Overleaf as the source of truth and always edit from a freshly pulled synced copy.
2. Remove the excessive top whitespace before `ВВЕДЕНИЕ` and chapter headings.
3. Make major headings visually stronger:
   - `ВВЕДЕНИЕ`, `ГЛАВА N`, `ЗАКЛЮЧЕНИЕ`, `СПИСОК ИСПОЛЬЗОВАННОЙ ЛИТЕРАТУРЫ` in uppercase and bold
   - main table-of-contents entries in uppercase and bold
   - subsection-level TOC entries remain normal.
4. Restructure the body into four main chapters:
   - analysis of the task and solution approaches
   - design of the environment and agent
   - implementation of the software system
   - experimental study and result analysis
5. Strengthen explanatory support with tables, figures, and diagrams so the text answers likely questions about:
   - why tabular Q-learning was chosen
   - why the state has 11 binary features
   - why actions are relative instead of absolute
   - how reward shaping affects behavior
   - when and why DQN would be preferable
6. Keep the document grounded in the real project code and measured metrics.

## Structure
- `ВВЕДЕНИЕ`
- `ГЛАВА 1. АНАЛИЗ ЗАДАЧИ И ПОДХОДОВ К ЕЁ РЕШЕНИЮ`
- `ГЛАВА 2. ПРОЕКТИРОВАНИЕ ИГРОВОЙ СРЕДЫ И ОБУЧАЮЩЕГО АГЕНТА`
- `ГЛАВА 3. РЕАЛИЗАЦИЯ ПРОГРАММНОЙ СИСТЕМЫ`
- `ГЛАВА 4. ЭКСПЕРИМЕНТАЛЬНОЕ ИССЛЕДОВАНИЕ И АНАЛИЗ РЕЗУЛЬТАТОВ`
- `ЗАКЛЮЧЕНИЕ`
- `СПИСОК ИСПОЛЬЗОВАННОЙ ЛИТЕРАТУРЫ`

## Visual and explanatory support
- retain architecture diagram
- retain application screenshots
- retain training-results chart
- add or strengthen comparison and parameter tables
- rewrite section boundaries so each visual supports the nearby argument.

## Verification
- pull before editing
- push after editing
- compile in Overleaf
- confirm heading style and TOC formatting
- confirm chapter count and updated section layout
- confirm the document still compiles after restructuring.
