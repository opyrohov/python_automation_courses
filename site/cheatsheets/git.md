# Git Cheatsheet

Швидкий довідник по Git командах.

## Налаштування

```bash
# Глобальна конфігурація
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Перегляд конфігурації
git config --list
git config user.name
```

## Початок роботи

```bash
# Ініціалізація нового репо
git init

# Клонування
git clone https://github.com/user/repo.git
git clone https://github.com/user/repo.git my-folder
```

## Базові команди

```bash
# Статус
git status
git status -s  # short format

# Додавання файлів
git add file.txt
git add .
git add -A
git add *.py

# Commit
git commit -m "Message"
git commit -am "Add and commit"  # tracked files only

# Історія
git log
git log --oneline
git log --graph --oneline --all
git log -n 5  # останні 5

# Різниця
git diff              # unstaged changes
git diff --staged     # staged changes
git diff HEAD~1       # з попереднім комітом
```

## Branches

```bash
# Список гілок
git branch        # локальні
git branch -a     # всі (включаючи remote)

# Створення
git branch feature
git checkout -b feature  # створити і перейти
git switch -c feature    # новий синтаксис

# Перемикання
git checkout main
git switch main

# Видалення
git branch -d feature    # safe delete
git branch -D feature    # force delete

# Перейменування
git branch -m old-name new-name
```

## Merge & Rebase

```bash
# Merge
git checkout main
git merge feature

# Merge без fast-forward
git merge --no-ff feature

# Rebase
git checkout feature
git rebase main

# Інтерактивний rebase
git rebase -i HEAD~3

# Скасування merge
git merge --abort

# Скасування rebase
git rebase --abort
```

## Remote

```bash
# Список remotes
git remote -v

# Додати remote
git remote add origin https://github.com/user/repo.git

# Отримати зміни
git fetch origin
git pull origin main

# Відправити зміни
git push origin main
git push -u origin main  # встановити upstream

# Видалити remote branch
git push origin --delete feature
```

## Stash

```bash
# Зберегти зміни
git stash
git stash push -m "WIP: feature"

# Список stashes
git stash list

# Застосувати
git stash pop          # apply and remove
git stash apply        # apply and keep
git stash apply stash@{2}

# Видалити
git stash drop stash@{0}
git stash clear  # all
```

## Скасування змін

```bash
# Unstage файл
git restore --staged file.txt
git reset HEAD file.txt  # старий синтаксис

# Скасувати зміни в файлі
git restore file.txt
git checkout -- file.txt  # старий синтаксис

# Скасувати останній коміт (зберегти зміни)
git reset --soft HEAD~1

# Скасувати останній коміт (видалити зміни)
git reset --hard HEAD~1

# Revert (створює новий коміт)
git revert HEAD
git revert abc1234
```

## Tags

```bash
# Список тегів
git tag

# Створення
git tag v1.0.0
git tag -a v1.0.0 -m "Release 1.0.0"

# Пуш тегів
git push origin v1.0.0
git push origin --tags

# Видалення
git tag -d v1.0.0
git push origin --delete v1.0.0
```

## Cherry-pick

```bash
# Застосувати конкретний коміт
git cherry-pick abc1234

# Без автоматичного коміту
git cherry-pick --no-commit abc1234
```

## Корисні команди

```bash
# Знайти коміт з помилкою
git bisect start
git bisect bad          # поточний коміт поганий
git bisect good abc123  # цей коміт хороший
# ... git автоматично знаходить

# Blame (хто змінив рядок)
git blame file.txt

# Показати коміт
git show abc1234
git show HEAD~2

# Порівняти гілки
git diff main..feature

# Очистити untracked файли
git clean -n  # dry run
git clean -f  # force
git clean -fd # включаючи директорії
```

## .gitignore

```gitignore
# Файли
*.log
*.pyc
.env

# Директорії
__pycache__/
node_modules/
.venv/
dist/

# Виключення
!important.log

# Патерни
docs/*.txt
**/temp/
```

## Aliases (рекомендовані)

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.lg "log --oneline --graph --all"
```
