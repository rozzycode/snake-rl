# Beamer Presentation Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create a 12-slide LaTeX Beamer presentation for the RL Snake coursework

**Architecture:** Single presentation.tex file in overleaf-sync directory, referencing existing images and reusing tables/formulas from the coursework .tex files. Beamer theme with large fonts, minimal text, Russian language support.

**Tech Stack:** LaTeX Beamer, babel (Russian), pgfplots, existing images from overleaf-sync/images/

---

### Task 1: Create Beamer skeleton

**Files:**
- Create: `overleaf-sync/presentation.tex`

**Step 1: Write the Beamer skeleton with Russian support and theme**

```latex
\documentclass[aspectratio=169,14pt]{beamer}
\usepackage[T2A]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[main=russian,english]{babel}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{amsmath}
\usepackage{tikz}
\usetheme{Madrid}
\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamerfont{frametitle}{size=\Large}
\setbeamerfont{normal text}{size=\large}

\title{Обучение с подкреплением\\для игры <<Змейка>>}
\author{Полегина А.\,Д.\\Научный руководитель: доцент С.\,Г.\,Красовский}
\institute{БГУ, мехмат, каф. дифф. уравнений и системного анализа}
\date{Минск, 2026}

\begin{document}
% slides will go here
\end{document}
```

**Step 2: Compile to verify skeleton works**

Run: `cd overleaf-sync && pdflatex presentation.tex`
Expected: PDF generated without errors

**Step 3: Commit**

```bash
git add overleaf-sync/presentation.tex
git commit -m "Add Beamer presentation skeleton"
```

---

### Task 2: Title slide + Task slide (slides 1-2)

**Files:**
- Modify: `overleaf-sync/presentation.tex`

**Step 1: Add title slide**

```latex
\begin{frame}[plain]
\titlepage
\end{frame}
```

**Step 2: Add Task & Relevance slide (slide 2)**

```latex
\begin{frame}{Цель и задачи}
\textbf{Цель:} разработать игру <<Змейка>> на Python, реализовать алгоритм RL для управления агентом и оценить качество обучения.

\vspace{0.5cm}
\textbf{Задачи:}
\begin{itemize}
    \item Изучить Q-learning
    \item Реализовать логику игры и RL-среду
    \item Задать состояние, действия и награду
    \item Провести эксперименты и оценить результат
\end{itemize}

\vspace{0.5cm}
\textbf{Почему <<Змейка>> + RL:} дискретная среда, мало действий, наглядный результат
\end{frame}
```

**Step 3: Compile and verify**

Run: `cd overleaf-sync && pdflatex presentation.tex`

**Step 4: Commit**

```bash
git add overleaf-sync/presentation.tex
git commit -m "Add slides 1-2: title and task"
```

---

### Task 3: Approach comparison slide (slide 3)

**Files:**
- Modify: `overleaf-sync/presentation.tex`

**Step 1: Add approach comparison table**

```latex
\begin{frame}{Сравнение подходов}
\centering
\small
\begin{tabularx}{0.95\textwidth}{>{\raggedright}p{0.22\textwidth} >{\raggedright}p{0.28\textwidth} X}
    \toprule
    Подход & Плюсы & Минусы \\
    \midrule
    Правила & Простота & Слабая адаптивность \\
    Поиск пути & Явный маршрут & Нет обучения на опыте \\
    \rowcolor{blue!15} Q-learning & Интерпретируемость, связь с дискретной средой & Масштабируемость \\
    DQN & Сложные состояния & Много ресурсов \\
    \bottomrule
\end{tabularx}

\vspace{0.5cm}
\textbf{Выбран табличный Q-learning} --- баланс простоты и пользы для учебного проекта
\end{frame}
```

Note: need to add `\usepackage{colortbl}` and `\usepackage{xcolor}` to preamble for `\rowcolor`.

**Step 2: Compile and verify**

**Step 3: Commit**

---

### Task 4: State vector slide (slide 4)

**Files:**
- Modify: `overleaf-sync/presentation.tex`

**Step 1: Add state vector slide with feature breakdown**

```latex
\begin{frame}{Состояние агента: 11 бинарных признаков}
\centering
\begin{tikzpicture}[
    box/.style={draw, rounded corners, minimum width=3cm, minimum height=0.7cm, font=\normalsize},
]
\node[box, fill=red!20] at (0,2.5) {danger\_straight / left / right};
\node[box, fill=blue!20] at (0,1.25) {dir\_up / down / left / right};
\node[box, fill=green!20] at (0,0) {food\_left / right / up / down};
\end{tikzpicture}

\vspace{0.4cm}
\begin{itemize}
    \item \textcolor{red!70}{3} --- опасность рядом
    \item \textcolor{blue!70}{4} --- текущее направление
    \item \textcolor{green!70}{4} --- положение пищи
\end{itemize}

\vspace{0.3cm}
Компактное описание $\Rightarrow$ подходит для табличного Q-learning
\end{frame}
```

Need to add TikZ library: `\usetikzlibrary{shapes.geometric}` in preamble.

**Step 2: Compile and verify**

**Step 3: Commit**

---

### Task 5: Actions & Reward slide (slide 5)

**Files:**
- Modify: `overleaf-sync/presentation.tex`

**Step 1: Add actions and reward slide**

