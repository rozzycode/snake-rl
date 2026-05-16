# LaTeX Coursework

В этой папке лежит LaTeX-версия курсовой работы по проекту Snake RL.

## Структура

- `main.tex` — основной файл документа
- `sections/` — введение, главы и заключение
- `images/` — иллюстрации и графики
- `references.bib` — библиография
- `Makefile` — локальная сборка после установки TeX

## Что нужно установить

На этой машине сейчас не найден ни `pdflatex`, ни `xelatex`, поэтому PDF здесь не собирался.

Для macOS самый прямой путь:

1. установить MacTeX или BasicTeX;
2. убедиться, что доступны `pdflatex` и `biber`.

Вариант через Homebrew:

```bash
brew install --cask mactex-no-gui
```

Если `biber` не появился автоматически, установите полный MacTeX или добавьте его отдельно через TeX Live Manager.

## Сборка

Из папки `latex-coursework/`:

```bash
make
```

или вручную:

```bash
pdflatex -interaction=nonstopmode main.tex
biber main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

## Что получится

После успешной сборки появится `main.pdf`.

## Примечание

Документ совместим с `pdfLaTeX`: для русского текста используется связка `fontenc` + `inputenc` + `babel`.