```latex
\begin{frame}{Действия и награда}
\textbf{3 относительных действия:}
\begin{center}
\Large идти прямо \quad повернуть влево \quad повернуть вправо
\end{center}

\vspace{0.3cm}
\small Относительные --- уменьшают избыточность: <<повернуть влево>> имеет один смысл при любом направлении.

\vspace{0.5cm}
\textbf{Функция награды:}
\begin{center}
\begin{tabular}{ccc}
    \toprule
    Событие & Награда \\
    \midrule
    Пища & $+10.0$ \\
    Столкновение & $-10.0$ \\
    Шаг & $-0.1$ \\
    \bottomrule
\end{tabular}
\end{center}

Штраф за шаг $\Rightarrow$ агент не движется бесконечно по кругу
\end{frame}
```

**Step 2: Compile and verify**

**Step 3: Commit**

---

### Task 6: Architecture slide (slide 6)

**Files:**
- Modify: `overleaf-sync/presentation.tex`

**Step 1: Add architecture diagram slide**

```latex
\begin{frame}{Архитектура программной системы}
\centering
\includegraphics[width=0.85\textwidth]{images/architecture.jpg}
\end{frame}
```

**Step 2: Compile and verify**

**Step 3: Commit**

---

### Task 7: Q-learning algorithm slide (slide 7)

**Files:**
- Modify: `overleaf-sync/presentation.tex`

**Step 1: Add Q-learning formula slide**

```latex
\begin{frame}{Алгоритм Q-learning}
\begin{center}
\Large
$Q(s,a) \leftarrow Q(s,a) + \alpha\bigl[r + \gamma\,\max_{a'}Q(s',a') - Q(s,a)\bigr]$
\end{center}

\vspace{0.6cm}
\textbf{Гиперпараметры:}
\begin{center}
\begin{tabular}{cccc}
    \toprule
    $\alpha$ & $\gamma$ & $\varepsilon_0$ & decay \\
    \midrule
    0.1 & 0.9 & 1.0 & 0.995 \\
    \bottomrule
\end{tabular}
\end{center}

\vspace{0.3cm}
$\varepsilon$-жадная стратегия: $\varepsilon$ от 1.0 до 0.05 --- баланс исследования и использования
\end{frame}
```

**Step 2: Compile and verify**

**Step 3: Commit**

---

### Task 8: Interface screenshots slide (slide 8)

**Files:**
- Modify: `overleaf-sync/presentation.tex`

**Step 1: Add interface slide with 3 screenshots**

```latex
\begin{frame}{Интерфейс программы}
\centering
\begin{columns}
\column{0.32\textwidth}
\centering
\includegraphics[width=\textwidth]{images/manual_game.jpg}
\small Ручная игра

\column{0.32\textwidth}
\centering
\includegraphics[width=\textwidth]{images/agent_mode.jpg}
\small Агент

\column{0.32\textwidth}
\centering
\includegraphics[width=\textwidth]{images/game_over_modal.jpg}
\small Game over
\end{columns}
\end{frame}
```

**Step 2: Compile and verify**

**Step 3: Commit**

---

### Task 9: Experiment setup slide (slide 9)

**Files:**
- Modify: `overleaf-sync/presentation.tex`

**Step 1: Add experiment methodology slide**

```latex
\begin{frame}{Методика эксперимента}
\begin{center}
\Large
5 независимых обучений $\times$ 8 вариантов эпизодов $\times$ 100 тестовых игр
\end{center}

\vspace{0.5cm}
Эпизоды обучения: 50, 100, 200, 300, 500, 800, 1000, 1200

\vspace{0.3cm}
Метрика: средний score на 100 тестовых играх (без исследования)
\end{frame}
```

**Step 2: Compile and verify**

**Step 3: Commit**

---

### Task 10: Results chart slide (slide 10)

**Files:**
- Modify: `overleaf-sync/presentation.tex`

**Step 1: Add results chart slide**

```latex
\begin{frame}{Результаты обучения}
\centering
\includegraphics[width=0.85\textwidth]{images/learning_chart.jpg}
\end{frame}
```

**Step 2: Compile and verify**

**Step 3: Commit**

---

### Task 11: Results table slide (slide 11)

**Files:**
- Modify: `overleaf-sync/presentation.tex`

**Step 1: Add results table slide**

```latex
\begin{frame}{Рост качества игры}
\centering
\begin{tabular}{ccc}
    \toprule
    Эпизоды & Средний score & Лучший score \\
    \midrule
    50 & 4.26 & 15.80 \\
    100 & 7.54 & 19.20 \\
    500 & 13.96 & 21.40 \\
    1200 & \textbf{16.23} & \textbf{21.60} \\
    \bottomrule
\end{tabular}

\vspace{0.5cm}
Средний score вырос с \textbf{4.26} до \textbf{16.23} --- агент усваивает стратегию.\\
После 800 эпизодов рост замедляется $\Rightarrow$ выход на плато.
\end{frame}
```

**Step 2: Compile and verify**

**Step 3: Commit**

---

### Task 12: Conclusions slide (slide 12)

**Files:**
- Modify: `overleaf-sync/presentation.tex`

**Step 1: Add conclusions slide**

```latex
\begin{frame}{Выводы}
\begin{itemize}
    \setlength\itemsep{0.5cm}
    \item Цель достигнута: игра реализована, агент обучен, результаты проанализированы
    \item Табличный Q-learning формирует эффективную стратегию без нейронных сетей
    \item 11 бинарных признаков --- компромисс между простотой и информативностью
    \item Перспективы: влияние гиперпараметров, DQN для более сложных состояний
\end{itemize}
\end{frame}
```

**Step 2: Compile final presentation and verify all 12 slides**

Run: `cd overleaf-sync && pdflatex presentation.tex`

**Step 3: Commit final version**

```bash
git add overleaf-sync/presentation.tex
git commit -m "Complete 12-slide Beamer presentation"
```